# Лимарев Степан ИУ7-11Б. Программа удаляет элемент с заданным индексом из списка с использованием любых средств Python.


# Приглашение пользователя на ввод количества элементов списка.
n = int(input("Введите количество элементов в списке: "))
lst = []


# Цикл для ввода каждого элемента списка.
for i in range(n):

    item = int(input("Введите элемент списка: "))
    lst.append(item)


# Приглашение пользователя на ввод индекса.
remove_index = int(input("Введите индекс элемента для удаления: "))


# Проверка корректности введённого индекса.
if remove_index >= len(lst) or remove_index < 0:

    print("Введён некорректный индекс. Значение индекса должно быть положительным и не должно выходить за пределы списка.")

else:


    # Удаление элемента из списка по индексу.
    lst.pop(remove_index)


    # Вывод изменённого списка.
    print(lst)