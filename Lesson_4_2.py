#   Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

import random

n = 0
lst_my = [101]
lst_new = []
while n<20:
    lst_my.append(random.randint(0,100))
    n+=1

n = 0
while n < (len(lst_my)-1):
    n = n + 1
    if lst_my[n] > lst_my[n-1]:
        lst_new.append(lst_my[n])

lst_my.pop(0)
print(f"Первоначальный список : - {lst_my} ")
print(f"Список после обработки: - {lst_new} ")
