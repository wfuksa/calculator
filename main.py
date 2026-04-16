import tkinter as tk

value = ""

window = tk.Tk()
window.title("Calculator")
window.geometry("475x800")
window.resizable(False, False)

def clear_all():
    global value
    value = ""

def set_one():
    global value
    value = value + "1"
    print(value)

def set_two():
    global value
    value = value + "2"
    print(value)

def set_three():
    global value
    value = value + "3"
    print(value)

def set_four():
    global value
    value = value + "4"
    print(value)

def set_five():
    global value
    value = value + "5"
    print(value)

def set_six():
    global value
    value = value + "6"
    print(value)

def set_seven():
    global value
    value = value + "7"
    print(value)

def set_eight():
    global value
    value = value + "8"
    print(value)

def set_nine():
    global value
    value = value + "9"
    print(value)

def set_zero():
    global value
    value = value + "0"
    print(value)

button = tk.Button(window, text="1", command=set_one)
button.place(x=15, y=340, width=100, height=100)

button = tk.Button(window, text="2", command=set_two)
button.place(x=130, y=340, width=100, height=100)

button = tk.Button(window, text="3", command=set_three)
button.place(x=245, y=340, width=100, height=100)

button = tk.Button(window, text="4", command=set_four)
button.place(x=15, y=450, width=100, height=100)

button = tk.Button(window, text="5", command=set_five)
button.place(x=130, y=450, width=100, height=100)

button = tk.Button(window, text="6", command=set_six)
button.place(x=245, y=450, width=100, height=100)

button = tk.Button(window, text="7", command=set_seven)
button.place(x=15, y=560, width=100, height=100)

button = tk.Button(window, text="8", command=set_eight)
button.place(x=130, y=560, width=100, height=100)

button = tk.Button(window, text="9", command=set_nine)
button.place(x=245, y=560, width=100, height=100)

button = tk.Button(window, text="0", command=set_zero)
button.place(x=15, y=670, width=215, height=100)

button = tk.Button(window, text="+")
button.place(x=360, y=340, width=100, height=100)

button = tk.Button(window, text="-")
button.place(x=360, y=450, width=100, height=100)

button = tk.Button(window, text="/")
button.place(x=360, y=560, width=100, height=100)

button = tk.Button(window, text="x")
button.place(x=360, y=670, width=100, height=100)

button = tk.Button(window, text="=")
button.place(x=245, y=670, width=100, height=100)

button = tk.Button(window, text="AC", command=clear_all)
button.place(x=15, y=230, width=100, height=100)

display = tk.Entry(window, bg="white", fg="black", font=("arial", 40))
display.place(x=15, y=20, width=445, height=100)

window.mainloop()