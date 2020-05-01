from math import *
from operator import *
from tkinter import *
from tkinter import ttk, _cnfmerge as cnfmerge

# version 3.2.0
# Hide Some Global Call , Make Lot Of Self Call, Last Time I Make Bad Decision
btn_prm = {'padx': 16,
           'pady': 1,
           'bd': 4,
           'fg': 'white',
           'bg': '#666666',
           'font': ('Segoe UI Symbol', 16),
           'width': 2,
           'height': 1,
           'relief': 'flat',
           'activebackground': '#666666',
           'activeforeground': "white"}
big_prm = {'padx': 16,
           'pady': 1,
           'bd': 4,
           'fg': 'white',
           'bg': 'slate gray',
           'font': ('Segoe UI Symbol', 16),
           'width': 5,
           'height': 1,
           'relief': 'raised',
           'activebackground': 'dim gray',
           'activeforeground': "white"}
ent_prm = {'bd': 4,
           'fg': 'white',
           'bg': 'gray94',
           'font': ('Segoe UI Symbol', 16),
           'relief': 'flat'}


class EntryBox(Entry):
    def __init__(self, master=None, cnf=None, **kw):
        if cnf is None:
            cnf = {}
        kw = cnfmerge((kw, cnf))
        kw['justify'] = kw.get('justify', 'left')
        kw['state'] = 'readonly'
        super(EntryBox, self).__init__(master=master, **kw)


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


class Calculator:
    def __init__(self, master):
        # expression that will be displayed on screen
        self.expression = ''
        # store expressions by order
        self.store_expression = []
        # answer of operation
        self.answer = ''
        # store last answer of operation
        self.callback = ['']
        # float numbers of equation
        self.a = ''
        self.b = ''
        self.c = ''
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
        FirstTextDisplay = EntryBox(master, width=44, **ent_prm, textvariable=self.TextVariable)
        FirstTextDisplay.grid(row=0, column=0, columnspan=2)
        FirstTextDisplay.configure(fg='black', font=('Segoe UI Symbol', 32))
        FirstTextDisplay.bind('<Key>', self.KeyboardInput)
        # Second Text Display
        SecondTextDisplay = Entry(master, width=33, **ent_prm, textvariable=self.FastTextVariable)
        SecondTextDisplay.grid(row=1, column=1)
        SecondTextDisplay.configure(bg='slate gray', font=('Segoe UI Symbol', 25), justify='right')
        # Full Text Display
        self.FullTextDisplay = Text(master, width=54, height=13, **ent_prm)
        self.FullTextDisplay.grid(row=2, column=1, rowspan=2)
        self.FullTextDisplay.configure(bg='#4d4d4d')
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
        # Operation
        self.Operation = Button(self.top_frame, **big_prm, text="Operation",
                                command=lambda: self.SwitchFunction("Operation"))
        self.Operation.grid(row=0, column=2, columnspan=2)
        # Equation
        self.Equation = Button(self.top_frame, **big_prm, text="Equation",
                               command=lambda: self.SwitchFunction("Equation"))
        self.Equation.grid(row=0, column=4, columnspan=2)
        # Function
        self.Function = Button(self.top_frame, **big_prm, text="Function",
                               command=lambda: self.SwitchFunction("Function"))
        self.Function.grid(row=0, column=6, columnspan=2)

        # buttons that will be displayed on middle frame ROW 0==========================================================
        pad = ['(', ')', "", '', '', ""]
        txt = ['(', ')', "", 'Answer', 'r', "Õ"]
        btn = []
        i = 0
        for k in range(6):
            btn.append(Button(self.middle_frame, **btn_prm, text=txt[i]))
            btn[i].grid(row=1, column=k)
            btn[i]["command"] = lambda n=pad[i]: self.Input(n)
            i += 1
        # Answer Stored
        btn[3].configure(bg='SeaGreen3', activebackground='SeaGreen3',
                         command=lambda: self.Input(str(self.callback[-1])))
        # Clear
        btn[4].configure(width=1, bg='indian red', activebackground='indian red', font=('Marlett', 23),
                         command=lambda: self.Clear())
        # Remove
        btn[5].configure(width=1, bg='Royalblue2', activebackground='Royalblue2', font=('Wingdings', 21),
                         command=lambda: self.Remove())
        # ROW 3
        # ========================Logarithm=============================================================================
        Logarithm_pad = ['log(', 'log10(', "log2(", 'log1p(', 'exp(', "expm1("]
        Logarithm_txt = ['logₑ', 'log¹º', "log²", 'log1p', 'exp', "expm1"]
        btn = []
        i = 0
        for k in range(6):
            btn.append(Button(self.middle_frame, **btn_prm, text=Logarithm_txt[i]))
            btn[i].grid(row=3, column=k)
            btn[i]["command"] = lambda n=Logarithm_pad[i]: self.Input(n)
            i += 1
        # buttons that will be displayed on bottom frame ROW 0==========================================================
        # ========================Numbers===============================================================================
        btn = ["7", "8", "9", "+", '**2', 'x', "4", "5", "6", "-", "**", "1j", "1", "2", "3", "*",
               "sqrt(", 'e', '0', ".", "=", "/", "factorial(", 'pi']
        btn_txt = ["7", "8", "9", "+", u'n\u00B2', 'x', "4", "5", "6", "-", "nˣ", "j", "1", "2", "3",
                   "*", "√n", 'e', '0', ".", "=", "/", "!n", 'π']
        self.btn = []
        i = 0
        for j in range(4):
            for k in range(6):
                self.btn.append(Button(bottom_frame, **btn_prm, text=btn_txt[i]))
                self.btn[i].grid(row=j, column=k)
                self.btn[i].configure(bg="#4d4d4d", activebackground="#4d4d4d",
                                      command=lambda n=btn[i]: self.Input(n))
                i += 1
        # Equals
        self.btn[20].configure(bg='#ff9950', activebackground='#ff9950', command=self.InputEquals)

        # run button switcher and display switcher mode=================================================================
        self.SwitchButtons('1st'), self.SwitchFunction('Operation'), self.SwitchDegRad('Radians')
        # Switch Menu In Bare Display=================================================================================
        filemenu.add_command(label="Operation", command=lambda: self.SwitchFunction("Operation"))
        filemenu.add_command(label='Equation', command=lambda: self.SwitchFunction('Equation'))
        filemenu.add_command(label='Function', command=lambda: self.SwitchFunction('Function'))
        filemenu.add_separator()
        filemenu.add_command(label='Radians', command=lambda: self.SwitchDegRad('Radians'))
        filemenu.add_command(label='Degree', command=lambda: self.SwitchDegRad('Degree'))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=Exit)

    def SwitchButtons(self, side):
        page = side
        # buttons to switch between buttons those will be displayed on middle frame
        if page == '1st':
            # ROW 1
            # 2nd
            second = Button(self.middle_frame, **btn_prm, text="1st", command=lambda: self.SwitchButtons("2nd"))
            second.grid(row=1, column=2)
            second.configure(fg='orange', activeforeground='indian red')
            # ROW 2
            # ========================Trigonometry======================================================================
            Trigonometry_pad = ['Cos(', 'Sin(', "Tan(", 'Cosh(', 'Sinh(', "Tanh("]
            Trigonometry_txt = ['Cos', 'Sin', "Tan", 'Cosh', 'Sinh', "Tanh"]
            btn = []
            i = 0
            for k in range(6):
                btn.append(Button(self.middle_frame, **btn_prm, text=Trigonometry_txt[i]))
                btn[i].grid(row=2, column=k)
                btn[i]["command"] = lambda n=Trigonometry_pad[i]: self.Input(n)
                i += 1

        elif page == '2nd':
            # ROW 1
            # 1st
            first = Button(self.middle_frame, **btn_prm, text="2nd", command=lambda: self.SwitchButtons("1st"))
            first.grid(row=1, column=2)
            first.configure(fg='orange', activeforeground='indian red')
            # ROW 2
            # ========================Trigonometry======================================================================
            Trigonometry_pad = ['aCos(', 'aSin(', "aTan(", 'aCosh(', 'aSinh(', "aTanh("]
            Trigonometry_txt = ['aCos', 'aSin', "aTan", 'aCosh', 'aSinh', "aTanh"]
            btn = []
            i = 0
            for k in range(6):
                btn.append(Button(self.middle_frame, **btn_prm, text=Trigonometry_txt[i]))
                btn[i].grid(row=2, column=k)
                btn[i]["command"] = lambda n=Trigonometry_pad[i]: self.Input(n)
                i += 1

    def SwitchFunction(self, passmode):
        self.mode = passmode
        self.FullTextDisplay.delete(1.0, END)
        if self.mode == 'Operation':
            self.FullTextDisplay.insert(INSERT, 'Mode Operation :')
            self.FastTextVariable.set('')
            self.Operation['bg'] = 'indian red'
            self.Equation['bg'] = 'slate gray'
            self.Function['bg'] = 'slate gray'
            self.btn[5]['state'] = ['disabled']
            self.btn[11].config(state=NORMAL)

        elif self.mode == 'Equation':
            self.FullTextDisplay.insert(INSERT, 'Mode Equation : aX² + bX + c = 0')
            self.FastTextVariable.set('aX² + bX + c = 0')
            self.Equation['bg'] = 'indian red'
            self.Function['bg'] = 'slate gray'
            self.Operation['bg'] = 'slate gray'
            self.btn[5].config(state=DISABLED)
            self.btn[11].config(state=DISABLED)

        elif self.mode == 'Function':
            self.FullTextDisplay.insert(INSERT, 'Mode Function : f(x)')
            self.FastTextVariable.set(f'From : A --> To : B | f(x) = Function')
            self.Function['bg'] = 'indian red'
            self.Equation['bg'] = 'slate gray'
            self.Operation['bg'] = 'slate gray'
            self.btn[5]['state'] = ['normal']
            self.btn[11]['state'] = ['disabled']

        self.Clear()

    def SwitchDegRad(self, convert):
        switch = convert
        if switch == 'Degree':
            global convert_constant, inverse_convert_constant
            convert_constant = pi / 180
            inverse_convert_constant = 180 / pi
            # Degree -> Radians
            Deg_Rad = Button(self.top_frame, **big_prm, text='Degree',
                             command=lambda: self.SwitchDegRad('Radians'))
            Deg_Rad.grid(row=0, column=0, columnspan=2)
            Deg_Rad.configure(fg='orange', activeforeground='indian red')

        elif switch == 'Radians':
            convert_constant = 1
            inverse_convert_constant = 1
            # Radians -> Degree
            Rad_Deg = Button(self.top_frame, **big_prm, text='Radians',
                             command=lambda: self.SwitchDegRad('Degree'))
            Rad_Deg.grid(row=0, column=0, columnspan=2)
            Rad_Deg.configure(fg='orange', activeforeground='indian red')

    def Clear(self):
        self.store_expression = []
        self.expression = ''
        self.TextVariable.set('')
        self.FastTextVariable.set('')

        if self.mode == 'Equation':
            self.TextVariable.set(f'a = ')
            self.FastTextVariable.set('aX² + bX + c = 0')

        elif self.mode == 'Function':
            self.TextVariable.set(f'From : ')
            self.FastTextVariable.set(f'From : A --> To : B | f(x) = Function')

        self.equal = False
        self.clear = False
        self.full = False
        self.half = False

    def Remove(self):
        if self.clear:
            self.Clear()

        try:
            self.expression = str(self.expression).replace(self.store_expression[-1], '')
            self.store_expression.remove(self.store_expression[-1])

        except IndexError:
            self.FastTextVariable.set('IndexError')

        self.Click()

    def Input(self, keyword):
        if self.clear:
            self.Clear()

        self.store_expression.append((str(keyword)))
        self.expression += str(keyword)

        self.Click()

    def KeyboardInput(self, keyword):
        put = keyword.keysym.lower()
        if self.clear:
            self.Clear()
        try:
            if keyword.keysym == 'BackSpace':
                self.Remove()

            elif keyword.keysym == 'Delete':
                self.Clear()

            elif put == 'slash':
                self.Input('/')

            elif put == 'asterisk':
                self.Input('*')

            elif put == 'minus':
                self.Input('-')

            elif put == 'plus':
                self.Input('+')

            elif put == 'period':
                self.Input('.')

            elif put == 'parenleft':
                self.Input('(')

            elif put == 'parenright':
                self.Input(')')

            elif put == 'backslash':
                self.Input('sqrt(')

            elif put == 's':
                self.Input('Sin')

            elif put == 'c':
                self.Input('Cos')

            elif put == 't':
                self.Input('Tan')

            elif put == 'l':
                self.Input('log')

            elif put == 'j':
                self.Input('1j')

            elif put == 'f' or put == 'exclam':
                self.Input('factorial(')

            elif put == 'm':
                self.Input('m1(')

            elif put == 'h':
                self.Input('h(')

            elif put == 'x' or put == 'e' or put == 'p' or put == '0' or put == '1' or put == '2' or put == '3' \
                    or put == '4' or put == '5' or put == '6' or put == '7' or put == '8' or put == '9':
                self.Input(put)

            elif keyword.keysym == 'Return' or put == 'equal':
                return self.InputEquals()

            else:
                pass

        except IndexError:
            self.FastTextVariable.set('IndexError')

        self.Click()

    def Click(self):
        try:
            if self.mode == 'Operation':
                self.FastTextVariable.set('')
                self.TextVariable.set(self.expression)
                self.FastTextVariable.set(eval(self.expression))

            elif self.mode == 'Equation':
                if not self.full and not self.half:
                    self.TextVariable.set(f'a = {self.expression}')
                    self.FastTextVariable.set(f'{self.expression}X² + bX + c = 0')

                elif not self.full and self.half:
                    self.TextVariable.set(f'b = {self.expression}')
                    self.FastTextVariable.set(f'{self.a}X² + ({self.expression})X + c = 0')

                elif self.full:
                    self.TextVariable.set(f'c = {self.expression}')
                    self.FastTextVariable.set(f'{self.a}X² + ({self.b})X + ({self.expression}) = 0')

            elif self.mode == "Function":
                if not self.full and not self.half:
                    self.TextVariable.set(f'From : {self.expression}')
                    self.FastTextVariable.set(f'From : {self.expression} --> To : B | f(x) = Function')

                elif not self.full and self.half:
                    self.TextVariable.set(f'To : {self.expression}')
                    self.FastTextVariable.set(f'From : {self.v} --> To : {self.expression} | f(x) = Function')

                elif self.full:
                    self.TextVariable.set(f'f(x) = {self.expression}')
                    self.FastTextVariable.set(f'From : {self.v} --> To : {int(self.w) - 1} | f(x) = {self.expression}')

        except ZeroDivisionError:
            pass
        except ValueError:
            pass
        except SyntaxError:
            pass
        except NameError:
            pass
        except TypeError:
            pass

    def InputEquals(self):
        global z
        try:
            if self.mode == 'Operation':

                if not self.equal:
                    self.answer = eval(self.expression)
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
                        if trs == '+' or trs == '-' or trs == '*' or trs == '/' or trs == '**':
                            while z <= g:
                                self.expression += str(self.store_expression[z])
                                z += 1
                            self.expression = str(self.callback[-1]) + str(self.expression)
                            self.answer = eval(self.expression)
                            self.FastTextVariable.set(self.answer)
                            self.TextVariable.set(f'{self.expression} = {self.answer}')
                            self.FullTextDisplay.insert(INSERT, f'\n{self.expression} = {self.answer}')
                            break
                        z -= 1

            elif self.mode == 'Equation':
                if not self.full:
                    if not self.half:
                        self.a = float(eval(self.expression))
                        self.expression = ""
                        self.TextVariable.set(f'b = ')
                        self.half = True

                    elif self.half:
                        self.b = float(eval(self.expression))
                        self.expression = ""
                        self.TextVariable.set(f'c = ')
                        self.full = True

                elif self.full:
                    c = float(eval(self.expression))
                    d = float((self.b ** 2) - 4 * self.a * c)
                    nd = neg(d)
                    nb = neg(self.b)
                    cx = complex
                    self.TextVariable.set(f'a = {self.a} | b = {self.b} | c = {c}')
                    self.FastTextVariable.set(f'{self.a}X² + ({self.b})X + ({c}) = 0')
                    if self.a > 0 or self.a < 0:
                        self.FullTextDisplay.insert(INSERT, f'''\n
The Equation : {self.a}X² + ({self.b})X + ({c}) = 0

 The Equation Have Two Solutions For X :

  ∆ =  b² - 4ac

  ∆ = {self.b}² - (4 x ({self.a}) x ({c})) 
      = {self.b ** 2} - ({4 * self.a * c}) 
      = {d}''')
                        if d == 0:
                            self.FullTextDisplay.insert(INSERT, f'''\n 
∆=0 : X = -b / 2a

    X[1] = X[2] = ({neg(self.b)}) / (2 x {self.a})
    X[1] = X[2] = {(neg(self.b)) / (2 * self.a)}''')
                        elif d >= 0:
                            self.FullTextDisplay.insert(INSERT, f'''\n
∆>0 : X = (-b ± √∆) / 2a

 X[1] = ({nb} + √{d}) / (2 x {self.a})
       = ({nb} + {sqrt(d)}) / ({2 * self.a})
       = {(nb + sqrt(d)) / (2 * self.a)}

 X[2] = ({nb} - √{d}) / (2 x {self.a})
       = ({nb} - {sqrt(d)}) / ({2 * self.a})
       = {(nb - sqrt(d)) / (2 * self.a)}''')
                        elif d <= 0:
                            self.FullTextDisplay.insert(INSERT, f'''\n      = {nd}j²

∆<0 : X = (-b ± j√∆) / 2a

 X[1] = ({nb} + √({nd})j) / (2 x {self.a})
       = {cx(nb + sqrt(nd) * 1j)} / ({2 * self.a})
       = {cx((nb + sqrt(nd) * 1j) / (2 * self.a))}

 X[2] = ({nb} - √({nd})j) / (2 x {self.a})
       = {cx(nb - sqrt(nd) * 1j)} / ({2 * self.a})
       = {cx((nb - sqrt(nd) * 1j) / (2 * self.a))}

  z = a ± bj

   a = {nb / (2 * self.a)}
   b = {sqrt(nd) / (2 * self.a)}''')
                    elif self.a == 0:
                        if self.b == 0 and c == 0:
                            self.TextVariable.set(f"Empty Solution {{Ꞩ}}")
                        elif self.b == 0:
                            self.TextVariable.set(f"Empty Solution {{Ꞩ}}")
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
  X = {neg(c) / self.b}''')

                    self.clear = True
                    self.full = False
                    self.half = False

            elif self.mode == 'Function':
                if not self.full:
                    if not self.half:
                        self.v = int(self.expression)
                        self.FullTextDisplay.insert(INSERT, f'\nfrom : {self.expression}')
                        self.expression = ""
                        self.TextVariable.set(f'To : ')
                        self.half = True

                    elif self.half:
                        self.w = int(self.expression) + 1
                        self.FullTextDisplay.insert(INSERT, f'\nTo : {self.expression}')
                        self.expression = ""
                        self.TextVariable.set(f'f(x) = ')
                        self.full = True

                elif self.full:
                    self.FullTextDisplay.insert(INSERT, f'\nf(x) = {self.expression}')
                    for x in range(self.v, self.w):
                        self.FullTextDisplay.insert(INSERT, f'\nf({x}) = {eval(self.expression)}')

                    self.clear = True
                    self.full = False
                    self.half = False

        except ZeroDivisionError:
            self.FastTextVariable.set('ZeroDivisionError')
        except ValueError:
            self.FastTextVariable.set('ValueError')
        except SyntaxError:
            self.FastTextVariable.set('SyntaxError')
        except NameError:
            self.FastTextVariable.set('NameError')
        except TypeError:
            self.FastTextVariable.set('TypeError')
        except IndexError:
            self.FastTextVariable.set('IndexError')
            try:
                if self.mode == 'Operation' and self.equal:
                    self.expression = str(self.callback[-1])
                    self.answer = eval(self.expression)
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
    style = ttk.Style()
    style.theme_use('alt')
    # Window configuration
    win.configure(menu=menubare, bg='#666666')
    # win.configure(menu=menubare, bg='#4d4d4d')
    win.resizable(False, False)
    win.title("Scientific Calculator v3.2.0")
    win.mainloop()
