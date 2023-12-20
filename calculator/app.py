from tkinter import *

#user interface
root = Tk()

root.title('Calculator')
root.geometry('275x257')
result = Text(root, height=2, width=16 , font=('Cascadia Code', 20))
result.grid(columnspan=5)

#functions 
calculation = ''
def operator(symbol):
    global calculation
    calculation += str(symbol)
    result.delete(1.0, 'end')
    result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation)) 
        result.delete(1.0, 'end')
        result.insert(1.0, calculation)
    except:
        clear_field()
        result.insert(1.0, 'Error')

def clear_field():
    global calculation
    calculation = ''
    result.delete(1.0, 'end')

#buttons
btn_1 = Button(root, text='1', command=lambda : operator(1), width=5, font=('Cascadia Code', 15))
btn_1.grid(row=2, column=1)

btn_2 = Button(root, text='2', command=lambda : operator(2), width=5, font=('Cascadia Code', 15))
btn_2.grid(row=2, column=2)

btn_3 = Button(root, text='3', command=lambda : operator(3), width=5, font=('Cascadia Code', 15))
btn_3.grid(row=2, column=3)

btn_4 = Button(root, text='4', command=lambda : operator(4), width=5, font=('Cascadia Code', 15))
btn_4.grid(row=3, column=1)

btn_5 = Button(root, text='5', command=lambda : operator(5), width=5, font=('Cascadia Code', 15))
btn_5.grid(row=3, column=2)

btn_6 = Button(root, text='6', command=lambda : operator(6), width=5, font=('Cascadia Code', 15))
btn_6.grid(row=3, column=3)

btn_7 = Button(root, text='7', command=lambda : operator(7), width=5, font=('Cascadia Code', 15))
btn_7.grid(row=4, column=1)

btn_8 = Button(root, text='8', command=lambda : operator(8), width=5, font=('Cascadia Code', 15))
btn_8.grid(row=4, column=2)

btn_9 = Button(root, text='9', command=lambda : operator(9), width=5, font=('Cascadia Code', 15))
btn_9.grid(row=4, column=3)

btn_0 = Button(root, text='0', command=lambda : operator(0), width=5, font=('Cascadia Code', 15))
btn_0.grid(row=5, column=2)

btn_plus = Button(root, text='+', command=lambda : operator('+'), width=5, font=('Cascadia Code', 15))
btn_plus.grid(row=2, column=4)

btn_minus = Button(root, text='-', command=lambda : operator('-'), width=5, font=('Cascadia Code', 15))
btn_minus.grid(row=3, column=4)

btn_division = Button(root, text='/', command=lambda : operator('/'), width=5, font=('Cascadia Code', 15))
btn_division.grid(row=4, column=4)

btn_multiply = Button(root, text='*', command=lambda : operator('*'), width=5, font=('Cascadia Code', 15))
btn_multiply.grid(row=5, column=4)

btn_open = Button(root, text='(', command=lambda : operator('('), width=5, font=('Cascadia Code', 15))
btn_open.grid(row=5, column=1)

btn_close = Button(root, text=')', command=lambda : operator(')'), width=5, font=('Cascadia Code', 15))
btn_close.grid(row=5, column=3)

btn_decimal = Button(root, text='.', command=lambda : operator('.'), width=5, font=('Cascadia Code', 15))
btn_decimal.grid(row=6, column=4)

btn_equal = Button(root, text='=', command=evaluate_calculation, width=5, font=('Cascadia Code', 15))
btn_equal.grid(row=6, column=3)

btn_clear = Button(root, text='C', command=clear_field, width=11, font=('Cascadia Code', 15))
btn_clear.grid(row=6, column=1, columnspan=2)


#run calculator 
root.mainloop()










    