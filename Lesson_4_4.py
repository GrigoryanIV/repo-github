#   Определить элементы списка, не имеющие повторений.

import random

n = 0
lst_my = []
lst_temp = []
lst_new = []
while n<30:
    lst_my.append(random.randint(0,50))
    n+=1

for el in set(lst_my):
    a = lst_my.count(el)
    if a==1:
            lst_temp.append(el)

for el in lst_my:
    if el in lst_temp:
            lst_new.append(el)

print(f"Первоначальный список : - {lst_my} ")
print(f"Список после обработки: - {lst_new} ")
