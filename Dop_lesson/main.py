import logic as db_main
import sqlite3


db_main.store_print('test.db')
while True:
    breaker = int(input('Хотите ли вы продолжить? Напишите 0 если нет, а если да то 1: '))
    if breaker == 0:
        break
    elif breaker == 1:
        pass
    add = db_main.find_product('test.db', int(input('''Вы можете отобразить список продуктов по выбранному id магазина из
перечня магазинов выше: ''')))