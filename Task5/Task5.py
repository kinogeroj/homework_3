# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. (Дополнительное)
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

import os

os.system('cls')

print('Найдем ряд чисел негафибоначчи для конкретного числа k.')

k = int(input('Введите число k: '))

def negaFibonacci(n):

    negafibonacci = []
    fibonacci = []
    a = 0
    b = 1

    for i in range(0, n + 1):
        
        fibonacci.append(a)
        a, b = b, a + b

    for i in range(1, n + 1):
        
        if i % 2 == 0:
            num = -fibonacci[i]

        else:
            num = fibonacci[i]

        negafibonacci.insert(0, num)

    negafibonacci = negafibonacci + fibonacci

    return negafibonacci

print()

print(f'Получается следующий ряд чисел: {negaFibonacci(k)}.')