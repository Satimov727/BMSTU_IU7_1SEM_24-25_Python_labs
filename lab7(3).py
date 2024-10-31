# Лимарев Степан ИУ7-11Б. Программа ищет элемент в списке строк по варианту.
# Элемент наибольшей длины, не содержащий английских гласных.


# Приглашение пользователя на ввод количества элементов списка.
n = int(input("Введите количество элементов в списке: "))
lst = []


# Цикл для ввода каждого элемента списка.
for i in range(n):

    item = (input("Введите элемент списка: "))
    lst.append(item)


# Необходимые переменные.
max_length = 0
max_elem = None


# Поиск элемента наибольшей длины, не содержащего английских гласных.
# Проверка элемента на наличие английской гласной.
for elem in lst:

    has_vowel = False

    for char in elem:

        if char in 'aeiouy' or char in 'AEIOUY':

            has_vowel = True

            break


    # Если гласной нет.
    if not has_vowel:

        length = len(elem)

        if length > max_length:

            max_length = length
            max_elem = elem


# Вывод элемента максимальной длины.
print(max_elem)