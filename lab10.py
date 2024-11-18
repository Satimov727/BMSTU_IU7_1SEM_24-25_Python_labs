# Лимарев Степан ИУ7-11Б. Программа вычисляет приближённое значение интеграла известной, заданной программе, функции двумя разными методами (по варианту).
# Далее строится таблица с началом и концом отрезка интегрирования, а также N1 и N2 - количеством участков разбиения.
# Далее на основе известной, заданной в программе, первообразной определить, какой метод является наиболее точным. Для этого требуется вычислить и отобразить
# абсолютную и относительную погрешности каждого из четырёх измерений. Метод, измерение которого с одним из разбиений дало самое близкое к первообразной
# значение, считается наиболее точным. Затем для другого, менее точного метода, итерационно вычислить количество участков
# разбиения, для которого интеграл будет вычислен с заданной точностью, на основе формулы: | 𝐼(𝑁) − 𝐼(2𝑁) | < ε.
# Вывести приближенное значение интеграла и количество отрезков, необходимых для его вычисления.
# Метод 1 - метод левых прямоугольников. Метод 2 - метод парабол.


# Импортирование модуля math для использования математических функций.
import math

# Импортирование модуля tabulate для вывода таблицы.
from tabulate import tabulate # type: ignore

# Проверка корректности ввода.
def check_input(input_string):
    
    # Проверка на целое число.
    if input_string.isdigit() or input_string == 0 or input_string.lstrip('-').isdigit():

        return int(input_string)

    # Проверка на вещественное число.
    if '.' in input_string:
        parts = input_string.split('.')

        if len(parts) == 2 and parts[0].lstrip('-').isdigit() and parts[1].isdigit():

            return float(input_string)

    return None

# Получение данных от пользователя.
a = input("Введите начальную точку интегрирования: ")
while check_input(a) is None:
    print("Введено некорректное значение. Начальная точка интегрирования должна быть целым или вещественным числом.")
    a = input("Введите начальную точку интегрирования: ")

b = input("Введите конечную точку интегрирования: ")
while check_input(b) is None:
    print("Введено некорректное значение. Конечная точка интегрирования должна быть целым или вещественным числом.")
    b = input("Введите конечную точку интегрирования: ")

while float(b) <= float(a):
    print("Конечная точка интегрирования должна быть больше начальной точки.")
    b = input("Введите конечную точку интегрирования: ")

N1 = input("Введите количество участков разбиения N1: ")
while check_input(N1) is None or float(N1) <= 0 or float(N1) % 1 != 0:
    print("Введено некорректное значение. Количество участков разбиения N1 должно быть целым положительным числом.")
    N1 = input("Введите количество участков разбиения N1: ")

N2 = input("Введите количество участков разбиения N2: ")
while check_input(N2) is None or float(N2) <= 0 or float(N2) % 1 != 0:
    print("Введено некорректное значение. Количество участков разбиения N2 должно быть целым положительным числом.")
    N2 = input("Введите количество участков разбиения N2: ")

eps = input("Введите точность ε: ")
while check_input(eps) is None:
    print("Введено некорректное значение. Точность ε должна быть целым или вещественным числом.")
    eps = input("Введите точность ε: ")

a = float(a)
b = float(b)

# Функция, которую нужно проинтегрировать. (Пользователь может менять на произвольную).
def f(x):
    return x * math.sin(x)

# Первообразная функции f(x). (Если пользователь меняет функцию на произвольную, то также необходимо поменять и первообразную).
def F(x):
    return -x * math.cos(x) + math.sin(x)

# Метод левых прямоугольников.
def left_rectangle(f, a, b, n):
    n = float(n)
    if n == 0:
        return None
    
    h = (b - a) / n
    integral = 0
    n = int(n)
    for i in range(n):
        x = a + i * h
        integral += f(x) * h
        
    return integral

# Метод парабол.
def parabola(f, a, b, n):
    n = float(n)
    if n % 2 != 0 or n < 2:
        return None
    
    h = (b - a) / n
    integral = f(a) + f(b)
    
    # Слагаемое с коэффициентом 4.
    n = int(n)
    for i in range(1, n, 2):
        x = a + i * h
        integral += 4 * f(x)
    
    # Слагаемое с коэффициентом 2.
    for i in range(2, n-1, 2):
        x = a + i * h
        integral += 2 * f(x)
    
    return integral * h / 3

# Вычисление истинного значения интеграла через первообразную.
def true_integral(F, a, b):
    return F(b) - F(a)

# Начальное значение N.
N = 10

# Шаг увеличения.
step = 2

# Количество итераций.
iterations = 0

# Булева переменная для выхода из цикла.
continue_loop = True

# Основной цикл.
while continue_loop:
    eps = float(eps)
    iterations += 1
    N_double = N * step
    
    I_N = left_rectangle(f, a, b, N)
    I_2N = left_rectangle(f, a, b, N_double)
    
    error = abs(I_N - I_2N)
    if error < eps:
        continue_loop = False
    else:
        N += step

# Вычисление интеграла методом левых прямоугольников.
I1 = left_rectangle(f, a, b, N1)
I2 = left_rectangle(f, a, b, N2)

# Вычисление интеграла методом парабол.
I3 = parabola(f, a, b, N1)
I4 = parabola(f, a, b, N2)

# Истинное значение интеграла.
true_value = true_integral(F, a, b)

# Формирование таблицы результатов.
data = [
    ["", N1, N2],
    ["Левые прямоугольники", I1, I2],
    ["Параболы", I3, I4]
]

# Вывод таблицы.
print(tabulate(data, headers='firstrow', tablefmt="simple_grid", missingval='-', colalign=("center", "center", "center")))

# Вывод результата точности.
print(f"Точность достигнута за {iterations} итераций с N = {N}.")
print(f"Погрешность: {error:.7f}")

# Отображение истинного значения интеграла.
print(f"\nИстинное значение интеграла: {true_value:.7f}")

# Погрешности для метода левых прямоугольников.
abs_error_I1 = abs(I1 - true_value) if I1 is not None else 0
rel_error_I1 = abs(abs_error_I1 / true_value) if true_value != 0 else 0
abs_error_I2 = abs(I2 - true_value) if I2 is not None else 0
rel_error_I2 = abs(abs_error_I2 / true_value) if true_value != 0 else 0

# Погрешности для метода парабол.
abs_error_I3 = abs(I3 - true_value) if I3 is not None else 0
rel_error_I3 = abs(abs_error_I3 / true_value) if true_value != 0 else 0
abs_error_I4 = abs(I4 - true_value) if I4 is not None else 0
rel_error_I4 = abs(abs_error_I4 / true_value) if true_value != 0 else 0

# Вывод всех погрешностей.
print("\nПогрешности:")
print(f"Абсолютная погрешность для метода левых прямоугольников с N1: {abs_error_I1:.7f}")
print(f"Относительная погрешность для метода левых прямоугольников с N1: {rel_error_I1:.7f}")
print(f"Абсолютная погрешность для метода левых прямоугольников с N2: {abs_error_I2:.7f}")
print(f"Относительная погрешность для метода левых прямоугольников с N2: {rel_error_I2:.7f}")
print(f"Абсолютная погрешность для метода парабол с N1: {abs_error_I3:.7f}")
print(f"Относительная погрешность для метода парабол с N1: {rel_error_I3:.7f}")
print(f"Абсолютная погрешность для метода парабол с N2: {abs_error_I4:.7f}")
print(f"Относительная погрешность для метода парабол с N2: {rel_error_I4:.7f}")

# Нахождение наименьшей относительной погрешности среди всех методов.
min_rel_error = rel_error_I1

if rel_error_I2 < min_rel_error:
    min_rel_error = rel_error_I2

if rel_error_I3 < min_rel_error:
    min_rel_error = rel_error_I3

if rel_error_I4 < min_rel_error:
    min_rel_error = rel_error_I4

# Определение лучшего метода.
if min_rel_error == rel_error_I1:
    best_method = "Левые прямоугольники с N1"
elif min_rel_error == rel_error_I2:
    best_method = "Левые прямоугольники с N2"
elif min_rel_error == rel_error_I3:
    best_method = "Параболы с N1"
else:
    best_method = "Параболы с N2"

# Вывод лучшего метода.
print(f"\nНаилучший метод: {best_method}")