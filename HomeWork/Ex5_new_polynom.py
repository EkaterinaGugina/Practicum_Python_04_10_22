# Ex5_sum_polynom  Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# Например, 2*x² + 4*x + 5 = 0 и 2*x^4 + 4*x^3 + 5x^2 = 0  --> 2*x^4 + 4*x^3 + 7x^2 + 4*x + 5 = 0
import random
import math
import Ex4_second_decid as p
import Ex5_function as f5

with open('file_1.txt', 'r') as f1:
    str1 = f1.read()
with open('file_2.txt', 'r') as f2:
    str2 = f2.read()
str1, str2 = str1.replace('= 0', ''), str2.replace('= 0', '')
str1, str2 = str1.rstrip(), str2.rstrip()
str1, str2 = str1.lstrip(), str2.lstrip()
print(str1, /n str2)

coef_p1 = f5.lst_coef(str1)
print(coef_p1)
deg_p1 = f5.lst_deg(str1)
print(deg_p1)
coef_p2 = f5.lst_coef(str2)
print(coef_p2)
deg_p2 = f5.lst_deg(str2)
print(deg_p2)
delta_deg_12 = abs(int(deg_p1[0]) - int(deg_p2[0]))
# print(delta_deg_12)
max_deg = max(int(deg_p1[0]), int(deg_p2[0]))
# print(max_deg)
coef_sum_12 = [0]*delta_deg_12
if deg_p1[0] > deg_p2[0]:
    coef_sum_12.extend(coef_p2)
    print(coef_sum_12)
    for i in range(int(deg_p1[0])+1):
        coef_sum_12[i] = int(coef_sum_12[i]) + int(coef_p1[i])
else:
    coef_sum_12.extend(coef_p1)
    for i in range(int(deg_p2[0]+1)):
        coef_sum_12[i] = int(coef_sum_12[i]) + int(coef_p2[i])
print(coef_sum_12) 
# print(p.creat_polynom(max_deg, coef_sum_12))
with open('file_sum_12.txt', 'w') as f12:
     f12.write(p.creat_polynom(max_deg, coef_sum_12))
   
