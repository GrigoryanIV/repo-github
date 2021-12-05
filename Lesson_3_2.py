# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон

def concatination (name,surname,year,city,email,phone ):
    a = name + " " + surname + " " + year + " " + city + " " + email + " " + phone
    return a


name = input("Введите имя: ")
surname = input("Введите фамилию: ")
year = input("Введите год рождения: ")
city = input("Введите город проживания: ")
email = input("Введите email: ")
phone = input("Введите телефон: ")

print(f"Итоговый результат: - {concatination (name,surname,year,city,email,phone )} ")
