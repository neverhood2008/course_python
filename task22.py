"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12

"""
count_1=int(input("Введите количество элементов 1 набора = "))
list_1=list(int(input(f" Введите {i} элемент 1 набора = ")) for i in range(count_1))
count_2=int(input("Введите количество элементов 2 набора = "))
list_2=list(int(input(f" Введите {i} элемент 2 набора = ")) for i in range(count_2))
print(list_1)
print(list_2)
list_1=set(list_1)
list_2=set(list_2)
new_list=list_1.intersection(list_2)
print(f"Результат = {sorted(new_list)}")
