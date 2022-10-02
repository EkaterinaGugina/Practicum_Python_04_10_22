# Ex3_dif_max_min. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:  [1.1, 1.2, 3.1, 5.05, 10.01] => 0.19

import random 
n = int(input('Введите число элементов n = '))
array_1 = [round(random.uniform(0.0, 11.0), 2) for i in range(n)]
array_2 = [0]*n
for i in  range(len(array_2)):
   array_2[i] = array_1[i] - int(array_1[i])
print(f'разницa между максимальным и минимальным значением дробной части элементов списка:\n {array_1} => {round(max(array_2) - min(array_2), 2)}')



# import random 
# n = int(input('Введите число элементов n = '))
# array_1 = [round(random.uniform(0.0, 12.0), 2) for i in range(n)]
# print(array_1)
# array_2 = [0]*n
# for i in  range(len(array_2)):
#    array_2[i] = (array_1[i] * 100) % 100
# print(f'разницa между максимальным и минимальным значением дробной части элементов данного списка равна {round(max(array_2)/100 - min(array_2



# import random 
# n = int(input('Введите число элементов n = '))
# array_1 = [round(random.uniform(0.0, 12.0), 2) for i in range(n)]
# array_2 = [0]*n
# # max_ind = 0
# # min_ind = 0
# # max = array_1[0] % 100
# # min = array_1[0] % 100
# for i in  range(1, len(array_2)):
#    array_2[i] = (array_1[i] * 100) % 100
# #    if array_2[i] > array_2[i - 1]:
# #        max_ind = i
# #    if array_2[i] < array_2[i - 1]:
# #        min_ind = i
# print(f'{array_1} ---> {array_2}')
