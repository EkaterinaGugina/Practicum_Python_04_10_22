# Ex5_sum_polynom  Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# Например, 2*x² + 4*x + 5 = 0 и 2*x^4 + 4*x^3 + 5x^2 = 0  --> 2*x^4 + 4*x^3 + 7x^2 + 4*x + 5 = 0
import random
import math
import Ex4_second_decid as p

def nul_coef(m_deg, str_deg):
    if int(m_deg) > len(str_deg)-1:
        str_deg = list(map(int, str_deg.split()))
        str_deg.revers()
        for i in range(len(str_deg)):
            if int(str_deg[i])-1 != int(str_deg[i-1]):
                str_deg.insert(int(str_deg[i])-1, 0)
        str_deg.revers()
    return str_deg
                
def lst_deg(data):
    deg_str = []
    while 'x' in data:                                
        space_pos = data.index('x')
        if data[space_pos+2].isdigit():
            deg_str.append(data[space_pos+2])
            data = data[space_pos+5:]
        elif not data[space_pos+2].isdigit():  
            data = data[space_pos+3:]
    deg_str.extend(['1', '0'])
    str_deg_polyn = ' '.join(deg_str)
    deg_polyn = nul_coef(deg_str[0], str_deg_polyn)
    # ls_deg_polyn = list(map(int, ls_deg_polyn.split()))
    return deg_polyn

def lst_coef(data):
    coef_str = []
    while 'x' in data:
        space_pos = data.index('x')
        if data[space_pos-1] != ' ':
            coef_str.append(int(data[: space_pos]))
        else:
            coef_str.append(int('1'))
        data = data[space_pos + 5:]
    coef_str.extend(data)
    coef_polyn = list(map(int, coef_str))
    return coef_polyn
       
with open('file_1.txt', 'r') as f1:
    str1 = f1.read()
with open('file_2.txt', 'r') as f2:
    str2 = f2.read()
str1 = str1.replace('= 0', '')
str2 = str2.replace('= 0', '')
str1 = str1.rstrip()
str1 = str1.lstrip()
str2 = str2.rstrip()
str2 = str2.lstrip()
print(str1)
print(str2)
coef_p1 = lst_coef(str1)
print(coef_p1)
deg_p1 = lst_deg(str1)
print(deg_p1)
coef_p2 = lst_coef(str2)
print(coef_p2)
deg_p2 = lst_deg(str2)
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
   






      
# k, n = map(int, input('Введите степени многочленов k и n через пробел: ' ).split())
# with open('file_1.txt', 'w', encoding='utf-8') as f1:
#     f1.write(p.creat_polynom(k))
# with open('file_2.txt', 'w', encoding='utf-8') as f2:
#     f2.write(p.creat_polynom(n))


# coef_str.extend(data[len(data)-1])
# data[space_pos+2] == '+':
   
 
# def write_poly_file(name_file, deg):
#     with open('name_file.txt', 'w', encoding='utf-8') as f:
#         return f.write(p.creat_polynom(deg))
#     
# write_poly_file(file_1.txt, k)
# write_poly_file(file_2.txt, n)


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
 
 
 
 # print(str1)
# str1 = str1.split(' + ')
# # str2 = str2.split(' + ')
# print(str1)
# coef_p1 = []
# deg_p1 = []
# for i in range(len(str1)):
#     for j in str1[i]:
#         coef_p1[i] = ''
#         if j.isdigit():
#             coef_p1[i] += 'j'
#     coef_p1[i] = int(coef_p1[i])
# print(coef_p1)
   