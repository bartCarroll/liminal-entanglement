import sqlite3
import time

from pynput import keyboard


# Builds dictionary from cursor result
def dict_factory(cursor, row):
    dict = {}
    for i, col in enumerate(cursor.description):
        dict[col[0]] = row[i]
    return dict


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


def do_user_interaction(cur, categories, cat_str):
    count = 0
    while not count == 3:
        print(cat_str)
        selection = input("> ").lower()
        selected_cat = next((item for item in categories if item["display"].lower() == selection), None)
        print(selected_cat)
        count+=1
        if selected_cat:
            cur.execute("select * from question where category_id = ? ORDER BY RANDOM() LIMIT 1", str(selected_cat['id']))
            question = cur.fetchone()
            print(question['text'])
            break


if __name__ == "__main__":
    print("terminal main init...")
    con = create_connection('data/le_data.db')
    con.row_factory = dict_factory
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM CATEGORY")
        categories = cur.fetchall()
        cat_str = format_categories(categories)
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        while 1:
            print("doing the main loop, doing images / etc")
            time.sleep(3)
            print("listener.is_alive: " + str(listener.is_alive()))
            print("listener.ident: " + str(listener.ident))
            if not listener.is_alive():
                do_user_interaction(cur, categories, cat_str)
                listener = keyboard.Listener(on_press=on_press)
                listener.start()
