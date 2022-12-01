# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import os
import random

os.system('cls')

print('Найдем список, состоящий из попарно перемноженных элементов исходного списка.')

n = int(input('Введите длину исходного списка, он будет сгенерирован автоматически: '))

randomlist = random.sample(range(0, 10), n)

print()

print(f'Получился такой исходный список: {randomlist}.')

print()

def multList(inputlist):

    length = len(inputlist) - 1
    i = 0
    outputlist = list()

    while length >= i:
        outputlist.append(int(inputlist[length] * inputlist[i]))
        i += 1
        length -= 1

    return outputlist

print(f'Результат перемножения элементов в виде списка: {multList(randomlist)}.')