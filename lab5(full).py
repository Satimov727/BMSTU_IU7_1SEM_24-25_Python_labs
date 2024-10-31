# Лимарев Степан ИУ7-11Б. Программа предназначена для вывода таблицы значений функций и построения графика одной из этих функций.


# Импортирование модуля math для выполнения математических операций.
from math import sin, e


# Ввод исходных данных.
a_0 = float(input("Введите начальное значение аргумента: "))  # Ввод начального значения аргумента.
a_n = float(input("Введите конечное значение аргумента: "))  # Ввод конечного значения аргумента.
h = float(input("Введите шаг разбиения отрезка: "))  # Ввод шага разбиения отрезка.


# Проверка на корректный ввод значений.
while (a_n < a_0) or (h < 0):

    if a_n < a_0:

        print("Конечное значение аргумента функции должно быть больше начального")

        exit()  # Выход из цикла.
    
    if h < 0 :

        print("Значение шага должно быть больше нуля")
        
        exit()  # Выход из цикла.
    
# Ввод необходимых параметров.
a = a_0
max_h1 = False  # Максимальное значение функции a ** 2 + 4 * sin(a)
min_h1 = False  # Минимальное значение функции a ** 2 + 4 * sin(a)
min_h2 = False  # Минимальное значение функции e ** a + e ** (-1.5 * a) - 4


# Вывод таблицы.
print('-------------------------------------------')
print('|      x      |      y1     |      y2     |')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')


# Вычисление значений функций.
while a <= a_n:

    h1 = a ** 2 + 4 * sin(a)  # Значение функции a ** 2 + 4 * sin(a)
    h2 = e ** a + e ** (-1.5 * a) - 4  # Значение функции e ** a + e ** (-1.5 * a) - 4
    

    # Вычисление минимального и максимального значений функции a ** 2 + 4 * sin(a)
    if min_h1 == False or h1 < min_h1:

        min_h1 = h1

    if max_h1 == False or h1 > max_h1:

        max_h1 = h1

    if min_h2 == False or h2 < min_h2:

        min_h2 = h2

    if abs(a) <= 1e-10:

        a = 0
    
    if abs(h1) <= 1e-10:

        h1 = 0
    
    if abs(h2) <= 1e-10:

        h2 = 0

    print('|{0:^13g}|{1:^13g}|{2:^13g}|'.format(a, h1, h2))  # Вывод значений функций в таблицу.

    a += h


# Ввод параметров для графика.
graph_width = int(input("Введите ширину оси y: "))
x_line_width = 8
x_lines_num = int((a_n - a_0) / h) + 1
cut_points_num = int(input("Введите целочисленное положительное кол-во засечек (от 4 до 8-ми): "))  # Ввод количества засечек.
eps = abs(min_h1 - max_h1) / (graph_width - x_line_width)
cut_space = (graph_width - x_line_width) // cut_points_num + 1
spaces_min_to_0 = int(abs(min_h1) // eps - 1)
spaces_0_to_max = int(max_h1 // eps - 1)


# Циклическая вывод значений оси ординат на графике функции a ** 2 + 4 * sin(a).
for i in range(cut_points_num):

    num = (max_h1 - min_h1) / (cut_points_num - 1) * i + min_h1

    print(('{0:' + '>{}'.format(cut_space) + '}').format('{:.5f}'.format(num)), end=' ')  # Вывод значений оси ординат на графике.

print()  # Вывод пробелов.


# Вывод оси абсцисс с помощью символов "|" в случае попадания 0 в диапазон значений функции на заданном отрезке.
if min_h1 <= 0 <= max_h1:
    
    for x_step in range(x_lines_num):

        cur_a = a_0 + x_step * h

        print('|{0:^6g}|'.format(cur_a), end='')  # Вывод символов "|".

        cur_h1 = cur_a ** 2 + 4 * sin(cur_a)  # Заданная функция a ** 2 + 4 * sin(a)
        

        # Вывод точек графика с помощью символов "*" в различных случаях.
        if cur_h1 <= 0:

            if (abs(cur_h1) - eps) < eps:

                print(' ' * spaces_min_to_0 + '*' + ' ' * spaces_0_to_max)  # Вывод точек графика.

            else:

                spaces_min_to_cur = int(abs(cur_h1 - min_h1 - (eps / 2)) // eps)  # - (eps / 2) не включительно брать точку
                spaces_cur_to_0 = spaces_min_to_0 - spaces_min_to_cur - 1

                print(' ' * spaces_min_to_cur + '*' + ' ' * spaces_cur_to_0 + '|' + ' ' * spaces_0_to_max)

        else:

            spaces_0_to_cur = int((cur_h1) // eps - 1)
            spaces_cur_to_max = int((max_h1 - cur_h1 + (eps / 2)) // eps - 1)

            print(' ' * spaces_min_to_0 + '|' + ' ' * spaces_0_to_cur + "*" + ' ' * spaces_cur_to_max)  # Вывод точек графика.

else:
    

    # Циклический вывод значений оси абсцисс на графике функции a ** 2 + 4 * sin(a).
    for x_step in range(x_lines_num):

        cur_a = a_0 + x_step * h

        print('|{0:<8.1e}|'.format(cur_a), end='')  # Вывод значений оси абсцисс графика функции a ** 2 + 4 * sin(a).

        cur_h1 = cur_a ** 2 + 4 * sin(cur_a)
        spaces_min_to_cur = int((cur_h1 - min_h1 - (eps / 2)) // eps)  # - (eps / 2) не включительно брать точку
        spaces_cur_to_max = int((max_h1 - cur_h1) // eps - 1)

        print(' ' * spaces_min_to_cur + "*" + ' ' * spaces_cur_to_max)  # Вывод точек графика.


# Дополнительное задание.
# Определить значения min_h1 и min_h2.


print(f"Минимальное значение функции h1 = a ** 2 + 4 * sin(a): {min_h1:.7g}")
print(f"Минимальное значение функции h2 = e ** a + e ** (-1.5 * a) - 4: {min_h2:.7g}")
