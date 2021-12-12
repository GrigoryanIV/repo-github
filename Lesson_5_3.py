# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.

with open("stuff.txt",encoding='utf-8') as my_file:
  n = 0
  my_list = list()
  my_lst = list()
  for line in my_file:
    n+=1
    my_lst.append(line.split())

print(f"Всего количество персонала - {n}")

for el in my_lst:
    my_list.append(int(el[1]))
    
print(f"Средняя зарплата - {sum(my_list)/len(my_list)}")
print("Список сотрудников с зарплатой меньше 20000")
for el in my_lst:
  if int(el[1]) < 20000:
    print(el[0])