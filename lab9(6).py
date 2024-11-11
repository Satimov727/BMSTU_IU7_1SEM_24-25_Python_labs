# Лимарев Степан ИУ7-11Б.
# Дана матрица символов. Преобразовать её следующим образом: заменить все согласные латинские букв на заглавные, а все гласные латинские буквы на
# строчные. Вывести матрицу до преобразования и после.


# Приглашение пользователя на ввод размерности матрицы.
rows = int(input("Введите количество строк матрицы: "))
cols = int(input("Введите количество столбцов матрицы: "))
matrix = []


# Цикл для ввода каждого элемента матрицы.
for i in range(rows):
    row = input(f"Введите элементы {i+1}-й строки матрицы через пробел: ").split()
    matrix.append(row)


# Преобразовываем каждую строку матрицы.
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        element = matrix[i][j]
        new_element = ''
        
        for char in element:
            if char.isalpha():
                if char in 'aeiou':
                    new_element += char.lower()
                else:
                    new_element += char.upper()
            else:
                new_element += char
        
        matrix[i][j] = new_element

# Вывод результатов.
print("Матрица до преобразования:")
for row in matrix:
    for col in row:
        print(f"{col:4}", end=" ")
    print()

print("\nМатрица после преобразования:")
for row in matrix:
    for col in row:
        print(f"{col:4}", end=" ")
    print()