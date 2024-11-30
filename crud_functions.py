import sqlite3
from random import randint

connection = sqlite3.connect('crud_functions.db')
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products (
id INTEGER PRIMARY KEY,
title TEXT INT NOT NULL,
description TEXT,
price INT NOT NULL
);
''')
def get_all_products():
    connection = sqlite3.connect('crud_functions.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    check_user = cursor.execute('SELECT * FROM Products')
    message = []
    for user in check_user:
        message.append([user[0], user[1], user[2], user[3]])
    connection.commit()
    return message

connection.commit()

# cursor.execute('INSERT INTO Products  (title, description, price) VALUES (?, ?, ?)',(f'Хром', f'Буря красок и эмоций!', 100))
# cursor.execute('INSERT INTO Products  (title, description, price) VALUES (?, ?, ?)',(f'Я стесняюсь', f'Порадуйте свою возлюбленную!', 200))
# cursor.execute('INSERT INTO Products  (title, description, price) VALUES (?, ?, ?)',(f'У нас пополнение', f'Устройте праздник семье в честь рождения малыша!', 300))
# cursor.execute('INSERT INTO Products  (title, description, price) VALUES (?, ?, ?)',(f'Вот мы шиканули!', f'Покажите всем что знаете толк в стиле, удивит даже бывалых гостей', 400))

#cursor.execute('DELETE FROM Users')


connection.commit()
connection.close()