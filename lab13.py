# Лимарев Степан ИУ7-11Б. Программа у, которая позволит с помощью меню выполнить следующие действия:
# 1. Выбрать файл для работы
# 2. Инициализировать базу данных (создать либо перезаписать файл и заполнить его записями)
# 3. Вывести содержимое базы данных
# 4. Добавить запись в конец базы данных
# 5. Поиск по одному полю
# 6. Поиск по двум полям
# Тематика базы данных- фиксированная, выбираемая на усмотрение исполнителя.
# Давать пользователю создавать БД произвольной структуры не требуется.
# Записи должны состоять из 3-4 полей разных типов (текстовые, числовые).
# Поля для поиска в пп. 5 и 6 выбираются на усмотрение исполнителя.


import os

# Функция для отображения главного меню
def show_menu():
    """
    Показывает пользователю главное меню и возвращает его выбор.
    """
    print("\nМеню:")
    print("1. Выбрать файл для работы")
    print("2. Инициализировать базу данных")
    print("3. Вывести содержимое базы данных")
    print("4. Добавить запись в конец базы данных")
    print("5. Поиск по одному полю")
    print("6. Поиск по двум полям")
    print("7. Выход")
    
    choice = input("Выберите пункт меню: ")
    return choice

# Функция для чтения файла
def read_file(filename):
    """
    Считывает данные из указанного файла и возвращает их в виде списка строк.
    Если файл не существует, возвращается пустой список.
    """
    if not os.path.exists(filename):
        print(f"Файл {filename} не найден.")
        return []
    
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read().splitlines()
        
    return data

# Функция для сохранения данных в файл
def write_to_file(filename, data):
    """
    Сохраняет переданные данные в указанный файл.
    Каждая строка сохраняется в отдельную строку файла.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        for line in data:
            file.write(line + '\n')

# Функция для инициализации базы данных
def initialize_database(filename):
    """
    Инициализирует базу данных, запрашивая у пользователя начальные данные.
    Данные сохраняются в указанном файле.
    """
    # Запрашиваем у пользователя начальные данные
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    year = int(input("Введите год издания: "))
    pages = int(input("Введите количество страниц: "))
    
    initial_data = f"{title}\t{author}\t{year}\t{pages}"
    
    # Перезаписываем файл с новыми данными
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(initial_data)
    
    print(f"База данных успешно создана в файле {filename}.")

# Функция для вывода содержимого базы данных
def display_database(data):
    """
    Выводит содержимое базы данных в удобной форме.
    Если база данных пуста, выводит соответствующее сообщение.
    """
    if len(data) == 0:
        print("База данных пуста.")
        return
    
    headers = ["Название", "Автор", "Год издания", "Количество страниц"]
    max_lengths = [max(len(row.split('\t')[i]) for row in data) for i in range(4)]
    
    header_line = ''.join([f'{header:<{length}}' for header, length in zip(headers, max_lengths)])
    print(header_line)
    
    for row in data:
        fields = row.split('\t')
        field_line = ''.join([f'{field:<{length}}' for field, length in zip(fields, max_lengths)])
        print(field_line)

# Функция для добавления записи в конец базы данных
def add_record(filename):
    """
    Добавляет новую запись в конец базы данных.
    Запрашивает у пользователя необходимые данные и сохраняет их в файл.
    """
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    year = int(input("Введите год издания: "))
    pages = int(input("Введите количество страниц: "))
    
    new_record = f"{title}\t{author}\t{year}\t{pages}"
    
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(new_record + '\n')
    
    print("Запись успешно добавлена.")

# Функция для поиска по одному полю
def search_by_one_field(data):
    """
    Выполняет поиск записей по указанному полю и значению.
    Выводит результаты поиска, если они найдены.
    """
    field_name = input("Введите имя поля для поиска (название, автор, год, страницы): ").lower()
    value = input("Введите значение для поиска: ")
    
    found_records = []
    
    if field_name == "название":
        index = 0
    elif field_name == "автор":
        index = 1
    elif field_name == "год":
        index = 2
    elif field_name == "страницы":
        index = 3
    else:
        print("Неверное имя поля.")
        return
    
    for row in data:
        fields = row.split('\t')
        if fields[index].strip() == value:
            found_records.append(row)
            
    if len(found_records) > 0:
        display_database(found_records)
    else:
        print("Нет записей, соответствующих запросу.")

# Функция для поиска по двум полям
def search_by_two_fields(data):
    """
    Выполняет поиск записей по двум указанным полям и значениям.
    Выводит результаты поиска, если они найдены.
    """
    field_name_1 = input("Введите первое имя поля для поиска (название, автор, год, страницы): ").lower()
    value_1 = input("Введите первое значение для поиска: ")
    
    field_name_2 = input("Введите второе имя поля для поиска (название, автор, год, страницы): ").lower()
    value_2 = input("Введите второе значение для поиска: ")
    
    found_records = []
    
    if field_name_1 == "название":
        index_1 = 0
    elif field_name_1 == "автор":
        index_1 = 1
    elif field_name_1 == "год":
        index_1 = 2
    elif field_name_1 == "страницы":
        index_1 = 3
    else:
        print("Неверное первое имя поля.")
        return
    
    if field_name_2 == "название":
        index_2 = 0
    elif field_name_2 == "автор":
        index_2 = 1
    elif field_name_2 == "год":
        index_2 = 2
    elif field_name_2 == "страницы":
        index_2 = 3
    else:
        print("Неверное второе имя поля.")
        return
    
    for row in data:
        fields = row.split('\t')
        if fields[index_1].strip() == value_1 and fields[index_2].strip() == value_2:
            found_records.append(row)
            
    if len(found_records) > 0:
        display_database(found_records)
    else:
        print("Нет записей, соответствующих запросу.")

# Основная функция программы
def main():
    """
    Главная функция программы, управляющая выполнением всего приложения.
    Предлагает пользователю выбирать действия из меню до тех пор, пока он не решит выйти.
    """
    filename = None
    while True:
        choice = show_menu()
        
        if choice == '1':
            filename = input("Введите путь к файлу: ")
            data = read_file(filename)
            print(f"Файл {filename} выбран для работы.")
        elif choice == '2':
            if filename is None:
                print("Сначала выберите файл.")
            else:
                initialize_database(filename)
        elif choice == '3':
            if filename is None:
                print("Сначала выберите файл.")
            else:
                data = read_file(filename)
                display_database(data)
        elif choice == '4':
            if filename is None:
                print("Сначала выберите файл.")
            else:
                add_record(filename)
        elif choice == '5':
            if filename is None:
                print("Сначала выберите файл.")
            else:
                data = read_file(filename)
                search_by_one_field(data)
        elif choice == '6':
            if filename is None:
                print("Сначала выберите файл.")
            else:
                data = read_file(filename)
                search_by_two_fields(data)
        elif choice == '7':
            break
        else:
            print("Некорректный ввод. Значение должно соответствовать одному из номеров пунктов меню.")

if __name__ == "__main__":
    main()