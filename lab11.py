# Лимарев Степан ИУ7-11Б. Программа демонстрирует работу метода сортировки (по варианту) на примере массива целых чисел.
# Программа должна состоять из двух частей (этапов работы) и выполнять два действия последовательно:
# 1. сначала отсортировать заданный пользователем массив для доказательства корректности работы алгоритма;
# 2. затем составить таблицу замеров времени сортировки списков трёх различных (заданных пользователем) размерностей и количества перестановок в каждом из них.


# Импортирование модуля для замеров времени сортировки.
import time
# Импортирование модуля random для генерации случайного списка.
import random
# Импортирование модуля tabulate для вывода таблицы.
from tabulate import tabulate


# Функция сортировки методом простых вставок.
def insertion_sort(arr):
    n = len(arr)
    count_swaps = 0  # Счётчик перестановок.
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            count_swaps += 1
            
        arr[j + 1] = key
        
    return count_swaps


# Проверка, является ли строка допустимым целым числом (положительным или отрицательным).
def is_valid_integer(number_str):

    return number_str.lstrip('-').isdigit()


# Проверка, является ли строка допустимым положительным целым числом.
def is_valid_positive_integer(number_str):

    return number_str.isdigit() and int(number_str) > 0


# Запрашивает у пользователя ввод целых чисел до тех пор, пока не будут введены корректные данные.
def check_int_input(prompt):
    while True:
        user_input = input(prompt).strip()
        values = user_input.split()
        if all(is_valid_integer(value) for value in values):
            return list(map(int, values))
        else:
            print("Введено некорректное значение. Элементы массива должны быть целыми числами.")
            print("Введите элементы массива через пробел: ")


# Запрашивает у пользователя ввод положительных целых чисел до тех пор, пока не будут введены корректные данные.
def check_positive_int_input(prompt):
    while True:
        user_input = input(prompt).strip()
        values = user_input.split()
        if all(is_valid_positive_integer(value) for value in values):
            return list(map(int, values))
        else:
            print("Введено некорректное значение. Размеры массивов должны быть положительными целыми числами.")
            print("Введите размеры массивов через пробел:")


# Сортировка пользовательского массива.
print("Введите элементы массива через пробел: ")
arr = check_int_input("")  # Использование функции проверки корректности ввода.

start_time = time.time()
swaps = insertion_sort(arr)
end_time = time.time()


# Вывод массива и измерений времени и перестановок.
print(f"Отсортированный массив: {arr}")
print(f"Время сортировки: {(end_time - start_time) * 1000:.7f} мс")
print(f"Количество перестановок: {swaps}\n")


# Измерение времени сортировки для размеров, введённых пользователем.
print("Введите размеры массивов через пробел:")
sizes = check_positive_int_input("")  # Использование функции проверки корректности ввода.

results = {}

for size in sizes:
    
    # Генерация случайного списка.
    random_list = [random.randint(-1000000, 1000000) for _ in range(size)]
    # Отсортированный список.
    sorted_list = sorted(random_list)
    # Список, отсортированный в обратном порядке.
    reversed_list = sorted_list[::-1]
    
    lists_to_test = {
        'Случайный список': random_list,
        'Отсортированный список': sorted_list,
        'Список, отсортированный в обратном порядке': reversed_list
    }
    

    # Измерение времени сортировки в миллисекундах.
    for type_name, lst in lists_to_test.items():
        start_time = time.time()
        swaps = insertion_sort(lst.copy()) # Копирование списка, чтобы не изменять исходный.
        end_time = time.time()
        
        if type_name not in results:
            results[type_name] = {}
        
        results[type_name][size] = (end_time - start_time) * 1000, swaps


# Формирование таблицы результатов.
headers = [""] + sizes
sub_headers = [""] + ["Время      |  Перестановки"] * len(sizes)


# Добавление данных в таблицу.
table_data = [
    sub_headers,
    ["Случайный список"] + [None] * len(sizes),
    ["Отсортированный список"] + [None] * len(sizes),
    ["Список, отсортированный в обратном порядке"] + [None] * len(sizes)
]

for i, type_name in enumerate(lists_to_test.keys()):
    for j, size in enumerate(sizes):
        time_ms, swaps = results[type_name][size]
        table_data[i+1][j+1] = f"{time_ms:.7f} | {swaps}"


# Вывод таблицы.
print("\nРезультаты измерений: ")
print(tabulate(table_data, headers=headers, tablefmt="simple_grid"))