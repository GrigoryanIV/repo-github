# скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника
import common
from sys import argv

hours, stavka, bonus = argv

hours = input("Введите количество отработанных часов - ")
stavka = input("Введите ставку - ")
bonus = input("Введите сумму премии - ")

a = common.chislo(hours,3)
b = common.chislo(stavka,3)
c = common.chislo(bonus)

if a != None or b != None or c != None:
    d = a * b + c
    print(f"Ваша заработная плата: - {d} ")
else:
    print("Введите корректное значение")


