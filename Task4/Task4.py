# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

import os

os.system('cls')

print('Переведем десятичное число в двоичное.')

n = int(input('Введите десятичное число: '))

def ConvertToBin(number):

    if number >= 1:
        ConvertToBin(number // 2)
    
    print(number % 2, end = '')

print()

print('Получается такое двоичное число: ', end = '')
    
ConvertToBin(n)