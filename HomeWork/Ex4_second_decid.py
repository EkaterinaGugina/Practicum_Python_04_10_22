# Ex4_coeff_polynom. Задана натуральная степень k. Сформировать случайным образом список коэффициентов # (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
import random

def creat_polynom(deg, coeff):
    # deg = int(input('Введите степень многочлена (натуральное число), k = ' ))
    # coeff = [random.randint(0, 100) for i in range(deg + 1)]
    print(f'Коэффициенты полинома: {coeff}, если первый коэф. = "0", \n \
        он будет заменен другим случ. числом')
    if coeff[0] == 0:
        coeff[0] = random.randint(1, 100)
    if deg > 1:
        if coeff[0] > 1:
            polynom_string = str(coeff[0])+'x^' + str(deg) + ' '
        elif coeff[0] == 1:
            polynom_string = 'x^' + str(deg) + ' '
        count = deg - 1
        while count > 1:
            if coeff[deg - count] != 0:
                if coeff[deg - count] > 1:
                    polynom_string += '+ ' + \
                        str(coeff[deg - count]) + \
                        'x^' + str(count) + ' '
                elif coeff[deg - count] == 1:
                    polynom_string += '+ ' + \
                            'x^' + str(count) + ' '
            count -= 1
        if count == 1:
            if coeff[deg - count] > 1:
                polynom_string += '+ ' + \
                    str(coeff[deg - count]) + 'x + ' + \
                    str(coeff[deg - count + 1]) + ' = 0'
            elif (coeff[deg - count], coeff[deg - count + 1]) == (1, 0):
                polynom_string += '+ x = 0'
            elif (coeff[deg - count], coeff[deg - count + 1]) == (0, 0):
                polynom_string += ' = 0'
            elif coeff[deg - count] == 0 and coeff[deg - count + 1] != 0:
                polynom_string += '+ ' + str(coeff[deg - count + 1]) + ' = 0'
            elif (coeff[deg - count], coeff[deg - count + 1]) == (1, 1):
                polynom_string += '+ x + ' + str(coeff[deg - count + 1]) + ' = 0'
    elif deg == 1:
        if coeff[0] > 1 and coeff[1] > 0:
            polynom_string = str(coeff[0]) + \
                'x + ' + str(coeff[1]) + ' = 0'
        elif coeff[0] > 1 and coeff[1] == 0:
            polynom_string = str(coeff[0]) + 'x = 0'
        elif coeff[0] == 1 and coeff[1] > 0:
            polynom_string = 'x + ' + str(coeff[1]) + ' = 0'
        elif (coeff[0], coeff[1]) == (1, 0):
            polynom_string = 'x = 0'
    elif deg < 1:
        print('Степень введена некорректно!')
        return
    return polynom_string

# k, n = map(int, input('Введите степени многочленов k и n через пробел: ' ).split())
# with open('file_1.txt', 'w', encoding='utf-8') as f1:
#     f1.write(p.creat_polynom(k))
# with open('file_2.txt', 'w', encoding='utf-8') as f2:
#     f2.write(p.creat_polynom(n))



# k = int(input('Введите степень многочлена (натуральное число, большее нуля), k = ' ))
# poly_coeff = [random.randint(0, 101) for i in range(k + 1)]
# print(creat_polynom(k, poly_coeff))

