# Лимарев Степан ИУ7-11Б. 
# Программа переставляет местами строки в матрице 
# с наибольшим и наименьшим количеством отрицательных элементов.


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
    min_negatives = rows * cols  # Максимально возможное количество отрицательных элементов
    max_negatives = 0   # Минимально возможное количество отрицательных элементов
    min_index = None
    max_index = None


    # Перебираем каждую строку матрицы
    for i in range(rows):
        negatives_in_row = 0  # Счетчик отрицательных элементов в данной строке
        
        for j in range(cols):
            if matrix[i][j] < 0:
                negatives_in_row += 1
                
        if negatives_in_row < min_negatives:
            min_negatives = negatives_in_row
            min_index = i
            
        if negatives_in_row > max_negatives:
            max_negatives = negatives_in_row
            max_index = i


    # Перестановка строк.
    if min_index is not None and max_index is not None:
        matrix[min_index], matrix[max_index] = matrix[max_index], matrix[min_index]


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
