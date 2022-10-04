#  ПРОВЕРКА ДЗ
# import random

# count = int(input("Введите любое целое число: "))
# list = []
# summ = 0
# for i in range(count):
#     list.append(random.randint(0, 10))

# for i in range(1, len(list)-1, 2):
#     summ += list[i]
    
# print(list)
# print(summ)



# import random

# # spisok = [28, 14, 51, 9, 3, 10, 2, 1, 32]
# n = int(input('Введите размер списка:'))
# spisok = []
# sum = 0

# for i in range(n):
#     spisok.append(random.randint(0,10))
#     if i % 2 != 0:
#         sum = sum + spisok[i]
# print(spisok)
# print(f'Сумма нечетных элементов списка = {sum}')


# import math

# def make_pairs_prodact():
#     try:
#         num_list = input("Enter numbers without spaces: ")
#         num_list = [int(i) for i in num_list]
#         pair_list = []
#         for i in range(math.ceil(len(num_list)/2)):
#             pair_prodact = num_list[i]*num_list[-1*(i+1)]
#             pair_list.append(pair_prodact)
#         print("\033[36m{}{}{}".format(num_list, " --> ", pair_list))
#     except ValueError:
#         print("\033[1m\033[31m{}".format("You must enter an integer!"))

# make_pairs_prodact()
