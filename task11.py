"""

Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.

"""
a = int(input('Введите число: ')) 
count = 2 
number0 = 0
number1 = 1
result=1
while result<a: 
        result = number0 + number1 
        number0 = number1      
        number1 = result
        count += 1   
if result==a:  
    print(count)
else :
      print(-1)