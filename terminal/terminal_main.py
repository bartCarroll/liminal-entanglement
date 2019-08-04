import sqlite3
import time
from effects import Effects
from flipdot import client, display
from pynput import keyboard

d = display.Display(28, 14,
                    panels={
                        2: ((0, 0), (28, 7)),
                        1: ((0, 7), (28, 7)),
                    })


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


def on_press(key):
    print('key pressed')
    return False  # Disable listener thread.


def format_categories(categories):
    disp_str = ""
    for cat in categories:
        disp_str += "{id}. {display}  ".format(**cat)
    return disp_str


def do_user_interaction(cur, categories, cat_str, d):
    count = 0
    while not count == 3:
        print(cat_str)
        selection = input("> ").lower()
        selected_cat = next((item for item in categories if item["display"].lower() == selection), None)
        print(selected_cat)
        count += 1
        if selected_cat:
            cur.execute("select * from question where category_id = ? ORDER BY RANDOM() LIMIT 1",
                        str(selected_cat['id']))
            question = cur.fetchone()
            Effects.scroll_text(d, question['text'], font=Effects.SmallFont)
            Effects.wipe_down(d)

            break


def transition(disp):
    Effects.rand(disp)


if __name__ == "__main__":
    print("terminal main init...")

    con = create_connection('data/le_data.db')
    d.connect(client.UDPClient("localhost", 9999))

    con.row_factory = dict_factory
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM CATEGORY")
        categories = cur.fetchall()
        cat_str = format_categories(categories)
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        while 1:
            Effects.display_text(d, "Hey")
            time.sleep(2)
            transition(d)
            Effects.blink_text(d, "Hi")
            transition(d)
            Effects.rand(d)
            Effects.scroll_text(d, "Please talk to me")
            Effects.gobble(d)
            if not listener.is_alive():
                do_user_interaction(cur, categories, cat_str, d)
                listener = keyboard.Listener(on_press=on_press)
                listener.start()
