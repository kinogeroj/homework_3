# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19 (максимальное значение у числа 1.2 , минимальное у 10.01)

import os

os.system('cls')

print('Найдем разницу дробной части элементов массива, у которых эта часть является максимальной и минимальной соответственно.')

a = input('Введите вещественные числа, которые буду являться элементами массива через пробел: ').split()

for i in range(len(a)):
    a[i] = float(a[i])

print(a)

def findDiff(inputlist):

    max = inputlist[0] - int(inputlist[0])
    min = max

    for i in range(1, len(inputlist)):

        diff = inputlist[i] - int(inputlist[i])
        
        if diff == 0:
            pass
        
        elif  diff > max:
            max = diff

        elif diff < min:
            min = diff
    
    res = max - min

    return res

print()

print(f'Искомая разница равна: {round(findDiff(a),2)}.')