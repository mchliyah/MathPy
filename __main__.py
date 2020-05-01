from __init__ import HoverButton, ScrolledListbox
from math import log2, log10
from random import randint
from operator import *
from tkinter import *
from sympy import *
from sympy.abc import x, y, z
from sympy.plotting import plot, plot_parametric, plot3d, plot3d_parametric_line, plot3d_parametric_surface, PlotGrid
from sympy.solvers.solveset import solvify

# version 5.1.3
# add possibility to show two plot in one page
# optimize set solution of system equation
# make anchor at last of full text display
# optimize bind : * equal now are perfect * input keys after equal click are perfect * add more keys
# more optimize for system equation : now support two equations and three equations at time
btn_prm = {'padx': 18,
           'pady': 2,
           'bd': 1,
           'background': '#666666',
           'fg': 'white',
           'bg': '#666666',
           'font': ('Segoe UI Symbol', 16),
           'width': 2,
           'height': 1,
           'relief': 'raised',
           'activeback': '#555555',
           'activebackground': '#444444',
           'activeforeground': "white"}
btnb_prm = {'padx': 18,
            'pady': 2,
            'bd': 1,
            'background': '#4d4d4d',
            'fg': 'white',
            'bg': '#4d4d4d',
            'font': ('Segoe UI Symbol', 16),
            'width': 2,
            'height': 1,
            'relief': 'raised',
            'activeback': '#3d3d3d',
            'activebackground': '#2d2d2d',
            'activeforeground': "white"}
big2_prm = {'padx': 14,
            'pady': 13,
            'bd': 1,
            'background': '#212121',
            'fg': 'white',
            'bg': '#212121',
            'font': ('Segoe UI Symbol', 12),
            'width': 5,
            'height': 1,
            'relief': 'raised',
            'activeback': '#49000A',
            'activebackground': '#80000B',
            'activeforeground': "white"}
ent_prm = {'fg': 'white',
           'bg': '#4d4d4d',
           'font': ('Segoe UI Symbol', 16),
           'relief': 'flat'}
π = pi
convert_constant = 1
inverse_convert_constant = 1


class Calculator(Canvas):
    def __init__(self, master):
        self.nb = ['₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉', '⏨', '₍₎']

        self.ENG = 16
        self.btn_u = []
        self.btn_a = []
        # expression that will be displayed on screen
        self.expression = ''
        # store expressions & order
        self.store_expression = []
        self.store_order = []
        # answer of operation
        self.answer = ''
        # store answers of operation
        self.callback = ['']
        # float numbers of equation
        self.a = ''
        self.b = ''
        self.c = ''
        # equation solver parameter
        self.sb = ['x', 'y', 'z']
        self.x = x
        self.y = y
        self.z = z
        self.R = S.Reals
        self.C = S.Complexes
        self.q = ''
        self.p = ''
        self.j = ''
        self.k = ''
        self.m = ''
        self.n = ''
        self.lslv = ''
        self.xexp = ''
        self.yexp = ''
        self.zexp = ''
        # int range numbers of function
        self.v = ''
        self.w = ''
        # functions
        self.fctx = ''
        self.fctx1 = ''
        self.fctx2 = ''
        self.fctxy = ''
        self.fctxy1 = ''
        self.fctxy2 = ''
        self.P3d = ''
        self.PA = ''
        self.P3dps = ''
        # store functions
        self.callback_function = []
        # used to switch between modes of Operation, Equation and Function
        self.mode = ''
        # default variable
        self.switched = False
        self.equal = False
        self.clear = False
        self.full = False
        self.half = False
        self.exist = None
        # string variable for text input
        self.TextVariable = StringVar()
        self.FastTextVariable = StringVar()
        # Master Display ===============================================================================================
        Canvas.__init__(self, master)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.bind_all('<Key>', self.KeyboardInput)
        self.grid_bbox('all')
        self.configure(scrollregion=self.bbox("all"))

        # Self Display ROW 0============================================================================================
        # First Text Display
        FirstTextDisplay = Entry(self, width=43, **ent_prm, textvariable=self.TextVariable, state='readonly')
        FirstTextDisplay.grid(row=0, column=0, columnspan=2, sticky=NSEW)
        FirstTextDisplay.configure(font=('Segoe UI Symbol', 32), readonlybackground='#4d4d4d')
        # Second Text Display
        SecondTextDisplay = Entry(self, width=27, **ent_prm, textvariable=self.FastTextVariable, state='readonly')
        SecondTextDisplay.grid(row=1, column=1, sticky=NSEW)
        SecondTextDisplay.configure(font=('Segoe UI Symbol', 30), justify='right', readonlybackground='slate gray')
        # Full Text Display
        self.FullTextDisplay = ScrolledListbox(self, width=52, height=13, **ent_prm)
        self.FullTextDisplay.grid(row=2, column=1, rowspan=2, sticky=NSEW)
        self.FullTextDisplay.rowconfigure(0, weight=1)
        self.FullTextDisplay.columnconfigure(0, weight=1)
        self.FullTextDisplay.focus_set()
        # ROW 1 set frame showing top buttons
        self.top_frame = Frame(self, relief='flat', bg='#212121')
        self.top_frame.grid(row=1, column=0, sticky=NSEW)
        self.top_frame.rowconfigure(0, weight=1)
        self.top_frame.columnconfigure(0, weight=1)
        self.top_frame.columnconfigure(1, weight=1)
        self.top_frame.columnconfigure(2, weight=1)
        self.top_frame.columnconfigure(3, weight=1)
        self.top_frame.columnconfigure(4, weight=1)
        # ROW 2 set frame showing middle buttons
        self.middle_frame = Frame(self, relief='flat', bg='#666666')
        self.middle_frame.grid(row=2, column=0, sticky=NSEW)
        self.middle_frame.rowconfigure(0, weight=1)
        self.middle_frame.rowconfigure(1, weight=1)
        self.middle_frame.rowconfigure(2, weight=1)
        self.middle_frame.columnconfigure(0, weight=1)
        self.middle_frame.columnconfigure(1, weight=1)
        self.middle_frame.columnconfigure(2, weight=1)
        self.middle_frame.columnconfigure(3, weight=1)
        self.middle_frame.columnconfigure(4, weight=1)
        self.middle_frame.columnconfigure(5, weight=1)
        # ROW 3 set frame showing bottom buttons
        self.bottom_frame = Frame(self, relief='flat', bg='#4d4d4d')
        self.bottom_frame.grid(row=3, column=0, sticky=NSEW)
        self.bottom_frame.rowconfigure(0, weight=1)
        self.bottom_frame.rowconfigure(1, weight=1)
        self.bottom_frame.rowconfigure(2, weight=1)
        self.bottom_frame.rowconfigure(3, weight=1)
        self.bottom_frame.rowconfigure(4, weight=1)
        self.bottom_frame.columnconfigure(0, weight=1)
        self.bottom_frame.columnconfigure(1, weight=1)
        self.bottom_frame.columnconfigure(2, weight=1)
        self.bottom_frame.columnconfigure(3, weight=1)
        self.bottom_frame.columnconfigure(4, weight=1)
        self.bottom_frame.columnconfigure(5, weight=1)
        # buttons that will be fake displayed on top frame ROW 0========================================================
        big_txt = ['', '', '', '', '']
        self.btn_b = []
        for k in range(5):
            self.btn_b.append(HoverButton(self.top_frame, **big2_prm, text=big_txt[k]))
        # buttons that will be displayed on middle frame ROW 0==========================================================
        txt = ['RAD', '1ST', 'ENG', 'ANS', 'r', 'Õ']
        self.btn_m = []
        for i in range(6):
            self.btn_m.append(HoverButton(self.middle_frame, **btn_prm, text=txt[i]))
            self.btn_m[i].grid(row=0, column=i, sticky=NSEW, padx=1, pady=1)
        # Answer Stored
        self.btn_m[3].configure(bg='#20B645', activebackground='#00751E',
                                command=lambda: self.Input(str(self.callback[-1])))
        self.btn_m[3].ActiveBack = '#009C27'
        self.btn_m[3].DefaultBackGround = '#20B645'
        # Clear
        self.btn_m[4].configure(width=1, bg='firebrick2', activebackground='firebrick4', font=('Marlett', 23),
                                command=lambda: self.Delete())
        self.btn_m[4].ActiveBack = 'firebrick3'
        self.btn_m[4].DefaultBackGround = 'firebrick2'
        # Remove
        self.btn_m[5].configure(width=1, bg='Royalblue2', activebackground='Royalblue4', font=('Wingdings', 21),
                                command=lambda: self.Remove())
        self.btn_m[5].ActiveBack = 'Royalblue3'
        self.btn_m[5].DefaultBackGround = 'Royalblue2'

        # ========================Trigonometry======================================================================
        self.btn_u = []
        for i in range(6):
            self.btn_u.append(HoverButton(self.middle_frame, **btn_prm))
            self.btn_u[i].grid(row=1, column=i, sticky=NSEW, padx=1, pady=1)
        # ROW 2
        # ========================Logarithm=============================================================================
        Logarithm_pad = ['Ln(', 'Log(', "Log2(", 'Exp(', 'sqrt(', "oo"]
        Logarithm_txt = ['Ln', 'Log⏨', "Log₂", 'Exp', '√n', "∞"]
        self.btn_d = []
        for i in range(6):
            self.btn_d.append(HoverButton(self.middle_frame, **btn_prm, text=Logarithm_txt[i]))
            self.btn_d[i].grid(row=2, column=i, sticky=NSEW, padx=1, pady=1)
            self.btn_d[i].configure(command=lambda n=Logarithm_pad[i]: self.Input(n))

        # buttons that will be displayed on bottom frame ROW 0==========================================================
        # ========================Numbers===============================================================================
        btn = ['π', 'E', "1j", '(', ')', self.x, "7", "8", "9", "+", '**3', self.y, "4", "5", "6", "-", "**2", self.z,
               "1", "2", "3", "*", "**", "e", '.', "0", "=", "/", "Fact(", '/100']

        btn_txt = ['π', 'E', "j", '(', ')', 'x', "7", "8", "9", "+", u'n\u00B3', 'y', "4", "5", "6", "-",
                   u'n\u00B2', 'z', "1", "2", "3", "*", "nˣ", '10ˣ', '.', "0", "=", "/", "!n", "n%"]
        self.btn = []
        i = 0
        for j in range(5):
            for k in range(6):
                self.btn.append(HoverButton(self.bottom_frame, **btnb_prm, text=btn_txt[i]))
                self.btn[i].grid(row=j, column=k, sticky=NSEW, padx=1, pady=1)
                self.btn[i].configure(command=lambda n=btn[i]: self.Input(n))
                i += 1
        for l in range(6, 9):
            self.btn[l].configure(bg='#212121', activebackground="#111111")
            self.btn[l].ActiveBack = '#161616'
            self.btn[l].DefaultBackGround = '#212121'
        for l in range(12, 15):
            self.btn[l].configure(bg='#212121', activebackground="#111111")
            self.btn[l].ActiveBack = '#161616'
            self.btn[l].DefaultBackGround = '#212121'
        for l in range(18, 21):
            self.btn[l].configure(bg='#212121', activebackground="#111111")
            self.btn[l].ActiveBack = '#161616'
            self.btn[l].DefaultBackGround = '#212121'
        self.btn[25].configure(bg='#212121', activebackground="#111111")
        self.btn[25].ActiveBack = '#161616'
        self.btn[25].DefaultBackGround = '#212121'
        # Equals
        self.btn[26].configure(bg='#FF5E00', activebackground='#A74400', command=self.InputEquals)
        self.btn[26].ActiveBack = '#CF4E00'
        self.btn[26].DefaultBackGround = '#FF5E00'
        # run button switcher and display switcher mode=================================================================
        self.SwitchButtons('1st'), self.SwitchFunction('Operation', True), self.SwitchDegRad('Radians')
        self.SwitchENG(int(16))
        # Switch Menu In Bare Display===================================================================================
        File.add_command(label='1st Page             V', command=lambda: self.SwitchButtons("1st"))
        File.add_command(label='2nd Page           B', command=lambda: self.SwitchButtons("2nd"))
        File.add_separator()
        File.add_command(label='Radians              R', command=lambda: self.SwitchDegRad('Radians'))
        File.add_command(label='Degree               D', command=lambda: self.SwitchDegRad('Degree'))
        File.add_separator()
        File.add_command(label="Close         Alt+F4", command=Exit)
        Mode.add_command(label="Operation",
                         command=lambda: [self.SwitchButtons('1st'), self.SwitchFunction("Operation", True)])
        Mode.add_command(label='Function',
                         command=lambda: [self.SwitchButtons('1st'), self.SwitchFunction('Function', True)])
        Mode.add_command(label="Simple Line Equation",
                         command=lambda: [self.SwitchButtons('1st'), self.SwitchFunction('Equation', True)])
        Mode.add_command(label='Line Equation Solver',
                         command=lambda: [self.SwitchButtons('1st'), self.SwitchFunction('Solve', True)])
        Mode.add_command(label='System Equation Solver',
                         command=lambda: [self.SwitchButtons('1st'), self.SwitchFunction('Matrix', True)])
        Mode.add_separator()
        Mode.add_command(label='Plot', command=lambda: [self.SwitchButtons('2nd'), self.SwitchFunction('Plot', True)])
        Mode.add_command(label='Plot Parametric',
                         command=lambda: [self.SwitchButtons('2nd'), self.SwitchFunction('Plot Prm', True)])
        Mode.add_command(label='Plot 3D',
                         command=lambda: [self.SwitchButtons('2nd'), self.SwitchFunction('Plot3D', True)])
        Mode.add_command(label='Plot 3D Parametric Line',
                         command=lambda: [self.SwitchButtons('2nd'), self.SwitchFunction('P3DPL', True)])
        Mode.add_command(label='Plot 3D Parametric Surface',
                         command=lambda: [self.SwitchButtons('2nd'), self.SwitchFunction('P3DPS', True)])
        Switch.add_command(label='ENG', command=lambda: self.SwitchENG(int(16)))
        Switch.add_command(label='ENG₁', command=lambda: self.SwitchENG(int(1)))
        Switch.add_command(label='ENG₂', command=lambda: self.SwitchENG(int(2)))
        Switch.add_command(label='ENG₃', command=lambda: self.SwitchENG(int(3)))
        Switch.add_command(label='ENG₆', command=lambda: self.SwitchENG(int(6)))
        Switch.add_command(label='ENG₉', command=lambda: self.SwitchENG(int(9)))
        Switch.add_command(label='ENG₁₂', command=lambda: self.SwitchENG(int(12)))
        Switch.add_command(label='ENG₁₅', command=lambda: self.SwitchENG(int(15)))

    def SwitchButtons(self, side):
        page = side
        # buttons to switch between buttons those will be displayed on middle & top frames
        if page == '1st':
            # buttons that will be displayed on top frame ROW 0=========================================================
            for i in range(5):
                self.btn_b[i].destroy()
            big_txt = ['Operation', 'Function', "Simple\nLine\nEquation", 'Line\nEquation\nSolver',
                       'System\nEquation\nSolver']
            big_pad = ['Operation', 'Function', 'Equation', 'Solve', 'Matrix']
            self.btn_a = []
            for i in range(5):
                self.btn_a.append(HoverButton(self.top_frame, **big2_prm, text=big_txt[i]))
                self.btn_a[i].grid(row=0, column=i, sticky=NSEW, padx=1, pady=1)
                self.btn_a[i]["command"] = lambda n=big_pad[i]: self.SwitchFunction(n, True)

            # buttons that will be displayed on middle frame ROW 0======================================================
            # 2nd
            self.btn_m[1].configure(text="1ST", command=lambda: self.SwitchButtons("2nd"), fg='#FF9950',
                                    activeforeground='orange')
            # ROW 1
            # ========================Trigonometry======================================================================
            Trigonometry_pad = ['Cos(', 'Sin(', "Tan(", 'Cosh(', 'Sinh(', "Tanh("]
            Trigonometry_txt = ['Cos', 'Sin', "Tan", 'Cosh', 'Sinh', "Tanh"]
            for i in range(6):
                self.btn_u[i].configure(text=Trigonometry_txt[i], command=lambda n=Trigonometry_pad[i]: self.Input(n))

            if self.mode == 'Operation' or self.mode == 'Function' or self.mode == 'Equation' or self.mode == 'Solve':
                self.SwitchFunction(self.mode, False)

        elif page == '2nd':
            # buttons that will be displayed on top frame ROW 0=========================================================
            for i in range(5):
                self.btn_a[i].destroy()
            big_txt = ['Plot\nf(x)', 'Plot\nParametric', 'Plot 3D\nParametric\nLine', "Plot3D\nf(x,y)",
                       'Plot 3D\nParametric\nSurface']
            big_pad = ['Plot', 'Plot Prm', 'P3DPL', "Plot3D", 'P3DPS']
            self.btn_b = []
            for i in range(5):
                self.btn_b.append(HoverButton(self.top_frame, **big2_prm, text=big_txt[i]))
                self.btn_b[i].grid(row=0, column=i, sticky=NSEW, padx=1, pady=1)
                self.btn_b[i]["command"] = lambda n=big_pad[i]: self.SwitchFunction(n, True)

            # buttons that will be displayed on middle frame ROW 0======================================================
            # 1st
            self.btn_m[1].configure(text="2ND", command=lambda: self.SwitchButtons("1st"), fg='#FF9950',
                                    activeforeground='orange')
            # ROW 1
            # ========================Trigonometry======================================================================
            Trigonometry_pad = ['aCos(', 'aSin(', "aTan(", 'aCosh(', 'aSinh(', "aTanh("]
            Trigonometry_txt = ['aCos', 'aSin', "aTan", 'aCosh', 'aSinh', "aTanh"]
            for i in range(6):
                self.btn_u[i].configure(text=Trigonometry_txt[i], command=lambda n=Trigonometry_pad[i]: self.Input(n))

            if self.mode == 'Plot' or self.mode == 'Plot Prm' or self.mode == 'P3DPL' or self.mode == "Plot3D" or \
                    self.mode == 'P3DPS':
                self.SwitchFunction(self.mode, False)

    def SwitchFunction(self, passmode, doing):
        self.mode = passmode
        self.switched = doing
        if self.switched:
            self.FullTextDisplay.delete(0, END)

        if self.mode == 'Operation':
            if self.switched:
                self.FullTextDisplay.insert(END, 'Mode Operation :')
                self.FastTextVariable.set('')
                self.btn[5]['state'] = ['disabled']
                self.btn[11]['state'] = ['disabled']
                self.btn[17].config(state=DISABLED)
                self.btn[2].config(state=NORMAL)
                self.btn_d[1].config(state=NORMAL)
                self.btn_d[2].config(state=NORMAL)

            self.btn_a[0].config(bg='#80000B', relief='sunken')
            self.btn_a[0].DefaultBackGround = '#80000B'
            for i in range(1, 5):
                self.btn_a[i].config(bg='#212121', relief='raised')
                self.btn_a[i].DefaultBackGround = '#212121'

        elif self.mode == 'Function':
            if self.switched:
                self.FullTextDisplay.insert(END, 'Mode Function : f(x)')
                self.FastTextVariable.set(f'From : A --> To : B | f(x) = Function')
                self.btn[5]['state'] = ['normal']
                self.btn[2]['state'] = ['disabled']
                self.btn[11]['state'] = ['disabled']
                self.btn[17].config(state=DISABLED)
                self.btn_d[1]['state'] = ['disabled']
                self.btn_d[2]['state'] = ['disabled']
                self.SwitchDegRad('Radians')

            self.btn_a[0].config(bg='#212121', relief='raised')
            self.btn_a[0].DefaultBackGround = '#212121'
            self.btn_a[1].config(bg='#80000B', relief='sunken')
            self.btn_a[1].DefaultBackGround = '#80000B'
            for i in range(2, 5):
                self.btn_a[i].config(bg='#212121', relief='raised')
                self.btn_a[i].DefaultBackGround = '#212121'

        elif self.mode == 'Equation':
            if self.switched:
                self.FullTextDisplay.insert(END, 'Mode Simple Line Equation : ax² + bx + c = 0')
                self.FastTextVariable.set('ax² + bx + c = 0')
                self.btn[5].config(state=DISABLED)
                self.btn[11].config(state=DISABLED)
                self.btn[17].config(state=DISABLED)
                self.btn[2].config(state=DISABLED)
                self.btn_d[1].config(state=NORMAL)
                self.btn_d[2].config(state=NORMAL)
                self.SwitchDegRad('Radians')

            for i in range(2):
                self.btn_a[i].config(bg='#212121', relief='raised')
                self.btn_a[i].DefaultBackGround = '#212121'
            self.btn_a[2].config(bg='#80000B', relief='sunken')
            self.btn_a[2].DefaultBackGround = '#80000B'
            for i in range(3, 5):
                self.btn_a[i].config(bg='#212121', relief='raised')
                self.btn_a[i].DefaultBackGround = '#212121'

        elif self.mode == 'Solve':
            if self.switched:
                self.FullTextDisplay.insert(END, 'Mode Line Equation Solver : One {eq} : [x] | Constants : (y,z)')
                self.btn[5].config(state=NORMAL)
                self.btn[11].config(state=NORMAL)
                self.btn[17].config(state=NORMAL)
                self.btn[2].config(state=DISABLED)
                self.btn_d[1]['state'] = ['disabled']
                self.btn_d[2]['state'] = ['disabled']
                self.SwitchDegRad('Radians')

            for i in range(3):
                self.btn_a[i].config(bg='#212121', relief='raised')
                self.btn_a[i].DefaultBackGround = '#212121'
            self.btn_a[3].config(bg='#80000B', relief='sunken')
            self.btn_a[3].DefaultBackGround = '#80000B'
            self.btn_a[4].config(bg='#212121', relief='raised')
            self.btn_a[4].DefaultBackGround = '#212121'

        elif self.mode == 'Matrix':
            if self.switched:
                self.FullTextDisplay.insert(END, 'Mode System Equation Solver :')
                self.btn[5].config(state=NORMAL)
                self.btn[11].config(state=NORMAL)
                self.btn[17].config(state=NORMAL)
                self.btn[2].config(state=DISABLED)
                self.btn_d[1]['state'] = ['disabled']
                self.btn_d[2]['state'] = ['disabled']
                self.SwitchDegRad('Radians')

            for i in range(4):
                self.btn_a[i].config(bg='#212121', relief='raised')
                self.btn_a[i].DefaultBackGround = '#212121'
            self.btn_a[4].config(bg='#80000B', relief='sunken')
            self.btn_a[4].DefaultBackGround = '#80000B'

        elif self.mode == 'Plot':
            if self.switched:
                self.FullTextDisplay.insert(END, 'Mode Plot : f(x)')
                self.FastTextVariable.set(f'f(x)₁ = ')
                self.btn[5]['state'] = ['normal']
                self.btn[11]['state'] = ['disabled']
                self.btn[17].config(state=DISABLED)
                self.btn[2]['state'] = ['disabled']
                self.btn_d[1]['state'] = ['disabled']
                self.btn_d[2]['state'] = ['disabled']
                self.SwitchDegRad('Radians')

            self.btn_b[0].config(bg='#80000B', relief='sunken')
            self.btn_b[0].DefaultBackGround = '#80000B'
            for i in range(1, 5):
                self.btn_b[i].config(bg='#212121', relief='raised')
                self.btn_b[i].DefaultBackGround = '#212121'

        elif self.mode == 'Plot Prm':
            if self.switched:
                self.FullTextDisplay.insert(END, 'Mode Plot Parametric : f(x)₁ | f(x)₂ ')
                self.FastTextVariable.set(f'f(x)₁ = ')
                self.btn[5]['state'] = ['normal']
                self.btn[11]['state'] = ['disabled']
                self.btn[17].config(state=DISABLED)
                self.btn[2]['state'] = ['disabled']
                self.btn_d[1]['state'] = ['disabled']
                self.btn_d[2]['state'] = ['disabled']
                self.SwitchDegRad('Radians')

            self.btn_b[0].config(bg='#212121', relief='raised')
            self.btn_b[0].DefaultBackGround = '#212121'
            self.btn_b[1].config(bg='#80000B', relief='sunken')
            self.btn_b[1].DefaultBackGround = '#80000B'
            for i in range(2, 5):
                self.btn_b[i].config(bg='#212121', relief='raised')
                self.btn_b[i].DefaultBackGround = '#212121'

        elif self.mode == 'P3DPL':
            if self.switched:
                self.FullTextDisplay.insert(END, 'Mode Plot3D Parametric Line : f(x)₁ | f(x)₂ ')
                self.FastTextVariable.set('f(x)₁ = ')
                self.btn[5]['state'] = ['normal']
                self.btn[11]['state'] = ['disabled']
                self.btn[17].config(state=DISABLED)
                self.btn[2]['state'] = ['disabled']
                self.btn_d[1]['state'] = ['disabled']
                self.btn_d[2]['state'] = ['disabled']
                self.SwitchDegRad('Radians')

            for i in range(2):
                self.btn_b[i].config(bg='#212121', relief='raised')
                self.btn_b[i].DefaultBackGround = '#212121'
            self.btn_b[2].config(bg='#80000B', relief='sunken')
            self.btn_b[2].DefaultBackGround = '#80000B'
            for i in range(3, 5):
                self.btn_b[i].config(bg='#212121', relief='raised')
                self.btn_b[i].DefaultBackGround = '#212121'

        elif self.mode == 'Plot3D':
            if self.switched:
                self.FullTextDisplay.insert(END, 'Mode Plot3D : f(x,y)')
                self.FastTextVariable.set(f'f(x,y)')
                self.btn[5]['state'] = ['normal']
                self.btn[11]['state'] = ['normal']
                self.btn[17].config(state=DISABLED)
                self.btn[2]['state'] = ['disabled']
                self.btn_d[1]['state'] = ['disabled']
                self.btn_d[2]['state'] = ['disabled']
                self.SwitchDegRad('Radians')

            for i in range(3):
                self.btn_b[i].config(bg='#212121', relief='raised')
                self.btn_b[i].DefaultBackGround = '#212121'
            self.btn_b[3].config(bg='#80000B', relief='sunken')
            self.btn_b[3].DefaultBackGround = '#80000B'
            self.btn_b[4].config(bg='#212121', relief='raised')
            self.btn_b[4].DefaultBackGround = '#212121'

        elif self.mode == 'P3DPS':
            if self.switched:
                self.FullTextDisplay.insert(END, 'Mode Plot3D Parametric Surface : f(x,y)₁ | f(x,y)₂ ')
                self.FastTextVariable.set(f'f(x,y)₁ = ')
                self.btn[5]['state'] = ['normal']
                self.btn[11]['state'] = ['normal']
                self.btn[17].config(state=DISABLED)
                self.btn[2]['state'] = ['disabled']
                self.btn_d[1]['state'] = ['disabled']
                self.btn_d[2]['state'] = ['disabled']
                self.SwitchDegRad('Radians')

            for i in range(4):
                self.btn_b[i].config(bg='#212121', relief='raised')
                self.btn_b[i].DefaultBackGround = '#212121'
            self.btn_b[4].config(bg='#80000B', relief='sunken')
            self.btn_b[4].DefaultBackGround = '#80000B'

        if self.switched:
            self.Delete()

    def SwitchDegRad(self, convert):
        switch = convert
        if switch == 'Degree':
            global convert_constant, inverse_convert_constant
            convert_constant = π / 180
            inverse_convert_constant = 180 / π
            # Degree -> Radians
            self.btn_m[0].configure(text='DEG', command=lambda: self.SwitchDegRad('Radians'), fg='#FF9950',
                                    activeforeground='orange')
            self.btn[0]['state'] = ['disabled']

        elif switch == 'Radians':
            convert_constant = 1
            inverse_convert_constant = 1
            # Radians -> Degree
            self.btn_m[0].configure(text='RAD', command=lambda: self.SwitchDegRad('Degree'), fg='#FF9950',
                                    activeforeground='orange')
            self.btn[0]['state'] = ['normal']

    def SwitchENG(self, NBR):
        dot = NBR
        self.ENG = NBR

        if dot == int(16):
            self.btn_m[2].configure(text='ENG', command=lambda: self.SwitchENG(int(15)), fg='#FF9950',
                                    activeforeground='orange')
        elif dot == int(15):
            self.btn_m[2].configure(text='ENG₁₅', command=lambda: self.SwitchENG(int(12)), fg='#FF9950',
                                    activeforeground='orange')
        elif dot == int(12):
            self.btn_m[2].configure(text='ENG₁₂', command=lambda: self.SwitchENG(int(9)), fg='#FF9950',
                                    activeforeground='orange')
        elif dot == int(9):
            self.btn_m[2].configure(text='ENG₉', command=lambda: self.SwitchENG(int(6)), fg='#FF9950',
                                    activeforeground='orange')
        elif dot == int(6):
            self.btn_m[2].configure(text='ENG₆', command=lambda: self.SwitchENG(int(3)), fg='#FF9950',
                                    activeforeground='orange')
        elif dot == int(3):
            self.btn_m[2].configure(text='ENG₃', command=lambda: self.SwitchENG(int(2)), fg='#FF9950',
                                    activeforeground='orange')
        elif dot == int(2):
            self.btn_m[2].configure(text='ENG₂', command=lambda: self.SwitchENG(int(1)), fg='#FF9950',
                                    activeforeground='orange')
        elif dot == int(1):
            self.btn_m[2].configure(text='ENG₁', command=lambda: self.SwitchENG(int(16)), fg='#FF9950',
                                    activeforeground='orange')
        self.Click()

    def Delete(self):
        self.a = ''
        self.b = ''
        self.c = ''
        self.q = ''
        self.p = ''
        self.j = ''
        self.k = ''
        self.m = ''
        self.n = ''
        self.lslv = ''
        self.xexp = ''
        self.yexp = ''
        self.zexp = ''
        self.fctx = ''
        self.fctx1 = ''
        self.fctx2 = ''
        self.fctxy = ''
        self.fctxy1 = ''
        self.fctxy2 = ''
        self.PA = ''
        self.P3d = ''
        self.P3dps = ''
        self.store_expression = []
        self.store_order = []
        self.callback_function = []
        self.expression = ''
        self.TextVariable.set('')
        self.FastTextVariable.set('')

        if self.mode == 'Function':
            self.TextVariable.set(f'From : ')
            self.FastTextVariable.set(f'From : A --> To : B')

        elif self.mode == 'Equation':
            self.TextVariable.set(f'a = ')
            self.FastTextVariable.set('ax² + bx + c = 0')

        elif self.mode == 'Solve':
            self.TextVariable.set(f'eq > ')
            self.FastTextVariable.set('eq > ')

        elif self.mode == 'Matrix':
            self.TextVariable.set(f'eq₁ > ')
            self.FastTextVariable.set('eq₁ > ')

        elif self.mode == 'Plot':
            self.TextVariable.set(f'f(x) = ')
            self.FastTextVariable.set(f'f(x) = ')

        elif self.mode == "Plot Prm" or self.mode == "P3DPL":
            self.TextVariable.set(f'f(x)₁ = ')
            self.FastTextVariable.set(f'f(x)₁ = ')

        elif self.mode == 'Plot3D':
            self.TextVariable.set(f'f(x,y) = ')
            self.FastTextVariable.set(f'f(x,y) = ')

        elif self.mode == "P3DPS":
            self.TextVariable.set(f'f(x,y)₁ = ')
            self.FastTextVariable.set(f'f(x,y)₁ = ')

        self.equal = False
        self.clear = False
        self.full = None
        self.exist = None

    def Remove(self):
        if self.clear:
            self.Delete()

        try:
            k = self.store_order[-1]
            while k > 0:
                self.expression = self.expression[:-1]
                k -= 1

            self.store_order.remove(self.store_order[-1])
            self.store_expression.remove(self.store_expression[-1])

        except IndexError:
            self.FastTextVariable.set('IndexError')

        self.Click()

    def KeyboardInput(self, keyword):
        put = keyword.keysym.lower()
        try:
            if keyword.keysym == 'Return' or put == 'equal':
                self.InputEquals()

            if self.clear:
                if self.mode == 'Operation':
                    if keyword.keysym == 'Return' or put == 'equal':
                        pass
                    else:
                        self.Delete()
                else:
                    self.Delete()

            if keyword.keysym == 'BackSpace':
                self.Remove()

            elif keyword.keysym == 'Delete':
                self.Delete()

            elif keyword.keysym == 'E':
                self.Input('E')

            elif keyword.keysym == 'e':
                self.Input('Exp(')

            elif put == 'v':
                self.SwitchButtons("1st")

            elif put == 'b':
                self.SwitchButtons("2nd")

            elif put == 'r':
                self.SwitchDegRad('Radians')

            elif put == 'd':
                self.SwitchDegRad('Degree')

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

            elif put == 'bar':
                self.Input('Sq(')

            elif put == 'backslash':
                self.Input('sqrt(')

            elif keyword.keysym == 's':
                self.Input('Sin(')

            elif keyword.keysym == 'c':
                self.Input('Cos(')

            elif keyword.keysym == 't':
                self.Input('Tan(')

            elif keyword.keysym == 'S':
                self.Input('Sinh(')

            elif keyword.keysym == 'C':
                self.Input('Cosh(')

            elif keyword.keysym == 'T':
                self.Input('Tanh(')

            elif keyword.keysym == 'l':
                self.Input('Ln(')

            elif put == 'i':
                self.Input('oo')

            elif put == 'j':
                self.Input('1j')

            elif put == 'exclam' or put == 'f':
                self.Input('factorial(')

            elif keyword.keysym == 'L':
                self.Input('Log')

            elif put == 'p':
                self.Input('π')

            elif put == 'x' or put == 'y' or put == 'z' or put == '0' or put == '1' or put == '2' or put == '3' \
                    or put == '4' or put == '5' or put == '6' or put == '7' or put == '8' or put == '9':
                self.Input(put)
            else:
                pass

            if keyword.keysym == 'Return' or put == 'equal':
                pass
            else:
                self.Click()

        except IndexError:
            self.FastTextVariable.set('IndexError')

    def Input(self, keyword):
        if self.clear:
            self.Delete()

        self.store_expression.append(str(keyword))
        self.store_order.append(len(str(keyword)))
        self.expression += str(keyword)

        self.Click()

    def Click(self):
        try:
            if self.mode == 'Operation':
                self.FastTextVariable.set('')
                self.TextVariable.set(self.expression)
                if self.ENG == 16:
                    self.FastTextVariable.set(eval(self.expression))

                else:
                    self.FastTextVariable.set(N(sympify(self.expression), self.ENG))

            elif self.mode == 'Function':
                if self.full is None:
                    self.TextVariable.set(f'From : {self.expression}')
                    self.FastTextVariable.set(f'From : {self.expression} --> To : B')

                elif not self.full:
                    self.TextVariable.set(f'To : {self.expression}')
                    self.FastTextVariable.set(f'From : {self.v} --> To : {self.expression}')

                elif self.full:
                    self.TextVariable.set(f'f(x) = {self.expression}')
                    self.FastTextVariable.set(f'f(x) = {self.expression}')

            elif self.mode == 'Equation':
                if self.full is None:
                    self.TextVariable.set(f'a = {self.expression}')
                    self.FastTextVariable.set(f'{self.expression}x² + bx + c = 0')

                elif not self.full:
                    self.TextVariable.set(f'b = {self.expression}')
                    self.FastTextVariable.set(f'{self.a}x² + ({self.expression})x + c = 0')

                elif self.full:
                    self.TextVariable.set(f'c = {self.expression}')
                    self.FastTextVariable.set(f'{self.a}x² + ({self.b})x + ({self.expression}) = 0')

            elif self.mode == 'Solve':
                if self.full is None:
                    self.TextVariable.set(f'eq > {self.expression}')
                    self.FastTextVariable.set(f'eq > {self.expression}')
                elif self.full:
                    self.TextVariable.set(f'eq > {self.q} = {self.expression}')
                    self.FastTextVariable.set(f'eq > {self.q} = {self.expression}')

            elif self.mode == 'Matrix':
                if self.full is None:
                    self.TextVariable.set(f'eq₁ > {self.expression}')
                    self.FastTextVariable.set(f'eq₁ > {self.expression}')
                elif not self.full:
                    self.TextVariable.set(f'eq₁ > {self.q} = {self.expression}')
                    self.FastTextVariable.set(f'eq₁ > {self.q} = {self.expression}')

                elif self.full and self.clear is None:
                    self.TextVariable.set(f'eq₂ > {self.expression}')
                    self.FastTextVariable.set(f'eq₂ > {self.expression}')
                elif self.full and not self.clear and self.equal is None:
                    self.TextVariable.set(f'eq₂ > {self.j} = {self.expression}')
                    self.FastTextVariable.set(f'eq₂ > {self.j} = {self.expression}')

                elif self.full and not self.clear and not self.equal:
                    self.TextVariable.set(f'eq₃ > {self.expression}')
                    self.FastTextVariable.set(f'eq₃ > {self.expression}')
                elif self.full and not self.clear and self.equal:
                    self.TextVariable.set(f'eq₃ > {self.m} = {self.expression}')
                    self.FastTextVariable.set(f'eq₃ > {self.m} = {self.expression}')

            elif self.mode == 'Plot':
                self.TextVariable.set(f'f(x) = {self.expression}')
                self.FastTextVariable.set(f'f(x) = {self.expression}')

            elif self.mode == "Plot Prm" or self.mode == "P3DPL":
                if self.full is None:
                    self.TextVariable.set(f'f(x)₁ = {self.expression}')
                    self.FastTextVariable.set(f'f(x)₁ = {self.expression}')

                elif self.full:
                    self.TextVariable.set(f'f(x)₂ = {self.expression}')
                    self.FastTextVariable.set(f'f(x)₁ = {self.fctx1} | f(x)₂ = {self.expression}')

            elif self.mode == "Plot3D":
                self.TextVariable.set(f'f(x,y) = {self.expression}')
                self.FastTextVariable.set(f'f(x,y) = {self.expression}')

            elif self.mode == "P3DPS":
                if self.full is None:
                    self.TextVariable.set(f'f(x,y)₁ = {self.expression}')
                    self.FastTextVariable.set(f'f(x,y)₁ = {self.expression}')

                elif self.full:
                    self.TextVariable.set(f'f(x,y)₂ = {self.expression}')
                    self.FastTextVariable.set(f'f(x,y)₁ = {self.fctx1} | f(x,y)₂ = {self.expression}')

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
        self.callback_function.append(str(self.expression))
        try:
            if self.mode == 'Operation':
                try:
                    if not self.equal:
                        if self.ENG == 16:
                            self.answer = eval(self.expression)
                        else:
                            self.answer = N(sympify(self.expression), self.ENG)
                        self.FastTextVariable.set('')
                        self.TextVariable.set(f'{self.expression} = {self.answer}')
                        self.FullTextDisplay.insert(END, f'{self.expression} = {self.answer}')
                        self.clear = True
                        self.equal = True

                    elif self.equal:
                        self.expression = ''
                        self.v = int(len(self.store_expression)) - 1
                        self.w = int(len(self.store_expression)) - 1
                        while True:
                            trs = str(self.store_expression[self.v])
                            if trs == '**' or trs == '+' or trs == '-' or trs == '*' or trs == '/' or trs == '^':
                                while self.v <= self.w:
                                    self.expression += str(self.store_expression[self.v])
                                    self.v += 1
                                self.expression = str(self.callback[-1]) + str(self.expression)
                                if self.ENG == 16:
                                    self.answer = eval(self.expression)
                                else:
                                    self.answer = N(sympify(self.expression), self.ENG)
                                self.FastTextVariable.set(self.answer)
                                self.TextVariable.set(f'{self.expression} = {self.answer}')
                                self.FullTextDisplay.insert(END, f'{self.expression} = {self.answer}')
                                break
                            self.v -= 1
                except IndexError or SyntaxError:
                    try:
                        self.expression = str(self.callback[-1])
                        if self.ENG == 16:
                            self.answer = eval(self.expression)
                        else:
                            self.answer = N(sympify(self.expression), self.ENG)
                        self.FastTextVariable.set(self.answer)
                        self.TextVariable.set(f'{self.expression} = {self.answer}')
                        self.FullTextDisplay.insert(END, f'{self.expression} = {self.answer}')
                    except IndexError or SyntaxError:
                        self.FastTextVariable.set('IndexError or SyntaxError')

                self.callback.append(str(self.answer))

            elif self.mode == 'Function':
                if self.full is None:
                    self.v = int(self.expression)
                    self.FullTextDisplay.insert(END, f'from : {self.expression}')
                    self.expression = ""
                    self.TextVariable.set('To : ')
                    self.full = False

                elif not self.full:
                    self.w = int(self.expression) + 1
                    self.FullTextDisplay.insert(END, f'To : {self.expression}')
                    self.expression = ""
                    self.TextVariable.set('f(x) = ')
                    self.FastTextVariable.set(f'f(x) = ')
                    self.full = True

                elif self.full:
                    if not self.equal:
                        self.fctx = str(eval(self.expression))
                        self.FullTextDisplay.insert(END, f'f(x) = {sympify(self.fctx)}')
                        for x in range(self.v, self.w):
                            if self.ENG == 16:
                                self.FullTextDisplay.insert(END, f'f({x}) = {eval(self.fctx)}')
                            else:
                                self.FullTextDisplay.insert(END, f'f({x}) = {N(eval(self.fctx), self.ENG)}')
                        self.P3d = plot(sympify(self.fctx), (self.x, self.v, int(self.w) - 1))
                        self.expression = ""
                        self.TextVariable.set(f'f(x) = ')
                        self.equal = True

                    elif self.equal:
                        self.fctx = str(eval(self.expression))
                        self.FullTextDisplay.insert(END, f'f(x) = {self.fctx}')
                        for x in range(self.v, self.w):
                            if self.ENG == 16:
                                self.FullTextDisplay.insert(END, f'f({x}) = {eval(self.fctx)}')
                            else:
                                self.FullTextDisplay.insert(END, f'f({x}) = {N(eval(self.fctx), self.ENG)}')
                        self.expression = ""
                        self.TextVariable.set(f'f(x) = ')
                        self.PA = plot(sympify(self.fctx), (self.x, self.v, int(self.w) - 1))
                        self.P3d.append(self.PA[0])
                        self.P3d.show()

            elif self.mode == 'Equation':
                if self.full is None:
                    self.a = float(eval(self.expression))
                    self.expression = ""
                    self.TextVariable.set(f'b = ')
                    self.full = False

                elif not self.full:
                    self.b = float(eval(self.expression))
                    self.expression = ""
                    self.TextVariable.set(f'c = ')
                    self.full = True

                elif self.full:
                    c = float(eval(self.expression))
                    d = float((self.b ** 2) - 4 * self.a * c)
                    nd = neg(d)
                    nb = neg(self.b)
                    self.TextVariable.set(f'a = {self.a} | b = {self.b} | c = {c}')
                    self.FastTextVariable.set(f'{self.a}x² + ({self.b})x + ({c}) = 0')
                    if self.a > 0 or self.a < 0:
                        self.FullTextDisplay.insert(END,
                                                    f'The Equation Have Two Solutions For x :',
                                                    f'  ∆ =  b² - 4ac',
                                                    f'  ∆ = {self.b}² - (4 ⨯ ({self.a}) ⨯ ({c}))',
                                                    f'      = {self.b ** 2} - ({4 * self.a * c})',
                                                    f'      = {d}')
                        if d == 0:
                            self.FullTextDisplay.insert(END,
                                                        f'∆=0 : x = -b / 2a',
                                                        f' x₁ = x₂ = ({N(neg(self.b), 3)}) / (2 ⨯ {self.a})',
                                                        f' x₁ = x₂ = {N(neg(self.b) / (2 * self.a), 3)}')
                        elif d >= 0:
                            self.FullTextDisplay.insert(END,
                                                        f'∆>0 : x = (-b ± √∆) / 2a',
                                                        f' x₁ = ({nb} + √{d}) / (2 ⨯ {self.a})',
                                                        f'     = {N((nb + sqrt(d)) / (2 * self.a), 3)}',
                                                        f' x₂ = ({nb} - √{d}) / (2 ⨯ {self.a})',
                                                        f'     = {N((nb - sqrt(d)) / (2 * self.a), 3)}')
                        elif d <= 0:
                            self.FullTextDisplay.insert(END,
                                                        f'      = {nd}i²',
                                                        f'∆<0 : x = (-b ± i√∆) / 2a',
                                                        f' x₁ = ({nb} + i√({nd})) / (2 ⨯ {self.a})',
                                                        f'     = {N((nb + sqrt(nd) * 1j) / (2 * self.a), 3)}',
                                                        f' x₂ = ({nb} - i√({nd})) / (2 ⨯ {self.a})',
                                                        f'     = {N((nb - sqrt(nd) * 1j) / (2 * self.a), 3)}',
                                                        f'  z = a ± ib',
                                                        f'  a = {N(nb / (2 * self.a), 3)}',
                                                        f'  b = ± {N(sqrt(nd) / (2 * self.a), 3)}')
                    elif self.a == 0:
                        if self.b == 0 and c == 0:
                            self.TextVariable.set(f"Empty Solution {{∅}}")
                        elif self.b == 0:
                            self.TextVariable.set(f"Empty Solution {{∅}}")
                        elif c == 0:
                            self.FullTextDisplay.insert(END,
                                                        f'The Equation Have One Solution For x :',
                                                        f'  {self.b}x = 0',
                                                        f'  x = 0', )
                        else:
                            self.FullTextDisplay.insert(END,
                                                        f'The Equation Have One Solution For x :',
                                                        f'  {self.b}x = {neg(c)}',
                                                        f'  x = {neg(c)} / {self.b}',
                                                        f'  x = {neg(c) / self.b}')

                    self.clear = True
                    self.full = None

            elif self.mode == 'Solve':
                if self.full is None:
                    self.q = str(eval(self.expression))
                    self.TextVariable.set(f'eq > {self.q} = ')
                    self.FastTextVariable.set(f'eq > {self.q} = ')
                    self.expression = ""
                    self.full = True

                elif self.full:
                    self.p = str(eval(self.expression))
                    self.TextVariable.set(f'eq > {self.q} = {self.p}')
                    self.FullTextDisplay.insert(END, f'eq > {self.q} = {self.p}')
                    sol = solvify(Eq(sympify(self.q), sympify(self.p)), self.x, self.C)
                    if sol is None:
                        sol = solvify(Eq(sympify(self.q), sympify(self.p)), self.x, self.R)
                    self.FastTextVariable.set(sol)
                    for l in range(len(sol)):
                        self.FullTextDisplay.insert(END, f'> x{self.nb[int(l) + 1]} = {sol[l]}')

                    self.clear = True
                    self.full = None

            elif self.mode == 'Matrix':
                if self.full is None:
                    self.q = str(sympify(self.expression))
                    self.TextVariable.set(f'eq₁ > {self.q} = ')
                    self.expression = ""
                    self.full = False

                elif not self.full:
                    self.p = str(sympify(self.expression))
                    self.TextVariable.set('eq₂ > ')
                    self.FastTextVariable.set('eq₂ > ')
                    self.FullTextDisplay.insert(END, 'New System :', f' eq₁ | {self.q} = {self.p}')
                    self.expression = ""
                    self.full = True
                    self.clear = None

                elif self.full:
                    if self.clear is None:
                        self.j = str(sympify(self.expression))
                        self.TextVariable.set(f'eq₂ > {self.j} = ')
                        self.expression = ""
                        self.equal = None
                        self.clear = False

                    elif not self.clear:
                        if self.equal is None:
                            self.k = str(sympify(self.expression))
                            self.FullTextDisplay.insert(END, f' eq₂ | {self.j} = {self.k}')
                            try:
                                self.lslv = linsolve(
                                    [Eq(sympify(self.q), sympify(self.p)), Eq(sympify(self.j), sympify(self.k))],
                                    [self.x, self.y])
                            except ValueError or TypeError:
                                self.lslv = nonlinsolve(
                                    [Eq(sympify(self.q), sympify(self.p)), Eq(sympify(self.j), sympify(self.k))],
                                    [self.x, self.y])

                            self.lslv = str(self.lslv)
                            self.w = int(len(self.lslv))
                            self.v = 0
                            while self.v < self.w:
                                self.exist = False
                                if self.lslv[self.v] == 'z' or self.lslv == 'EmptySet':
                                    self.TextVariable.set('eq₃ > ')
                                    self.FastTextVariable.set('eq₃ > ')
                                    self.expression = ""
                                    self.equal = False
                                    self.exist = True
                                    break
                                self.v += 1

                            if not self.exist:
                                self.lslv = str(self.lslv[11:-2])
                                self.FastTextVariable.set('System of Two Equations : {eq₁,eq₂}_[x,y]')

                                self.w = int(len(self.lslv))
                                self.v = 0
                                while self.v < self.w:
                                    self.xexp = str(self.xexp) + str(self.lslv[self.v])
                                    self.v += 1
                                    if self.lslv[self.v] == ',':
                                        while self.v < self.w:
                                            self.yexp = str(self.yexp) + str(self.lslv[self.v])
                                            self.v += 1

                                self.yexp = str(self.yexp).replace(', ', '')
                                self.TextVariable.set(f'{self.sb[0]} = {self.xexp} | {self.sb[1]} = {self.yexp}')
                                self.FullTextDisplay.insert(END, f'> {self.sb[0]} = {self.xexp}',
                                                            f'> {self.sb[1]} = {self.yexp}')
                                self.clear = True
                                self.full = None

                        elif not self.equal:
                            self.m = str(sympify(self.expression))
                            self.TextVariable.set(f'eq₃ > {self.m} = ')
                            self.expression = ""
                            self.equal = True

                        elif self.equal:
                            self.n = str(sympify(self.expression))
                            self.FullTextDisplay.insert(END, f' eq₃ | {self.m} = {self.n}')
                            try:
                                self.lslv = linsolve(
                                    [Eq(sympify(self.q), sympify(self.p)), Eq(sympify(self.j), sympify(self.k)),
                                     Eq(sympify(self.m), sympify(self.n))], [self.x, self.y, self.z])
                            except ValueError or TypeError:
                                self.lslv = nonlinsolve(
                                    [Eq(sympify(self.q), sympify(self.p)), Eq(sympify(self.j), sympify(self.k)),
                                     Eq(sympify(self.m), sympify(self.n))], [self.x, self.y, self.z])

                            self.lslv = str(self.lslv)

                            if self.lslv == 'EmptySet':
                                self.TextVariable.set(self.lslv)
                                self.FastTextVariable.set(self.lslv)

                            else:
                                self.lslv = str(self.lslv[11:-2])
                                self.FastTextVariable.set('System of Three Equations : {eq₁,eq₂,eq₃}_[x,y,z]')

                                self.w = int(len(self.lslv))
                                self.v = 0
                                while self.v < self.w:
                                    self.xexp = str(self.xexp) + str(self.lslv[self.v])
                                    self.v += 1
                                    if self.lslv[self.v] == ',':
                                        while self.v < self.w:
                                            self.yexp = str(self.yexp) + str(self.lslv[self.v])
                                            self.v += 1
                                            if self.lslv[self.v] == ',':
                                                while self.v < self.w:
                                                    self.zexp = str(self.zexp) + str(self.lslv[self.v])
                                                    self.v += 1

                                self.yexp = str(self.yexp).replace(', ', '')
                                self.zexp = str(self.zexp).replace(', ', '')
                                self.TextVariable.set(f'{self.sb[0]} = {self.xexp} | {self.sb[1]} = {self.yexp} | '
                                                      f'{self.sb[2]} = {self.zexp}')
                                self.FullTextDisplay.insert(END, f'> {self.sb[0]} = {self.xexp}',
                                                            f'> {self.sb[1]} = {self.yexp}',
                                                            f'> {self.sb[2]} = {self.zexp}')
                            self.clear = True
                            self.full = None

            elif self.mode == 'Plot':
                if self.full is None:
                    self.fctx = str(eval(self.expression))
                    self.FullTextDisplay.insert(END, f'f(x) = {self.fctx}')
                    self.P3d = plot(sympify(self.fctx), ylim=(-10, 10), xlim=(-10, 10))
                    self.expression = ""
                    self.TextVariable.set(f'f(x) = ')
                    self.full = True

                elif self.full:
                    self.fctx = str(eval(self.expression))
                    self.FullTextDisplay.insert(END, f'f(x) = {self.fctx}')
                    self.PA = plot(sympify(self.fctx), ylim=(-10, 10), xlim=(-10, 10), show=False)
                    self.P3d.append(self.PA[0])

                    s = int(len(self.callback_function) - 1)
                    RD = randint(1048576, 16777000)
                    HX = hex(RD)
                    HX = HX[2:8].upper()
                    self.P3d[s].line_color = str('#') + str(HX)
                    PlotGrid(1, 2, self.P3d, self.PA)
                    self.expression = ""
                    self.TextVariable.set(f'f(x) = ')

            elif self.mode == 'Plot Prm':
                if self.full is None:
                    self.fctx1 = str(eval(self.expression))
                    self.FullTextDisplay.insert(END, f'f(x)₁ = {self.fctx1}')
                    self.FastTextVariable.set(f'f(x)₁ = {self.fctx1} | f(x)₂ =')
                    self.TextVariable.set(f'f(x)₂ =')
                    self.expression = ""
                    self.full = True

                elif self.full:
                    self.fctx2 = str(eval(self.expression))
                    self.FullTextDisplay.insert(END, f'f(x)₂ = {self.fctx2}')
                    self.FastTextVariable.set(f'f(x)₁ = {self.fctx1} | f(x)₂ = {self.fctx2}')
                    if not self.equal:
                        self.P3d = plot_parametric(sympify(self.fctx1), sympify(self.fctx2), ylim=(-10, 10),
                                                   xlim=(-10, 10))
                        self.expression = ""
                        self.TextVariable.set(f'f(x)₁ = ')
                        self.equal = True
                        self.full = None

                    elif self.equal:
                        self.PA = plot_parametric(sympify(self.fctx1), sympify(self.fctx2), ylim=(-10, 10),
                                                  xlim=(-10, 10), show=False)
                        self.P3d.append(self.PA[0])
                        s = int((len(self.callback_function) / 2) - 1)
                        RD = randint(1048576, 16777000)
                        HX = hex(RD)
                        HX = HX[2:8].upper()
                        self.P3d[s].line_color = str('#') + str(HX)
                        PlotGrid(1, 2, self.P3d, self.PA)
                        self.expression = ""
                        self.TextVariable.set(f'f(x)₁ = ')
                        self.full = None

            elif self.mode == 'P3DPL':
                if self.full is None:
                    self.fctx1 = str(eval(self.expression))
                    self.FullTextDisplay.insert(END, f'f(x)₁ = {self.fctx1}')
                    self.FastTextVariable.set(f'f(x)₁ = {self.fctx1} | f(x)₂ = ')
                    self.TextVariable.set(f'f(x)₂ =')
                    self.expression = ""
                    self.full = True

                elif self.full:
                    self.fctx2 = str(eval(self.expression))
                    self.FullTextDisplay.insert(END, f'f(x)₂ = {self.fctx2}')
                    self.FastTextVariable.set(f'f(x)₁ = {self.fctx1} | f(x)₂ = {self.fctx2}')
                    if not self.equal:
                        self.P3d = plot3d_parametric_line(sympify(self.fctx1), sympify(self.fctx2), self.x,
                                                          ylim=(-10, 10), xlim=(-10, 10))
                        self.expression = ""
                        self.TextVariable.set(f'f(x)₁ = ')
                        self.equal = True
                        self.full = None

                    elif self.equal:
                        self.PA = plot3d_parametric_line(sympify(self.fctx1), sympify(self.fctx2), self.x,
                                                         ylim=(-10, 10), xlim=(-10, 10), show=False)
                        self.P3d.append(self.PA[0])
                        s = int((len(self.callback_function) / 2) - 1)
                        RD = randint(1048576, 16777000)
                        HX = hex(RD)
                        HX = HX[2:8].upper()
                        self.P3d[s].line_color = str('#') + str(HX)
                        PlotGrid(1, 2, self.P3d, self.PA)
                        self.expression = ""
                        self.TextVariable.set(f'f(x)₁ = ')
                        self.full = None

            elif self.mode == 'Plot3D':
                if self.full is None:
                    self.fctxy = str(eval(self.expression))
                    self.FullTextDisplay.insert(END, f'f(x,y) = {self.fctxy}')
                    self.P3d = plot3d(sympify(self.fctxy))
                    self.expression = ""
                    self.TextVariable.set(f'f(x,y) = ')
                    self.full = True

                elif self.full:
                    self.fctxy = str(eval(self.expression))
                    self.FullTextDisplay.insert(END, f'f(x,y) = {self.fctxy}')
                    self.PA = plot3d(sympify(self.fctxy), show=False)
                    self.P3d.append(self.PA[0])

                    s = int(len(self.callback_function) - 1)
                    RD = randint(1048576, 16777000)
                    HX = hex(RD)
                    HX = HX[2:8].upper()
                    self.P3d[s].surface_color = str('#') + str(HX)
                    PlotGrid(1, 2, self.P3d, self.PA)
                    self.expression = ""
                    self.TextVariable.set(f'f(x,y) = ')

            elif self.mode == 'P3DPS':
                if self.full is None:
                    self.fctxy1 = str(eval(self.expression))
                    self.FullTextDisplay.insert(END, f'f(x,y)₁ = {self.fctxy1}')
                    self.FastTextVariable.set(f'f(x,y)₁ = {self.fctxy1} | f(x,y)₂ = ')
                    self.expression = ""
                    self.TextVariable.set(f'f(x,y)₂ = ')
                    self.full = True

                elif self.full:
                    self.fctxy2 = str(eval(self.expression))
                    self.FullTextDisplay.insert(END, f'f(x,y)₂ = {self.fctxy2}')
                    self.FastTextVariable.set(f'f(x,y)₁ = {self.fctxy1} | f(x,y)₂ = {self.fctxy2}')
                    if not self.equal:
                        self.P3d = plot3d_parametric_surface(sympify(self.fctxy1), sympify(self.fctxy2),
                                                             self.x - self.y)
                        self.expression = ""
                        self.TextVariable.set(f'f(x)₁ = ')
                        self.equal = True
                        self.full = None

                    elif self.equal:
                        self.PA = plot3d_parametric_surface(sympify(self.fctx1), sympify(self.fctx2), self.x - self.y,
                                                            show=False)
                        self.P3d.append(self.PA[0])
                        s = int((len(self.callback_function) / 2) - 1)
                        RD = randint(1048576, 16777000)
                        HX = hex(RD)
                        HX = HX[2:8].upper()
                        self.P3d[s].surface_color = str('#') + str(HX)
                        PlotGrid(1, 2, self.P3d, self.PA)
                        self.expression = ""
                        self.TextVariable.set(f'f(x)₁ = ')
                        self.full = None

        except ZeroDivisionError:
            self.FastTextVariable.set(oo)
        except ValueError:
            self.FastTextVariable.set('ValueError')
        except NotImplementedError:
            self.FastTextVariable.set('Cannot Solve This Equation')
        except SyntaxError:
            self.FastTextVariable.set('SyntaxError')
        except NameError:
            self.FastTextVariable.set('NameError')
        except TypeError:
            self.FastTextVariable.set('TypeError')
        except OverflowError:
            self.FastTextVariable.set('OverflowMathRangeError')
        except IndexError:
            self.FastTextVariable.set('IndexError')

        self.FullTextDisplay.see(END)


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


if __name__ == "__main__":
    win = Tk()
    menubare = Menu(win)
    File = Menu(menubare, tearoff=0)
    Mode = Menu(menubare, tearoff=0)
    Switch = Menu(menubare, tearoff=0)
    menubare.add_cascade(label="File", menu=File)
    menubare.add_cascade(label="Mode", menu=Mode)
    menubare.add_cascade(label="Float", menu=Switch)
    # run calculator
    root = Calculator(win)
    root.pack(fill="both", expand=True)
    root.configure(bg='#4d4d4d')
    # Window configuration
    win.configure(menu=menubare, bg='#4d4d4d')
    win.geometry("1100x580")
    win.minsize(width=1100, height=580)
    win.title("PyMathon v5.1.3")
    win.mainloop()
