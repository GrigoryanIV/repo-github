#   Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.

lst_my = [i for i in range(20,240) if i%20==0 or i%21==0]
print(f"Список чисел кратных 20 или 21: - {lst_my} ")