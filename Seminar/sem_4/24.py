# В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены 
# только по окружности. Таким образом, у каждого куста 
# есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени 
# бора на них выросло различное число ягод – на i-ом кусте 
# выросло ai ягод. В этом фермерском хозяйстве внедрена система 
# автоматического сбора черники. Эта система состоит из управляющего 
# модуля и нескольких собирающих модулей. Собирающий модуль за один 
# заход, находясь непосредственно перед некоторым кустом, собирает 
# ягоды с этого куста и с двух соседних с ним. Напишите программу 
# для нахождения максимального числа ягод, которое может собрать 
# за один заход собирающий модуль, находясь перед некоторым кустом 
# заданной во входном файле грядки.

my_lst = [int(x) for x in input('Задайте колличество ягот на кусту: ').split()]

max_sum = list()

for i in range(len(my_lst) - 1):
    max_sum.append(my_lst[i - 1] + my_lst[i] + my_lst[i + 1])

max_sum.append(my_lst[-2] + my_lst[-1] + my_lst[0])
print(max(max_sum))