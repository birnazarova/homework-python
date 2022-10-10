# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

from curses.ascii import isdigit


mnogochlen1 = "2a + b + 5"
mnogochlen2 = "3a**2 + 6b + 1"

summa = []

alltogether = mnogochlen1 + " + " + mnogochlen2
split_alltogether = list(map(str, alltogether.split()))
print(split_alltogether)

ashki = []
stepeni = []
bshki = []
numbers = []

for i in split_alltogether:
    if "a" in i and not "**" in i:
        ashki.append(i)
        print(ashki)
    elif "**" in i:
        stepeni.append(i)
        print(stepeni)
    elif "b" in i:
        bshki.append(i)
        print(bshki)
    elif i.isdigit():
        numbers.append(i)
        print(numbers)

summa.append(stepeni)

if len(ashki) == 1:
    summa.append(ashki)
else:
    ashki_list = list(map(str, ashki.split()))
    for i in ashki_list:
        if i.isdigit():
            count = 0
            count += int(i)
        else:
            ashki_list.append

