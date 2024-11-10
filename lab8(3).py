# Лимарев Степан ИУ7-11Б. 
# Программа ищет столбец в матрице, имеющий определённое свойство по варианту.
# Наименьшее количество отрицательных элементов.


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
    min_negatives_count = rows
    result_column_index = None


    # Поиск столбца с наименьшим количеством отрицательных элементов.
    for col in range(cols):
        negatives_count = 0
        for row in range(rows):
            if matrix[row][col] < 0:
                negatives_count += 1
            
        if negatives_count < min_negatives_count:
            min_negatives_count = negatives_count
            result_column_index = col
        

    # Вывод изменённой матрицы в виде форматированной таблицы чисел.
    border_length = 5 * cols  # Длина верхней границы
    header = '-' * border_length

    if result_column_index is not None:
        print("Столбец с наименьшим количеством отрицательных элементов: ")


        # Вывод верхней границы.
        print(header)


        for i in range(rows):
            print(f"| {matrix[i][result_column_index]:^11} |")
        

        # Вывод нижней границы.
        print(header)


    else:
        print("Все столбцы содержат одинаковое количество отрицательных элементов")