# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов
import common

def my_func (a,b,c):
    lst_abc = [a,b,c]
    lst_abc.sort(reverse=True)
    d = lst_abc[0] + lst_abc[1]
    return d

a1 = input("Введите первое число: ")
a1 = common.chislo(a1,4)
a2 = input("Введите второе число: ")
a2 = common.chislo(a2,4)
a3 = input("Введите третье число: ")
a3 = common.chislo(a3,4)

if a1 is None or a2 is None or a3 is None:
    print("Некорректный ввод данных")
else:
    print(f"Итоговый результат: - {my_func (a1,a2,a3)} ")