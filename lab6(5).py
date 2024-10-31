# Лимарев Степан ИУ7-11Б. Программа меняет местами элементы с характеристиками по варианту.
# Минимальный положительный и максимальный положительный.


# Приглашение пользователя на ввод списка.
n = int(input("Введите количество элементов в списке: "))
lst = []


# Цикл для ввода каждого элемента списка.
for i in range(n):

    item = int(input("Введите элемент списка: "))
    lst.append(item)


# Необходимые переменные.
min_val = None
max_val = None


# Циклическое вычисление минимального положительного и максимального положительного элемента списка.
for num in lst:

    if num > 0:

        if min_val is None or num < min_val:

            min_val = num

        if max_val is None or num > max_val:

            max_val = num

if min_val is not None:

    min_idx = lst.index(min_val)
    max_idx = lst.index(max_val)
    temp = lst[min_idx]
    lst[min_idx] = lst[max_idx]
    lst[max_idx] = temp


# Вывод изменённого списка.
print(lst)

