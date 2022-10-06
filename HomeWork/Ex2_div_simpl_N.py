# Ex2_div_simpl_N. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

n = int(input('Введите натуральное число N = '))
num = n
div_simpl = 2
array_div = []
while num > 1:
   while num % div_simpl == 0:
      array_div.append(div_simpl)
      num //= div_simpl
   div_simpl +=1
print(f'Это все простые делители числа {n}: {array_div}')