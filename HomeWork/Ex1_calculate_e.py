# Ex1_calculate_e Вычислить число c заданной точностью d
# Пример:  при $d = 0.001, π = 3.141.$    
#   $10^{-1} ≤ d ≤10^{-10}$
import math
epsylon = input('Введите точность вычислений в пределах от одной десятой до одной десятимиллиардной: \n e = ')
frac_part = epsylon.find('1') - epsylon.find('.')
# math.radians(90), math.e
print(f'Значение числа {math.e} с точностью до {epsylon} равна {round(math.e, frac_part)}')