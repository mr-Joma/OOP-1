# # 1. Статичтический метод (@staticmethod)
#
# # Используются когда методу не нужны ни self ни cls
# # Обычная функция, но логичкски относящийся к классу
#
# class Math:
#     @staticmethod
#     def add(a, b):
#         return a + b
#
# # Обьекты класса
# # obj_1 = Math()
#
# # print(Math.add(11, 22))
#
# # 2. Декоратор/ Метод @classmethod
#
# class Bank:
#     # Атрибута класса
#     bank_name = "Mbank"
#
#     def __init__(self, sum, user):
#         # Атрибута экземпляра/обьекта класса
#         self.__sum = sum
#         self.user = user
#
#     def get_sum(self):
#         return self.__sum
#
#     @classmethod
#     def get_bank_name(cls):
#         return cls.bank_name
#
# agr = Bank(123515, "agr")
# bino = Bank(123, "bino")
#
# # print(agr.get_bank_name())
# # print(bino.get_bank_name())
# # print(agr.get_sum())
# # print(bino.get_sum())
#
#
# # 3. Декоратор @property
# # Описание:
# # Декоратор @property используется для того, чтобы метод стал доступным как атрибут, но при этом оставался методом.
# # Это позволяет скрыть логику вычисления или проверки, делая код более чистым. Обычно используется
# # для создания геттеров и сеттеров
#
# class Product:
#     def __init__(self, price):
#         self.__price = price
#
#     @property
#     def price(self):
#         return self.__price
#
#     @price.setter
#     def price(self, value):
#         if value < 0:
#             return print("Не может быть меньше 0!!")
#         self.__price = value
#         return print("OK!!")
#
# first_product = Product(100)
#
# # print(first_product.price)
# # first_product.price = 11
# # print(first_product.price)
#
# # Пример:
# # class User:
# #
# #     def __init__(self, first_name, last_name):
# #         self.first_name = first_name
# #         self.last_name = last_name
# #
# #     @property
# #     def full_name(self):
# #         return f'{self.first_name} {self.last_name}'
# #
# # ardager1 = User("Ivan", "Ivanov")
# #
# # print(ardager1.full_name)


# Создание декоратора

# def simple_decorator(func):
#     def wrapper():
#         print("До выполнения!")
#         func()
#         print("После выполнения!")
#     return wrapper
#
# @simple_decorator
# def say_hello():
#     print("Hello!!")
#
# # say_hello()
#
# def greeting_decorator(func):
#     def wrapper(name):
#         print(f'Привет {name}')
#         func(name)
#     return wrapper
#
# @greeting_decorator
# def greeting(name):
#     print(f'Как дела {name}?')

# greeting('Vitalik')

# def repeat_decorator(count):
#     def decorator(func):
#         def wrapper(name):
#             for i in range(count):
#                 print(f"{i} раз!!! \n")
#                 print(f"Привет {name}!!")
#                 func(name)
#         return wrapper
#     return decorator
# @repeat_decorator(5)
# def greeting(name):
#     print(f"Как дела {name}?")
# greeting("Ardager")

# Разница между декоратором с параметрами и без их вложенности:
# Декоратор с параметрами имеет двойную вложенность
# А без параметров одну

def class_decorator(cls):
    class NewClass(cls):
        def method(self):
            print("New method!!")
    return NewClass

@class_decorator
class OldClass:
    def method(self):
        print("Old method!!")

obj_1 = OldClass()
obj_1.method()

