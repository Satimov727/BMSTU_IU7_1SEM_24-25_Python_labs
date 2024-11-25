# Лимарев Степан ИУ7-11Б.
# Сортировка массива методом быстрой сортировки.


# Импортирование модуля time для замеров времени сортировки.
import time


# Функция метода быстрой сортировки.
def quick_sort(arr, count_swaps = 0):

    if len(arr) <= 1:

        return arr, count_swaps
    
    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    mid = [x for x in arr if x == pivot]

    left_sorted, count_left = quick_sort(left, count_swaps)
    right_sorted, count_right = quick_sort(right, count_swaps)

    result = left_sorted + mid + right_sorted
    total_count_swaps = count_left + count_right + len(left) + len(right)

    return result, total_count_swaps


# Сортировка пользовательского массива.
print("Введите элементы массива через пробел: ")
array = list(map(int, input().split()))

sorted_array, swaps = quick_sort(array)
start_time = time.time()
end_time = time.time()


# Вывод массива, измерений времени и перестановок.
print(f"Отсортированный массив: {sorted_array}")
print(f"Время сортировки: {(end_time - start_time) * 1000:.7f} мс")
print(f"Количество перестановок: {swaps}\n")




    