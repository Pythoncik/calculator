import tkinter as tk


def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + value)


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")


def clear():
    entry.delete(0, tk.END)


root = tk.Tk()
root.title("Калькулятор")


entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

for button in buttons:
    action = lambda x=button: button_click(x) if x != '=' else calculate()
    tk.Button(root, text=button, padx=20, pady=20, command=action).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1


tk.Button(root, text="Очистить", padx=20, pady=20, command=clear).grid(row=row, columnspan=4)


root.mainloop()
