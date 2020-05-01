from tkinter import *
from tkinter import ttk
from math import *
from operator import neg

# version 0.1
# Add New More Buttons and make New Design to Surface
# Add Button Remove and Call Last Answer
# Add Equation and Function as Testing beta
win = Tk()
win.title("Scientific Calculator v0.1")

Answer = ''
last = ['']
TextInput = StringVar()
clear = False
full = False
half = False


def Clear():
    global operator, mode, clear, full, half, last
    last = ['']
    operator = ''
    TextInput.set('')

    if mode == 'Equation':
        TextInput.set(f'''Equation : aX² + bX + c = 0''')
        print(f'''Equation : aX² + bX + c = 0''')
        TextInput.set(f'a = ')

    elif mode == 'Function':
        TextInput.set(f'From : ')

    clear = False
    full = False
    half = False


def Remove():
    global operator, last
    if clear:
        Clear()

    try:
        operator = str(operator).replace(last[-1], '')
        last.remove(last[-1])

    except IndexError:
        pass

    Click()


def InputClick(Operation):
    global operator, last
    if clear:
        Clear()

    last.append((str(Operation)))
    operator += str(Operation)

    Click()


def Click():
    global operator
    if mode == "Operation":
        TextInput.set(operator)
        print(operator)

    elif mode == 'Equation':
        if not full and not half:
            TextInput.set(f'a = {operator}')
            print(f'a = {operator}')

        elif not full and half:
            TextInput.set(f'b = {operator}')
            print(f'b = {operator}')

        elif full:
            TextInput.set(f'c = {operator}')
            print(f'c = {operator}')

    elif mode == "Function":
        if not full and not half:
            TextInput.set(f'From : {operator}')
            print(f'From : {operator}')

        elif not full and half:
            TextInput.set(f'To : {operator}')
            print(f'To : {operator}')

        elif full:
            TextInput.set(f'f(x) = {operator}')
            print(f'f(x) = {operator}')


def SwitchFunction(Function):
    global mode
    mode = Function
    Clear()


def InputEquals():
    global operator, Answer, clear, a, b, c, v, w, full, half
    try:
        if mode == 'Operation':
            operator = str(TextDisplay.get()).lower()
            Answer = str(eval(operator))
            TextInput.set(f'{operator} = {Answer}')
            print(f'{operator} = {Answer}')
            clear = True

        elif mode == 'Equation':
            if not full:
                if not half:
                    a = float(operator)
                    operator = ""
                    TextInput.set(f'b = ')
                    half = True

                elif half:
                    b = float(operator)
                    operator = ""
                    TextInput.set(f'c = ')
                    full = True

            elif full:
                c = float(operator)
                d = float((b ** 2) - 4 * a * c)
                nd = neg(d)
                nb = neg(b)
                cx = complex
                if a > 0 or a < 0:
                    TextInput.set(f'''
The Equation : {a}X² + ({b})X + ({c}) = 0

 The Equation Have Two Solutions For X :

  ∆ =  b² - 4ac

  ∆ = {b}² - (4 x ({a}) x ({c})) 
    = {b ** 2} - ({4 * a * c}) 
    = {d}''')
                    print(f'''
The Equation : {a}X² + ({b})X + ({c}) = 0

 The Equation Have Two Solutions For X :

  ∆ =  b² - 4ac

  ∆ = {b}² - (4 x ({a}) x ({c})) 
    = {b ** 2} - ({4 * a * c}) 
    = {d}''')
                    if d == 0:
                        TextInput.set(f''' 
   ∆=0 : X = -b / 2a

    X[1] = X[2] = ({neg(b)}) / (2 x {a})
    X[1] = X[2] = {(neg(b)) / (2 * a)}''')
                        print(f''' 
   ∆=0 : X = -b / 2a

    X[1] = X[2] = ({neg(b)}) / (2 x {a})
    X[1] = X[2] = {(neg(b)) / (2 * a)}''')
                    elif d >= 0:
                        TextInput.set(f'''
∆>0 : X = (-b ± √∆) / 2a

 X[1] = ({nb} + √{d}) / (2 x {a})
      = ({nb} + {sqrt(d)}) / ({2 * a})
      = {(nb + sqrt(d)) / (2 * a)}

 X[2] = ({nb} - √{d}) / (2 x {a})
      = ({nb} - {sqrt(d)}) / ({2 * a})
      = {(nb - sqrt(d)) / (2 * a)}''')
                        print(f'''
∆>0 : X = (-b ± √∆) / 2a

 X[1] = ({nb} + √{d}) / (2 x {a})
      = ({nb} + {sqrt(d)}) / ({2 * a})
      = {(nb + sqrt(d)) / (2 * a)}

 X[2] = ({nb} - √{d}) / (2 x {a})
      = ({nb} - {sqrt(d)}) / ({2 * a})
      = {(nb - sqrt(d)) / (2 * a)}''')
                    elif d <= 0:
                        TextInput.set(f'''    = {nd}j²

∆<0 : X = (-b ± j√∆) / 2a

 X[1] = ({nb} + √({nd})j) / (2 x {a})
      = {cx(nb + sqrt(nd) * 1j)} / ({2 * a})
      = {cx((nb + sqrt(nd) * 1j) / (2 * a))}

 X[2] = ({nb} - √({nd})j) / (2 x {a})
      = {cx(nb - sqrt(nd) * 1j)} / ({2 * a})
      = {cx((nb - sqrt(nd) * 1j) / (2 * a))}

 z = a ± bj

  a = {nb / (2 * a)}
  b = {sqrt(nd) / (2 * a)}''')
                        print(f'''    = {nd}j²

∆<0 : X = (-b ± j√∆) / 2a

 X[1] = ({nb} + √({nd})j) / (2 x {a})
      = {cx(nb + sqrt(nd) * 1j)} / ({2 * a})
      = {cx((nb + sqrt(nd) * 1j) / (2 * a))}

 X[2] = ({nb} - √({nd})j) / (2 x {a})
      = {cx(nb - sqrt(nd) * 1j)} / ({2 * a})
      = {cx((nb - sqrt(nd) * 1j) / (2 * a))}

 z = a ± bj

  a = {nb / (2 * a)}
  b = {sqrt(nd) / (2 * a)}''')
                elif a == 0:
                    if b == 0 and c == 0:
                        TextInput.set("   Empty Solution {Ꞩ}.")
                        print("   Empty Solution {Ꞩ}.")
                    elif b == 0:
                        TextInput.set("   Empty Solution {Ꞩ}.")
                        print("   Empty Solution {Ꞩ}.")
                    elif c == 0:
                        TextInput.set(f'''The Equation : {b}X + ({c}) = 0

 The Equation Have One Solution For X :

  {b}X = 0
  X = 0''')
                        print(f'''The Equation : {b}X + ({c}) = 0

 The Equation Have One Solution For X :

  {b}X = 0
  X = 0''')
                    else:
                        TextInput.set(f'''The Equation : {b}X + ({c}) = 0 

 The Equation Have One Solution For X :  

  {b}X = {neg(c)}    
  X = {neg(c)} / {b}
  X = {neg(c) / b}''')
                        print(f'''The Equation : {b}X + ({c}) = 0 

 The Equation Have One Solution For X :  

  {b}X = {neg(c)}    
  X = {neg(c)} / {b}
  X = {neg(c) / b}''')
                clear = True
                full = False
                half = False

        elif mode == 'Function':
            if not full:
                if not half:
                    v = int(operator)
                    operator = ""
                    TextInput.set(f'To : ')
                    half = True

                elif half:
                    w = int(operator) + 1
                    operator = ""
                    TextInput.set(f'f(x) = ')
                    full = True

            elif full:
                TextInput.set(f'f(x) = {operator}')
                print(f'f(x) = {operator}')
                for x in range(v, w):
                    TextInput.set(f'f({x}) = {eval(operator)}')
                    print(f'f({x}) = {eval(operator)}')
                clear = True
                full = False
                half = False

    except ZeroDivisionError:
        pass
    except ValueError:
        pass
    except SyntaxError:
        pass
    except NameError:
        pass


def DisplayButtons():
    global win, TextDisplay, cmt, tnt

    # ROW 0
    # TextDisplay
    TextDisplay = Spinbox(win, relief=RIDGE, width=101, font=('Segoe UI Symbol', 16), textvariable=TextInput, bd=15,
                          bg='powder blue')
    TextDisplay.grid(row=0, column=0, columnspan=12)

    # ROW 1
    tnt = Text(win, relief=RIDGE, width=26, height=7, font=('Segoe UI Symbol', 16), bd=10, bg='powder blue')
    tnt.grid(row=1, column=11, rowspan=5)

    # btn7
    Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="7", bg='powder blue',
           relief=RIDGE, command=lambda: InputClick(7)).grid(row=1, column=0)

    # btn8
    Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="8", bg='powder blue',
           relief=RIDGE, command=lambda: InputClick(8)).grid(row=1, column=1)

    # btn9
    Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="9", bg='powder blue',
           relief=RIDGE, command=lambda: InputClick(9)).grid(row=1, column=2)

    # Addition
    Button(win, width=6, height=1, bd=4, fg='purple', font=('Segoe UI Symbol', 16), text="+", bg='powder blue',
           relief=RIDGE, command=lambda: InputClick("+")).grid(row=1, column=3)

    # PI
    Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="π", bg="powder blue",
           relief=RIDGE, command=lambda: InputClick('pi')).grid(row=1, column=4)

    # left
    Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="(", bg="powder blue",
           relief=RIDGE, command=lambda: InputClick('(')).grid(row=1, column=5)

    # right
    Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text=")", bg="powder blue",
           relief=RIDGE, command=lambda: InputClick(')')).grid(row=1, column=6)

    # Clear
    Button(win, width=3, height=1, bd=4, fg='red', font=('Marlett', 23), text="r", bg="powder blue", relief=RIDGE,
           command=lambda: Clear()).grid(row=1, column=8)

    # Remove
    Button(win, width=3, height=1, bd=4, fg='blue', font=('Wingdings', 21), text="Õ", bg="powder blue",
           relief=RIDGE, command=lambda: Remove()).grid(row=1, column=9)
    # ROW 2
    # btn4
    Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="4", bg='powder blue',
           relief=RIDGE, command=lambda: InputClick(4)).grid(row=2, column=0)

    # btn5
    Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="5", bg='powder blue',
           relief=RIDGE, command=lambda: InputClick(5)).grid(row=2, column=1)

    # btn6
    Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="6", bg='powder blue',
           relief=RIDGE, command=lambda: InputClick(6)).grid(row=2, column=2)

    # subtraction
    Button(win, width=6, height=1, bd=4, fg='purple', font=('Segoe UI Symbol', 16), text="-", bg='powder blue',
           relief=RIDGE, command=lambda: InputClick("-")).grid(row=2, column=3)

    # Logarithm base e
    Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="logₑ", bg="powder blue",
           relief=RIDGE, command=lambda: InputClick('log(')).grid(row=2, column=4)

    # Factorial
    Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="!", bg='powder blue',
           relief=RIDGE, command=lambda: InputClick("factorial(")).grid(row=2, column=9)
    # ROW 3
    # btn1
    Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="1", bg='powder blue',
           relief=RIDGE, command=lambda: InputClick(1)).grid(row=3, column=0)

    # btn2
    Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="2", bg='powder blue',
           relief=RIDGE, command=lambda: InputClick(2)).grid(row=3, column=1)

    # btn3
    Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="3", bg='powder blue',
           relief=RIDGE, command=lambda: InputClick(3)).grid(row=3, column=2)

    # Multiplication
    Button(win, width=6, height=1, bd=4, fg='purple', font=('Segoe UI Symbol', 16), text="*", bg='powder blue',
           relief=RIDGE, command=lambda: InputClick("*")).grid(row=3, column=3)
    # ROW 4
    # btn0
    Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="0", bg='powder blue',
           relief=RIDGE, command=lambda: InputClick(0)).grid(row=4, column=0)

    # point
    Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text=".", bg="powder blue",
           relief=RIDGE, command=lambda: InputClick(".")).grid(row=4, column=1)

    # btnEquals
    Button(win, width=6, height=1, bd=4, fg='purple', font=('Segoe UI Symbol', 16), text="=", bg="powder blue",
           relief=RIDGE, command=InputEquals).grid(row=4, column=2)

    # Division
    Button(win, width=6, height=1, bd=4, fg='purple', font=('Segoe UI Symbol', 16), text="/", bg="powder blue",
           relief=RIDGE, command=lambda: InputClick("/")).grid(row=4, column=3)

    # Answer
    Button(win, width=6, height=1, bd=4, fg='green', font=('Segoe UI Symbol', 16), text='Answer', bg="powder blue",
           relief=RIDGE, command=lambda: InputClick(Answer)).grid(row=4, column=4)

    # x
    Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text='x', bg="powder blue",
           relief=RIDGE, command=lambda: InputClick('x')).grid(row=4, column=5)

    # Operation
    Button(win, width=13, height=1, bd=4, fg='blue', font=('Segoe UI Symbol', 16), text="Operation", bg="powder blue",
           relief=RIDGE, command=lambda: SwitchFunction("Operation")).grid(row=4, column=8, columnspan=2)

    # ROW 5
    # TextDisplay
    # cmt = Entry(win, width=55, textvariable=TextInput, font=('Segoe UI Symbol', 16), bd=30, bg='powder blue',
    #             relief=RIDGE)
    # cmt.grid(row=5, column=0, columnspan=10)


def SwitchButtonsDisplay(Buttons):
    page = Buttons

    if page == '1st':
        # ROW 1
        # 2nd
        Button(win, width=6, height=1, bd=4, fg='orange', font=('Segoe UI Symbol', 16), text="1st", bg="powder blue",
               relief=RIDGE, command=lambda: SwitchButtonsDisplay("2nd")).grid(row=1, column=7)

        # ROW 2
        # Logarithm base 10
        Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="log¹º", bg='powder blue',
               relief=RIDGE, command=lambda: InputClick('log10(')).grid(row=2, column=5)

        # Logarithm base 2
        Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="log²", bg='powder blue',
               relief=RIDGE, command=lambda: InputClick("log2(")).grid(row=2, column=6)

        # EXP
        Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="exp", bg="powder blue",
               relief=RIDGE, command=lambda: InputClick('exp(')).grid(row=2, column=7)

        # SQUARE
        Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="√", bg='powder blue',
               relief=RIDGE, command=lambda: InputClick("sqrt(")).grid(row=2, column=8)

        # ROW 3
        # COS
        Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="cos", bg="powder blue",
               relief=RIDGE, command=lambda: InputClick('cos(')).grid(row=3, column=4)

        # SIN
        Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="sin", bg="powder blue",
               relief=RIDGE, command=lambda: InputClick('sin(')).grid(row=3, column=5)

        # TAN
        Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="tan", bg="powder blue",
               relief=RIDGE, command=lambda: InputClick('tan(')).grid(row=3, column=6)

        # COSH
        Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="cosh", bg="powder blue",
               relief=RIDGE, command=lambda: InputClick('cosh(')).grid(row=3, column=7)

        # SINH
        Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="sinh", bg="powder blue",
               relief=RIDGE, command=lambda: InputClick('sinh(')).grid(row=3, column=8)

        # TANH
        Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="tanh", bg="powder blue",
               relief=RIDGE, command=lambda: InputClick('tanh(')).grid(row=3, column=9)
        # ROW 4
        # Equation
        Button(win, width=13, height=1, bd=4, fg='blue', font=('Segoe UI Symbol', 16), text="Equation",
               bg="powder blue", relief=RIDGE, command=lambda: SwitchFunction("Equation")).grid(row=4, column=6,
                                                                                                columnspan=2)

    elif page == '2nd':
        # ROW 1
        # 1st
        Button(win, width=6, height=1, bd=4, fg='orange', font=('Segoe UI Symbol', 16), text="2nd", bg="powder blue",
               relief=RIDGE, command=lambda: SwitchButtonsDisplay("1st")).grid(row=1, column=7)
        # ROW 2
        # Logarithm 1P
        Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="log1p", bg='powder blue',
               relief=RIDGE, command=lambda: InputClick('log1p(')).grid(row=2, column=5)

        # e
        Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="e", bg="powder blue",
               relief=RIDGE, command=lambda: InputClick('e')).grid(row=2, column=6)

        # EXPM1
        Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="expm1", bg='powder blue',
               relief=RIDGE, command=lambda: InputClick("expm1(")).grid(row=2, column=7)

        # SQUARE
        Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="^", bg='powder blue',
               relief=RIDGE, command=lambda: InputClick("**")).grid(row=2, column=8)

        # ROW 3
        # aCOS
        Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="acos", bg="powder blue",
               relief=RIDGE, command=lambda: InputClick('acos(')).grid(row=3, column=4)

        # aSIN
        Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="asin", bg="powder blue",
               relief=RIDGE, command=lambda: InputClick('asin(')).grid(row=3, column=5)

        # aTAN
        Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="atan", bg="powder blue",
               relief=RIDGE, command=lambda: InputClick('atan(')).grid(row=3, column=6)

        # aCOSH
        Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="acosh", bg="powder blue",
               relief=RIDGE, command=lambda: InputClick('acosh(')).grid(row=3, column=7)

        # aSINH
        Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="asinh", bg="powder blue",
               relief=RIDGE, command=lambda: InputClick('asinh(')).grid(row=3, column=8)

        # aTANH
        Button(win, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="atanh", bg="powder blue",
               relief=RIDGE, command=lambda: InputClick('atanh(')).grid(row=3, column=9)
        # ROW 4
        # Function
        Button(win, width=13, height=1, bd=4, fg='blue', font=('Segoe UI Symbol', 16), text="Function",
               bg="powder blue", relief=RIDGE, command=lambda: SwitchFunction("Function")).grid(row=4, column=6,
                                                                                                columnspan=2)


SwitchFunction('Operation'), DisplayButtons(), SwitchButtonsDisplay('1st')

style = ttk.Style()
style.theme_use('alt')

win.mainloop()

print(cos(1))
