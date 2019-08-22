import random
import time
import keyboard

from data.Repository import Repository, create_connection
from effects import DisplayEffects
from flipdot import client, display
from threading import Thread, Lock
from InteractionManager import InteractionManager


# CONFIGS
SIMULATED = True

if not SIMULATED:
    from gpio import GPIOManager

SIMULATED_IP = "127.0.0.1"
SIMULATED_PORT = 9999
FLIPDOT_USB = '/dev/ttyUSB0'
KEYBOARD_USB = '/dev/ttyUSB1'

display_lock = Lock()
key_pressed = False


def on_press(event):
    global key_pressed
    print('key pressed' + str(event))
    with display_lock:
        key_pressed = True


def do_user_interaction(repo, io_manager):
    count = 0

    while not count == 3:
        io_manager.select_boundary()
        selection = io_manager.get_boundary_selection(repo.category_string)
        if not selection:
            io_manager.try_again()
            continue
        selected_cat = next((item for item in repo.categories if item["display"].lower() == selection.lower()), None)

        count += 1
        if selected_cat:
            question = repo.get_random_category(selected_cat['id'])
            answer = io_manager.get_question_response(question['text'])
            if not answer:
                io_manager.try_again()
                continue
            repo.insert_answer((question['id'], answer))
            if not SIMULATED:
                t = Thread(target=GPIOManager.unlock_door, args=(), daemon=True)
                t.start()
            io_manager.scroll_text(answer)
            break
        else:
            io_manager.try_again()
            continue


def transition(disp):
    DisplayEffects.random_transition(disp)


def waiting_thread(disp):

    wait_times = [150, 300, 600]
    print("Started waiting thread...")
    while 1:
        try:
            # Do transition
            with display_lock:
                DisplayEffects.random_transition(disp)

            # Display Static Image
            with display_lock:
                DisplayEffects.display_random_image(disp)
            time.sleep(random.choice(wait_times))
        except Exception as e:
            print("Exception in waiting thread: " + str(e))
            continue


def interaction_thread(disp):
    global key_pressed
    con = create_connection('data/le_data.db')
    with con:
        repo = Repository(con)
        io_manager = InteractionManager(disp)
        keyboard.on_press(on_press)
        while True:
            try:
                with display_lock:
                    if key_pressed:
                        keyboard.unhook_all()
                        do_user_interaction(repo, io_manager)
                        key_pressed = False
                        keyboard.on_press(on_press)
                        print("Current Image: " + str(DisplayEffects.current_image))
                        if DisplayEffects.current_image:
                            DisplayEffects.current_image(disp)
                time.sleep(1)
            except Exception as e:
                print("Exception in interaction thread: " + str(e))
                continue


if __name__ == "__main__":
    flipdot_display = display.Display(28, 14,
                                      panels={
                                          2: ((0, 0), (28, 7)),
                                          1: ((0, 7), (28, 7)),
                                      })

    if SIMULATED:
        flipdot_display.connect(client.UDPClient(SIMULATED_IP, SIMULATED_PORT))
    else:
        flipdot_display.connect(client.SerialClient(FLIPDOT_USB))

    # Start Display Idol Thread
    wait_thread = Thread(target=waiting_thread, args=(flipdot_display,), daemon=True)
    wait_thread.start()

    # Start User Interaction Thread
    interact_thread = Thread(target=interaction_thread, args=(flipdot_display,), daemon=True)
    interact_thread.start()

    # Wait until threads complete
    wait_thread.join()
    interact_thread.join()
