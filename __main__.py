from tkinter import *

# Calculator v0.0
# Start Project of Calculator
# System Working With str() and eval()
cal = Tk()
cal.title("Calculator v0.0")
operator = ""
cal.rowconfigure(0, weight=1, minsize=1)
cal.rowconfigure(1, weight=1, minsize=1)
cal.rowconfigure(2, weight=1, minsize=1)
cal.rowconfigure(3, weight=1, minsize=1)
cal.rowconfigure(4, weight=1, minsize=1)
cal.rowconfigure(5, weight=1, minsize=1)

cal.columnconfigure(0, weight=1, minsize=1)
cal.columnconfigure(1, weight=1, minsize=1)
cal.columnconfigure(2, weight=1, minsize=1)
cal.columnconfigure(3, weight=1, minsize=1)


def btnClick(numbers):
    global operator
    operator += str(numbers)
    text_Input.set(operator)
    print(operator)


def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    print(sumup)
    print(eval(operator))
    operator = ""


def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")


text_Input = StringVar()

txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                   bg='powder blue', justify='right').grid(row=0, columnspan=4)

btn7 = Button(cal, bd=8, padx=15, pady=15, fg='black', font=('arial', 20, 'bold'), text="7", bg='powder blue',command=lambda: btnClick(7))
btn7.grid(row=1, column=0)

btn8 = Button(cal, padx=15, pady=15, bd=8, fg='black', font=('arial', 20, 'bold'),
              text="8", bg='powder blue', command=lambda: btnClick(8)).grid(row=1, column=1)

btn9 = Button(cal, padx=15, pady=15, bd=8, fg='black', font=('arial', 20, 'bold'),
              text="9", bg='powder blue', command=lambda: btnClick(9)).grid(row=1, column=2)

Addition = Button(cal, padx=15, pady=15, bd=8, fg='black', font=('arial', 20, 'bold'),
                  text="+", bg='powder blue', command=lambda: btnClick("+")).grid(row=1, column=3)

btn4 = Button(cal, padx=15, pady=15, bd=8, fg='black', font=('arial', 20, 'bold'),
              text="4", bg='powder blue', command=lambda: btnClick(4)).grid(row=2, column=0)

btn5 = Button(cal, padx=15, pady=15, bd=8, fg='black', font=('arial', 20, 'bold'),
              text="5", bg='powder blue', command=lambda: btnClick(5)).grid(row=2, column=1)

btn6 = Button(cal, padx=15, pady=15, bd=8, fg='black', font=('arial', 20, 'bold'),
              text="6", bg='powder blue', command=lambda: btnClick(6)).grid(row=2, column=2)

Subtraction = Button(cal, padx=15, pady=15, bd=8, fg='black', font=('arial', 20, 'bold'),
                     text="-", bg='powder blue', command=lambda: btnClick("-")).grid(row=2, column=3)

btn1 = Button(cal, padx=15, pady=15, bd=8, fg='black', font=('arial', 20, 'bold'),
              text="1", bg='powder blue', command=lambda: btnClick(1)).grid(row=3, column=0)

btn2 = Button(cal, padx=15, pady=15, bd=8, fg='black', font=('arial', 20, 'bold'),
              text="2", bg='powder blue', command=lambda: btnClick(2)).grid(row=3, column=1)

btn3 = Button(cal, padx=15, pady=15, bd=8, fg='black', font=('arial', 20, 'bold'),
              text="3", bg='powder blue', command=lambda: btnClick(3)).grid(row=3, column=2)

Multiplication = Button(cal, padx=15, pady=15, bd=8, fg='black', font=('arial', 20, 'bold'),
                        text="*", bg='powder blue', command=lambda: btnClick("*")).grid(row=3, column=3)

btn0 = Button(cal, padx=15, pady=15, bd=8, fg='black', font=('arial', 20, 'bold'),
              text="0", bg='powder blue', command=lambda: btnClick(0)).grid(row=4, column=0)

btnClear = Button(cal, padx=15, pady=15, bd=8, fg='black', font=('arial', 20, 'bold'),
                  text="C", bg="powder blue", command=btnClearDisplay).grid(row=4, column=1)

btnEquals = Button(cal, padx=15, pady=15, bd=8, fg='black', font=('arial', 20, 'bold'),
                   text="=", bg="powder blue", command=btnEqualsInput).grid(row=4, column=2)

Division = Button(cal, padx=15, pady=15, bd=8, fg='black', font=('arial', 20, 'bold'),
                  text="/", bg="powder blue", command=lambda: btnClick("/")).grid(row=4, column=3)

point = Button(cal, padx=15, pady=15, bd=8, fg='black', font=('arial', 20, 'bold'),
               text=".", bg="powder blue", command=lambda: btnClick(".")).grid(row=5, column=0)

cal.mainloop()
