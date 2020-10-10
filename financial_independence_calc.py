from tkinter import *
import math

root = Tk()
headline = Label(root, text="This is financial independence calculator! enjoy :)",font='bold')
headline.pack()
e1 = Entry(root, width=25, borderwidth=5)
e1.pack()
e1.insert(0, "Enter your expenses rate ")
e2 = Entry(root, width=25, borderwidth=5)
e2.pack()
e2.insert(0, "Enter your saving rate ")
e3 = Entry(root, width=25, borderwidth=5)
e3.pack()
e3.insert(0, "Enter your withdrawal rate ")
e4 = Entry(root, width=25, borderwidth=5)
e4.pack()
e4.insert(0, "Enter your yield rate ")

def check_input(rate):
    """"""
    if not isinstance(rate,float):
        return False
    else:
        return True


def until_when(expenses_rate, savings_rate, withdrawal_rate, yield_rate):
    """"""
    x = math.log(((expenses_rate * (1 / withdrawal_rate) * yield_rate) / savings_rate) + 1)
    y = math.log(1 + yield_rate)
    return x / y


def myClick():
    expenses = e1.get()
    saving = e2.get()
    withdrawal = e3.get()
    yield_ = e4.get()
    result = until_when(float(expenses), float(saving), float(withdrawal), float(yield_))
    myLabel = Label(root, text="You have %.2f years until retirement!!" % result, font='bold')
    myLabel.pack()


myButton = Button(root, text="UNTIL WHEN!?", font='bold', command=myClick, borderwidth=5)
myButton.pack()
root.mainloop()
