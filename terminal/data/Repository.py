import sqlite3


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return None


class Repository:
    def __init__(self, con):
        self.connection = con
        self.connection.row_factory = self.__dict_factory
        self.cur = self.connection.cursor()
        self.categories = self.__retrieve_categories()
        self.category_string = self.__format_categories()

    # Builds dictionary from cursor result
    def __dict_factory(self, cursor, row):
        res_dict = {}
        for i, col in enumerate(cursor.description):
            res_dict[col[0]] = row[i]
        return res_dict

    def __retrieve_categories(self):
        self.cur.execute("SELECT * FROM CATEGORY")
        categories = self.cur.fetchall()
        return categories

    def __format_categories(self):
        disp_str = ""
        for cat in self.categories:
            disp_str += "{id}. {display}  ".format(**cat)
        return disp_str

    def get_random_category(self, category_id):
        self.cur.execute("select * from question where category_id = ? ORDER BY RANDOM() LIMIT 1",
                         str(category_id))
        return self.cur.fetchone()
