"""Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.
"""
import math
summa=int(input("Введите сумму двух чисел = "))
multiply=int(input("Введите произведение двух чисел = "))
i=1
j=1
key=False
temp1=0
for i in range(1,1000+1):
    for j in range(1,1000+1):
        if (i*j==multiply) and (i+j==summa) and (j!=temp1):
            print(f"загаданные числа : {i} , {j}")
            temp1=i
            temp2=j
            key=True
        j+=1
    i+=1
if key==False:
      print("таких чисел не существует")
