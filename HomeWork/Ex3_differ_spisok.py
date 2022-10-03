# Ex3_differ_spisok. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
from random import randrange
array = [randrange(1, 10) for i in range(int(input('Введите число элементов списка n = ')))]
differ_spisok = []
print(f'{array},  неповторяющиеся элементы: ')
for  i in range(len(array)):
    kolvo = 0
    for j in range(len(array)):
        if array[j] == array[i]:
            kolvo += 1
    if kolvo == 1:
        differ_spisok.append(array[i])
print(differ_spisok)
    




# from itertools import count
# from random import randrange
# array = [randrange(1, 10) for i in range(int(input('Введите число элементов списка n = ')))]
# print(f'{array}, а неповторяющиеся элементы: ')
# for  i in range(len(array)-1):
#     count = 0
#     for j in range(len(array)-1):
#         if array[j] == array[i]:
#             count += 1
#     if count == 1:
#         print(array[i], end=' ')
#     else:  break