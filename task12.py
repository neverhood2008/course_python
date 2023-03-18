"""Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.
"""
"""
import math
summa=int(input("Введите сумму двух чисел = "))
multiply=int(input("Введите произведение двух чисел = "))
key=False
temp1=0
for i in range(1,1001):
    for j in range(1,1001):
        if (i*j==multiply) and (i+j==summa) and (j!=temp1):
            print(f"загаданные числа : {i} , {j}")
            temp1=i
            temp2=j
            key=True
        j+=1
    i+=1
if key==False:
      print("таких чисел не существует")

# x = int(input()) # сумма
# y = int(input()) # произведение
# for i in range(1, x):
#     for j in range(y):
#         if x == i + j and y == i * j:
#             print(i, j)


"""
s=int(input(""))
p=int(input(""))
for i in range(1,s//2+2):
     if i*(s-i)==p:
          print(f"{i} {s-i}")