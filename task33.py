"""
Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
Пользователь вводит n – количество элементов массива. Затем пользователь вводит сами элементы массива(цифры).  Необходимо заменить все максимальные элементы в массиве на минимальные.
Input: 5 -> 1 3 3 3 4

Output: 1 3 3 3 1
"""
from random import randint 
def magazin(n):
    array=[int(input()) for _ in range(n)]
    print(array)
    return array

def minmax (array):
    small=min(array)
    large=max(array)
    for i in range(len(array)-1):
        if array[i]==large:
            array[i]=small
    return array

arraynew=magazin(10)
print(minmax(arraynew))
