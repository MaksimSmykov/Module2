first_stone_list = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
result = []

first_stone_number = int(input('Введите число из первого камня: '))
for num in range(1, first_stone_number):
    for num1 in range(num+1,first_stone_number):
        if first_stone_number % (num + num1) == 0:
            result.append(num)
            result.append(num1)
print(f'Ваш пароль:', *result)