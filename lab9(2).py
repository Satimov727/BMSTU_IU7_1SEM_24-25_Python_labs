# Лимарев Степан ИУ7-11Б.
# Программа поворачивает квадратную целочисленную матрицу на 90 градусов по часовой стрелке, 
# затем на 90 градусов против часовой стрелки. Выводит исходную, промежуточную и итоговую матрицы. 


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


    # Вывод исходной матрицы
    print("Исходная матрица:")
    for row in matrix:
        for col in row:
            print(f"{col:4}", end=" ")
        print()


    # Поворот на 90 градусов по часовой стрелке
    for layer in range(len(matrix) // 2):
        first, last = layer, len(matrix) - layer - 1
        for i in range(first, last):
            top = matrix[first][i]
            
            # Перемещаем левый элемент вправо
            matrix[first][i] = matrix[-i - 1][first]
            
            # Перемещаем нижний элемент вверх
            matrix[-i - 1][first] = matrix[last][-i - 1]
            
            # Перемещаем правый элемент вниз
            matrix[last][-i - 1] = matrix[i][last]
            
            # Перемещаем верхний элемент влево
            matrix[i][last] = top


    # Вывод промежуточной матрицы
    print("Промежуточная матрица (поворот на 90 градусов по часовой стрелке):")
    for row in matrix:
        for col in row:
            print(f"{col:4}", end=" ")
        print()


    # Поворот на 90 градусов против часовой стрелки
    for layer in range(len(matrix) // 2):
        first, last = layer, len(matrix) - layer - 1
        for i in range(first, last):
            top = matrix[first][i]
            
            # Перемещаем правый элемент вверх
            matrix[first][i] = matrix[i][last]
            
            # Перемещаем нижний элемент вправо
            matrix[i][last] = matrix[last][-i - 1]
            
            # Перемещаем левый элемент вниз
            matrix[last][-i - 1] = matrix[-i - 1][first]
            
            # Перемещаем верхний элемент влево
            matrix[-i - 1][first] = top


    # Вывод итоговой матрицы
    print("Итоговая матрица (поворот на 90 градусов против часовой стрелки):")
    for row in matrix:
        for col in row:
            print(f"{col:4}", end=" ")
        print()
