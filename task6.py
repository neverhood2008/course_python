"""
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
расплачивались за проезд и получали билет с номером. Счастливым
билетом называют такой билет с шестизначным номером, где сумма
первых трех цифр равна сумме последних трех. Т.е. билет с номером
385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
программу, которая проверяет счастливость билета.

"""
number=int(input("Введите номер счастливого билета = "))
if number in range(100000,1000000,1):
    sumLast=number%10+number//10%10+number//100%10
    sumFirst=number//1000%10+number//10000%10+number//100000%10
    if sumFirst==sumLast:
        print("Билет счастливый")
    else :
        print("Билет несчастливый")
else :
    print("Введите шестизначное число счастливого билета")

#2 способ

num=int(input("Введите номер счастливого билета = "))
num2=num
count=0
summaLast=0
summaFirst=0
while num2>0:
    count+=1
    num2=num2//10
print (count)
for i in range(0,count//2,1):
    summaLast=summaLast+num%10
    num=num//10
    i+=1
print(summaLast)
if count%2!=0:
    num=num//10
for i in range(0,count//2,1):
    summaFirst=summaFirst+num%10
    num=num//10
    i+=1
print(summaFirst)
if summaFirst==summaLast:
    print("Билет счастливый")
else :
    print("Билет несчастливый")




