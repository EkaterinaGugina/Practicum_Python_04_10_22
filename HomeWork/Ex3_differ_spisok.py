# Ex3_differ_spisok. Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности.
from random import randrange
array = [randrange(1, 10) for i in range(int(input('Введите число элементов списка n = ')))]
differ_elem = []
print(f'{array},  неповторяющиеся элементы: ')
for elem in array:
        count_elem = array.count(elem)
        if count_elem == 1:
            differ_elem.append(elem)
print(differ_elem)   
  
