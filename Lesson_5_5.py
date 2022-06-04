# Создать (программно) текстовый файл, записать в него программно набор чисел,
import common
NoProblem = True
my_list = []

my_file = open("myfile.txt","w")
my_line = input("Введите числа через пробелы: ")
my_file.write(my_line)
my_file.close()

with open("myfile.txt") as my_file:
  my_text = my_file.read()
  my_lst = my_text.split()
  
for el in my_lst:
  el = common.chislo(el)
  my_list.append(el)
  if el == None:
    NoProblem = False
    
if NoProblem:
  print(f"Сумма чисел в файле {sum(my_list)}")
else:
  print("Введённое значение не является числом")
  