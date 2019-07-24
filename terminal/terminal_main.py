import sqlite3
import time
from threading import Thread, current_thread
import signal
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
    return False # Disable listener thread.

def output_categories(categories):
    disp_str = ""
    for cat in categories:
        disp_str+="{id}. {display}  ".format(**cat)
    print(disp_str)

def do_user_interaction():
    for i in range(0,3):
        print("doing user interaction...")
        time.sleep(5)

def main_wait():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    while 1:
        print("here's some random text or image")
        time.sleep(3)
        if not listener.is_alive():
            do_user_interaction()
            listener = keyboard.Listener(on_press=on_press)

if __name__ == "__main__":
    print("terminal main init...")
    con = create_connection('data/le_data.db')
    con.row_factory = dict_factory
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM CATEGORY")
        categories = cur.fetchall()
        output_categories(categories)
        main_wait()





