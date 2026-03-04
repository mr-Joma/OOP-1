class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    # Метод greet
    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    # Метод attack
    def attack(self):
        if self.strength > 0:
            print(f"{self.name} наносит удар!")
            self.strength -= 1
        else:
            print(f"{self.name} слишком слаб!")

    # Метод rest
    def rest(self):
        print(f"{self.name} отдыхает…")
        self.health += 1

# Создаем два объекта класса Hero
hero1 = Hero("Скорпион", 100, 1000, 8000)
hero2 = Hero("Субзеро", 99, 1000, 7999)

# Вызов всех методов для hero1
hero1.greet()
hero1.attack()
hero1.rest()

print(f"{hero1.name}: здоровье={hero1.health}, сила={hero1.strength}\n")

# Вызов всех методов для hero2
hero2.greet()
hero2.attack()
hero2.rest()

print(f"{hero2.name}: здоровье={hero2.health}, сила={hero2.strength}")