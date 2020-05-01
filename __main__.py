from tkinter import *
from math import *
from operator import *

# version 2.1.1
# fix Size Between First Text Display And Second Text Display And Full Text Display
btn_prm = {'padx': 16,
           'pady': 1,
           'bd': 4,
           'fg': 'white',
           'bg': '#666666',
           'font': ('Segoe UI Symbol', 16),
           'width': 2,
           'height': 1,
           'relief': 'flat',
           'activebackground': "#666666"}
big_prm = {'padx': 16,
           'pady': 1,
           'bd': 4,
           'fg': 'white',
           'bg': '#666666',
           'font': ('Segoe UI Symbol', 16),
           'width': 5,
           'height': 1,
           'relief': 'flat',
           'activebackground': "#666666"}
ent_prm = {'bd': 4,
           'fg': 'white',
           'bg': '#4d4d4d',
           'font': ('Segoe UI Symbol', 18),
           'relief': 'flat'}


class Calculator:
    def __init__(self, master):
        # expression that will be displayed on screen
        self.expression = ''
        # store expressions by order
        self.store = []
        # store last answer of operation
        self.ans = ''
        # float numbers of equation
        self.a = ''
        self.b = ''
        self.c = ''
        # int range numbers of function
        self.v = ''
        self.w = ''
        # used to switch between buttons those will be displayed on screen
        self.first = ''
        self.secend = ''
        # used to switch between modes of Operation, Equation and Function
        self.mode = ''
        # default variable
        self.clear = False
        self.full = False
        self.half = False
        # create string for text input
        self.TextInput = StringVar()
        self.FastText = StringVar()

        # Master Display ROW 0==========================================================================================
        # First Text Display
        self.FirstTextDisplay = Entry(master, width=44, **ent_prm, textvariable=self.TextInput)
        self.FirstTextDisplay.grid(row=0, column=0, columnspan=2)
        self.FirstTextDisplay.configure(bg='slate gray', font=('Segoe UI Symbol', 35))
        # Second Text Display
        self.SecondTextDisplay = Entry(master, width=36, **ent_prm, textvariable=self.FastText)
        self.SecondTextDisplay.grid(row=1, column=1)
        self.SecondTextDisplay.configure(bg='slate gray', font=('Segoe UI Symbol', 26), justify='right')
        # Full Text Display
        self.FullTextDisplay = Text(master, width=52, height=13, **ent_prm)
        self.FullTextDisplay.grid(row=2, column=1, rowspan=2)
        # ROW 1 set frame showing top buttons
        top_frame = Frame(master, relief='flat', bg='dark slate gray')
        top_frame.grid(row=1, column=0)
        # ROW 2 set frame showing middle buttons
        self.middle_frame = Frame(master, relief='flat', bg='#666666')
        self.middle_frame.grid(row=2, column=0)
        # ROW 3 set frame showing bottom buttons
        bottom_frame = Frame(master, relief='flat', bg='#666666')
        bottom_frame.grid(row=3, column=0)
        # buttons that will be displayed on top frame ROW 0=============================================================
        # Operation
        self.Operation = Button(top_frame, **big_prm, text="Operation",
                                command=lambda: self.SwitchFunction("Operation"))
        self.Operation.grid(row=0, column=0, columnspan=2)
        self.Operation.configure(bg='dark slate gray', activebackground='dark slate gray')
        # Equation
        self.Equation = Button(top_frame, **big_prm, text="Equation", command=lambda: self.SwitchFunction("Equation"))
        self.Equation.grid(row=0, column=2, columnspan=2)
        self.Equation.configure(bg='dark slate gray', activebackground='dark slate gray')
        # Function
        self.Function = Button(top_frame, **big_prm, text="Function", command=lambda: self.SwitchFunction("Function"))
        self.Function.grid(row=0, column=4, columnspan=2)
        self.Function.configure(bg='dark slate gray', activebackground='dark slate gray')
        # COMPLEX
        self.Complex = Button(top_frame, **big_prm, text='Complex', command=lambda: self.SwitchFunction("Complex"))
        self.Complex.grid(row=0, column=6, columnspan=2)
        self.Complex.configure(bg='dark slate gray', activebackground='dark slate gray')

        # buttons that will be displayed on middle frame ROW 0==========================================================
        # left
        Button(self.middle_frame, **btn_prm, text="(", command=lambda: self.Input('(')).grid(row=1, column=1)
        # right
        Button(self.middle_frame, **btn_prm, text=")", command=lambda: self.Input(')')).grid(row=1, column=2)
        # bntClear
        btnClear = Button(self.middle_frame, **btn_prm, text="r", command=lambda: self.Clear())
        btnClear.grid(row=1, column=4)
        btnClear.configure(width=1, bg='indian red', activebackground='indian red', font=('Marlett', 23))
        # btnRemove
        btnRemove = Button(self.middle_frame, **btn_prm, text="Õ", command=lambda: self.Remove())
        btnRemove.grid(row=1, column=5)
        btnRemove.configure(width=1, bg='Royalblue2', activebackground='Royalblue2', font=('Wingdings', 21))
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
        number_pad = ["7", "8", "9", "+", self.ans, 'x', "4", "5", "6", "-", "**", "1j", "1", "2", "3", "*", "sqrt(",
                      'e', '0', ".", "=", "/", "factorial(", 'pi']
        number_txt = ["7", "8", "9", "+", 'Answer', 'x', "4", "5", "6", "-", "^", "j", "1", "2", "3", "*", "√",
                      'e', '0', ".", "=", "/", "!", 'π']
        self.btn = []
        i = 0
        for j in range(4):
            for k in range(6):
                self.btn.append(Button(bottom_frame, **btn_prm, text=number_txt[i]))
                self.btn[i].grid(row=j, column=k)
                self.btn[i].configure(bg="#4d4d4d", activebackground="#4d4d4d",
                                      command=lambda n=number_pad[i]: self.Input(n))
                i += 1
        # Equals
        self.btn[20].configure(bg='#ff9980', activebackground='#ff9980', command=self.InputEquals)
        # run button switcher and display switcher mode=================================================================
        self.SwitchButtons('1st'), self.SwitchFunction('Operation')

    def SwitchButtons(self, side):
        page = side
        # buttons that will be Switched on middle frame
        if page == '1st':
            # ROW 1
            # 2nd
            secend = Button(self.middle_frame, **btn_prm, text="1st", command=lambda: self.SwitchButtons("2nd"))
            secend.grid(row=1, column=3)
            secend.configure(foreground='orange', activeforeground='indian red')
            # ROW 2
            # ========================Trigonometry======================================================================
            Trigonometry_pad = ['cos(', 'sin(', "tan(", 'cosh(', 'sinh(', "tanh("]
            Trigonometry_txt = ['cos', 'sin', "tan", 'cosh', 'sinh', "tanh"]
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
            first.grid(row=1, column=3)
            first.configure(foreground='orange', activeforeground='indian red')
            # ROW 2
            # ========================Trigonometry======================================================================
            Trigonometry_pad = ['acos(', 'asin(', "atan(", 'acosh(', 'asinh(', "atanh("]
            Trigonometry_txt = ['acos', 'asin', "atan", 'acosh', 'asinh', "atanh"]
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
            self.Operation['bg'] = 'indian red'
            self.Equation['bg'] = 'dark slate gray'
            self.Function['bg'] = 'dark slate gray'
            self.Complex['bg'] = 'dark slate gray'
            self.btn[5]['state'] = ['disabled']
            self.btn[11]['state'] = ['disabled']

        elif self.mode == 'Equation':
            self.FullTextDisplay.insert(INSERT, 'Mode Equation : aX² + bX + c = 0')
            self.Equation['bg'] = 'indian red'
            self.Function['bg'] = 'dark slate gray'
            self.Operation['bg'] = 'dark slate gray'
            self.Complex['bg'] = 'dark slate gray'
            self.btn[5].config(state=DISABLED)
            self.btn[11].config(state=DISABLED)

        elif self.mode == 'Function':
            self.FullTextDisplay.insert(INSERT, 'Mode Function : f(x)')
            self.Function['bg'] = 'indian red'
            self.Equation['bg'] = 'dark slate gray'
            self.Operation['bg'] = 'dark slate gray'
            self.Complex['bg'] = 'dark slate gray'
            self.btn[5]['state'] = ['normal']
            self.btn[11]['state'] = ['disabled']

        elif self.mode == 'Complex':
            self.FullTextDisplay.insert(INSERT, 'Mode Complex :')
            self.Function['bg'] = 'dark slate gray'
            self.Equation['bg'] = 'dark slate gray'
            self.Operation['bg'] = 'dark slate gray'
            self.Complex['bg'] = 'indian red'
            self.btn[5].config(state=DISABLED)
            self.btn[11].config(state=NORMAL)

        self.Clear()

    def Clear(self):
        self.store = []
        self.expression = ''
        self.TextInput.set('')

        if self.mode == 'Equation':
            self.TextInput.set(f'a = ')

        elif self.mode == 'Function':
            self.TextInput.set(f'From : ')

        self.clear = False
        self.full = False
        self.half = False

    def Remove(self):
        if self.clear:
            self.Clear()

        try:
            self.expression = str(self.expression).replace(self.store[-1], '')
            self.store.remove(self.store[-1])

        except IndexError:
            self.FullTextDisplay.insert(INSERT, f'\nIndexError')

        self.Click()

    def Input(self, keyword):
        if self.clear:
            self.Clear()

        self.store.append((str(keyword)))
        self.expression += str(keyword)

        self.Click()

    def Click(self):
        try:
            if self.mode == 'Operation':
                self.TextInput.set(self.expression)
                self.ans = eval(self.expression)
                self.FastText.set(self.ans)

            elif self.mode == 'Equation':
                if not self.full and not self.half:
                    self.TextInput.set(f'a = {self.expression}')

                elif not self.full and self.half:
                    self.TextInput.set(f'b = {self.expression}')

                elif self.full:
                    self.TextInput.set(f'c = {self.expression}')

            elif self.mode == "Function":
                if not self.full and not self.half:
                    self.TextInput.set(f'From : {self.expression}')

                elif not self.full and self.half:
                    self.TextInput.set(f'To : {self.expression}')

                elif self.full:
                    self.TextInput.set(f'f(x) = {self.expression}')

            elif self.mode == 'Complex':
                self.TextInput.set(self.expression)
                self.ans = eval(self.expression)
                self.FastText.set(self.ans)

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
        try:
            if self.mode == 'Operation':
                # self.expression = str(self.FirstTextDisplay.get()).lower()
                self.ans = eval(self.expression)
                self.FastText.set('')
                self.TextInput.set(f'{self.expression} = {self.ans}')
                self.FullTextDisplay.insert(INSERT, f'\n{self.expression} = {self.ans}')
                self.clear = True

            elif self.mode == 'Equation':
                if not self.full:
                    if not self.half:
                        self.a = float(eval(self.expression))
                        self.expression = ""
                        self.TextInput.set(f'b = ')
                        self.half = True

                    elif self.half:
                        self.b = float(eval(self.expression))
                        self.expression = ""
                        self.TextInput.set(f'c = ')
                        self.full = True

                elif self.full:
                    c = float(eval(self.expression))
                    d = float((self.b ** 2) - 4 * self.a * c)
                    nd = neg(d)
                    nb = neg(self.b)
                    cx = complex
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
                            self.FullTextDisplay.insert(INSERT, f'''\n          = {nd}j²

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
                            self.FullTextDisplay.insert(INSERT, "\nEmpty Solution {Ꞩ}.")
                        elif self.b == 0:
                            self.FullTextDisplay.insert(INSERT, "\nEmpty Solution {Ꞩ}.")
                        elif c == 0:
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
                        self.TextInput.set(f'To : ')
                        self.half = True

                    elif self.half:
                        self.w = int(self.expression) + 1
                        self.FullTextDisplay.insert(INSERT, f'\nTo : {self.expression}')
                        self.expression = ""
                        self.TextInput.set(f'f(x) = ')
                        self.full = True

                elif self.full:
                    self.FullTextDisplay.insert(INSERT, f'\nf(x) = {self.expression}')
                    for x in range(self.v, self.w):
                        self.FullTextDisplay.insert(INSERT, f'\nf({x}) = {eval(self.expression)}')

                    self.clear = True
                    self.full = False
                    self.half = False

            elif self.mode == 'Complex':
                # self.expression = str(self.FirstTextDisplay.get()).lower()
                self.ans = eval(self.expression)
                self.FastText.set('')
                self.TextInput.set(f'{self.expression} = {self.ans}')
                self.FullTextDisplay.insert(INSERT, f'\n{self.expression} = {self.ans}')
                self.clear = True

        except ZeroDivisionError:
            self.FullTextDisplay.insert(INSERT, f'\nZeroDivisionError')
        except ValueError:
            self.FullTextDisplay.insert(INSERT, f'\nValueError')
        except SyntaxError:
            self.FullTextDisplay.insert(INSERT, f'\nSyntaxError')
        except NameError:
            self.FullTextDisplay.insert(INSERT, f'\nNameError')
        except TypeError:
            self.FullTextDisplay.insert(INSERT, f'\nTypeError')


win = Tk()
win.title("Scientific Calculator v2.1.1")
# win.configure(bg='#666666')
win.configure(bg='#4d4d4d')
win.resizable(False, False)
# run calculator
Calculator(win)
win.mainloop()
