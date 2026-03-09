class BankAccount:
    def __init__(self, login, password, balance):
        self.login = login
        self._balance = balance # Атрибута защищена
        self.__password = password # Приватная

    def get_balance(self, password):
        if password == self.__password:
            return self._balance
        return 'Не верный пароль!'

# Взаимодействие с пиватными атрибутами или методами
    def change_pass(self, old_pass, new_pass):
        if self.__password == old_pass:
            self.__password = new_pass
            return 'Пароль изменен!'
        return 'Неверный старый пароль!'

ardager = BankAccount('ardager', 'def1234', 1000)

# print(ardager.get_balance('def1234'))
# print(ardager._BankAccount__password)
# print(ardager.change_pass('def1234','12345'))
# print(ardager._BankAccount__password)
# print(dir(ardager))

# Прицип ООП: __Абстракция__

from abc import ABC, abstractmethod
#
# #Абстрактный класс
# class Animal(ABC):
#
#     @abstractmethod
#     def make_sound(self):
#         pass
#
#     @abstractmethod
#     def  move(self):
#         pass
#
# class Dog(Animal):
#
#     def make_sound(self):
#         return 'Gaf Gaf'
#     def move(self):
#         return 'Step Step'
#
# class Duck(Animal):
#     def make_sound(self):
#         return 'Krya Krya'
#     def move(self):
#         return 'Step Step'
#
# gufi = Dog()
# print(gufi.make_sound())
# print(gufi.move())
#
# donald = Duck()
# print(donald.make_sound())
# print(donald.move())

class OTPSend(ABC):

    @abstractmethod
    def send_otp_to_phone(self, phone):
        pass

class KGOTPSend(OTPSend):
    def send_otp_to_phone(self, phone):
        sms = """
        <Phone>+996777666555</Phone>
        <Text>Ваш пароль 1234</Text>
        """
        return sms

class RUOTPSend(OTPSend):
    def send_otp_to_phone(self, phone):
        sms = {
            "Phone": "+79652107311",
            "Text": "Ваш пароль 1234"
        }
        return sms


