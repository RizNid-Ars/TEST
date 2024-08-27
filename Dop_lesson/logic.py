import sqlite3


def store_print(db_file):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''SELECT store_id, title FROM store'''
            cursor = connection.cursor()
            cursor.execute(sql)
            rows_list = cursor.fetchall()
            for row in rows_list:
                print(row)
        except sqlite3.Error as error:
            print(error)


def find_product(db_file, store_id):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''
            SELECT p.*, c.title FROM products as p
            inner join 
            categories as c on c.code = p.category_code
            where p.store_id = ?
            '''
            cursor = connection.cursor()
            cursor.execute(sql, (store_id,))
            rows_list = cursor.fetchall()
            for row in rows_list:
                print(row)
        except sqlite3.Error as error:
            print(error)


# store_print('test.db')
# find_product('test.db', 2)