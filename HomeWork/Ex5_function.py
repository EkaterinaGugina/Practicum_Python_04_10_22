# НАБОР ФУНКЦИЙ к ЗАДАЧЕ:  Ex5_sum_polynom  Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# Например, 2*x² + 4*x + 5 = 0 и 2*x^4 + 4*x^3 + 5x^2 = 0  --> 2*x^4 + 4*x^3 + 7x^2 + 4*x + 5 = 0
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