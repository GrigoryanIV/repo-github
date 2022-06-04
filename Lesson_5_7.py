# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
import json
n = 0
total_profit = 0
my_dict_1 = dict()
my_dict_2 = dict()
lst_result = []

  
with open("firm.txt") as my_file:
 
  for line in my_file:

    my_lst = line.split()
    my_lst.append(int(my_lst[2])-int(my_lst[3]))
    if my_lst[4] > 0:
      n += 1
      total_profit = total_profit + my_lst[4]
    my_dict_1[my_lst[0]] = my_lst[4] 
        

my_dict_2["average_profit"] = int(total_profit/n)

lst_result.append(my_dict_1)
lst_result.append(my_dict_2)

with open("firm.json", "w") as my_file:
  json.dump(lst_result, my_file)

  

  