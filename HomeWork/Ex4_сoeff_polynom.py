# Ex4_koeff_polynom. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
import random

def creat_polynom(k):
    k = int(input('Введите степень многочлена (натуральное число, большее нуля), k = '))
    polynom_coeff = [random.randint(0, 101) for i in range(k + 1)]
    print(polynom_coeff)
    if polynom_coeff[0] == 0:
        polynom_coeff[0] = random.randint(1, 5*deg)
    if k != 1:
        polynom_string = str(polynom_coeff[0])+'x^' + str(k) + ' '
        count = k - 1
        while count > 1:
            if polynom_coeff[k - count] != 0:
                polynom_string += '+ ' + \
                    str(polynom_coeff[k - count]) + \
                    'x^' + str(count) + ' '
            count -= 1
        if count == 1:
            polynom_string += '+ ' + \
                str(polynom_coeff[k - count]) + 'x  + ' + \
                str(polynom_coeff[k - count + 1]) + ' = 0'
    elif k == 1:
        polynom_string = str(polynom_coeff[0]) + \
            'x + ' + str(polynom_coeff[1]) + ' = 0'
    print(polynom_string)
    return polynom_string


# p1 = creat_polynom()






# with open('file_1.txt', 'w', encoding='utf-8') as f:
#     f.write(f1)
# f.close()
# with open('file_2.txt', 'w', encoding='utf-8') as f:
#     f.write(f2)
# f.close()



# def write_poly_file(name_file):
#     with open('name_file.txt', 'w', encoding='utf-8') as f:
#         return f.write(creat_polynom())
#     
# write_poly_file(file_1.txt)
# write_poly_file('file_2')
    