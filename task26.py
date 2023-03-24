"""
Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
 и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 

"""
def degree(a,b):
    if b==1:
        return a
    return degree(a,b-1)*a
a=int(input("Введите число A = "))
b=int(input("Введите число B = "))
if b>0:
    print(f" A в степени B = {degree(a,b)}")
elif b==0:
    print(f" A в степени B = 1 ")
else :
    res=1/(degree(a,-b))
    print(f" A в степени B = {res}")