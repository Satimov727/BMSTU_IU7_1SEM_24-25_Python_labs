# Лимарев Степан ИУ7-21Б. Используя библиотеку создания оконных приложений Tkinter, создать приложение, реализующее 
# индивидуальное задание.
# Сложение и вычитание вещественных чисел в 5-й системе счисления.


# Функция для перевода числа из десятичной системы счисления в пятиричную.
def to_base_5(number, max_precision=None):
    
    if number == 0:
        return '0'
    
    result = []
    sign = '-' if float(number) < 0 else ''
    number = abs(float(number))
    
    int_part = int(number)
    fract_part = number - int_part
    
    # Целая часть.
    int_digits = []
    while int_part > 0:
        remain = int_part % 5
        int_digits.append(str(remain))
        int_part //= 5
    
    result.extend(reversed(int_digits))
    
    # Дробная часть.
    if fract_part > 0:
        result.append('.')
        precision = max_precision or 0
        
        for _ in range(precision):
            fract_part *= 5
            digit = int(fract_part)
            result.append(str(digit))
            fract_part -= digit
            if fract_part == 0:
                break
    
    return sign + ''.join(result)


# Функция для перевода числа из пятиричной системы счисления в десятичную.
def from_base_5(base_5_number):

    base_5_number = str(base_5_number)
    point_index = base_5_number.find('.')
    
    if point_index == -1:
        if base_5_number.startswith("-"):
            dec_value = -sum(int(digit) * (5 ** index) for index, digit in enumerate(reversed(base_5_number.lstrip("-"))))
        else:
            dec_value = sum(int(digit) * (5 ** index) for index, digit in enumerate(reversed(base_5_number)))
    else:

        int_part = base_5_number[:point_index]
        fract_part = base_5_number[point_index + 1:]
        
        if base_5_number.startswith("-"):
            mul = -1
        else:
            mul = 1

        int_value = sum(int(digit) * (5 ** index) for index, digit in enumerate(reversed(int_part.lstrip("-"))))
        fract_value = sum(int(digit) * (5 ** -(index + 1)) for index, digit in enumerate(fract_part))
        
        dec_value = mul * (int_value + fract_value)

    return dec_value


def round_result(value, max_precision):

    scale = 10 ** max_precision
    rounded_value = round(value * scale) / scale

    return rounded_value


# Функция для сложения двух чисел в пятиричной системе счисления.
def add_in_base_5(num1, num2):

    dec_num1 = from_base_5(num1)
    dec_num2 = from_base_5(num2)
    
    sum_dec = dec_num1 + dec_num2
    
    max_precision = max(len(num1.split('.')[1]) if '.' in num1 else 0, len(num2.split('.')[1]) if '.' in num2 else 0)

    rounded_sum = round_result(sum_dec, max_precision)
    
    return to_base_5(rounded_sum, max_precision=max_precision)


# Функция для вычитания двух чисел в пятиричной системе счисления.
def subtract_in_base_5(num1, num2):

    dec_num1 = from_base_5(num1)
    dec_num2 = from_base_5(num2)
    
    diff_dec = dec_num1 - dec_num2
    
    max_precision = max(len(num1.split('.')[1]) if '.' in num1 else 0, len(num2.split('.')[1]) if '.' in num2 else 0)
    
    return to_base_5(diff_dec, max_precision=max_precision)
