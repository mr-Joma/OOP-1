import sqlite3

# A4(бумага) == Данная ф-ция либо создает БД либо подключаетсяя БД ==
connect = sqlite3.connect("users.db")
# Рука с ручкой
cursor = connect.cursor()

# Создание таблицы
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (50) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')
# Сохранить
connect.commit()

# CRUD Create - Read - Update - Delete

def create_user(name, age, hobby):
          # Не правильный способ
    # cursor.execute(f"INSERT INTO users(name, age, hobby) VALUES ('{name}', '{age}', '{hobby}')")
          # Правильный метод (MySQL и PostGREsql)
    cursor.execute(
        "INSERT INTO users(name, age, hobby) VALUES (?, ?, ?)",
        (name, age, hobby)
    )
    connect.commit()
    print('Пользователь добавлен!!')

# create_user("Arsen", 22, "football")
# create_user("Joma", 23, "wrestling")
# create_user("Tima", 24, "sleeping")
# create_user("Alesha", 25, "Tennis")
# create_user("Mike", 26, "boxing")


# Чтобы показать в терминале или передать ФРОНТУ
def read_users():
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall() # Все что у тебя есть в руке помести его сюда
    for i in data:
        print(f'name: {i[0]}, age: {i[1]}, hobby: {i[2]}')

# read_users()

def update_user(name, age, hobby, id):
    cursor.execute(
        'UPDATE users SET name = ? WHERE id = ?',
        (name, id)
    )
    cursor.execute(
        'UPDATE users SET age = ? WHERE id = ?',
        (age, id)
    )
    cursor.execute(
        'UPDATE users SET hobby = ? WHERE id = ?',
        (hobby, id)
    )
    connect.commit()
    print('Пользователь обновлен!!')

update_user('Vitalik', 33, 'Жрать',3)

def delete_user(id):
    cursor.execute(
        'DELETE FROM users WHERE id = ?',
        (id,)
    )
    connect.commit()
    print('Пользователь удален!!')

# delete_user(2)