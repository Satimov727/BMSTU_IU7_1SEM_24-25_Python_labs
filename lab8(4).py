# Лимарев Степан ИУ7-11Б. 
# Программа переставляет местами столбцы в матрице с максимальной и минимальной суммой элементов.


# Приглашение пользователя на ввод размерности матрицы.
rows = int(input("Введите количество строк матрицы: "))
cols = int(input("Введите количество столбцов матрицы: "))
matrix = []


# Цикл для ввода каждого элемента матрицы.
for i in range(rows):
    row = list(map(int, input(f"Введите элементы {i+1}-й строки матрицы через пробел: ").split()))
    matrix.append(row)


# Проверка корректности ввода матрицы.
if len(matrix) != rows or any(len(row) != cols for row in matrix):
    print("Введён некорректный размер матрицы")

else:


    # Необходимые переменные.
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    max_sum_index = 0  # Индекс столбца с максимальной суммой
    min_sum_index = 0  # Индекс столбца с минимальной суммой
    max_sum = 0  # Переменная для хранения максимальной суммы
    min_sum = 0  # Переменная для хранения минимальной суммы


    # Вычисление суммы элементов для первого столбца.
    first_column_sum = 0
    for i in range(n_rows):
        first_column_sum += matrix[i][0]
    min_sum = first_column_sum


    for j in range(n_cols):
        # Подсчет суммы элементов текущего столбца
        col_sum = 0
        for i in range(n_rows):
            col_sum += matrix[i][j]


        # Обновление индексов максимума и минимума.
        if col_sum > max_sum:
            max_sum = col_sum
            max_sum_index = j
        if col_sum < min_sum:
            min_sum = col_sum
            min_sum_index = j

    # Перестановка столбцов.
    for i in range(n_rows):
        matrix[i][max_sum_index], matrix[i][min_sum_index] = matrix[i][min_sum_index], matrix[i][max_sum_index]
    

    # Вывод изменённой матрицы в виде форматированной таблицы чисел.
    border_length = 11 * cols  # Длина верхней границы
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