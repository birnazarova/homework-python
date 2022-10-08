# Реализуйте алгоритм перемешивания списка.
# import random

# given_list = [1, 6, 3, 679, "some_string"]
# random.shuffle(given_list)
# print(given_list)

### Другой способ ###

import random

given_list = [1, 6, 3, 679, "some_string"]
print(f"Given list: {given_list}")
mixed_list = given_list[:]
list_len = len(mixed_list) 
for i in range(list_len): 
    random_index = random.randint(0, list_len - 1) # 3
    temp_var = mixed_list[i] # нулевой элемент списка mixed_list равен временной переменной temp_var
    mixed_list[i] = mixed_list[random_index] # нулевой элемент списка mixed_list переносим на индекс под рандомным номером
    mixed_list[random_index] = temp_var
print(f"Mixed list: {mixed_list}")

### Teacher's solution ###

list = ["Anna", "Alex", 3.14159, 0]
for i in range(len(list)):
    index_a = random.randint(0, len(list) - 1)
    list[i], list[index_a]=list[index_a],list[i]