# Лимарев Степан ИУ7-11Б. Программа изменяет элемент в списке строк по варианту.
# Замена всех заглавных согласных английских букв на строчные.


# Приглашение пользователя на ввод количества элементов списка.
n = int(input("Введите количество элементов в списке: "))
lst = []


# Цикл для ввода каждого элемента списка.
for i in range(n):

    item = (input("Введите элемент списка: "))
    lst.append(item)


# Необходимые переменные.
vowels = 'aeiouy'


# Замена всех заглавных согласных английских букв на строчные.
for i in range(len(lst)):

    elem = list(lst[i])
    
    for j in range(len(elem)):

        if elem[j].isupper() and elem[j] not in vowels:

            elem[j] = elem[j].lower()
        lst[i] = ''.join(elem)


# Вывод изменённого списка.
print(lst)


