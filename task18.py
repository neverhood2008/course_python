"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по
 величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N 
 – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
"""
n=int(input("ВВедите число элементов массива =  "))
x=int(input("ВВедите число X =  "))
list=[int(input(f"Введите {i} элемент массива ")) for i in range(n)]
print(list)
uniq=set()
max=list[0]
difference=abs(list[0]-x)
for i in range(1,n):
    if abs(list[i]-x)<difference and list[i]!=x:
        max=list[i]
        difference=list[i]-x
        uniq.clear
        uniq.add(max)
    elif  abs(list[i]-x)==difference and list[i]!=x:
        uniq.add(max)
print(f"Самое близкое число к {x} = {uniq}")

