# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1
text_1 =["qwe", "asd", "zxc", "ertqwe"]
key_word = "qwe"
def find_coincidence(new_text, key):
    count = 0
    for i in range(len(new_text)):
        if new_text[i] == key:
            count += 1
            if count == 2:
                print(i)
                break
    if count < 2:
        print("-1")
            
find_coincidence(text_1, key_word)
