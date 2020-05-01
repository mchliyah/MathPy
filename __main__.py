import tkinter as tk
from math import log2, log10
from operator import *
from tkinter import *
from sympy import *
from sympy.abc import x
from sympy.solvers.solveset import solvify

# version 4.1.3
# Change Background of First Text Display
btn_prm = {'padx': 18,
           'pady': 2,
           'bd': 1,
           'fg': 'white',
           'bg': '#666666',
           'font': ('Segoe UI Symbol', 16),
           'width': 2,
           'height': 1,
           'relief': 'raised',
           'activebackground': '#666666',
           'activeforeground': "white"}
big_prm = {'padx': 8,
           'pady': 7,
           'bd': 1,
           'fg': 'white',
           'bg': 'slate gray',
           'font': ('Segoe UI Symbol', 15),
           'width': 7,
           'height': 1,
           'relief': 'raised',
           'activebackground': '#80000B',
           'activeforeground': "white"}
ent_prm = {'bd': 1,
           'fg': 'white',
           'bg': '#4d4d4d',
           'font': ('Segoe UI Symbol', 16),
           'relief': 'flat'}
π = 3.141592653589793


def Exit():
    return win.destroy()


def Sin(arg):
    return sin(arg * convert_constant)


def Cos(arg):
    return cos(arg * convert_constant)


def Tan(arg):
    return tan(arg * convert_constant)


def aSin(arg):
    return inverse_convert_constant * (asin(arg))


def aCos(arg):
    return inverse_convert_constant * (acos(arg))


def aTan(arg):
    return inverse_convert_constant * (atan(arg))


def Sinh(arg):
    return sinh(arg)


def Cosh(arg):
    return cosh(arg)


def Tanh(arg):
    return tanh(arg)


def aSinh(arg):
    return asinh(arg)


def aCosh(arg):
    return acosh(arg)


def aTanh(arg):
    return atanh(arg)


def Sq(arg):
    return sqrt(arg)


def Ln(arg):
    return log(arg)


def Log(arg):
    return log10(arg)


def Log2(arg):
    return log2(arg)


def Exp(arg):
    return exp(arg)


def Fact(arg):
    return factorial(arg)


class Calculator:
    def __init__(self, master):
        self.btn_u = []
        # expression that will be displayed on screen
        self.expression = ''
        # store expressions & order
        self.store_expression = []
        self.store_order = []
        # answer of operation
        self.answer = ''
        # store last answer of operation
        self.callback = []
        # float numbers of equation
        self.a = ''
        self.b = ''
        self.c = ''
        # equation solver parametre
        self.q = ''
        self.p = ''
        self.x = x
        self.R = S.Reals
        self.C = S.Complexes
        # int range numbers of function
        self.v = ''
        self.w = ''
        # used to switch between modes of Operation, Equation and Function
        self.mode = ''
        # default variable
        self.equal = False
        self.clear = False
        self.full = False
        self.half = False
        # string variable for text input
        self.TextVariable = StringVar()
        self.FastTextVariable = StringVar()

        # Master Display ROW 0==========================================================================================
        # First Text Display
        FirstTextDisplay = Entry(master, width=43, **ent_prm, textvariable=self.TextVariable)
        FirstTextDisplay.grid(row=0, column=0, columnspan=2)
        FirstTextDisplay.configure(font=('Segoe UI Symbol', 32), state='readonly', readonlybackground='#4d4d4d')
        FirstTextDisplay.bind('<Key>', self.KeyboardInput)
        # Second Text Display
        SecondTextDisplay = Entry(master, width=27, **ent_prm, textvariable=self.FastTextVariable)
        SecondTextDisplay.grid(row=1, column=1)
        SecondTextDisplay.configure(font=('Segoe UI Symbol', 30), justify='right', state='readonly',
                                    readonlybackground='slate gray')
        # Full Text Display
        self.FullTextDisplay = Text(master, width=54, height=14, **ent_prm)
        self.FullTextDisplay.grid(row=2, column=1, rowspan=2)
        # ROW 1 set frame showing top buttons
        self.top_frame = Frame(master, relief='flat', bg='slate gray')
        self.top_frame.grid(row=1, column=0)
        # ROW 2 set frame showing middle buttons
        self.middle_frame = Frame(master, relief='flat', bg='#666666')
        self.middle_frame.grid(row=2, column=0)
        # ROW 3 set frame showing bottom buttons
        bottom_frame = Frame(master, relief='flat', bg='#666666')
        bottom_frame.grid(row=3, column=0)
        # buttons that will be displayed on top frame ROW 0=============================================================
        big_txt = ['Operation', 'Function', "Equation", 'Solve']
        big_pad = ['Operation', 'Function', "LinEqua", 'Solve']
        self.btn_b = []
        i = 0
        for k in range(0, 8, 2):
            self.btn_b.append(Button(self.top_frame, **big_prm, text=big_txt[i]))
            self.btn_b[i].grid(row=0, column=k)
            self.btn_b[i]["command"] = lambda n=big_pad[i]: self.SwitchFunction(n)
            i += 1
        # buttons that will be displayed on middle frame ROW 0==========================================================
        txt = ['RAD', '1ST', 'ENG', 'ANS', 'r', 'Õ']
        self.btn_m = []
        i = 0
        for k in range(6):
            self.btn_m.append(Button(self.middle_frame, **btn_prm, text=txt[i]))
            self.btn_m[i].grid(row=0, column=k)
            i += 1
        # Answer Stored
        self.btn_m[3].configure(bg='SeaGreen3', activebackground='SeaGreen3',
                                command=lambda: self.Input(str(self.callback[-1])))
        # Clear
        self.btn_m[4].configure(width=1, bg='indian red', activebackground='indian red', font=('Marlett', 23),
                                command=lambda: self.Clear())
        # Remove
        self.btn_m[5].configure(width=1, bg='Royalblue2', activebackground='Royalblue2', font=('Wingdings', 21),
                                command=lambda: self.Remove())
        # ROW 2
        # ========================Logarithm=============================================================================
        Logarithm_pad = ['Ln(', 'Log(', "Log2(", 'Exp(', 'sqrt(', "oo"]
        Logarithm_txt = ['Ln', 'Log₍₁₀₎', "Log₍₂₎", 'Exp', '√n', "∞"]
        self.btn_d = []
        i = 0
        for k in range(6):
            self.btn_d.append(Button(self.middle_frame, **btn_prm, text=Logarithm_txt[i]))
            self.btn_d[i].grid(row=2, column=k)
            self.btn_d[i]["command"] = lambda n=Logarithm_pad[i]: self.Input(n)
            i += 1
        # buttons that will be displayed on bottom frame ROW 0==========================================================
        # ========================Numbers===============================================================================
        btn = ['π', 'E', "1j", '(', ')', self.x, "7", "8", "9", "+", '**3', 'e-', "4", "5", "6", "-", "**2", 'e', "1",
               "2", "3", "*", "**", "Sq(", '.', "0", "=", "/", "Fact(", '/100']

        btn_txt = ['π', 'E', "j", '(', ')', 'x', "7", "8", "9", "+", u'n\u00B3', '10ˉˣ', "4", "5", "6", "-",
                   u'n\u00B2', '10ˣ', "1", "2", "3", "*", "nˣ", '√n', '.', "0", "=", "/", "!n", "n%"]
        self.btn = []
        i = 0
        for j in range(5):
            for k in range(6):
                self.btn.append(Button(bottom_frame, **btn_prm, text=btn_txt[i]))
                self.btn[i].grid(row=j, column=k)
                self.btn[i].configure(bg="#4d4d4d", activebackground="#4d4d4d",
                                      command=lambda n=btn[i]: self.Input(n))
                i += 1
        for l in range(6, 9):
            self.btn[l].configure(bg='#292929', activebackground="#292929")
        for l in range(12, 15):
            self.btn[l].configure(bg='#292929', activebackground="#292929")
        for l in range(18, 21):
            self.btn[l].configure(bg='#292929', activebackground="#292929")
        self.btn[25].configure(bg='#292929', activebackground="#292929")
        # Equals #292929
        self.btn[26].configure(bg='#ff9950', activebackground='#ff9950', command=self.InputEquals)
        # run button switcher and display switcher mode=================================================================
        self.SwitchButtons('1st'), self.SwitchFunction('Operation'), self.SwitchDegRad('Radians')
        self.SwitchENG(int(16))
        # Switch Menu In Bare Display===================================================================================
        filemenu.add_command(label="Operation          O", command=lambda: self.SwitchFunction("Operation"))
        filemenu.add_command(label='Function            F', command=lambda: self.SwitchFunction('Function'))
        filemenu.add_command(label="Equation", command=lambda: self.SwitchFunction('LinEqua'))
        filemenu.add_command(label='Solve', command=lambda: self.SwitchFunction('Equation'))
        filemenu.add_separator()
        filemenu.add_command(label='Radians              R', command=lambda: self.SwitchDegRad('Radians'))
        filemenu.add_command(label='Degree               D', command=lambda: self.SwitchDegRad('Degree'))
        filemenu.add_separator()
        filemenu.add_command(label='1st Page             V', command=lambda: self.SwitchButtons("1st"))
        filemenu.add_command(label='2nd Page           B', command=lambda: self.SwitchButtons("2nd"))
        filemenu.add_separator()
        filemenu.add_command(label="Close         Alt+F4", command=Exit)

    def SwitchButtons(self, side):
        page = side
        # buttons to switch between buttons those will be displayed on middle frame
        if page == '1st':
            # ROW 0
            # 2nd
            self.btn_m[1].configure(text="1ST", command=lambda: self.SwitchButtons("2nd"), fg='orange',
                                    activeforeground='indian red')
            # ROW 1
            # ========================Trigonometry======================================================================
            Trigonometry_pad = ['Cos(', 'Sin(', "Tan(", 'Cosh(', 'Sinh(', "Tanh("]
            Trigonometry_txt = ['Cos', 'Sin', "Tan", 'Cosh', 'Sinh', "Tanh"]
            self.btn_u = []
            i = 0
            for k in range(6):
                self.btn_u.append(Button(self.middle_frame, **btn_prm, text=Trigonometry_txt[i]))
                self.btn_u[i].grid(row=1, column=k)
                self.btn_u[i]["command"] = lambda n=Trigonometry_pad[i]: self.Input(n)
                i += 1

        elif page == '2nd':
            # ROW 0
            # 1st
            self.btn_m[1].configure(text="2ND", command=lambda: self.SwitchButtons("1st"), fg='orange',
                                    activeforeground='indian red')
            # ROW 1
            # ========================Trigonometry======================================================================
            Trigonometry_pad = ['aCos(', 'aSin(', "aTan(", 'aCosh(', 'aSinh(', "aTanh("]
            Trigonometry_txt = ['aCos', 'aSin', "aTan", 'aCosh', 'aSinh', "aTanh"]
            self.btn_u = []
            i = 0
            for k in range(6):
                self.btn_u.append(Button(self.middle_frame, **btn_prm, text=Trigonometry_txt[i]))
                self.btn_u[i].grid(row=1, column=k)
                self.btn_u[i]["command"] = lambda n=Trigonometry_pad[i]: self.Input(n)
                i += 1

    def SwitchFunction(self, passmode):
        self.mode = passmode
        self.FullTextDisplay.delete(1.0, END)
        if self.mode == 'Operation':
            self.FullTextDisplay.insert(INSERT, 'Mode Operation :')
            self.FastTextVariable.set('')
            self.btn_b[0]['bg'] = 'indian red'
            for i in range(1, 4):
                self.btn_b[i]['bg'] = '#292929'
            self.btn[5]['state'] = ['disabled']
            self.btn[2].config(state=NORMAL)

        elif self.mode == 'Function':
            self.FullTextDisplay.insert(INSERT, 'Mode Function : f(x)')
            self.FastTextVariable.set(f'From : A --> To : B | f(x) = Function')
            self.btn_b[0]['bg'] = '#292929'
            self.btn_b[1]['bg'] = 'indian red'
            for i in range(2, 4):
                self.btn_b[i]['bg'] = '#292929'
            self.btn[5]['state'] = ['normal']
            self.btn[2]['state'] = ['disabled']

        elif self.mode == 'LinEqua':
            self.FullTextDisplay.insert(INSERT, 'Mode Equation : aX² + bX + c = 0')
            self.FastTextVariable.set('aX² + bX + c = 0')
            for i in range(2):
                self.btn_b[i]['bg'] = '#292929'
            self.btn_b[2]['bg'] = 'indian red'
            self.btn_b[3]['bg'] = '#292929'
            self.btn[5].config(state=DISABLED)
            self.btn[2].config(state=DISABLED)

        elif self.mode == 'Solve':
            self.FullTextDisplay.insert(INSERT, 'Mode Equation :')
            for i in range(3):
                self.btn_b[i]['bg'] = '#292929'
            self.btn_b[3]['bg'] = 'indian red'
            self.btn[5].config(state=NORMAL)
            self.btn[2].config(state=DISABLED)

        self.Clear()

    def SwitchDegRad(self, convert):
        switch = convert
        if switch == 'Degree':
            global convert_constant, inverse_convert_constant
            convert_constant = π / 180
            inverse_convert_constant = 180 / π
            # Degree -> Radians
            self.btn_m[0].configure(text='DEG', command=lambda: self.SwitchDegRad('Radians'), fg='orange',
                                    activeforeground='indian red')
            self.btn[0]['state'] = ['disabled']

        elif switch == 'Radians':
            convert_constant = 1
            inverse_convert_constant = 1
            # Radians -> Degree
            self.btn_m[0].configure(text='RAD', command=lambda: self.SwitchDegRad('Degree'), fg='orange',
                                    activeforeground='indian red')
            self.btn[0]['state'] = ['normal']

    def Clear(self):
        self.a = ''
        self.b = ''
        self.c = ''
        self.q = ''
        self.p = ''
        self.store_expression = []
        self.store_order = []
        self.expression = ''
        self.TextVariable.set('')
        self.FastTextVariable.set('')

        if self.mode == 'Function':
            self.TextVariable.set(f'From : ')
            self.FastTextVariable.set(f'From : A --> To : B | f(x) = Function')

        elif self.mode == 'LinEqua':
            self.TextVariable.set(f'a = ')
            self.FastTextVariable.set('aX² + bX + c = 0')

        self.equal = False
        self.clear = False
        self.full = None

    def Remove(self):
        if self.clear:
            self.Clear()

        try:
            k = self.store_order[-1]
            while k > 0:
                self.expression = self.expression[:-1]
                k -= 1

            self.store_expression.remove(self.store_expression[-1])
            self.store_order.remove(self.store_order[-1])

        except IndexError:
            self.FastTextVariable.set('IndexError')

        self.Click()

    def Input(self, keyword):
        if self.clear:
            self.Clear()

        self.store_expression.append(str(keyword))
        self.store_order.append(len(str(keyword)))
        self.expression += str(keyword)

        self.Click()

    def KeyboardInput(self, keyword):
        put = keyword.keysym.lower()
        try:
            if self.clear:
                if self.mode == 'Operation':
                    if keyword.keysym == 'Return' or put == 'equal':
                        self.InputEquals()

                    else:
                        self.Clear()

                else:
                    self.Clear()

            if not self.clear:
                if keyword.keysym == 'BackSpace':
                    self.Remove()

                elif keyword.keysym == 'Delete':
                    self.Clear()

                elif keyword.keysym == 'Return' or put == 'equal':
                    self.InputEquals()

                elif keyword.keysym == 'E':
                    self.Input('E')

                elif keyword.keysym == 'e':
                    self.Input('e')

                elif put == 'v':
                    self.SwitchButtons("1st")

                elif put == 'b':
                    self.SwitchButtons("2nd")

                elif put == 'b':
                    self.SwitchButtons("3rd")

                elif put == 'r':
                    self.SwitchDegRad('Radians')

                elif put == 'd':
                    self.SwitchDegRad('Degree')

                elif put == 'o':
                    self.SwitchFunction("Operation")

                elif put == 'f':
                    self.SwitchFunction("Function")

                elif put == 'slash':
                    self.Input('/')

                elif put == 'asterisk':
                    self.Input('*')

                elif put == 'minus':
                    self.Input('-')

                elif put == 'plus':
                    self.Input('+')

                elif put == 'asciicircum':
                    self.Input('^')

                elif put == 'period':
                    self.Input('.')

                elif put == 'parenleft':
                    self.Input('(')

                elif put == 'parenright':
                    self.Input(')')

                elif put == 'backslash':
                    self.Input('Sq(')

                elif put == 's':
                    self.Input('Sin')

                elif put == 'c':
                    self.Input('Cos')

                elif put == 't':
                    self.Input('Tan')

                elif put == 'l':
                    self.Input('Ln')

                elif put == 'i':
                    self.Input('oo')

                elif put == 'j':
                    self.Input('1j')

                elif put == 'exclam':
                    self.Input('factorial(')

                elif put == 'g':
                    self.Input('Log')

                elif put == 'h':
                    self.Input('h(')

                elif put == 'x' or put == 'p' or put == '0' or put == '1' or put == '2' or put == '3' \
                        or put == '4' or put == '5' or put == '6' or put == '7' or put == '8' or put == '9':
                    self.Input(put)

                else:
                    pass

        except IndexError:
            self.FastTextVariable.set('IndexError')

        self.Click()

    def SwitchENG(self, NBR):
        dot = NBR
        self.ENG = NBR
        if dot == int(16):
            self.btn_m[2].configure(text='ENG', command=lambda: self.SwitchENG(int(15)), fg='orange',
                                    activeforeground='indian red')
        elif dot == int(15):
            self.btn_m[2].configure(text='ENG₍₁₅₎', command=lambda: self.SwitchENG(int(12)), fg='orange',
                                    activeforeground='indian red')
        elif dot == int(12):
            self.btn_m[2].configure(text='ENG₍₁₂₎', command=lambda: self.SwitchENG(int(9)), fg='orange',
                                    activeforeground='indian red')
        elif dot == int(9):
            self.btn_m[2].configure(text='ENG₍₉₎', command=lambda: self.SwitchENG(int(6)), fg='orange',
                                    activeforeground='indian red')
        elif dot == int(6):
            self.btn_m[2].configure(text='ENG₍₆₎', command=lambda: self.SwitchENG(int(3)), fg='orange',
                                    activeforeground='indian red')
        elif dot == int(3):
            self.btn_m[2].configure(text='ENG₍₃₎', command=lambda: self.SwitchENG(int(2)), fg='orange',
                                    activeforeground='indian red')
        elif dot == int(2):
            self.btn_m[2].configure(text='ENG₍₂₎', command=lambda: self.SwitchENG(int(1)), fg='orange',
                                    activeforeground='indian red')
        elif dot == int(1):
            self.btn_m[2].configure(text='ENG₍₁₎', command=lambda: self.SwitchENG(int(16)), fg='orange',
                                    activeforeground='indian red')
        self.Click()

    def Click(self):
        try:
            if self.mode == 'Operation':
                self.FastTextVariable.set('')
                self.TextVariable.set(self.expression)
                if self.ENG == 16:
                    self.FastTextVariable.set(eval(self.expression))

                else:
                    self.FastTextVariable.set(N(eval(self.expression), self.ENG))
                    
            elif self.mode == "Function":
                if self.full is None:
                    self.TextVariable.set(f'From : {self.expression}')
                    self.FastTextVariable.set(f'From : {self.expression} --> To : B | f(x) = Function')

                elif not self.full:
                    self.TextVariable.set(f'To : {self.expression}')
                    self.FastTextVariable.set(f'From : {self.v} --> To : {self.expression} | f(x) = Function')

                elif self.full:
                    self.TextVariable.set(f'f(x) = {self.expression}')
                    self.FastTextVariable.set(f'From : {self.v} --> To : {int(self.w) - 1} | f(x) = {self.expression}')
                    
            elif self.mode == 'LinEqua':
                if self.full is None:
                    self.TextVariable.set(f'a = {self.expression}')
                    self.FastTextVariable.set(f'{self.expression}X² + bX + c = 0')

                elif not self.full:
                    self.TextVariable.set(f'b = {self.expression}')
                    self.FastTextVariable.set(f'{self.a}X² + ({self.expression})X + c = 0')

                elif self.full:
                    self.TextVariable.set(f'c = {self.expression}')
                    self.FastTextVariable.set(f'{self.a}X² + ({self.b})X + ({self.expression}) = 0')

            elif self.mode == 'Solve':
                if self.full is None:
                    self.TextVariable.set(self.expression)
                    self.FastTextVariable.set(self.expression)
                elif self.full:
                    self.TextVariable.set(f'{self.q} = {self.expression}')
                    self.FastTextVariable.set(f'{self.q} = {self.expression}')

        except ZeroDivisionError:
            self.FastTextVariable.set(oo)
        except ValueError:
            pass
        except SyntaxError:
            pass
        except NameError:
            pass
        except IndexError:
            pass
        except TypeError:
            pass

    def InputEquals(self):
        global z
        try:
            if self.mode == 'Operation':
                if not self.equal:
                    if self.ENG == 16:
                        self.answer = eval(self.expression)
                    else:
                        self.answer = N(eval(self.expression), self.ENG)
                    self.FastTextVariable.set('')
                    self.TextVariable.set(f'{self.expression} = {self.answer}')
                    self.FullTextDisplay.insert(INSERT, f'\n{self.expression} = {self.answer}')
                    self.clear = True
                    self.equal = True

                elif self.equal:
                    self.expression = ''
                    z = int(len(self.store_expression)) - 1
                    g = int(len(self.store_expression)) - 1
                    while True:
                        trs = str(self.store_expression[z])
                        if trs == '+' or trs == '-' or trs == '*' or trs == '/' or trs == '**' or trs == '^':
                            while z <= g:
                                self.expression += str(self.store_expression[z])
                                z += 1
                            self.expression = str(self.callback[-1]) + str(self.expression)
                            if self.ENG == 16:
                                self.answer = eval(self.expression)
                            else:
                                self.answer = N(eval(self.expression), self.ENG)
                            self.FastTextVariable.set(self.answer)
                            self.TextVariable.set(f'{self.expression} = {self.answer}')
                            self.FullTextDisplay.insert(INSERT, f'\n{self.expression} = {self.answer}')
                            break
                        z -= 1

            elif self.mode == 'Function':
                if self.full is None:
                    self.v = int(self.expression)
                    self.FullTextDisplay.insert(INSERT, f'\nfrom : {self.expression}')
                    self.expression = ""
                    self.TextVariable.set(f'To : ')
                    self.full = False

                elif not self.full:
                    self.w = int(self.expression) + 1
                    self.FullTextDisplay.insert(INSERT, f'\nTo : {self.expression}')
                    self.expression = ""
                    self.TextVariable.set(f'f(x) = ')
                    self.full = True

                elif self.full:
                    self.FullTextDisplay.insert(INSERT, f'\nf(x) = {sympify(self.expression)}')
                    for x in range(self.v, self.w):
                        self.FullTextDisplay.insert(INSERT, f'\nf({x}) = {N(eval(self.expression), self.ENG)}')

                    self.clear = True
                    self.full = None

            elif self.mode == 'LinEqua':
                if self.full is None:
                    self.a = N(eval(self.expression), 3)
                    self.expression = ""
                    self.TextVariable.set(f'b = ')
                    self.full = False

                elif not self.full:
                    self.b = N(eval(self.expression), 3)
                    self.expression = ""
                    self.TextVariable.set(f'c = ')
                    self.full = True

                elif self.full:
                    c = N(eval(self.expression), 3)
                    d = N((self.b ** 2) - 4 * self.a * c, 3)
                    nd = neg(d)
                    nb = neg(self.b)
                    self.TextVariable.set(f'a = {self.a} | b = {self.b} | c = {c}')
                    self.FastTextVariable.set(f'{self.a}X² + ({self.b})X + ({c}) = 0')
                    if self.a > 0 or self.a < 0:
                        self.FullTextDisplay.insert(INSERT, f'''\n
The Equation : {self.a}X² + ({self.b})X + ({c}) = 0

 The Equation Have Two Solutions For X :

  ∆ =  b² - 4ac

  ∆ = {self.b}² - (4 x ({self.a}) x ({c})) 
      = {N(self.b ** 2, 3)} - ({N(4 * self.a * c, 3)}) 
      = {d}''')
                        if d == 0:
                            self.FullTextDisplay.insert(INSERT, f'''\n 
∆=0 : X = -b / 2a

    X[1] = X[2] = ({N(neg(self.b), 3)}) / (2 x {self.a})
    X[1] = X[2] = {neg(self.b)} / ({N(2 * self.a, 3)})''')
                        elif d >= 0:
                            self.FullTextDisplay.insert(INSERT, f'''\n
∆>0 : X = (-b ± √∆) / 2a

 X[1] = ({nb} + √{d}) / (2 x {self.a})
       = ({nb} + √{d}) / ({N(2 * self.a, 3)})
       = {nb} / ({N(2 * self.a, 3)}) + √({d}) / ({N(2 * self.a, 3)})

 X[2] = ({nb} - √{d}) / (2 x {self.a})
       = ({nb} - √{d}) / ({2 * self.a})
       = {nb} / ({N(2 * self.a, 3)}) - √({d}) / ({N(2 * self.a, 3)})''')
                        elif d <= 0:
                            self.FullTextDisplay.insert(INSERT, f'''\n      = {nd}i²

∆<0 : X = (-b ± i√∆) / 2a

 X[1] = ({nb} + i√({nd})) / (2 x {self.a})
       = ({nb} + i√({nd})) / ({N(2 * self.a, 3)})
       = {nb} / ({N(2 * self.a, 3)}) + i√({nd}) / ({N(2 * self.a, 3)})

 X[2] = ({nb} - i√({nd})) / (2 x {self.a})
       = ({nb} - i√({nd})) / ({N(2 * self.a, 3)})
       = {nb} / ({N(2 * self.a, 3)}) - i√({nd}) / ({N(2 * self.a, 3)})

  z = a ± ib

   a = {nb} / ({N(2 * self.a, 3)})
   b = ± √{nd} / ({N(2 * self.a, 3)})''')
                    elif self.a == 0:
                        if self.b == 0 and c == 0:
                            self.TextVariable.set(f"Empty Solution {{∅}}")
                        elif self.b == 0:
                            self.TextVariable.set(f"Empty Solution {{∅}}")
                        elif c == 0:
                            self.FastTextVariable.set(f'{self.a}X² + ({self.b})X + ({c}) = 0')
                            self.FullTextDisplay.insert(INSERT, f'''\nThe Equation : {self.b}X + ({c}) = 0

 The Equation Have One Solution For X :

  {self.b}X = 0
  X = 0''')
                        else:
                            self.FullTextDisplay.insert(INSERT, f'''\nThe Equation : {self.b}X + ({c}) = 0 

 The Equation Have One Solution For X :  

  {self.b}X = {neg(c)}    
  X = {neg(c)} / {self.b}
  X = {N(eval(neg(c) / self.b), 3)}''')

                    self.clear = True
                    self.full = None

            elif self.mode == 'Solve':
                if self.full is None:
                    self.q = str(eval(self.expression))
                    self.expression = ""
                    self.TextVariable.set(f'{self.q} = ')
                    self.full = True

                elif self.full:
                    self.p = str(eval(self.expression))
                    self.TextVariable.set(f'\n{self.q} = {self.p}')
                    self.FullTextDisplay.insert(INSERT, f'\n{self.q} = {self.p}')
                    sol = solvify(Eq(sympify(self.q), sympify(self.p)), self.x, self.C)
                    if sol is None:
                        sol = solvify(Eq(sympify(self.q), sympify(self.p)), self.x, self.R)
                    self.FastTextVariable.set(sol)
                    for l in range(len(sol)):
                        self.FullTextDisplay.insert(INSERT, f'\nX[{int(l) + 1}] = {sol[l]}')

                    self.clear = True
                    self.full = None

        except ZeroDivisionError:
            self.FastTextVariable.set(oo)
        except ValueError:
            self.FastTextVariable.set('ValueError')
        except NotImplementedError:
            self.FastTextVariable.set('Cannot Solve This Equation')
        except SyntaxError:
            self.FastTextVariable.set('SyntaxError')
            try:
                if self.mode == 'Operation' and self.equal:
                    self.expression = str(self.callback[-1])
                    if self.ENG == 16:
                        self.answer = eval(self.expression)
                    else:
                        self.answer = N(eval(self.expression), self.ENG)
                    self.FastTextVariable.set(self.answer)
                    self.TextVariable.set(f'{self.expression} = {self.answer}')
                    self.FullTextDisplay.insert(INSERT, f'\n{self.expression} = {self.answer}')
            except IndexError:
                self.FastTextVariable.set('SyntaxError')
        except NameError:
            self.FastTextVariable.set('NameError')
        except TypeError:
            self.FastTextVariable.set('TypeError')
        except OverflowError:
            self.FastTextVariable.set('OverflowMathRangeError')
        except IndexError:
            self.FastTextVariable.set('IndexError')
            try:
                if self.mode == 'Operation' and self.equal:
                    self.expression = str(self.callback[-1])
                    if self.ENG == 16:
                        self.answer = eval(self.expression)
                    else:
                        self.answer = N(eval(self.expression), self.ENG)
                    self.FastTextVariable.set(self.answer)
                    self.TextVariable.set(f'{self.expression} = {self.answer}')
                    self.FullTextDisplay.insert(INSERT, f'\n{self.expression} = {self.answer}')
            except IndexError:
                self.FastTextVariable.set('IndexError')

        self.callback.append(str(self.answer))


if __name__ == "__main__":
    win = Tk()
    menubare = Menu(win)
    filemenu = Menu(menubare, tearoff=0)
    menubare.add_cascade(label="File", menu=filemenu)
    # run calculator
    Calculator(win)
    # Window configuration
    win.configure(menu=menubare, bg='#666666')
    # win.configure(menu=menubare, bg='#4d4d4d')
    win.resizable(False, False)
    win.title("PyMathon v4.1.3")
    win.mainloop()
