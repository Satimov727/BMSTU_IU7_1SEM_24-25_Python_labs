# Лимарев Степан ИУ7-11Б. 
# Программа ищет строку в матрице, имеющую определённое свойство по варианту.
# Наибольшее количество чётных элементов.


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
    max_even_count = 0
    row_index = 0


    # Нахождение строки с наибольшим количеством четных элементов.
    for i in range(len(matrix)):
        even_count = 0
        for element in matrix[i]:
            if element % 2 == 0:
                even_count += 1
        
        if even_count > max_even_count:
            max_even_count = even_count
            row_index = i


    # Вывод результата.
    if max_even_count > 0:
        print(f'Строка {row_index + 1} содержит наибольшее количество четных элементов ({max_even_count})')
    else:
        print("Четных элементов в матрице нет")