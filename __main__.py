from tkinter import *
from math import *
from operator import *

# version 1.0
# Add New More Buttons
# New Style And New Version of class Writing
btn_prm = {
    'padx': 16,
    'pady': 1,
    'bd': 4,
    'fg': 'white',
    'bg': '#666666',
    'font': ('Segoe UI Symbol', 16),
    'width': 2,
    'height': 1,
    'relief': 'flat',
    'activebackground': "#666666"
}
nbr_prm = {
    'padx': 16,
    'pady': 1,
    'bd': 4,
    'fg': 'white',
    'bg': '#4d4d4d',
    'font': ('Segoe UI Symbol', 16),
    'width': 2,
    'height': 1,
    'relief': 'flat',
    'activebackground': "#4d4d4d"
}
big_prm = {
    'padx': 16,
    'pady': 1,
    'bd': 4,
    'fg': 'white',
    'bg': '#666666',
    'font': ('Segoe UI Symbol', 16),
    'width': 5,
    'height': 1,
    'relief': 'flat',
    'activebackground': "#666666"
}
ent_prm = {
    'bd': 4,
    'fg': 'white',
    'bg': '#666666',
    'font': ('Segoe UI Symbol', 18),
    'relief': 'flat'
}


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

        # ROW 0 TextDisplay
        self.TextDisplay = Entry(master, width=41, **ent_prm, textvariable=self.TextInput)
        self.TextDisplay.grid(row=0, column=0, columnspan=2)
        self.TextDisplay.configure(bg='slate gray', font=('Segoe UI Symbol', 36))
        # FullTextDisplay
        self.FullTextDisplay = Text(master, width=50, height=15, **ent_prm)
        self.FullTextDisplay.grid(row=1, column=1, rowspan=3)
        self.FullTextDisplay.configure(bg='#4d4d4d')
        # ROW 1 set frame showing top buttons
        self.frame = Frame(master, width=200, height=50, relief='flat', bg='dark slate gray')
        self.frame.grid(row=1, column=0)
        # ROW 2 set frame showing top buttons
        self.top_frame = Frame(master, width=200, height=150, relief='flat', bg='#666666')
        self.top_frame.grid(row=2, column=0)
        # ROW 3 set frame showing bottom buttons
        self.bottom_frame = Frame(master, width=200, height=200, relief='flat', bg='#666666')
        self.bottom_frame.grid(row=3, column=0)
        # buttons that will be displayed on top frame ROW 0
        # Operation
        self.Operation = Button(self.frame, **big_prm, text="Operation",
                                command=lambda: self.SwitchFunction("Operation"))
        self.Operation.grid(row=0, column=0, columnspan=2)
        self.Operation.configure(bg='dark slate gray', activebackground='dark slate gray')
        # Equation
        self.Equation = Button(self.frame, **big_prm, text="Equation", command=lambda: self.SwitchFunction("Equation"))
        self.Equation.grid(row=0, column=2, columnspan=2)
        self.Equation.configure(bg='dark slate gray', activebackground='dark slate gray')
        # Function
        self.Function = Button(self.frame, **big_prm, text="Function", command=lambda: self.SwitchFunction("Function"))
        self.Function.grid(row=0, column=4, columnspan=2)
        self.Function.configure(bg='dark slate gray', activebackground='dark slate gray')

        # buttons that will be displayed on top frame ROW 0
        # COMPLEX
        Button(self.top_frame, **btn_prm, text='complx', command=lambda: self.Input("complex(")).grid(row=1, column=0)
        # left
        Button(self.top_frame, **btn_prm, text="(", command=lambda: self.Input('(')).grid(row=1, column=1)
        # right
        Button(self.top_frame, **btn_prm, text=")", command=lambda: self.Input(')')).grid(row=1, column=2)
        # bntClear
        self.bntClear = Button(self.top_frame, **btn_prm, text="r", command=lambda: self.Clear())
        self.bntClear.grid(row=1, column=4)
        self.bntClear.configure(width=1, bg='indian red', activebackground='indian red', font=('Marlett', 23))
        # btnRemove
        self.btnRemove = Button(self.top_frame, **btn_prm, text="Õ", command=lambda: self.Remove())
        self.btnRemove.grid(row=1, column=5)
        self.btnRemove.configure(width=1, bg='Royalblue2', activebackground='Royalblue2', font=('Wingdings', 21))
        # ROW 3
        # Logarithm base e
        Button(self.top_frame, **btn_prm, text="logₑ", command=lambda: self.Input('log(')).grid(row=3, column=0)
        # Logarithm base 10
        Button(self.top_frame, **btn_prm, text="log¹º", command=lambda: self.Input('log10(')).grid(row=3, column=1)
        # Logarithm base 2
        Button(self.top_frame, **btn_prm, text="log²", command=lambda: self.Input("log2(")).grid(row=3, column=2)
        # Logarithm 1P
        Button(self.top_frame, **btn_prm, text="log1p", command=lambda: self.Input('log1p(')).grid(row=3, column=3)
        # EXP
        Button(self.top_frame, **btn_prm, text="exp", command=lambda: self.Input('exp(')).grid(row=3, column=4)
        # EXPM1
        Button(self.top_frame, **btn_prm, text="expm1", command=lambda: self.Input("expm1(")).grid(row=3, column=5)
        # buttons that will be displayed on bottom frame ROW 0
        # seven
        Button(self.bottom_frame, **nbr_prm, text="7", command=lambda: self.Input(7)).grid(row=0, column=0)
        # eight
        Button(self.bottom_frame, **nbr_prm, text="8", command=lambda: self.Input(8)).grid(row=0, column=1)
        # nine
        Button(self.bottom_frame, **nbr_prm, text="9", command=lambda: self.Input(9)).grid(row=0, column=2)
        # Addition
        Button(self.bottom_frame, **nbr_prm, text="+", command=lambda: self.Input("+")).grid(row=0, column=3)
        # Answer
        Button(self.bottom_frame, **nbr_prm, text='Answer', command=lambda: self.Input(self.ans)).grid(row=0, column=4)
        # x
        self.x = Button(self.bottom_frame, **nbr_prm, text='x', command=lambda: self.Input('x'))
        self.x.grid(row=0, column=5)
        # ROW 1
        # four
        Button(self.bottom_frame, **nbr_prm, text="4", command=lambda: self.Input(4)).grid(row=1, column=0)
        # five
        Button(self.bottom_frame, **nbr_prm, text="5", command=lambda: self.Input(5)).grid(row=1, column=1)
        # six
        Button(self.bottom_frame, **nbr_prm, text="6", command=lambda: self.Input(6)).grid(row=1, column=2)
        # subtraction
        Button(self.bottom_frame, **nbr_prm, text="-", command=lambda: self.Input("-")).grid(row=1, column=3)
        # SQUARE
        Button(self.bottom_frame, **nbr_prm, text='^', command=lambda: self.Input("**")).grid(row=1, column=4)
        # COMPLEX j
        Button(self.bottom_frame, **nbr_prm, text="j", command=lambda: self.Input("1j")).grid(row=1, column=5)
        # ROW 2
        # one
        Button(self.bottom_frame, **nbr_prm, text="1", command=lambda: self.Input(1)).grid(row=2, column=0)
        # two
        Button(self.bottom_frame, **nbr_prm, text="2", command=lambda: self.Input(2)).grid(row=2, column=1)
        # three
        Button(self.bottom_frame, **nbr_prm, text="3", command=lambda: self.Input(3)).grid(row=2, column=2)
        # Multiplication
        Button(self.bottom_frame, **nbr_prm, text="*", command=lambda: self.Input("*")).grid(row=2, column=3)
        # RACING SQUARE
        Button(self.bottom_frame, **nbr_prm, text="√", command=lambda: self.Input("sqrt(")).grid(row=2, column=4)
        # e
        Button(self.bottom_frame, **nbr_prm, text="e", command=lambda: self.Input('e')).grid(row=2, column=5)
        # ROW 3
        # btn0
        Button(self.bottom_frame, **nbr_prm, text="0", command=lambda: self.Input(0)).grid(row=3, column=0)
        # point
        Button(self.bottom_frame, **nbr_prm, text=".", command=lambda: self.Input(".")).grid(row=3, column=1)
        # btnEquals
        self.btnEquals = Button(self.bottom_frame, **nbr_prm, text="=", command=self.InputEquals)
        self.btnEquals.grid(row=3, column=2)
        self.btnEquals.configure(bg='#ff9980', activebackground='#ff9980')
        # Division
        Button(self.bottom_frame, **nbr_prm, text="/", command=lambda: self.Input("/")).grid(row=3, column=3)
        # Factorial
        Button(self.bottom_frame, **nbr_prm, text="!", command=lambda: self.Input("factorial(")).grid(row=3, column=4)
        # PI
        Button(self.bottom_frame, **nbr_prm, text="π", command=lambda: self.Input('pi')).grid(row=3, column=5)
        # run button switcher and display switcher mode
        self.SwitchButtons('1st'), self.SwitchFunction('Operation')

    def SwitchFunction(self, passmode):
        self.mode = passmode
        self.FullTextDisplay.delete(1.0, END)
        if self.mode == 'Operation':
            self.FullTextDisplay.insert(INSERT, 'Mode Operation :')
            self.x.config(state=DISABLED)
        elif self.mode == 'Equation':
            self.FullTextDisplay.insert(INSERT, 'Mode Equation : aX² + bX + c = 0')
            self.x.config(state=DISABLED)
        elif self.mode == 'Function':
            self.FullTextDisplay.insert(INSERT, 'Mode Function : f(x)')
            self.x.config(state=NORMAL)
        self.Clear()

    def SwitchButtons(self, side):
        page = side
        # buttons that will be Switched on top frame
        if page == '1st':
            # ROW 1
            # 2nd
            self.secend = Button(self.top_frame, **btn_prm, text="1st", command=lambda: self.SwitchButtons("2nd"))
            self.secend.grid(row=1, column=3)
            self.secend.configure(foreground='orange', activeforeground='indian red')
            # ROW 2
            # COS
            Button(self.top_frame, **btn_prm, text="cos", command=lambda: self.Input('cos(')).grid(row=2, column=0)
            # SIN
            Button(self.top_frame, **btn_prm, text="sin", command=lambda: self.Input('sin(')).grid(row=2, column=1)
            # TAN
            Button(self.top_frame, **btn_prm, text="tan", command=lambda: self.Input('tan(')).grid(row=2, column=2)
            # COSH
            Button(self.top_frame, **btn_prm, text="cosh", command=lambda: self.Input('cosh(')).grid(row=2, column=3)
            # SINH
            Button(self.top_frame, **btn_prm, text="sinh", command=lambda: self.Input('sinh(')).grid(row=2, column=4)
            # TANH
            Button(self.top_frame, **btn_prm, text="tanh", command=lambda: self.Input('tanh(')).grid(row=2, column=5)

        elif page == '2nd':
            # ROW 1
            # 1st
            self.first = Button(self.top_frame, **btn_prm, text="2nd", command=lambda: self.SwitchButtons("1st"))
            self.first.grid(row=1, column=3)
            self.first.configure(foreground='orange', activeforeground='indian red')
            # ROW 2
            # aCOS
            Button(self.top_frame, **btn_prm, text="acos", command=lambda: self.Input('acos(')).grid(row=2, column=0)
            # aSIN
            Button(self.top_frame, **btn_prm, text="asin", command=lambda: self.Input('asin(')).grid(row=2, column=1)
            # aTAN
            Button(self.top_frame, **btn_prm, text="atan", command=lambda: self.Input('atan(')).grid(row=2, column=2)
            # aCOSH
            Button(self.top_frame, **btn_prm, text="acosh", command=lambda: self.Input('acosh(')).grid(row=2, column=3)
            # aSINH
            Button(self.top_frame, **btn_prm, text="asinh", command=lambda: self.Input('asinh(')).grid(row=2, column=4)
            # aTANH
            Button(self.top_frame, **btn_prm, text="atanh", command=lambda: self.Input('atanh(')).grid(row=2, column=5)

    def Clear(self):
        self.store = []
        self.expression = ''
        self.TextInput.set('')

        if self.mode == 'Operation':
            self.Operation['bg'] = 'indian red'
            self.Equation['bg'] = 'dark slate gray'
            self.Function['bg'] = 'dark slate gray'

        elif self.mode == 'Equation':
            self.TextInput.set(f'a = ')
            self.Equation['bg'] = 'indian red'
            self.Function['bg'] = 'dark slate gray'
            self.Operation['bg'] = 'dark slate gray'

        elif self.mode == 'Function':
            self.TextInput.set(f'From : ')
            self.Function['bg'] = 'indian red'
            self.Equation['bg'] = 'dark slate gray'
            self.Operation['bg'] = 'dark slate gray'

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
        if self.mode == 'Operation':
            self.TextInput.set(self.expression)

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

    def InputEquals(self):
        try:
            if self.mode == 'Operation':
                self.expression = str(self.TextDisplay.get()).lower()
                self.ans = str(eval(self.expression))
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
                        self.expression = ""
                        self.TextInput.set(f'To : ')
                        self.half = True

                    elif self.half:
                        self.w = int(self.expression) + 1
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
win.title("Scientific Calculator v1.0")
# win.configure(bg='#666666')
win.configure(bg='#4d4d4d')
win.resizable(False, False)
# run calculator
Calculator(win)
win.mainloop()
