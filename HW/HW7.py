import sqlite3

connect = sqlite3.connect('store.db')
cursor = connect.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (50) NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL
)
''')
connect.commit()

# CREATE
def create_product(name, price, quantity):
    cursor.execute(
        "INSERT INTO products(name, price, quantity) VALUES (?, ?, ?)",
        (name, price, quantity)
    )
    connect.commit()
    print("Товар добавлен!")

create_product("Плита", 13000, 6)
create_product("Стиральная машина", 24000, 7)


# READ
def read_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    print("\nСписок товаров:")
    for product in products:
        print(product)

# read_products()

# UPDATE
def update_product(id, price):
    cursor.execute(
        "UPDATE products SET price = ? WHERE id = ?",
        (price, id)
    )
    connect.commit()
    print("Цена обновлена!")

# update_product(1, 54000)

# DELETE
def delete_product(id):
    cursor.execute(
        "DELETE FROM products WHERE id = ?",
        (id,)
    )
    connect.commit()
    print("Товар удален!")

# delete_product(2)



