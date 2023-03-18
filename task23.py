
from random import randint 
n = int (input("Введите количество элементов ")) 
counter = 0 
list_1 = [randint(1, 10) for _ in range(n)] 
print(list_1) 
for i in range(1, n):     
    if list_1[i-1] < list_1[i]:   
        counter += 1 
print(counter)

