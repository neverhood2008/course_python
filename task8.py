"""
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить 
k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
"""
n=int(input("Введите n долек шоколадки =  "))
m=int(input("Введите m долек шоколадки =  "))
k=int(input("Введите k долек шоколадки =  "))
if  (k<=m*n):
    if (k%m==0 or k%n==0):
        print(f" {k} долек можно отломить по 1 разлому")
    else :
        print(f" {k} долек нельзя отломить по 1 разлому")
else :
    print("Долек больше,чем есть в шоколадке")
