# Создать текстовый файл (не программно),  выполнить подсчет количества строк, количества слов в каждой строке.

with open("test.txt",encoding='utf-8') as my_file:
  n = 0
  m = 0
  for line in my_file:
    n+=1
    my_lst = line.split()
    m = len(my_lst)
    print(line)
    print(f"Количество слов в строке № {n} - {m}")
    print("*****************************************")

print(f"Всего количество строк - {n}")
   