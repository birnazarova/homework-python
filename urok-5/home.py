# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

with open('/Users/aika/Desktop/Git/python/homework-python/urok-5/file.txt', 'r') as data:
    text = data.read()


def coding_text(text):
    i = 0
    encoding = ""
    while i < len(text):
        count = 1 # колво вхождений символа в индексе i

        while i+1 < len(text) and text[i] == text[i+1]:
            count = count + 1
            i = i + 1
       # добавляет к результату текущий символ и его количество
        encoding += str(count) + text[i]
        i = i + 1
 
    return encoding

print(coding_text(text))

with open('/Users/aika/Desktop/Git/python/homework-python/urok-5/file2.txt', 'w') as data:
    text2 = data.write(coding_text(text))

with open('/Users/aika/Desktop/Git/python/homework-python/urok-5/file2.txt', 'r') as data:
    text2 = data.read()

# Выполнение алгоритма сжатия данных кодирования длин серий (RLE) для строки `str`
def decoding_text(text2):
    count = ''
    str_decode = ''
    for char in text2:
        if char.isdigit():
            count += char
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode

str_decode = decoding_text(text2)
print(str_decode)