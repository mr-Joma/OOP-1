import sqlite3

connect = sqlite3.connect("cinema.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    genre TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS reviews(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    movie_id INTEGER,
    rating INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(movie_id) REFERENCES movies(id)
)
""")

connect.commit()

# ДОБАВЛЕНИЕ ДАННЫХ
users = ["Ali", "Aida", "Bek", "Dana", "Egor"]

for user in users:
    cursor.execute("INSERT INTO users(name) VALUES (?)", (user,))

movies = [
    ("The Matrix", "Sci-Fi"),
    ("Forrest Gump", "Drama"),
    ("Avatar", "Fantasy"),
    ("Batman", "Action"),
    ("The Godfather", "Crime")
]

for movie in movies:
    cursor.execute("INSERT INTO movies(title, genre) VALUES (?, ?)", movie)

# Отзывы (user_id, movie_id, rating)
reviews = [
    (1, 1, 9),
    (1, 2, 8),
    (2, 1, 10),
    (2, 3, 7),
    (3, 4, 6),
    (3, 5, 9),
    (4, 2, 7),
    (4, 3, 8),
    (5, 1, 10),
    (5, 5, 9),
]

for review in reviews:
    cursor.execute(
        "INSERT INTO reviews(user_id, movie_id, rating) VALUES (?, ?, ?)",
        review
    )

connect.commit()


# JOIN ЗАПРОСЫ
print("\n Пользователь |  Фильм |  Оценка")

cursor.execute("""
SELECT users.name, movies.title, reviews.rating
FROM reviews
JOIN users ON reviews.user_id = users.id
JOIN movies ON reviews.movie_id = movies.id
""")

for row in cursor.fetchall():
    print(row)

# ВСЕ ФИЛЬМЫ (даже без отзывов)
print("\n Все фильмы:")

cursor.execute("""
SELECT movies.title, reviews.rating
FROM movies
LEFT JOIN reviews ON movies.id = reviews.movie_id
""")

for row in cursor.fetchall():
    print(row)


# АГРЕГАЦИИ
print("\n Статистика:")

                        # Средняя
cursor.execute("SELECT AVG(rating) FROM reviews")
print("Средняя оценка:", cursor.fetchone()[0])

                        # Максимум
cursor.execute("SELECT MAX(rating) FROM reviews")
print("Максимальная оценка:", cursor.fetchone()[0])

                        # Минимум
cursor.execute("SELECT MIN(rating) FROM reviews")
print("Минимальная оценка:", cursor.fetchone()[0])