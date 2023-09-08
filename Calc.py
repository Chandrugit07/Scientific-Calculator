from tkinter import *
import math
from tkinter import Entry

root = Tk()
root.title("Scientific Calculator")
root.configure(background='azure1')
root.resizable(width=False, height=False)
root.geometry("580x700")
calc = Frame(root)
calc.grid()


class Calculator:
    def __init__(self):
        self.total = 0
        self.current = ''
        self.input_value = True
        self.check_sum = False
        self.op = ''
        self.result = False

    def input_entry(self, num):
        self.result = False
        first_number = txtDisplay.get()
        second_number = str(num)
        if self.input_value:
            self.current = second_number
            self.input_value = False
        else:
            if second_number == '.':
                if second_number in first_number:
                    return
            self.current = first_number + second_number
        self.display(self.current)

    def total_value(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    @staticmethod
    def display(value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def clear_entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def all_clear_entry(self):
        self.clear_entry()
        self.total = 0

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)


added_value = Calculator()

txtDisplay: Entry = Entry(calc, font=('Xena-ra', 20, 'bold'),
                          bg='Gray', fg='azure1',
                          bd=30, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=5, pady=1)
txtDisplay.insert(0, "0")

array_numbers = "789456123"
i = 0
btn = []
for j in range(2, 5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2,
                          bg='Gray', fg='azure1',
                          font=('Xena-ra', 20, 'bold'),
                          bd=4, text=array_numbers[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x=array_numbers[i]: added_value.input_entry(x)
        i += 1

Button(calc, text=chr(67), width=6,
       height=2, bg='azure3',
       font=('Xena-ra', 20, 'bold'), bd=4, command=added_value.clear_entry
       ).grid(row=1, column=0, pady=1)

Button(calc, text=chr(67) + chr(69),
       width=6, height=2,
       bg='azure3',
       font=('Xena-ra', 20, 'bold'),
       bd=4,
       command=added_value.all_clear_entry
       ).grid(row=1, column=1, pady=1)

Button(calc, text="\u221A", width=6, height=2,
       bg='azure3', font=('Xena-ra', 20, 'bold'),
       bd=4, command=added_value.squared
       ).grid(row=1, column=2, pady=1)

Button(calc, text="+", width=6, height=2,
       bg='azure3',
       font=('Xena-ra', 20, 'bold'),
       bd=4, command=lambda: added_value.operation("add")
       ).grid(row=1, column=3, pady=1)

Button(calc, text="-", width=6,
       height=2, bg='azure3',
       font=('Xena-ra', 20, 'bold'),
       bd=4, command=lambda: added_value.operation("sub")
       ).grid(row=2, column=3, pady=1)

Button(calc, text="x", width=6,
       height=2, bg='azure3',
       font=('Xena-ra', 20, 'bold'),
       bd=4, command=lambda: added_value.operation("multi")
       ).grid(row=3, column=3, pady=1)

Button(calc, text="/", width=6,
       height=2, bg='azure3',
       font=('Xena-ra', 20, 'bold'),
       bd=4, command=lambda: added_value.operation("divide")
       ).grid(row=4, column=3, pady=1)

Button(calc, text="0", width=6,
       height=2, bg='Gray', fg='azure1',
       font=('Xena-ra', 20, 'bold'),
       bd=4, command=lambda: added_value.input_entry(0)
       ).grid(row=5, column=0, pady=1)

Button(calc, text=".", width=6,
       height=2, bg='azure3',
       font=('Xena-ra', 20, 'bold'),
       bd=4, command=lambda: added_value.input_entry(".")
       ).grid(row=5, column=1, pady=1)

Button(calc, text="exp", width=6, height=2,
       bg='Gray', fg='azure1',
       font=('Xena-ra', 20, 'bold'),
       bd=4, command=added_value.exp
       ).grid(row=5, column=2, pady=1)

Button(calc, text="=", width=6,
       height=2, bg='azure3',
       font=('Xena-ra', 20, 'bold'),
       bd=4, command=added_value.total_value
       ).grid(row=5, column=3, pady=1)
# ROW 1 :
Button(calc, text="pi", width=6,
       height=2, bg='Gray', fg='azure1',
       font=('Xena-ra', 20, 'bold'),
       bd=4, command=added_value.pi
       ).grid(row=4, column=4, pady=1)

Button(calc, text="Cos", width=6,
       height=2, bg='Gray', fg='azure1',
       font=('Xena-ra', 20, 'bold'),
       bd=4, command=added_value.cos
       ).grid(row=5, column=4, pady=1)

Button(calc, text="tan", width=6,
       height=2, bg='Gray', fg='azure1',
       font=('Xena-ra', 20, 'bold'),
       bd=4, command=added_value.tan
       ).grid(row=6, column=0, pady=1)

Button(calc, text="sin", width=6,
       height=2, bg='Gray', fg='azure1',
       font=('Xena-ra', 20, 'bold'),
       bd=4, command=added_value.sin
       ).grid(row=6, column=1, pady=1)

# ROW 3 :
Button(calc, text="log", width=6,
       height=2, bg='Gray', fg='azure1',
       font=('Xena-ra', 20, 'bold'),
       bd=4, command=added_value.log
       ).grid(row=1, column=4, pady=1)
Button(calc, text="Mod", width=6,
       height=2, bg='Gray', fg='azure1',
       font=('Xena-ra', 20, 'bold'),
       bd=4, command=lambda: added_value.operation("mod")
       ).grid(row=2, column=4, pady=1)
Button(calc, text="e", width=6,
       height=2, bg='Gray', fg='azure1',
       font=('Xena-ra', 20, 'bold'),
       bd=4, command=added_value.e
       ).grid(row=3, column=4, pady=1)

root.mainloop()
