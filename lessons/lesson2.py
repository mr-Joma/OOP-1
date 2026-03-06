# class Hero:
#
#     def __init__(self, name, lvl, hp):
#         self.name = name
#         self.lvl = lvl
#         self.hp = hp
#
#     def action(self):
#         return f' {self.name} Base action!!'
#
# class MageHero(Hero):
# # Атрибуты класса
#     def __init__(self, name, lvl, hp, mp):
#         super().__init__(name,lvl,hp)
#         self.mp = mp
#
#     def action(self):
#         return f'HP: {self.hp} NAME: {self.name}'
#
#     def cast_spell(self):
#         return f' MP: {self.mp} Cast spell{self.name}'
#
# kirito = Hero('Kirito', 100, 1000)
# asuna = MageHero('Asuna', 101, 1001, 99)
#
# # print(kirito.action())
# # print(asuna.action())
# print(kirito.name)
# print(asuna.name)

# Алмазная проблема / Diamond problem
class Step:
    def action(self):
        print("Step")

class Fly:
    def action(self):
        print("Fly")

class Swim:
    def action(self):
        print("Swim")

class Animal(Step, Swim, Fly):
    ...

# duck = Animal()
# duck.action()


class A:
    def action(self):
        print("A")
class B(A):
    def action(self):
        super().action()
        print("B")
class C(A):
    def action(self):
        super().action()
        print("C")
class D(B, C):
    def action(self):
        super().action()
        print("D")

test = D()
# test.action()
# print(D.mro())

