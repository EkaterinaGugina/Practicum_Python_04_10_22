# Ex5_sum_polynom  Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# Например, 2*x² + 4*x + 5 = 0 и 2*x^4 + 4*x^3 + 5x^2 = 0  --> 2*x^4 + 4*x^3 + 7x^2 + 4*x + 5 = 0
import random
import math
import Ex5_function as p5

k, n = map(int, input('Введите степени многочленов k и n через пробел: ' ).split())
with open('file_1.txt', 'w') as f1:
    f1.write(p5.creat_polynom(k))
with open('file_2.txt', 'w') as f2:
    f2.write(p5.creat_polynom(n))
      
with open('file_1.txt', 'r') as f1:
    str1 = f1.read()
with open('file_2.txt', 'r') as f2:
    str2 = f2.read()
str1 = str1.replace('= 0', '')
str2 = str2.replace('= 0', '')
print(str1)
print(str2)
coef_p1 = p5.lst_coef(str1)
print(coef_p1)
deg_p1 = p5.lst_deg(str1)
print(deg_p1)
coef_p2 = p5.lst_coef(str2)
print(coef_p2)
deg_p2 = p5.lst_deg(str2)
print(deg_p2)
delta_deg_12 = abs(deg_p1[0] - deg_p2[0])
max_deg = max(deg_p1[0], deg_p2[0])
coef_sum_12 = [0]*delta_deg_12
if deg_p1[0] > deg_p2[0]:
    coef_sum_12.extend(coef_p2)
    print(coef_sum_12)
    for i in range(deg_p1[0]+1):
        coef_sum_12[i] = int(coef_sum_12[i]) + int(coef_p1[i])
else:
    coef_sum_12.extend(coef_p1)
    print(coef_sum_12)
    for i in range(int(deg_p2[0])+1):
        coef_sum_12[i] = int(coef_sum_12[i]) + int(coef_p2[i])
print(coef_sum_12) 
print(p5.creat_polynom1(max_deg, coef_sum_12))
with open('file_sum_12.txt', 'w') as f12:
    f12.write(p5.creat_polynom1(max_deg, coef_sum_12))
   






      
# k, n = map(int, input('Введите степени многочленов k и n через пробел: ' ).split())
# with open('file_1.txt', 'w', encoding='utf-8') as f1:
#     f1.write(p.creat_polynom(k))
# with open('file_2.txt', 'w', encoding='utf-8') as f2:
#     f2.write(p.creat_polynom(n))



# def lst_coef(data):
#     coef_str = []
#     deg_str = []
#     while 'x' in data                                #!= '':
#         space_pos = data.index('x')
#         deg_str.append(int(data[space_pos + 2])) 
#         if data[space_pos - 1] == ' ':
#             coef_str.append(int('1'))
#         else:
#             coef_str.append(int(data[ : space_pos]))
#         data = data[space_pos + 5: ]
#     deg_str.append('1', '0')
#     coef_str.append(data[len(data) - 1])
#     max = int(deg_str[0])
#     deg_polyn = list(map(int, nul_coef(deg_str)))
#     coef_str = list(map(int, coef_str))
#     return coef_str
 