# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import os
import random

os.system('cls')

print('Найдем сумму чисел на нечетных позициях случайно сгенерированного списка.')

n = int(input('Введите длину списка: '))

randomlist = random.sample(range(0, 10), n)

print()

print(f'Получился такой список: {randomlist}.')

print()

def getSumOdds(inputlist):

    sum = 0

    for i in range(0, len(inputlist)):
        if i % 2 == 0:
            pass

        if i % 2 != 0:
            sum = sum + inputlist[i]
        
    return sum

print(f'Сумма чисел на нечетных позициях списка выше равна: {getSumOdds(randomlist)}.')