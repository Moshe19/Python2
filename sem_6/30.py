# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input('Введите первый элемент арифметической прогрессии: ')) 
d = int(input('Укажите разность прогрессии: ')) 
n = int(input('Задайте количество элементов: ')) 
for i in range(n): 
    print(a1 + i * d)