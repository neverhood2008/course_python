"""
Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов или символами конца строки.Определите,
сколько различных слов содержится в этом тексте.
Input: She sells sea shells on the sea shore;The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore,I'm sure that the shells are sea
shore shells.
Output: 19

"""
text_user=''' She sells sea shells on the sea shore;The shells
that she sells '''
text_user=text_user.lower()
print(f'результат = {len(set(text_user.split()  )   ) }')