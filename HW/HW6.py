# Задание 1
from faker import Faker

# Эта библиотека нужна для генерации случайных данных (имена, адреса и т.д.)
# Используется, чтобы создавать тестовые данные

fake = Faker()

print("Случайное имя:", fake.name())
print("Случайный адрес:", fake.address())

# Задание 2
nums = [2, 7, 11, 15]
target = 9

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])