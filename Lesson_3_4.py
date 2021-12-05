# Необходимо выполнить возведение числа x в степень y (y-отрицательное)
import common

def my_func (x,y):
    d = 1 / (x**y)
    return d

def my_func_1 (x,y):
    n = 1
    d = x
    while n < y:
        n = n + 1
        d = d*x

    return 1 / d

a = input ("Введите число x ")
x = common.chislo(a,3)
a = input ("Введите число y ")
y = common.chislo(a,)

print(f"Итоговый результат:  {my_func (x,y)} ")
print(f"Итоговый результат:  {my_func_1 (x,y)} ")