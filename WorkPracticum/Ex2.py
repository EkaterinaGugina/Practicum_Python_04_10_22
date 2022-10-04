# Найти корни квадратного уравнения
a, b, c = map(int,input().split())
d = b**2 - 4*a*c
if d > 0:
    print(f'x1 = {round((-b+d**0.5)/(2*a), 2)}, x2 = {round((-b-d**0.5)/(2*a), 2)}')
elif d == 0:
    print(f'x1 = {round(-b/(2*a), 2)}')
else:
    print('Корней нет')
    

# # Найти наименьшее общее кратное двух чисел
# a, b = map(int, input().split())
# nod = 2
# while True:
#     if a % nod == 0 and b % nod == 0:
#         break
#     else:
#         nod += 1

# nok = int(a * b / nod)
# print(f'nod: {nod}, nok: {nok}')
