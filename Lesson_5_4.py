# Создать (не программно) текстовый файл со следующим содержимым:
import sys

en_dict = dict()
en_dict["one"] = "Один"
en_dict["two"] = "Два"
en_dict["three"] = "Три"
en_dict["four"] = "Четыре"

def form(my_str):
  new_str = my_str.lower()
  new_str = new_str.strip() 
  return new_str

out_file = open("out_file.txt", "w")
sys.stdout = out_file
with open("test1.txt") as my_file:
  for line in my_file:
    my_lst = line.split("-")
    my_lst[0] = form(my_lst[0])
    my_lst[1] = form(my_lst[1])
    a = en_dict[my_lst[0]]+" - "+my_lst[1]
    print(a)

out_file.close()
