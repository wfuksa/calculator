import tkinter as tk

value = ""

window = tk.Tk()
window.title("Calculator")
window.geometry("475x800")
window.resizable(False, False)

def update_display():
    display.delete(0, tk.END)
    display.insert(0, value)

def clear_all():
    global value
    value = ""
    update_display()

def add_digit(digit):
    global value
    value = value + str(digit)
    update_display()

def add_operator(operator):
    global value

    if value == "":
        if operator == "-":
            value = "-"
        update_display()
        return

    if value[-1] in "+-*/":
        value = value[:-1] + operator
    else:
        value = value + operator

    update_display()

def calculate():
    global value

    if value == "":
        return

    if value[-1] in "+-*/":
        return

    try:
        result = eval(value)
        if result == int(result):
            value = str(int(result))
        else:
            value = str(result)
        update_display()
    except:
        value = "Error"
        update_display()

button = tk.Button(window, text="1", command=lambda: add_digit(1))
button.place(x=15, y=340, width=100, height=100)

button = tk.Button(window, text="2", command=lambda: add_digit(2))
button.place(x=130, y=340, width=100, height=100)

button = tk.Button(window, text="3", command=lambda: add_digit(3))
button.place(x=245, y=340, width=100, height=100)

button = tk.Button(window, text="4", command=lambda: add_digit(4))
button.place(x=15, y=450, width=100, height=100)

button = tk.Button(window, text="5", command=lambda: add_digit(5))
button.place(x=130, y=450, width=100, height=100)

button = tk.Button(window, text="6", command=lambda: add_digit(6))
button.place(x=245, y=450, width=100, height=100)

button = tk.Button(window, text="7", command=lambda: add_digit(7))
button.place(x=15, y=560, width=100, height=100)

button = tk.Button(window, text="8", command=lambda: add_digit(8))
button.place(x=130, y=560, width=100, height=100)

button = tk.Button(window, text="9", command=lambda: add_digit(9))
button.place(x=245, y=560, width=100, height=100)

button = tk.Button(window, text="0", command=lambda: add_digit(0))
button.place(x=15, y=670, width=215, height=100)

button = tk.Button(window, text="+", command=lambda: add_operator("+"))
button.place(x=360, y=340, width=100, height=100)

button = tk.Button(window, text="-", command=lambda: add_operator("-"))
button.place(x=360, y=450, width=100, height=100)

button = tk.Button(window, text="/", command=lambda: add_operator("/"))
button.place(x=360, y=560, width=100, height=100)

button = tk.Button(window, text="*", command=lambda: add_operator("*"))
button.place(x=360, y=670, width=100, height=100)

button = tk.Button(window, text="=", command=calculate)
button.place(x=245, y=670, width=100, height=100)

button = tk.Button(window, text="AC", command=clear_all)
button.place(x=15, y=230, width=100, height=100)

display = tk.Entry(window, bg="white", fg="black", font=("arial", 40))
display.place(x=15, y=20, width=445, height=100)

window.mainloop()