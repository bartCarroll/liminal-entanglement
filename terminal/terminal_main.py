import sqlite3
import time
import keyboard
from effects import Effects
from flipdot import client, display
from threading import Thread, Lock


# CONFIGS
SIMULATED = True
SIMULATED_IP = "127.0.0.1"
SIMULATED_PORT = 9999
FLIPDOT_USB = '/dev/ttyUSB0'
KEYBOARD_USB = '/dev/ttyUSB1'

flipdot_display = display.Display(28, 14,
                                  panels={
                        2: ((0, 0), (28, 7)),
                        1: ((0, 7), (28, 7)),
                    })

display_lock = Lock()
key_pressed = False


# Builds dictionary from cursor result
def dict_factory(cursor, row):
    res_dict = {}
    for i, col in enumerate(cursor.description):
        res_dict[col[0]] = row[i]
    return res_dict


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)

    return None


def on_press(event):
    global key_pressed
    print('key pressed' + str(event))
    display_lock.acquire()
    key_pressed = True
    display_lock.release()


def format_categories(categories):
    disp_str = ""
    for cat in categories:
        disp_str += "{id}. {display}  ".format(**cat)
    return disp_str


def do_user_interaction(cur, categories, cat_str, d):
    count = 0

    while not count == 3:
        Effects.scroll_text(d, cat_str)
        Effects.display_text(d, '???', font=Effects.BigFont)
        cat_events = keyboard.record(until="enter")
        selection = next(keyboard.get_typed_strings(cat_events))
        selected_cat = next((item for item in categories if item["display"].lower() == selection), None)

        count += 1
        if selected_cat:
            cur.execute("select * from question where category_id = ? ORDER BY RANDOM() LIMIT 1",
                        str(selected_cat['id']))
            question = cur.fetchone()
            Effects.scroll_text(d, question['text'], font=Effects.SmallFont)
            Effects.display_text(d, '???', font=Effects.BigFont)
            events = keyboard.record(until="enter")
            answer = next(keyboard.get_typed_strings(events))
            if not answer:
                # TODO ANGRY EFFECT HERE
                Effects.scroll_text(d, font=Effects.SmallFont)
                continue
            Effects.scroll_text(d, answer, font=Effects.SmallFont)



            break


def transition(disp):
    Effects.rand(disp)


def waiting_thread(disp):
    print("Started waiting thread...")
    while 1:
        display_lock.acquire()
        Effects.rand(disp)
        display_lock.release()
        time.sleep(1)


def interaction_thread(disp):
    global key_pressed
    con = create_connection('data/le_data.db')
    con.row_factory = dict_factory
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM CATEGORY")
        categories = cur.fetchall()
        cat_str = format_categories(categories)
        keyboard.on_press(on_press)
        while True:
            display_lock.acquire()
            if key_pressed:
                keyboard.unhook_all()
                do_user_interaction(cur, categories, cat_str, disp)
                key_pressed = False
                keyboard.on_press(on_press)
            display_lock.release()
            time.sleep(1)


if __name__ == "__main__":
    print("terminal main init...")

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
