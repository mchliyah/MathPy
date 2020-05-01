from tkinter import *
from tkinter import ttk
from math import *
from operator import *

# version 0.2
# Make New Distribution For Buttons
# Insert Answer Of Equation, Function and Operation in Full Text Display
win = Tk()
win.title("Scientific Calculator v0.2")

f0 = Frame(win, width=200, height=200)
f0.grid(row=1, column=0)
f1 = Frame(win, width=200, height=200)
f1.grid(row=2, column=0)

TextInput = StringVar()
Answer = ''


def Clear():
    global operator, mode, clear, full, half, last
    last = []
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
    if mode == 'Operation':
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
    global operator, Answer, clear, a, b, c, v, w, full, half, tnt
    try:
        if mode == 'Operation':
            operator = str(TextDisplay.get()).lower()
            Answer = str(eval(operator))
            TextInput.set(f'{operator} = {Answer}')
            tnt.insert(INSERT, f'\n{operator} = {Answer}')
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
                    tnt.insert(INSERT, f'''\n
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
                        tnt.insert(INSERT, f'''\n 
   ∆=0 : X = -b / 2a

    X[1] = X[2] = ({neg(b)}) / (2 x {a})
    X[1] = X[2] = {(neg(b)) / (2 * a)}''')
                        print(f''' 
   ∆=0 : X = -b / 2a

    X[1] = X[2] = ({neg(b)}) / (2 x {a})
    X[1] = X[2] = {(neg(b)) / (2 * a)}''')
                    elif d >= 0:
                        tnt.insert(INSERT, f'''\n
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
                        tnt.insert(INSERT, f'''\n    = {nd}j²

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
                        tnt.insert(INSERT, f'''\nThe Equation : {b}X + ({c}) = 0

 The Equation Have One Solution For X :

  {b}X = 0
  X = 0''')
                        print(f'''The Equation : {b}X + ({c}) = 0

 The Equation Have One Solution For X :

  {b}X = 0
  X = 0''')
                    else:
                        tnt.insert(INSERT, f'''\nThe Equation : {b}X + ({c}) = 0 

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
                tnt.insert(INSERT, f'f(x) = {operator}')
                print(f'f(x) = {operator}')
                for x in range(v, w):
                    tnt.insert(INSERT, f'\nf({x}) = {eval(operator)}')
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
    global f0, f1, win, TextDisplay, cmt, tnt, last

    # ROW 0
    # TextDisplay
    TextDisplay = Spinbox(win, width=70, font=('Segoe UI Symbol', 16), textvariable=TextInput, bd=15,
                          bg='powder blue')
    TextDisplay.grid(row=0, column=0, columnspan=2)

    # ROW 1
    tnt = Text(win, width=50, height=14, font=('Segoe UI Symbol', 16), bd=6, bg='white')
    tnt.grid(row=1, column=1, rowspan=2)

    # f0 ROW 0
    # PI
    Button(f0, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="π", bg="powder blue",
           command=lambda: InputClick('pi')).grid(row=1, column=0)

    # left
    Button(f0, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="(", bg="powder blue",
           command=lambda: InputClick('(')).grid(row=1, column=1)

    # right
    Button(f0, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text=")", bg="powder blue",
           command=lambda: InputClick(')')).grid(row=1, column=2)

    # Clear
    Button(f0, width=3, height=1, bd=4, fg='red', font=('Marlett', 23), text="r", bg="powder blue",
           command=lambda: Clear()).grid(row=1, column=4)

    # Remove
    Button(f0, width=3, height=1, bd=4, fg='blue', font=('Wingdings', 21), text="Õ", bg="powder blue",
           command=lambda: Remove()).grid(row=1, column=5)
    # ROW 2
    # Logarithm base e
    Button(f0, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="logₑ", bg="powder blue",
           command=lambda: InputClick('log(')).grid(row=2, column=0)

    # COMPLEX
    Button(f0, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text='complex', bg='powder blue',
           command=lambda: InputClick("complex(")).grid(row=2, column=4)

    # COMPLEX j
    Button(f0, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="▯j", bg='powder blue',
           command=lambda: InputClick("j")).grid(row=2, column=5)
    # ROW 4
    # Answer
    Button(f0, width=6, height=1, bd=4, fg='green', font=('Segoe UI Symbol', 16), text='Answer', bg="powder blue",
           command=lambda: InputClick(Answer)).grid(row=4, column=0)

    # Operation
    Button(f0, width=13, height=1, bd=4, fg='blue', font=('Segoe UI Symbol', 16), text="Operation", bg="powder blue",
           command=lambda: SwitchFunction("Operation")).grid(row=4, column=3, columnspan=2)

    # x
    Button(f0, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text='x', bg="powder blue",
           command=lambda: InputClick('x')).grid(row=4, column=5)
    # f1 ROW 0
    # btn7
    Button(f1, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="7", bg='powder blue',
           command=lambda: InputClick(7)).grid(row=0, column=0)

    # btn8
    Button(f1, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="8", bg='powder blue',
           command=lambda: InputClick(8)).grid(row=0, column=1)

    # btn9
    Button(f1, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="9", bg='powder blue',
           command=lambda: InputClick(9)).grid(row=0, column=2)

    # Addition
    Button(f1, width=6, height=1, bd=4, fg='purple', font=('Segoe UI Symbol', 16), text="+", bg='powder blue',
           command=lambda: InputClick("+")).grid(row=0, column=3)
    # ROW 1
    # btn4
    Button(f1, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="4", bg='powder blue',
           command=lambda: InputClick(4)).grid(row=1, column=0)

    # btn5
    Button(f1, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="5", bg='powder blue',
           command=lambda: InputClick(5)).grid(row=1, column=1)

    # btn6
    Button(f1, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="6", bg='powder blue',
           command=lambda: InputClick(6)).grid(row=1, column=2)

    # subtraction
    Button(f1, width=6, height=1, bd=4, fg='purple', font=('Segoe UI Symbol', 16), text="-", bg='powder blue',
           command=lambda: InputClick("-")).grid(row=1, column=3)

    # Factorial
    Button(f1, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="!", bg='powder blue',
           command=lambda: InputClick("factorial(")).grid(row=1, column=4)
    # ROW 2
    # btn1
    Button(f1, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="1", bg='powder blue',
           command=lambda: InputClick(1)).grid(row=2, column=0)

    # btn2
    Button(f1, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="2", bg='powder blue',
           command=lambda: InputClick(2)).grid(row=2, column=1)

    # btn3
    Button(f1, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="3", bg='powder blue',
           command=lambda: InputClick(3)).grid(row=2, column=2)

    # Multiplication
    Button(f1, width=6, height=1, bd=4, fg='purple', font=('Segoe UI Symbol', 16), text="*", bg='powder blue',
           command=lambda: InputClick("*")).grid(row=2, column=3)

    # RACING SQUARE
    Button(f1, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="√", bg='powder blue',
           command=lambda: InputClick("sqrt(")).grid(row=2, column=4)

    # SQUARE
    Button(f1, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text='^', bg='powder blue',
           command=lambda: InputClick("**")).grid(row=2, column=5)
    # ROW 3
    # btn0
    Button(f1, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="0", bg='powder blue',
           command=lambda: InputClick(0)).grid(row=3, column=0)

    # point
    Button(f1, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text=".", bg="powder blue",
           command=lambda: InputClick(".")).grid(row=3, column=1)

    # btnEquals
    Button(f1, width=6, height=1, bd=4, fg='purple', font=('Segoe UI Symbol', 16), text="=", bg="powder blue",
           command=InputEquals).grid(row=3, column=2)

    # Division
    Button(f1, width=6, height=1, bd=4, fg='purple', font=('Segoe UI Symbol', 16), text="/", bg="powder blue",
           command=lambda: InputClick("/")).grid(row=3, column=3)

    # ROW 9
    # TextDisplay
    # cmt = Entry(f1, width=65, textvariable=TextInput, font=('Segoe UI Symbol', 16), bd=30, bg='powder blue',
    #             relief=RIDGE)
    # cmt.grid(row=9, column=0, columnspan=7)


def SwitchButtonsDisplay(Buttons):
    page = Buttons

    if page == '1st':
        # ROW 1
        # 2nd
        Button(f0, width=6, height=1, bd=4, fg='orange', font=('Segoe UI Symbol', 16), text="1st", bg="powder blue",
               command=lambda: SwitchButtonsDisplay("2nd")).grid(row=1, column=3)

        # ROW 2
        # Logarithm base 10
        Button(f0, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="log¹º", bg='powder blue',
               command=lambda: InputClick('log10(')).grid(row=2, column=1)

        # Logarithm base 2
        Button(f0, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="log²", bg='powder blue',
               command=lambda: InputClick("log2(")).grid(row=2, column=2)

        # EXP
        Button(f0, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="exp", bg="powder blue",
               command=lambda: InputClick('exp(')).grid(row=2, column=3)
        # ROW 3
        # COS
        Button(f0, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="cos", bg="powder blue",
               command=lambda: InputClick('cos(')).grid(row=3, column=0)

        # SIN
        Button(f0, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="sin", bg="powder blue",
               command=lambda: InputClick('sin(')).grid(row=3, column=1)

        # TAN
        Button(f0, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="tan", bg="powder blue",
               command=lambda: InputClick('tan(')).grid(row=3, column=2)

        # COSH
        Button(f0, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="cosh", bg="powder blue",
               command=lambda: InputClick('cosh(')).grid(row=3, column=3)

        # SINH
        Button(f0, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="sinh", bg="powder blue",
               command=lambda: InputClick('sinh(')).grid(row=3, column=4)

        # TANH
        Button(f0, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="tanh", bg="powder blue",
               command=lambda: InputClick('tanh(')).grid(row=3, column=5)
        # ROW 4
        # Equation
        Button(f0, width=13, height=1, bd=4, fg='blue', font=('Segoe UI Symbol', 16), text="Equation",
               bg="powder blue", command=lambda: SwitchFunction("Equation")).grid(row=4, column=1, columnspan=2)

    elif page == '2nd':
        # ROW 1
        # 1st
        Button(f0, width=6, height=1, bd=4, fg='orange', font=('Segoe UI Symbol', 16), text="2nd", bg="powder blue",
               command=lambda: SwitchButtonsDisplay("1st")).grid(row=1, column=3)
        # ROW 2
        # Logarithm 1P
        Button(f0, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="log1p", bg='powder blue',
               command=lambda: InputClick('log1p(')).grid(row=2, column=1)

        # e
        Button(f0, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="e", bg="powder blue",
               command=lambda: InputClick('e')).grid(row=2, column=2)

        # EXPM1
        Button(f0, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="expm1", bg='powder blue',
               command=lambda: InputClick("expm1(")).grid(row=2, column=3)

        # ROW 3
        # aCOS
        Button(f0, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="acos", bg="powder blue",
               command=lambda: InputClick('acos(')).grid(row=3, column=0)

        # aSIN
        Button(f0, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="asin", bg="powder blue",
               command=lambda: InputClick('asin(')).grid(row=3, column=1)

        # aTAN
        Button(f0, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="atan", bg="powder blue",
               command=lambda: InputClick('atan(')).grid(row=3, column=2)

        # aCOSH
        Button(f0, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="acosh", bg="powder blue",
               command=lambda: InputClick('acosh(')).grid(row=3, column=3)

        # aSINH
        Button(f0, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="asinh", bg="powder blue",
               command=lambda: InputClick('asinh(')).grid(row=3, column=4)

        # aTANH
        Button(f0, width=6, height=1, bd=4, fg='black', font=('Segoe UI Symbol', 16), text="atanh", bg="powder blue",
               command=lambda: InputClick('atanh(')).grid(row=3, column=5)
        # ROW 4
        # Function
        Button(f0, width=13, height=1, bd=4, fg='blue', font=('Segoe UI Symbol', 16), text="Function",
               bg="powder blue", command=lambda: SwitchFunction("Function")).grid(row=4, column=1,
                                                                                  columnspan=2)


SwitchFunction('Operation'), DisplayButtons(), SwitchButtonsDisplay('1st')

style = ttk.Style()
style.theme_use('alt')

win.mainloop()

print(cos(1))
