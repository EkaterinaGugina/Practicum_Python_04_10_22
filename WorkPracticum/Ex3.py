# Найти наименьшее общее кратное двух чисел
a, b = map(int, input().split())
nod = 2
while True:
    if a % nod == 0 and b % nod == 0:
        break
    else:
        nod += 1

nok = int(a * b / nod)
print(f'nod: {nod}, nok: {nok}')