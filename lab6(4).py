# Лимарев Степан ИУ7-11Б. Программа находит наиболее длинную непрерывную последовательность по варианту.
# Возрастающая последовательность простых чисел.


# Приглашение пользователя на ввод списка.
n = int(input("Введите количество элементов в списке: "))
lst = []


# Цикл для ввода каждого элемента списка.
for i in range(n):

    item = int(input("Введите элемент списка: "))
    lst.append(item)


# Поиск простых чисел.
simple_nums = []

for num in lst:

    simple = True

    for div in range(2, int(num ** 0.5) + 1):

        if num % div == 0:

            simple = False

            break

    if simple:

        simple_nums.append(num)


# Вычисление максимальной возрастающей последовательности простых чисел.
max_len = 0
seq = []
cur_seq = []
prev_num = None

for num in simple_nums:

    if prev_num is None or num > prev_num:

        cur_seq.append(num)

        if len(cur_seq) > max_len:

            seq = []

            for elem in cur_seq:

                seq.append(elem)
            
            max_len = len(seq)
    
    else:
        
        cur_seq = [num]
    prev_num = num


# Вывод полученной последовательности.
print("Максимальная возрастающая последовательность простых чисел: ", seq)


    




