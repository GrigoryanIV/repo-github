# скрипт - итератор, генерирующий целые числа, начиная с указанного
import common
import itertools
from sys import argv

begin, kol = argv

a = common.chislo(begin)

if kol.isdigit():
    b = int(begin)
else:
    b = 10

if a is None:
    print("Необходимо ввести число")
else:

    for el in itertools.count(a):
        if el > (a + b-1):
            break
        print(el)
        
# итератор, повторяющий элементы некоторого списка, определенного заранее

lst_my =['a1', 'a2', 'a3', 'a4', 'a5']
n = 0

for el in itertools.cycle(lst_my):
    print(el)
    n+=1
    if n > 20:
        break
    