from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень - {self.level}")

    def rest(self):
        print(f"{self.name} отдыхает…")
        self.__health += 1

    @abstractmethod
    def attack(self):
        pass

class Warrior(Hero):
    def attack(self):
        print('Воие атакует мечем!')

class Mage(Hero):
    def attack(self):
        print('Маг использует магию!')

class Assassin(Hero):
    def attack(self):
        print('Ассасин атакует из-под тишка!')

warrior = Warrior("Скорпион", 100, 1000, 8000)
mage = Mage("Сабзиро", 99, 950, 7800)
assassin = Assassin("Нуб Сайбот", 98, 900, 7500)

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
