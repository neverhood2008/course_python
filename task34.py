"""
Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
в порядке
Ввод: Вывод:
пара-ра-рам рам-пам-папам па-ра-па-дам Парам пам-пам
"""
#1способ

def count_str(list_1):
    counter=[]
    
    for phrase in list_1:
        count1=0
        for letter in phrase:
            if letter in russian_alphabet:
                count1+=1
        counter.append(count1)
        
       
    return counter
result=input("Введите строку ").lower().split()
print(result)
russian_alphabet={"а", "я", "у", "ю", "о", "е", "ё", "э", "и", "ы"}
result=count_str(result)
print(result)
result=set(result)
if len(result)==1:
    print("рифма есть")
else :
     print("рифмы нет")

#2способ
# пара-ра-рам рам-пам-папам па-ра-па-дам 
def rifma(result):
    list_counter=[] #[4,4,4]
    for phrase in result: # prase = 'пара-ра-рам' 
        
        temp=list(filter(lambda symbol1 : symbol1 in russian_alphabet,phrase)) # [а,а,а,а]
        sum_v=len(temp)  # 4
        list_counter.append(sum_v)
    print(list_counter)
    list_counter=set(list_counter)
    if len(list_counter)>1:
        print("нет рифмы")
    else:
        print("есть рифма")      

russian_alphabet={"а", "я", "у", "ю", "о", "е", "ё", "э", "и", "ы"}    
result=input("Введите строку (2 способ) ").lower().split()
rifma(result)