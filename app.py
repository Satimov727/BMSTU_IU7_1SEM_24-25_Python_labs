# Лимарев Степан ИУ7-21Б. Используя библиотеку создания оконных приложений Tkinter, создать приложение, реализующее 
# индивидуальное задание.
# Сложение и вычитание чисел в 5-й системе счисления.


import tkinter as tk
from tkinter import messagebox
from operations import add_in_base_5, subtract_in_base_5


# Функция для добавления символа в поле ввода.
def append_digit(digit):
    if digit in '-01234.':
        active_entry = window.focus_get()
        if isinstance(active_entry, tk.Entry):
            current_text = active_entry.get()
            new_text = current_text + digit
            active_entry.delete(0, tk.END)
            active_entry.insert(0, new_text)


# Функция для сложения двух чисел в пятиричной системе.
def perform_addition():

    try:
        num1 = num1_entry.get().strip()
        num2 = num2_entry.get().strip()
        
        if not num1 or not num2:
            raise ValueError("Некорректный ввод. Должны быть введены оба числа.")
        
        if not all(c in '-01234.' for c in num1) or not all(c in '-01234.' for c in num2):
            raise ValueError("Некорректный ввод. Числа должны содержать только цифры от 0 до 4 и точку.")

        if num2.startswith('-'):
            result = subtract_in_base_5(num1, num2.lstrip('-'))

        result = add_in_base_5(num1, num2)
        result_entry.config(state='normal')
        result_entry.delete(0, tk.END)
        result_entry.insert(0, result)
        result_entry.config(state='readonly')

    except Exception as e:
        messagebox.showerror("Некорректный ввод. Должны быть введены пятиричные числа с правильной комбинацией символов", str(e))


# Функция для вычитания двух чисел в пятиричной системе.
def perform_subtraction():

    try:
        num1 = num1_entry.get().strip()
        num2 = num2_entry.get().strip()
        
        if not num1 or not num2:
            raise ValueError("Некорректный ввод. Должны быть введены оба числа.")
        
        if not all(c in '-01234.' for c in num1) or not all(c in '-01234.' for c in num2):
            raise ValueError("Некорректный ввод. Числа должны содержать только цифры от 0 до 4 и точку.")
            
        result = subtract_in_base_5(num1, num2)
        result_entry.config(state='normal')
        result_entry.delete(0, tk.END)
        result_entry.insert(0, result)
        result_entry.config(state='readonly')

    except Exception as e:
        messagebox.showerror("Некорректный ввод. Должны быть введены числа с правильной комбинацией символов", str(e))


# Функция для удаления последнего символа из поля ввода.
def delete_last_char():
    active_entry = window.focus_get()
    if isinstance(active_entry, tk.Entry):
        current_text = active_entry.get()
        if current_text:
            new_text = current_text[:-1]
            active_entry.delete(0, tk.END)
            active_entry.insert(0, new_text)


# Функция для очистки всего поля ввода.
def clear_active_field():
    active_entry = window.focus_get()
    if isinstance(active_entry, tk.Entry):
        active_entry.delete(0, tk.END)


# Функция для очистки всех полей ввода.
def clear_all_fields():
    num1_entry.delete(0, tk.END)
    num2_entry.delete(0, tk.END)
    result_entry.config(state='normal')
    result_entry.delete(0, tk.END)
    result_entry.config(state='readonly')


# Окно калькулятора.
window = tk.Tk()
window.title("Пятиричный калькулятор")
window.geometry('500x500')


# Меню.
menu_bar = tk.Menu(window)
operations_menu = tk.Menu(menu_bar, tearoff=False)
clear_menu = tk.Menu(menu_bar, tearoff=False)
about_menu = tk.Menu(menu_bar, tearoff=False)


# Операции.
menu_bar.add_cascade(label="Операции", menu=operations_menu)
operations_menu.add_command(label="Сложить", command=perform_addition)
operations_menu.add_command(label="Вычесть", command=perform_subtraction)


# Функции очситки.
menu_bar.add_cascade(label="Очистка", menu=clear_menu)
clear_menu.add_command(label="Удалить последний символ", command=delete_last_char)
clear_menu.add_command(label="Очистить активное поле", command=clear_active_field)
clear_menu.add_command(label="Очистить все поля", command=clear_all_fields)


# Информация.
menu_bar.add_cascade(label="Информация", menu=about_menu)
about_menu.add_command(label="О программе", command=lambda: messagebox.showinfo("О программе", "Калькулятор сложения и вычитания чисел в пятиричной системе."))
about_menu.add_command(label="Об авторе", command=lambda: messagebox.showinfo("Об авторе", "Автор: Лимарев Степан ИУ7-21Б."))

window.config(menu=menu_bar)


# Поле ввода первого числа.
num1_label = tk.Label(text="Первое число:")
num1_entry = tk.Entry(width=20)
num1_label.pack(pady=(10, 0))
num1_entry.pack(pady=(0, 10))


# Поле ввода второго числа.
num2_label = tk.Label(text="Второе число:")
num2_entry = tk.Entry(width=20)
num2_label.pack(pady=(10, 0))
num2_entry.pack(pady=(0, 10))


# Кнопки операций.
add_button = tk.Button(text="Сложить", width=15, command=perform_addition)
subtract_button = tk.Button(text="Вычесть", width=15, command=perform_subtraction)
add_button.pack(pady=(10, 5))
subtract_button.pack(pady=(5, 10))


# Результат.
result_label = tk.Label(text="Результат:")
result_entry = tk.Entry(state='readonly', width=30)
result_label.pack(pady=(10, 0))
result_entry.pack(pady=(0, 10))


# Кнопки ввода цифр.
button_frame = tk.Frame()
for i in range(9, -1, -1):
    button = tk.Button(button_frame, text=str(i), width=3, command=lambda x=i: append_digit(str(x)))
    button.grid(row=int((8-i)/3), column=(i+1)%3, padx=2, pady=2)

dot_button = tk.Button(button_frame, text='.', width=3, command=lambda: append_digit('.'))
dot_button.grid(row=3, column=0, padx=2, pady=2)

button_frame.pack()


# Кнопки удаления символов и очистки полей.
del_last_char_button = tk.Button(text="Удалить последний символ", command=delete_last_char)
clear_active_field_button = tk.Button(text="Очистить активное поле", command=clear_active_field)
clear_all_fields_button = tk.Button(text="Очистить все поля", command=clear_all_fields)

del_last_char_button.pack(pady=(10, 5))
clear_active_field_button.pack(pady=(5, 5))
clear_all_fields_button.pack(pady=(5, 10))


# Привязка клавиш.
window.bind('<Return>', lambda event: perform_addition())
window.bind('<KP_Add>', lambda event: perform_addition())
window.bind('<KP_Subtract>', lambda event: perform_subtraction())
window.bind('<BackSpace>', lambda event: delete_last_char())

window.mainloop()