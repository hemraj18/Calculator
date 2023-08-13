import tkinter as tk

calculation = ""

def add_to_calcualtions(symbol):
    global calculation
    calculation += str(symbol)
    test_result.delete(1.0, tk.END) 
    test_result.insert(1.0, calculation) 
    
def evaluate_calculations():
    global calculation
    try:
        calculation = str(eval(calculation))
        test_result.delete(1.0, tk.END)
        test_result.insert(1.0, calculation)
    except:
        clear_field()
        test_result.insert(1.0, "Error" )
    
def clear_field():
    global calculation
    calculation = ""
    test_result.delete(1.0, tk.END)

def handle_key(event):
    key = event.char
    if key.isdigit():
        add_to_calcualtions(int(key))
    elif key == "+":
        add_to_calcualtions("+")
    elif key == "-":
        add_to_calcualtions("-")
    elif key == "*":
        add_to_calcualtions("*")
    elif key == "/":
        add_to_calcualtions("/")
    elif key == "=" or key == "\r":
        evaluate_calculations()
    elif key == "c":
        clear_field()    

root = tk.Tk()
root.geometry("300x275")
root.title("Calculator by Hemraj")

test_result = tk.Text(root, height=2, width= 16, font=("Ariel 24 "))
test_result.grid(ipadx=5, ipady=2, columnspan=10)

buttons = [
    ("7", 3, 1), ("8", 3, 2), ("9", 3, 3), ("/", 2, 4),
    ("4", 4, 1), ("5", 4, 2), ("6", 4, 3), ("*", 3, 4),
    ("1", 5, 1), ("2", 5, 2), ("3", 5, 3), ("-", 4, 4),
    ("0", 6, 2), (".", 6, 3), ("+", 5, 4),
    ("Sqrt", 2, 2), ("%", 2, 3)
]

for text, row, column in buttons:
    button = tk.Button(root, text=text, width=5, font=("Arial 14"), command=lambda t=text: add_to_calcualtions(t))
    button.grid(row=row, column=column)
but_return = tk.Button(root, text="=", width=5, font=("Arial 14"), command=evaluate_calculations)
but_return.grid(row=5, column=4)
but_clear = tk.Button(root, text="C", width=5, font=("Arial 14"), command=clear_field)
but_clear.grid(row=2, column=1)

root.bind("<Key>", handle_key)

root.mainloop()