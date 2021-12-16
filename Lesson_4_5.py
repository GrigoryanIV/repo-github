#   В список должны войти четные числа от 100 до 1000 (включая границы).

import random

n = 0
a = 1

lst_my = [i for i in range(100,1001,2)]

while n < (len(lst_my)-1):
    a = a * lst_my[n]
    n+=1

print(f"Первоначальный список : - {lst_my} ")
print(f"Результат вычисления: - {a} ")
