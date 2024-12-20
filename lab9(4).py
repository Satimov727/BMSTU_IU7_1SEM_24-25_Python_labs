# Лимарев Степан ИУ7-11Б.
# Задана матрица D и массив I, содержащий номера строк, для которых необходимо определить максимальный элемент. Значения максимальных
# элементов запомнить в массиве R. Определить среднее арифметическое вычисленных максимальных значений. Напечатать матрицу D, массивы I и R,
# среднее арифметическое значение.


# Приглашение пользователя на ввод размерности матрицы D.
rows = int(input("Введите количество строк матрицы: "))
cols = int(input("Введите количество столбцов матрицы: "))
D = []


# Цикл для ввода каждого элемента матрицы.
for i in range(rows):
    row = list(map(int, input(f"Введите элементы {i+1}-й строки матрицы через пробел: ").split()))
    D.append(row)


# Приглашение пользователя на ввод списка I.
k = int(input("Введите количество номеров строк: "))
I = []


# Проверка корректности ввода списка.
while len(I) < k:
    index = int(input(f"Введите номер строки: "))
    if 1 <= index <= rows:
        I.append(index)
    else:
        print("Неверный номер строки. Номер должен быть от 1 до", rows)


# Поиск максимальных элементов для указанных строк.
R = []
for index in I:
    # Преобразуем индекс к нулю, так как вводим с 1.
    current_row = D[index - 1]
    max_value = current_row[0]
    for value in current_row:
        if value > max_value:
            max_value = value
    R.append(max_value)


# Вычисляем сумму и среднее арифметическое.
total_sum = 0
for value in R:
    total_sum += value

if len(R) == 0:
    average_max = 0
else:
    average_max = total_sum / len(R)

# Вывод результатов
print("\nМатрица D:")
for row in D:
    print(*row, end=' ')

print("\nМассив индексов I:", I)
print("\nМассив максимальных значений R:", R)
print(f"\nСреднее арифметическое максимальное значение: {average_max:.2f}")
