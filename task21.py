"""
Задача №21. Решение в группах
Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
Примечание: Список словарей задан изначально.
Пользователь его не вводит
"""
"""
data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "},
         {" V ":" S009 "}, {" VIII ":" S007 "}] 
unique_values = [] 
for item in data: 
    print(item)    
    for value in item.values():         
        value = value.strip()  # удаляем лишние пробелы вокруг значений        
        if value not in unique_values:            
            unique_values.append(value) 
print(set(unique_values))
"""
"""
my_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
            {"VII": " S005 "}, {" V ":" S009 "},  {" VIII":" S007 "}] 
mno=set()
print(my_list) 
for dict_i in my_list:   
      print(dict_i)    
      for key in dict_i:   
            ma=dict_i[key].strip()
            mno.add(ma)
print(mno)
"""


dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
               {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII": "S007"}] 
n = set() 
for dict_i in dictionary: 
        print(dict_i)  
        for key in dict_i:    
            n.add(dict_i[key]) 
print(n)

