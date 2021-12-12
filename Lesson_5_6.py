# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету 
def my_form(my_str):
  new_str = str()
  for el in my_str:
    if el.isdigit():
      new_str = new_str + el
  if new_str.isdigit():
    return int(new_str)
  else:
    return 0

with open("lab.txt",encoding='utf-8') as my_file:

  my_dict = dict()
  dict_result = dict()

  for line in my_file:
    n = 0
    b = []
    my_lst = line.split()
    for el in my_lst:
      n += 1
      if n == 1:
        pr = el
        my_dict[pr] = ""
      else:
        a = my_form(el)
        b.append(a)
        my_dict[pr] = b

for k in my_dict.keys():
  dict_result[k] = sum(my_dict[k])
  
print(dict_result)
  

  