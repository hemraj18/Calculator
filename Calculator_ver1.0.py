import tkinter as tk
from math import sqrt

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

root = tk.Tk()
root.geometry("300x275")
root.title("Calculator by Hemraj")

test_result = tk.Text(root, height=2, width= 16, font=("Ariel 24 "))
test_result.grid(ipadx=5, ipady=2, columnspan=10)

btn1 = tk.Button(root, text="1", command=(lambda:add_to_calcualtions(1)), width=5, font=("Ariel 14"))
btn1.grid(row=5, column=1)
btn2 = tk.Button(root, text="2", command=(lambda:add_to_calcualtions(2)), width=5, font=("Ariel 14"))
btn2.grid(row=5, column=2)
btn3 = tk.Button(root, text="3", command=(lambda:add_to_calcualtions(3)), width=5, font=("Ariel 14"))
btn3.grid(row=5, column=3)
btn4 = tk.Button(root, text="4", command=(lambda:add_to_calcualtions(4)), width=5, font=("Ariel 14"))
btn4.grid(row=4, column=1)
btn5 = tk.Button(root, text="5", command=(lambda:add_to_calcualtions(5)), width=5, font=("Ariel 14"))
btn5.grid(row=4, column=2)
btn6 = tk.Button(root, text="6", command=(lambda:add_to_calcualtions(6)), width=5, font=("Ariel 14"))
btn6.grid(row=4, column=3)
btn7 = tk.Button(root, text="7", command=(lambda:add_to_calcualtions(7)), width=5, font=("Ariel 14"))
btn7.grid(row=3, column=1)
btn8 = tk.Button(root, text="8", command=(lambda:add_to_calcualtions(8)), width=5, font=("Ariel 14"))
btn8.grid(row=3, column=2)
btn9 = tk.Button(root, text="9", command=(lambda:add_to_calcualtions(9)), width=5, font=("Ariel 14"))
btn9.grid(row=3, column=3)
btn0 = tk.Button(root, text="0", command=(lambda:add_to_calcualtions(0)), width=5, font=("Ariel 14"))
btn0.grid(row=6, column=2)
btnopen = tk.Button(root, text="%", command=(lambda:add_to_calcualtions("%")), width=5, font=("Ariel 14"))
btnopen.grid(row=2, column=3)
btnsqrt = tk.Button(root, text="Sqrt", command=(lambda:add_to_calcualtions("**2")), width=5, font=("Ariel 14"))
btnsqrt.grid(row=2, column=2)
btnadd = tk.Button(root, text="+", command=(lambda:add_to_calcualtions("+")), width=5, font=("Ariel 14"))
btnadd.grid(row=5, column=4)
btnsub = tk.Button(root, text="-", command=(lambda:add_to_calcualtions("-")), width=5, font=("Ariel 14"))
btnsub.grid(row=4, column=4)
btnmul = tk.Button(root, text="*", command=(lambda:add_to_calcualtions("*")), width=5, font=("Ariel 14"))
btnmul.grid(row=3, column=4)
btndiv = tk.Button(root, text="/", command=(lambda:add_to_calcualtions("/")), width=5, font=("Ariel 14"))
btndiv.grid(row=2, column=4)
btnclear = tk.Button(root, text="C", command=clear_field, width=5, font=("Ariel 14"))
btnclear.grid(row=2, column=1 )
btnequal = tk.Button(root, text="=", command=evaluate_calculations, width=5, font=("Ariel 14"))
btnequal.grid(row=6, column=4)
btndot = tk.Button(root, text=".", command=(lambda:add_to_calcualtions(".")), width=5, font=("Ariel 14"))
btndot.grid(row=6, column=3)

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

root.bind("<Key>", handle_key)

root.mainloop()