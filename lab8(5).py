# Лимарев Степан ИУ7-11Б. 
# Программа находит максимальное значение в квадратной матрице над главной диагональю и минимальное - под побочной диагональю.


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


    # Максимум над главной диагональю.
    max_value = matrix[0][1]
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]


    # Минимум под побочной диагональю.
    min_value = matrix[n - 1][0]
    for i in range(n):
        for j in range(n - i, n):
            if matrix[i][j] < min_value:
                min_value = matrix[i][j]


    # Вывод результата.
    print(f"Максимальное значение над главной диагональю: {max_value}")
    print(f"Минимальное значение под побочной диагональю: {min_value}")
