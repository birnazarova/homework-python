# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_text = list(' Напишите программу, удаляющую из текста все слова, содержащие ""абв"" '.split())
for i in my_text:
    if 'абв' not in i:
        print(i, end=' ')