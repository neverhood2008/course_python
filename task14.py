#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
n=int(input("Введите число = "))
temp=1
while temp<=n:
    print(temp)
    temp=temp*2
