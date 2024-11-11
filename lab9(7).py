# Лимарев Степан ИУ7-11Б.
# Ввести трёхмерный массив (массив матриц размера X*Y*Z). Вывести срез массива по большему измерению, индекс среза– середина размерности с
# округлением в меньшую сторону


# Приглашение пользователя на ввод размерности трёхмерного массива.
X = int(input("Введите значение высоты трёхмерного массива: "))
while X <= 0:
    print("Некорректный ввод. Значение высоты трёхмерного массива должно быть больше нуля.")
Y = int(input("Введите значение ширины трёхмерного массива: "))
while Y <= 0:
    print("Некорректный ввод. Значение ширины трёхмерного массива должно быть больше нуля.")
Z = int(input("Введите значение глубины массива: "))
while Z <= 0:
    print("Некорректный ввод. Значение глубины трёхмерного массива должно быть больше нуля.")


# Создание пустого трехмерного массива
array_3d = []


# Заполнение массива значениями.
for i in range(X):
    array_3d.append([])
    for j in range(Y):
        array_3d[i].append([])
        for k in range(Z):
            value = int(input(f"Введите элемент [{i}, {j}, {k}]: "))
            array_3d[i][j].append(value)


# Определение наибольшего измерения.
max_dim = 0
if X > Y:
    if X > Z:
        max_dim = X
    else:
        max_dim = Z
elif Y > Z:
    max_dim = Y
else:
    max_dim = Z

max_dim = max_dim // 2


# Срез.
if max_dim == X:
    # Срез по оси X
    slice_index = X // 2
    result_slice = array_3d[slice_index]
elif max_dim == Y:
    # Срез по оси Y
    slice_index = Y // 2
    result_slice = []
    for row in array_3d:
        result_slice.append(row[slice_index])
else:
    # Срез по оси Z
    slice_index = Z // 2
    result_slice = []
    for row in array_3d:
        new_row = []
        for col in row:
            new_row.append(col[slice_index])
        result_slice.append(new_row)


# Вывод среза массива.
for row in result_slice:
    print(row)