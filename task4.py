"""Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
они сделали S журавликов. Сколько журавликов сделал каждый
ребенок, если известно, что Петя и Сережа сделали одинаковое
количество журавликов, а Катя сделала в два раза больше журавликов,
чем Петя и Сережа вместе?
"""
number=int(input("Введите общее число журавликов = "))
if number%6==0:
    print(f"Петя и Сережа сделали по {number//6} журавликов/а, а Катя сделала {4*number//6} журавликов")
else :
    print("С данным числом решить задачу невозможно, введите число кратное 6")
