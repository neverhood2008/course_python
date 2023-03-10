"""Задача 2: Найдите сумму цифр трехзначного числа. """
number=abs(int(input("Введите число ")))
if number in range(100,999+1,1):
    print(f"Сумма цифр числа = {number%10+(number//10)%10+(number//100)}")
else :
    print ("Введите трехзначное число")
#2 способ

summa=0
while number>0:
    summa=summa+number%10
    number=number//10
print(f"Сумма цифр числа вторым способом = {summa}")
