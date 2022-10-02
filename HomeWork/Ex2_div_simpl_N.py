# Ex2_mult_simm_elem. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16]
# - [2, 3, 5, 6] => [12, 15]

from random import randrange
n = int(input('Введите число элементов n = '))
array_1 = [randrange(1, 10) for i in range(n)]
if n % 2 == 0:
   array_2 = [0]*(n // 2)
else: array_2 = [0]*(n // 2 + 1)
for i in  range(len(array_2)):
   array_2[i] = array_1[i] * array_1[len(array_1) - 1 - i]
print(f'{array_1} ---> {array_2}')

