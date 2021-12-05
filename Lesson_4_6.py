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
        if el > b:
            break
        print(el)