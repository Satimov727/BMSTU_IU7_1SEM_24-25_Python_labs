# Ввод размера матриц
rows_A = int(input("Введите количество строк матрицы A: "))
cols_A = int(input("Введите количество столбцов матрицы A: "))
rows_B = int(input("Введите количество строк матрицы B: "))
cols_B = int(input("Введите количество столбцов матрицы B: "))

# Проверка возможности умножения матриц
if cols_A != rows_B:
    print("Невозможно умножить матрицы.")
else:


    # Ввод матриц
    A = []
    print("Введите элементы матрицы A:")
    for _ in range(rows_A):
        row = list(map(int, input().split()))
        A.append(row)

    B = []
    print("Введите элементы матрицы B:")
    for _ in range(rows_B):
        row = list(map(int, input().split()))
        B.append(row)


    # Создание результирующей матрицы C.
    C = []
    for i in range(rows_A):
        row = []
        for j in range(cols_B):
            element = 0
            for k in range(cols_A):
                element += A[i][k] * B[k][j]
            row.append(element)
        C.append(row)


    # Вывод матриц.
    print("Матрица A:")
    for row in A:
        for col in row:
            print(f"{col:4}", end=" ")
        print()
    
    print("Матрица B:")
    for row in B:
        for col in row:
            print(f"{col:4}", end=" ")
        print()
    
    print("Матрица C (произведение A и B):")
    for row in C:
        for col in row:
            print(f"{col:4}", end=" ")
        print()