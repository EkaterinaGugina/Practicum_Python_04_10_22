# Определить, присутствует ли в заданном списке строк, некоторое число
# Если нужно будет всамом элементе списка искать, то применять isdigit надо к самим элементам списка еще одним циклом for j in new_text[i]: if  j.isdigit(): cмотри ниже закомментино
def find_digit(new_text, num):
    for i in range(len(new_text)):
        if new_text[i].isdigit():
            if int(new_text[i]) == num:
                print(i)
str1 = ['воп23', 'д1ы', '56', 'ьу', '0', '8', 'ло765п', '2', 'вк']
num = 8
find_digit(str1, num)

# def find_digit(new_text, num):
#     for i in range(len(new_text)):
#         for j in new_text[i]
#          if j.isdigit():
#             if int(j) == num:
#                 print(i)
