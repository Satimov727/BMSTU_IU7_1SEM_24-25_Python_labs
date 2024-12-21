# Лимарев Степан ИУ7-11Б. Программа, которая позволит с помощью меню выполнить следующие действия:
# 1. Выбрать файл для работы.
# 2. Инициализировать базу данных (создать либо перезаписать файл и заполнить его записями).
# 3. Вывести содержимое базы данных.
# 4. Добавить запись в произвольное место базы данных (пользователь указывает номер позиции, в которую должна быть вставлена запись).
# 5. Удалить произвольную запись из базы данных (пользователь указывает номер удаляемой записи).
# 6. Поиск по одному полю.
# 7. Поиск по двум полям.
# Тематика базы данных - фиксированная, выбираемая на усмотрение исполнителя.
# Давать пользователю создавать БД произвольной структуры не требуется.
# Записи должны состоять из 3-4 полей разных типов (текстовые, числовые).
# Для формирования записей фиксированного размера (структур) в бинарном формате следует использовать модуль struct.
# Поля для поиска в пп. 6 и 7 выбираются на усмотрение исполнителя.


# Импортирование модуля os для работы с путями к файлам.
import os.path


# Импортирование модуля struct для работы со структурами фиксированной длины.
from struct import pack, unpack, calcsize


# Формат записи: строка (название), строка (автор), целое число (год), целое число (количество страниц).
RECORD_FORMAT = '32s32sii'
RECORD_SIZE = calcsize(RECORD_FORMAT)
db_file = None


# Функция реализации меню для работы с пользователем и обработки его последующих действий.
def main():

    while True:
        print("\nМеню:")
        print("1. Выбрать файл для работы")
        print("2. Инициализировать базу данных ")
        print("3. Вывести содержимое базы данных")
        print("4. Добавить запись в произвольное место базы данных")
        print("5. Удалить произвольную запись из базы данных")
        print("6. Поиск по одному полю")
        print("7. Поиск по двум полям")
        print("8. Выход")

        choice = input("Выберите пункт меню: ")
        
        if choice == '1':
            file_path = select_file()
            if not file_path:
                continue
            
            global db_file
            db_file = open(file_path, 'a+b')  # Открытие файла в режиме добавления и чтения
            print(f"База данных открыта в файле: {file_path}")
        
        elif choice == '2':
            initialize_database()
        
        elif choice == '3':
            display_database_content()
        
        elif choice == '4':
            add_record_at_position()
        
        elif choice == '5':
            delete_record_by_index()
        
        elif choice == '6':
            single_field_search()
        
        elif choice == '7':
            two_fields_search()
        
        elif choice == '8':
            break

        else:
            print("Некоррретный ввод. Значение должно соответствовать одному из пунктов меню.")


# Функция для выбора файла для работы.
def select_file():
    file_path = input("Укажите путь к файлу базы данных: ")
    if not os.path.exists(file_path):
        print("Файл {file_path} не существует. Создадим новый файл.")
        with open(file_path, 'wb') as f:
            pass
    else:
        print(f"Вы выбрали файл {file_path}.")
    return file_path


# Функция для инициализации базы данных.
def initialize_database():
    if not db_file:
        print("Сначала выберите файл для работы.")
        return
    
    db_file.seek(0)  # Установка курсора в начало файла
    db_file.truncate()  # Очистка файла перед записью новых данных
    
    num_records = int(input("Сколько записей вы хотите добавить? "))
    
    for _ in range(num_records):
        title = input("Название книги: ").encode('utf-8')[:32]
        author = input("Автор: ").encode('utf-8')[:32]
        year = int(input("Год издания: "))
        pages = int(input("Количество страниц: "))
        
        packed_data = pack(RECORD_FORMAT, title, author, year, pages)
        db_file.write(packed_data)
    
    print("База данных успешно инициализирована.")


# Функция для вывода содержимого базы данных.
def display_database_content():
    if not db_file:
        print("Сначала выберите файл для работы.")
        return
    
    db_file.seek(0)  # Переход в начало файла
    index = 1  # Индекс для нумерации записей
    try:
        while True:
            data = db_file.read(RECORD_SIZE)  # Чтение записи
            if len(data) != RECORD_SIZE:  # Проверка размера записи
                break
            title, author, year, pages = unpack(RECORD_FORMAT, data)
            print(f"{index}. Название: {title.decode().strip()} | Автор: {author.decode().strip()} | Год: {year} | Страниц: {pages}")
            index += 1
    except EOFError:
        pass


# Функция для добавления записи в произвольное место.
def add_record_at_position():
    if not db_file:
        print("Сначала выберите файл для работы.")
        return
    
    position = int(input("Введите номер позиции для добавления записи: "))
    if position <= 0:
        print("Номер позиции должен быть положительным числом.")
        return
    
    title = input("Название книги: ").encode('utf-8')[:32]
    author = input("Автор: ").encode('utf-8')[:32]
    year = int(input("Год издания: "))
    pages = int(input("Количество страниц: "))
    
    # Переходим к нужной позиции
    db_file.seek((position - 1) * RECORD_SIZE)
    
    # Читаем остаток файла
    remaining_data = db_file.read()
    
    # Возвращаемся на начало файла
    db_file.seek(0)
    
    # Создаем временный список записей
    records = []
    
    # Читаем все записи до нужной позиции
    for _ in range(position - 1):
        data = db_file.read(RECORD_SIZE)
        if len(data) != RECORD_SIZE:
            break
        records.append(unpack(RECORD_FORMAT, data))
    
    # Добавляем новую запись
    records.append((title, author, year, pages))
    
    # Продолжаем читать остальные записи
    while True:
        data = db_file.read(RECORD_SIZE)
        if len(data) != RECORD_SIZE:
            break
        records.append(unpack(RECORD_FORMAT, data))
    
    # Перезаписываем файл новыми данными
    db_file.seek(0)
    db_file.truncate()
    
    for record in records:
        packed_data = pack(RECORD_FORMAT, *record)
        db_file.write(packed_data)
    
    print(f"Запись добавлена в позицию {position}.")


# Функция для удаления записи по индексу.
def delete_record_by_index():
    if not db_file:
        print("Сначала выберите файл для работы.")
        return
    
    index = int(input("Введите номер записи для удаления: "))
    if index <= 0:
        print("Номер записи должен быть положительным числом.")
        return
    
    db_file.seek(0)
    records = []
    
    try:
        while True:
            data = db_file.read(RECORD_SIZE)
            if len(data) != RECORD_SIZE:
                break
            title, author, year, pages = unpack(RECORD_FORMAT, data)
            records.append((title, author, year, pages))
    except EOFError:
        pass
    
    if index > len(records):
        print("Такой записи нет.")
        return
    
    del records[index - 1]
    
    db_file.seek(0)
    db_file.truncate()
    
    for record in records:
        packed_data = pack(RECORD_FORMAT, *record)
        db_file.write(packed_data)
    
    print(f"Запись под номером {index} удалена.")


# Функция для поиска по одному полю.
def single_field_search():
    if not db_file:
        print("Сначала выберите файл для работы.")
        return
    
    fields = {
        '1': 'Название',
        '2': 'Автор',
        '3': 'Год издания',
        '4': 'Количество страниц'
    }
    
    print("Выберите поле для поиска:")
    for key, value in fields.items():
        print(f"{key}: {value}")
    
    field_choice = input("Введите номер поля: ")
    
    if field_choice == '1':
        query = input("Введите название книги для поиска: ").lower().encode('utf-8')[:32]
    elif field_choice == '2':
        query = input("Введите автора для поиска: ").lower().encode('utf-8')[:32]
    elif field_choice == '3':
        query = int(input("Введите год издания для поиска: "))
    elif field_choice == '4':
        query = int(input("Введите количество страниц для поиска: "))
    else:
        print("Неправильный выбор поля.")
        return
    
    db_file.seek(0)
    index = 1
    results = []
    
    try:
        while True:
            data = db_file.read(RECORD_SIZE)
            if len(data) != RECORD_SIZE:
                break
            title, author, year, pages = unpack(RECORD_FORMAT, data)
            if field_choice == '1' and query in title.decode():
                results.append((index, title.decode(), author.decode(), year, pages))
            elif field_choice == '2' and query in author.decode():
                results.append((index, title.decode(), author.decode(), year, pages))
            elif field_choice == '3' and query == year:
                results.append((index, title.decode(), author.decode(), year, pages))
            elif field_choice == '4' and query == pages:
                results.append((index, title.decode(), author.decode(), year, pages))
            index += 1
    except EOFError:
        pass
    
    if not results:
        print("Книг, соответствующих запросу, не найдено.")
    else:
        print("Результаты поиска:")
        for result in results:
            print(f"{result[0]}. Название: {result[1]} | Автор: {result[2]} | Год: {result[3]} | Страниц: {result[4]}")


# Функция для поиска по двум полям.
def two_fields_search():
    if not db_file:
        print("Сначала выберите файл для работы.")
        return
    
    fields = {
        '1': 'Название',
        '2': 'Автор',
        '3': 'Год издания',
        '4': 'Количество страниц'
    }
    
    print("Выберите два поля для поиска:")
    for key, value in fields.items():
        print(f"{key}: {value}")
    
    first_field = input("Первое поле: ")
    second_field = input("Второе поле: ")
    
    if first_field == '1':
        first_query = input("Введите название книги для поиска: ").lower().encode('utf-8')[:32]
    elif first_field == '2':
        first_query = input("Введите автора для поиска: ").lower().encode('utf-8')[:32]
    elif first_field == '3':
        first_query = int(input("Введите год издания для поиска: "))
    elif first_field == '4':
        first_query = int(input("Введите количество страниц для поиска: "))
    else:
        print("Неправильный выбор первого поля.")
        return
    
    if second_field == '1':
        second_query = input("Введите название книги для поиска: ").lower().encode('utf-8')[:32]
    elif second_field == '2':
        second_query = input("Введите автора для поиска: ").lower().encode('utf-8')[:32]
    elif second_field == '3':
        second_query = int(input("Введите год издания для поиска: "))
    elif second_field == '4':
        second_query = int(input("Введите количество страниц для поиска: "))
    else:
        print("Неправильный выбор второго поля.")
        return
    
    db_file.seek(0)
    index = 1
    results = []
    
    try:
        while True:
            data = db_file.read(RECORD_SIZE)
            if len(data) != RECORD_SIZE:
                break
            title, author, year, pages = unpack(RECORD_FORMAT, data)
            if (
                (first_field == '1' and first_query.lower() in title.decode().lower()) or
                (first_field == '2' and first_query.lower() in author.decode().lower()) or
                (first_field == '3' and first_query == year) or
                (first_field == '4' and first_query == pages)
            ) and (
                (second_field == '1' and second_query.lower() in title.decode().lower()) or
                (second_field == '2' and second_query.lower() in author.decode().lower()) or
                (second_field == '3' and second_query == year) or
                (second_field == '4' and second_query == pages)
            ):
                results.append((index, title.decode(), author.decode(), year, pages))
            index += 1
    except EOFError:
        pass
    
    if not results:
        print("Книг, соответствующих запросу, не найдено.")
    else:
        print("Результаты поиска:")
        for result in results:
            print(f"{result[0]}. Название: {result[1]} | Автор: {result[2]} | Год: {result[3]} | Страниц: {result[4]}")

if __name__ == "__main__":
    main()