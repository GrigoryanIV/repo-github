# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
import itertools
import math

def fact(num):
  for i in itertools.count(1,1):
    if i <= num:
      yield math.factorial(i)
    else:
      break
      
for el in fact(5):
  print(el)
