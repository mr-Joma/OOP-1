player = input('Выберите героя: Warrior/Mage/Assasin: ')
enemy = input('Выберите противника: Warrior/Mage/Assasin: ')


print(f'Вы выбрали: {player}')
print(f'Противник выбрал: {enemy}')

if player == enemy:
    print('Ничья!')
elif player == "Warrior" and enemy == 'Assasin':
    print('Warrior победил!')
elif player == 'Assasin' and enemy == 'Mage':
    print('Assasin победил!')
elif player == 'Mage' and enemy == 'Warrior':
    print('Mage победил!')
else:
    print(f'{enemy} победил!')