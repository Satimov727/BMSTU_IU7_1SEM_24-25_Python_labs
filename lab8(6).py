# Лимарев Степан ИУ7-11Б. 
# Программа выполянет транспонирование квадратной матрицы.


# Приглашение пользователя на ввод размерности квадратной матрицы.
n = int(input("Введите размер квадратной матрицы: "))
matrix = []


# Цикл для ввода каждого элемента матрицы.
for i in range(n):
    row = list(map(int, input(f"Введите элементы {i+1}-й строки матрицы через пробел: ").split()))
    matrix.append(row)


# Проверка корректности ввода матрицы.
if len(matrix) != n or any(len(row) != n for row in matrix):
    print("Введён некорректный размер матрицы")

else:


    # Транспонирование матрицы.
    for i in range(n):
        for j in range(i + 1, n):  # Начинаем со следующего элемента после диагонали
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    

    # Вывод изменённой матрицы в виде форматированной таблицы чисел.
    border_length = 11 * n  # Длина верхней границы
    header = '-' * border_length + '-'


    # Вывод верхней границы.
    print(header)


    # Вывод содержимого таблицы.
    for row in matrix:
        line = '|'
        for item in row:
            line += f"{item:^10.0f}|"
        print(line)
        print(header)  # Нижняя граница строки
