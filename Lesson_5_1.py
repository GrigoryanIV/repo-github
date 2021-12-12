# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
my_file = open("myfile.txt","w")
while True:
  my_line = input("Введите строку: ")
  if my_line == "":
    break
  my_file.write(my_line + "\n")
my_file.close()  
