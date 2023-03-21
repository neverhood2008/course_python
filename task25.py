"""Задача №25. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()
"""
"""
s= "a a a b c a a d c d d".split() 
new_dist = {} 
for i in s:    
    if i in new_dist:         
        print(f'{i}_{new_dist[i]}', end = " ")       
        print(new_dist[i])  
        print(type(new_dist))
        new_dist[i]+=1     
    else:         
        new_dist[i]=1         
        print(i, end=" ")
print(new_dist)
"""
text_user= "a a a b c a a d c d d".split() 
text_unique = set(text_user) 
for elem in text_unique: 
    counter = text_user.count(elem)  
    if counter > 1:      
        j = text_user.index(elem)  
    for i in range(1, counter):       
        text_user[text_user.index(elem, j + 1)] = elem + '_' + str(i) 
print('Результат: ', end=' ') 
print(' '.join(text_user))