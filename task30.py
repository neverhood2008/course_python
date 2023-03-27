"""
Задача 30:  Заполните массив элементами арифметической прогрессии.
 Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
 Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""
def progression(first_element,diff,count_elements):
    list=[]
    list.append(first_element)
    for i in range(2,count_elements+1):
        list.append(first_element+(i-1)*diff)
    return list    

first_element=int(input("Введите первый элемент = "))
difference_elements=int(input("Введите разницу = "))
count_elements=int(input("Введите количество элементов = "))

print(*progression(first_element,difference_elements,count_elements))