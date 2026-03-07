class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень - {self.level}")

    def attack(self):
        print(f"{self.name} наносит удар!")

    def rest(self):
        print(f"{self.name} отдыхает…")
        self.health += 1


# Класс Warrior (Воин)
class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print(f"{self.name}: Воин атакует мечом!")


# Класс Mage (Маг)
class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print(f"{self.name}: Маг кастует заклинание!")


# Класс Assassin (Ассасин)
class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print(f"{self.name}: Ассасин атакует из-под тишка!")


# Создаем объекты
warrior = Warrior("Скорпион", 100, 1000, 8000, 500)
mage = Mage("Субзеро", 99, 1000, 7800, 1000)
assassin = Assassin("Нуб Сайбот", 98, 900, 7500, 1200)

warrior.greet()
warrior.attack()
warrior.rest()

print()

mage.greet()
mage.attack()
mage.rest()

print()

assassin.greet()
assassin.attack()
assassin.rest()
