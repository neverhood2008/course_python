"""

Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону (т.е. 
не меньше заданного минимума и не больше заданного максимума)

"""
from random import randint

def fill_array(n):
    list=[randint (-20,20) for _ in range(n)]
    print(list)
    return list
def range_elements(array,list_range):
    list=[]
    for i in range(len(array)):
        if list_range[0]<=array[i]<=list_range[1]:
            list.append(i)
    return list
count=int(input("Введите количество элементов массива = "))
array_new=fill_array(count)
min_range=int(input("Введите минимальный элемента диапазона = "))
max_range=int(input("Введите максимальный элемента диапазона = "))
list_range=[min_range,max_range]
print(list_range)
print(f"Позиции элементов в диапазоне {list_range} : ", end= "")
print(*range_elements(array_new,list_range))