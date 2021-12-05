# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
d = 0
theend = False

def my_func (str_x):
    m = 0
    lst_d = str_x.split()
    n = len(lst_d)
    while m < n:
        if lst_d[m].isdigit():
            lst_d[m] = int(lst_d[m])
        else:
            lst_d[m] = 0
        m = m + 1
    return lst_d

def my_func_1 (lst_x):
    m = 0
    n = len(lst_x)
    d = 0
    while m < n:
        d = d + lst_x[m]
        m = m + 1

    return d


while theend == False:

    str_1 = input("Введите строку чисел, разделённых пробелом: ")
    if str_1.count("*") > 0:
        if str_1.index("*") == 0:
            break
        else:
            str_x = str_1.replace("*","")
            theend = True
    else:
        str_x = str_1

    
    lst_x = my_func(str_x)
    d = d + my_func_1(lst_x)
    print(f"Итоговый результат: - {d} ")
