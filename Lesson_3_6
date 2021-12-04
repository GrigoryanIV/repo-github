#  Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
text = ""
def int_func(str_x):
    return str_x.capitalize()

def int_func_text(txt):
    m = 0
    n = len(txt)
    while m < n:
        txt[m] = int_func(txt[m])
        m = m + 1
    return txt

str_x = input("Введите набор слов, разделённых пробелом: ")
txt = str_x.split()
str_text = int_func_text(txt)
my_text = " ".join(str_text)
print(f"Итоговый результат: - {my_text} ")
