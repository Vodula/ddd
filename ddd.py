import tkinter as tk
import math


def button_click(event):
    text = event.widget.cget("text")

    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + text)


def clear():
    entry.delete(0, tk.END)


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


def calculate_sin():
    try:
        result = math.sin(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


def exit_program():
    window.quit()


window = tk.Tk()
window.title("Калькулятор")

entry = tk.Entry(window, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('sin', 5, 0), ('C', 5, 1), ('Вихід', 5, 2), ('+', 5, 3)
]

for (text, row, column) in buttons:
    button = tk.Button(window, text=text, font=("Arial", 20), padx=20, pady=20)
    button.grid(row=row, column=column, sticky="nsew")
    if text == '=':
        button.config(command=calculate)
    elif text == 'sin':
        button.config(command=calculate_sin)
    elif text == 'C':
        button.config(command=clear)
    elif text == 'Вихід':
        button.config(command=exit_program)
    else:
        button.bind("<Button-1>", button_click)

equal_button = tk.Button(window, text="=", font=("Arial", 20), padx=20, pady=20, command=calculate)
equal_button.grid(row=4, column=2, columnspan=2, sticky="nsew")

for i in range(6):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

window.mainloop()
