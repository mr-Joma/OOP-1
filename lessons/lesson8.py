import sqlite3
from gc import get_count

connect = sqlite3.connect('order.db')
cursor = connect.cursor()

# ==One to Many==
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (50)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        total INTEGER NOT NULL,
        product VARCHAR (250) NOT NULL,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
''')
connect.commit()

def added_data():
    cursor.executemany(
        'INSERT INTO users(name) VALUES (?)',
        [
            ("Ardager",),
            ("Oleg",),
            ("Slava",),
        ]
    )
    connect.executemany(
        'INSERT INTO orders(total, product, user_id) VALUES (?, ?, ?)',
        [
            (12, "Iphone 17 PRO MAX", 1),
            (12, "MI 17 PRO", 2),
            (12, "S25 ULTRA", 4),
        ]
    )
    connect.commit()
    print("Данные заполнены!!")
# added_data()

# def get_order_user():
#
#     cursor.execute('''
#         SELECT users.name, orders.total, orders.product
#         FROM users FULL OUTER JOIN orders
#         ON users.id = orders.user_id
#     ''')
#
#     data = cursor.fetchall()
#
#     for i in data:
#         print(i)
#
# get_order_user()

def grt_count_user():
                    # Агригационные ф-ции
                            # COUNT
                            # AVG (среднее ариф.)
                            # MAX
                            # MIN
                            # SUM (общая сумма)
    cursor.execute('SELECT SUM(total) FROM orders')
    data = cursor.fetchall()
    print(data)
# grt_count_user()

def get_best_user():
    cursor.execute('''
        SELECT name FROM users
        WHERE id IN (
            SELECT user_id FROM orders WHERE total < 13
        )
    ''')
    data = cursor.fetchall()
    print(data)
# get_best_user()


def create_view():
    cursor.execute('''
        CREATE VIEW IF NOT EXISTS my_view AS 
        SELECT users.name, orders.total, orders.product
        FROM users FULL OUTER JOIN orders
        ON users.id = orders.user_id
    ''')
    connect.commit()
    print("Представление создано!!")
# create_view()

def my_view():
    cursor.execute('SELECT * FROM my_view')
    data = cursor.fetchall()
    for i in data:
        print(i)
my_view()