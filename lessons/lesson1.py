class Hero:

    # Конструктор класса
    def __init__(self, name, hp, lvl):
        # Атрибуты класса
        self.name = name
        self.hp = hp
        self.lvl = lvl

        # Методы класса
    def action(self):
        return f'{self.name} Base action activate!!'

# Обьект/Экземпляр класса
kirito = Hero('Kirito', 1000, 100)
asuna = Hero('Asuna', 1001, 101)

print(kirito.action())
print(asuna.action())
