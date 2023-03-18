"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
 В последующих  строках записаны N целых чисел Ai. 
 Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1

"""
n=int(input("ВВедите число элементов массива =  "))
x=int(input("ВВедите число X =  "))
#list=[int(input(f"Введите {i} элемент массива ")) for i in range(n)]
#print(list)
list=[]
counter=0
for i in range(n):
    list.append(int(input(f"Введите {i} элемент массива ")))
    if x ==list[i]:
        counter+=1
print(list)
print(f"Число {x} встречается в массиве {counter} раз/а")
list2=list.copy()
counter2=0
for i in range(n):
    number=len(str(abs(list2[i])))
   # print(number)
    for j in range(number):
        temp=str(abs(list2[i]))
        if str(x) ==temp[j]:
            counter2+=1
print(f"Цифра {x} встречается в массиве {counter2} раз/а")
