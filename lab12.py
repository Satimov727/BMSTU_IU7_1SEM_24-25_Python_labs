# Лимарев Степан ИУ7-11Б. Программа выполняет некоторые операции над текстом. Вводить текст не требуется, 
# он должен быть задан в исходном тексте программы в виде списка строк (при выводе на экран каждый элемент этого списка должен начинаться с новой строки). 
# В качестве текста в программе следует указать фрагмент литературного произведения из 5-7 предложений, который разбить на 7-10 строк.
# Программа должна позволять с помощью меню выполнить следующие действия:
# 1. Выровнять текст по левому краю.
# 2. Выровнять текст по правому краю.
# 3. Выровнять текст по ширине.
# 4. Удаление всех вхождений заданного слова.
# 5. Замена одного слова другим во всём тексте.
# 6. Вычисление арифметических выражений над целыми числами внутри текста
# (по варианту).
# 7. Найти (вывести на экран) и затем удалить слово или предложение по варианту.
# Текст следует разбить по строкам так, чтобы предложения не заканчивались в концах строк (никакая строка, кроме последней, не должна оканчиваться точкой).
# П. 6: Сложение и вычитание; П. 7:  Предложение с максимальным количеством слов, начинающихся на заданную букву.


# Функция для выравнивания текста по левому краю.
def align_left(text):

    return text

# Функция для выравнивания текста по правому краю.
def align_right(text):

    max_len = max(len(line) for line in text)

    return [line.rjust(max_len) for line in text]

# Функция для выравнивания текста по ширине.
def align_width(text):

    max_len = max(len(line) for line in text)
    aligned_text = []

    for line in text:
        words = line.split()
        extra_spaces = max_len - sum(len(w) for w in words)
        spaces_per_gap = extra_spaces // (len(words) - 1) if len(words) > 1 else 0
        remaining_spaces = extra_spaces % (len(words) - 1) if len(words) > 1 else 0
        gaps = [" " * (spaces_per_gap + 1)] * remaining_spaces + [" " * spaces_per_gap] * (len(words) - 1 - remaining_spaces)
        spaced_words = [word + gap for word, gap in zip(words, gaps + [""])]
        aligned_text.append("".join(spaced_words))

    return aligned_text

# Функция для удаления всех вхождений заданного слова из текста.
def remove_word(text, word_to_remove):
    new_text = []

    for line in text:
        words = line.split()
        filtered_words = []

        for word in words:
            if word.strip(',.?').lower() != word_to_remove.lower():
                filtered_words.append(word)

        new_line = ' '.join(filtered_words)
        new_text.append(new_line)

    return new_text

# Проверка корректности ввода для функции удаления всех вхождений заданного слова из текста.
def check_word_in_text(word_to_remove, text):
    found = False
    for line in text:
        words = line.split()
        if word_to_remove.lower() in words:
            found = True
            break
    if not found:
        print(f"Параметр {word_to_remove} отсутствует в тексте.")
        return False
    else:
        return True

# Функция для замены одного слова другим во всём тексте.
def replace_word(text, old_word, new_word):

    new_text = []

    for line in text:
        words = line.split()
        replaced_words = [new_word if w.lower() == old_word.lower() else w for w in words]
        new_line = ' '.join(replaced_words)
        new_text.append(new_line)

    return new_text

# Проверка корректности ввода для функции замены одного слова другим во всём тексте.
def check_old_word_in_text(old_word, text):
    found = False
    for line in text:
        words = line.split()
        if old_word.lower() in words:
            found = True
            break
    if not found:
        print(f"Параметр {old_word} отсутствует в тексте.")
        return False
    else:
        return True

# Функция для вычисления арифметических выражений над целыми числами внутри текста. Сложение и вычитание.
def process_expression(expr):

    parts = expr.split()
    result = int(parts[0])
    i = 1

    while i < len(parts):
        if parts[i] == '+':
            result += int(parts[i+1])
        elif parts[i] == '-':
            result -= int(parts[i+1])
        i += 2

    return str(result)

def calculate_arithmetic_expressions(text):

    new_text = []

    for line in text:
        parts = line.split()
        new_parts = []
        index = 0
        while index < len(parts):
            part = parts[index]
            if part.isdigit() and (index + 1 < len(parts)) and parts[index + 1] in ('+', '-') and parts[index + 2].isdigit():
                expression = f'{part} {parts[index + 1]} {parts[index + 2]}'
                result = process_expression(expression)
                new_parts.append(result)
                index += 3
            else:
                new_parts.append(part)
                index += 1
        new_text.append(' '.join(new_parts))

    return new_text

# Проверка текста на наличие операций сложения или вычитания.
def check_parameter_for_calculation(parameter, text):
    found = False
    for line in text:
        parts = line.split()
        if parameter in parts:
            found = True
            break
    if not found:
        print(f"Параметр {parameter} отсутствует в тексте.")
        return False
    else:
        return True

# Функция для нахождения и удаления слова или предложения с максимальной частотой начала на заданную букву.
def find_and_delete_by_letter(text, letter):
    lower_letter = letter.lower()
    
    max_count = 0
    sentence_with_max_words = None
    
    for line in text:
        words = line.split()
        count_words_start_with_letter = sum(1 for word in words if word.lower().startswith(lower_letter))
        
        if count_words_start_with_letter > max_count:
            max_count = count_words_start_with_letter
            sentence_with_max_words = line
    
    if sentence_with_max_words is not None:
        print(f"Слово или предложение с максимальной частотой начала на букву '{letter.upper()}':")
        
        text.remove(sentence_with_max_words)
    
    return text

# Проверка корректности ввода для функции нахождения и удаления слова или предложения с максимальной частотой начала на заданную букву.
def check_letter_in_text(letter, text):
    found = False
    for line in text:
        words = line.split()
        if any(word.startswith(letter) for word in words):
            found = True
            break
    if not found:
        print(f"Параметр {letter} отсутствует в тексте.")
        return False
    else:
        return True

# Исходный текст.
initial_text = [
    "В одном царстве, в некотором государстве жил-был царь",
    "И было у него три сына: Дмитрий, Василий и Иван",
    "Пошёл царь на охоту и заблудился в дремучем лесу",
    "Долго бродил он по лесу, пока не набрёл на избушку",
    "В этой избушке жила Баба-Яга",
    "Царь решил посчитать, сколько шагов сделал: 1000 + 500 - 200",
    "Баба-Яга сказала, что это 1300 шагов.",
]

# Функци для реализации меню для работы с пользователем и обработки выбранных действий.
def main():
    
    text = initial_text[:]
    menu_options = {
        1: ("Выровнять текст по левому краю", align_left),
        2: ("Выровнять текст по правому краю", align_right),
        3: ("Выровнять текст по ширине", align_width),
        4: ("Удаление всех вхождений заданного слова", remove_word),
        5: ("Замена одного слова другим во всём тексте", replace_word),
        6: ("Вычислить арифметические выражения", calculate_arithmetic_expressions),
        7: ("Найти и удалить слово или предложение по варианту", find_and_delete_by_letter),
        8: ("Завершить программу", lambda x: None)
    }

    while True:
        print("\nМеню:")
        for key, value in menu_options.items():
            print(f"{key}. {value[0]}")

        choice = input("Ваш выбор: ")
        try:
            choice = int(choice)
            if choice not in menu_options:
                raise ValueError
        except ValueError:
            print("Некорректный ввод. Значение должно соответствовать одному из номеров пунктов меню.")
            continue

        if choice == 8:
            break

        if choice in [4, 5, 7]:
            param = input("Введите параметр: ").strip()

        if choice == 4:
            text = menu_options[choice][1](text, param)
        elif choice == 5:
            new_param = input("На что заменить? ").strip()
            text = menu_options[choice][1](text, param, new_param)
        elif choice == 7:
            text = menu_options[choice][1](text, param)
        else:
            text = menu_options[choice][1](text)

        for line in text:
            print(line)

if __name__ == "__main__":
    main()