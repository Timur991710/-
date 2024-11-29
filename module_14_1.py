import sqlite3

connection = sqlite3.connect('not_telegram.db')
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY, 
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

# for i in range(10):
#     i +=1
#     cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',(f'User{i}', f'example{i}@gmail.com', i * 10, 1000))

# for i in range(10):
#     i +=1
#     if i % 2 != 0:
#         cursor.execute('UPDATE  Users SET balance = ? WHERE id = ?',(500, i))

for i in range(1, 11, 3):

    cursor.execute('DELETE FROM Users WHERE username = ?', (f'User{i}',))

cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()
for user in users:
    if user['age'] != 60:
        print('Имя: ', user['username'], '| Почта: ', user['email'], '| Возраст: ', user['age'], '| Баланс: ', user['balance'] )

connection.commit()
connection.close()




