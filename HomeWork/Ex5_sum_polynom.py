# Ex5_  Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# Например, 2*x² + 4*x + 5 = 0 и 2*x^4 + 4*x^3 + 5x^2 = 0  --> 2*x^4 + 4*x^3 + 7x^2 + 4*x + 5 = 0
import random

import Ex4_second_decid as p

from unicodedata import name

with open('file_1.txt', 'w', encoding='utf-8') as f:
    f.write(f1)
f.close()
with open('file_2.txt', 'w', encoding='utf-8') as f:
    f.write(f2)
f.close()



k = int(input('Введите степень многочлена (натуральное число, большее нуля), k = ' ))
f1 = creat_polynom(k)
n = int(input('Введите степень второго многочлена, n = ' ))
f2 = creat_polynom()



# def write_poly_file(name_file):
#     with open('name_file.txt', 'w', encoding='utf-8') as f:
#         return f.write(creat_polynom())
#     
# write_poly_file(file_1.txt)
# write_poly_file('file_2')
    