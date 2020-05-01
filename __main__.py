from matplotlib.figure import Figure
from sympy.abc import y, z
from sympy.plotting import plot, plot_parametric, plot3d, plot3d_parametric_line, plot3d_parametric_surface
from sympy.solvers.solveset import solvify

from __jeep_v4__ import *

"""
# version 6.1
# optimize first TkAgg by add scroll bar axe X named Scrollable_TkAgg_X
# build and add TkAgg scrolled in two axes {X , Y} and turn switching between Scrolled_Listbox and Scrollable_TkAgg_XY
# setting the write hand result in Scrollable_TkAgg_XY
"""

btn_prm = {'padx': 18,
           'pady': 1,
           'bd': 1,
           'background': '#666666',
           'fg': 'white',
           'bg': '#666666',
           'font': ('Segoe UI Symbol', 16, 'bold'),
           'width': 2,
           'height': 1,
           'relief': 'raised',
           'activeback': '#555555',
           'activebackground': '#444444',
           'activeforeground': "white"}
btn_dif = {'padx': 18,
           'pady': 1,
           'bd': 1,
           'background': '#666666',
           'fg': '#FF9950',
           'bg': '#666666',
           'font': ('Wingdings', 21),
           'width': 1,
           'height': 1,
           'relief': 'raised',
           'activeback': '#555555',
           'activebackground': '#444444',
           'activeforeground': 'orange'}
btnb_prm = {'padx': 18,
            'pady': 1,
            'bd': 1,
            'background': '#4d4d4d',
            'fg': 'white',
            'bg': '#4d4d4d',
            'font': ('Segoe UI Symbol', 17),
            'width': 2,
            'height': 1,
            'relief': 'raised',
            'activeback': '#3d3d3d',
            'activebackground': '#2d2d2d',
            'activeforeground': "white"}
big2_prm = {'padx': 14,
            'pady': 19,
            'bd': 1,
            'background': '#212121',
            'fg': 'white',
            'bg': '#212121',
            'font': ('Segoe UI Symbol', 13),
            'width': 5,
            'height': 1,
            'relief': 'raised',
            'activeback': '#49000A',
            'activebackground': '#80000B',
            'activeforeground': "white"}
ent_prm = {'fg': 'black',
           'bg': '#F0F0F0',
           'font': ('Segoe UI Symbol', 16),
           'relief': 'flat'}
# noinspection NonAsciiCharacters
π = pi


class Calculator:
    def __init__(self):
        self.win = Tk()
        self.nb = ['₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉', '⏨', '₍₎']
        self.btn_u = []
        self.btn_a = []
        self.mathext = []
        # expression that will be displayed on screen
        self.expression = ''
        # store expressions & order
        self.store_expression = []
        self.store_order = []
        # answer of operation
        self.answer = ''
        # store answers of operation
        self.callback = []
        # float numbers of equation
        self.a = ''
        self.b = ''
        self.c = ''
        # equation solver parameter
        self.x = x
        self.y = y
        self.z = z
        self.R = S.Reals
        self.C = S.Complexes
        self.q = ''
        self.p = ''
        self.SolutionOS = ''
        self.j = ''
        self.k = ''
        self.m = ''
        self.n = ''
        self.SolutionTT = ''
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
        self.PlotFirstFunc = ''
        self.PlotAddFunc = ''
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
        self.FirstStrVar = StringVar()
        self.SecondStrVar = StringVar()
        self.LabelStrVar = StringVar()
        # ROW 0 First Canvas============================================================================================
        canvas = Canvas(self.win, relief='flat', bg='#F0F0F0', width=42)
        canvas.grid(row=0, column=0, columnspan=2, sticky=NSEW)
        canvas.rowconfigure(0, weight=1)
        canvas.columnconfigure(1, weight=1)
        # Label Text Display
        self.label = Label(canvas, **ent_prm, textvariable=self.LabelStrVar)
        self.label.grid(row=0, column=0, sticky=NSEW)
        self.label.configure(font=('Segoe UI Symbol', 32), anchor='e')
        # First Text Display, insertbackground='white'
        self.FirstTextDisplay = Entry(canvas, **ent_prm, textvariable=self.FirstStrVar, insertwidth=2)
        self.FirstTextDisplay.grid(row=0, column=1, sticky=NSEW)
        self.FirstTextDisplay.configure(font=('Segoe UI Symbol', 32), takefocus=True)
        self.FirstTextDisplay.bind("<Button-1>", self.Info)
        self.FirstTextDisplay.focus_set()
        self.IndexCursor = 0
        # ROW 1 set MathPlot LaTex Display==============================================================================
        self.Figure = Figure(figsize=(100, 5), facecolor='#212121')
        # self.CanvasFigure = FigureCanvasTkAgg(figure=self.Figure, master=self.win)
        # self.TkAgg = self.CanvasFigure.get_tk_widget()
        # self.TkAgg.grid(row=1, column=0, columnspan=2, sticky=NSEW)
        # bilko = Canvas(self.win)
        self.CanvasFigure = ScrollableTkAggX(figure=self.Figure, master=self.win)
        self.CanvasFigure.grid(row=1, column=0, columnspan=2, sticky=NSEW)
        self.CanvasFigure.rowconfigure(0, weight=1)
        self.CanvasFigure.columnconfigure(0, weight=1)
        # ROW 2 set frame showing top buttons===========================================================================
        self.top_frame = Frame(self.win, relief='flat')
        self.top_frame.grid(row=2, column=0, sticky=NSEW)
        self.top_frame.rowconfigure(0, weight=1)
        self.top_frame.columnconfigure(0, weight=1)
        self.top_frame.columnconfigure(1, weight=1)
        self.top_frame.columnconfigure(2, weight=1)
        self.top_frame.columnconfigure(3, weight=1)
        self.top_frame.columnconfigure(4, weight=1)
        # Second Text Display
        SecondTextDisplay = Entry(self.win, width=27, **ent_prm, textvariable=self.SecondStrVar, state='readonly')
        SecondTextDisplay.grid(row=2, column=1, sticky=NSEW)
        SecondTextDisplay.configure(font=('Segoe UI Symbol', 30), fg='white', readonlybackground='#212121',
                                    cursor="arrow", justify='center')
        # ROW 3 set frame showing middle buttons========================================================================
        self.middle_frame = Frame(self.win, relief='flat')
        self.middle_frame.grid(row=3, column=0, sticky=NSEW)
        self.middle_frame.rowconfigure(0, weight=1)
        self.middle_frame.rowconfigure(1, weight=1)
        self.middle_frame.rowconfigure(2, weight=1)
        self.middle_frame.columnconfigure(0, weight=1)
        self.middle_frame.columnconfigure(1, weight=1)
        self.middle_frame.columnconfigure(2, weight=1)
        self.middle_frame.columnconfigure(3, weight=1)
        self.middle_frame.columnconfigure(4, weight=1)
        self.middle_frame.columnconfigure(5, weight=1)
        # Full Text Display
        self.FullTextDisplay = ScrolledListbox(self.win, width=52, height=12, **ent_prm)
        self.FullTextDisplay.grid(row=3, column=1, rowspan=2, sticky=NSEW)
        self.FullTextDisplay.rowconfigure(0, weight=1)
        self.FullTextDisplay.columnconfigure(0, weight=1)
        # ROW 4 set frame showing bottom buttons========================================================================
        self.bottom_frame = Frame(self.win, relief='flat')
        self.bottom_frame.grid(row=4, column=0, sticky=NSEW)
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
        txta = ['Û', 'Ü', '1ST']
        self.btn_m1 = []
        for i1 in range(3):
            self.btn_m1.append(HoverButton(self.middle_frame, **btn_dif, text=txta[i1]))
            self.btn_m1[i1].grid(row=0, column=i1, sticky=NSEW)
        # Cursor Disposition
        self.btn_m1[0]['command'] = lambda: self.ChangeDirectionCursor('Left')
        self.btn_m1[1]['command'] = lambda: self.ChangeDirectionCursor('Right')

        txtb = ['ANS', 'r', 'Õ']
        self.btn_m2 = []
        i2b = 3
        for i2a in range(3):
            self.btn_m2.append(HoverButton(self.middle_frame, **btn_prm, text=txtb[i2a]))
            self.btn_m2[i2a].grid(row=0, column=i2b, sticky=NSEW)
            i2b += 1
        # Answer Stored
        self.btn_m2[0].configure(bg='#20B645', activebackground='#00751E', font=('Segoe UI Symbol', 16, 'bold'),
                                 command=lambda: self.Input(str(self.callback[-1])))
        self.btn_m2[0].ABG = '#009C27'
        self.btn_m2[0].DBG = '#20B645'
        # Clear
        self.btn_m2[1].configure(width=1, bg='firebrick2', activebackground='firebrick4', font=('Marlett', 23),
                                 command=lambda: self.Delete())
        self.btn_m2[1].ABG = 'firebrick3'
        self.btn_m2[1].DBG = 'firebrick2'
        # Remove
        self.btn_m2[2].configure(width=1, bg='Royalblue2', activebackground='Royalblue4', font=('Wingdings', 21),
                                 command=lambda: self.Remove())
        self.btn_m2[2].ABG = 'Royalblue3'
        self.btn_m2[2].DBG = 'Royalblue2'
        # ========================Trigonometry==========================================================================
        self.btn_u = []
        for i3 in range(6):
            self.btn_u.append(HoverButton(self.middle_frame, **btn_prm))
            self.btn_u[i3].grid(row=1, column=i3, sticky=NSEW)
        # ROW 2
        # ========================logarithm=============================================================================
        logarithm_pad = ['log(', 'exp(', 'LambertW(', 'integrate(', 'sqrt(', "factorial("]
        logarithm_txt = ['log', 'exp', 'W', "∫f(x)", '√n', "n!"]
        self.btn_d = []
        for i4 in range(6):
            self.btn_d.append(HoverButton(self.middle_frame, **btn_prm, text=logarithm_txt[i4]))
            self.btn_d[i4].grid(row=2, column=i4, sticky=NSEW)
            self.btn_d[i4].configure(
                command=lambda f0=logarithm_pad[i4]: [self.Input(f0), self.Input(')'),
                                                      self.ChangeDirectionCursor('Left')])

        # buttons that will be displayed on bottom frame ROW 0==========================================================
        # ========================Numbers===============================================================================
        btn = ['π', 'E', "1j", "+", '(', ')', "7", "8", "9", "-", '/100', 'x', "4", "5", "6", "*", "**2", 'y',
               "1", "2", "3", "/", "**", 'z', "0", '', '.', "=", 'e', "oo"]

        btn_txt = ['π', 'e¹', "j", "+", '(', ')', "7", "8", "9", "-", 'n%', 'x', "4", "5", "6", "⨯",
                   u'n\u00B2', 'y', "1", "2", "3", "/", "nˣ", 'z', "0", '', '.', "=", "10ˣ", "∞"]
        self.btn = []
        i5 = 0
        for j in range(5):
            for k in range(6):
                self.btn.append(HoverButton(self.bottom_frame, **btnb_prm, text=btn_txt[i5]))
                self.btn[i5].grid(row=j, column=k, sticky=NSEW)
                self.btn[i5].configure(command=lambda f1=btn[i5]: self.Input(f1))
                i5 += 1
        # (
        self.btn[4]['command'] = lambda f2=btn[4]: [self.Input(f2), self.Input(')'), self.ChangeDirectionCursor('Left')]
        # + - * / =  'slate gray'
        for l0 in range(3, 22, 6):
            self.btn[l0].configure(bg='light slate gray', activebackground='slate gray4')
            self.btn[l0].ABG = 'slate gray'
            self.btn[l0].DBG = 'light slate gray'
        # equals
        self.btn[27].configure(command=lambda: self.ShowEqual(), bg='#FF5E00', activebackground='#A74400')
        self.btn[27].ABG = '#CF4E00'
        self.btn[27].DBG = '#FF5E00'
        # seven four one zero
        for l1 in range(6, 25, 6):
            self.btn[l1].configure(bg='#212121', activebackground="#111111")
            self.btn[l1].ABG = '#161616'
            self.btn[l1].DBG = '#212121'
        # zero
        self.btn[24].grid(columnspan=2)
        self.btn[25].destroy()
        # eight five two
        for l2 in range(7, 20, 6):
            self.btn[l2].configure(bg='#212121', activebackground="#111111")
            self.btn[l2].ABG = '#161616'
            self.btn[l2].DBG = '#212121'
        # nine six three
        for l3 in range(8, 21, 6):
            self.btn[l3].configure(bg='#212121', activebackground="#111111")
            self.btn[l3].ABG = '#161616'
            self.btn[l3].DBG = '#212121'
        # x y z
        for l4 in range(11, 24, 6):
            self.btn[l4].configure(bg='#212121', activebackground="#111111")
            self.btn[l4].ABG = '#161616'
            self.btn[l4].DBG = '#212121'
        # run button switcher and display switcher mode=================================================================
        self.SwitchButtons('1st'), self.SwitchFunction('Operation', True)
        # Switch Menu In Bare Display===================================================================================
        menubare = Menu(self.win)
        File = Menu(menubare, tearoff=0)
        Mode = Menu(menubare, tearoff=0)
        menubare.add_cascade(label="File", menu=File)
        menubare.add_cascade(label="Mode", menu=Mode)
        File.add_command(label='1st Page             V', command=lambda: self.SwitchButtons("1st"))
        File.add_command(label='2nd Page           B', command=lambda: self.SwitchButtons("2nd"))
        File.add_separator()
        File.add_command(label="Close         Alt+F4", command=self.Exit)
        Mode.add_command(label="Operation",
                         command=lambda: [self.SwitchButtons('1st'), self.SwitchFunction("Operation", True)])
        Mode.add_command(label='Function',
                         command=lambda: [self.SwitchButtons('1st'), self.SwitchFunction('Function', True)])
        Mode.add_command(label="Simple Line Equation",
                         command=lambda: [self.SwitchButtons('1st'), self.SwitchFunction('Equation', True)])
        Mode.add_command(label='Line Equation Solver',
                         command=lambda: [self.SwitchButtons('1st'), self.SwitchFunction('Solve', True)])
        Mode.add_command(label='System Equation Solver',
                         command=lambda: [self.SwitchButtons('1st'), self.SwitchFunction('Matrices', True)])
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
        # Master Display ===============================================================================================
        # Window configuration
        self.win.rowconfigure(1, weight=1)
        self.win.columnconfigure(1, weight=1)

        self.win.bind_all('<Key>', self.KeyboardInput)
        self.win.iconbitmap('Alecive-Flatwoken-Apps-Libreoffice-Math-B.ico')
        self.win.configure(menu=menubare, bg='#4d4d4d')
        self.win.geometry("1100x680")
        self.win.minsize(width=1100, height=680)
        self.win.resizable(width=True, height=False)
        self.win.title("MathPy v6.1")
        self.win.mainloop()

    def iCursor(self, cursor):
        self.FirstTextDisplay.icursor(cursor)

    def Info(self, event):
        self.IndexCursor = int(self.FirstTextDisplay.index("@%d" % event.x))
        try:
            end = len(str(self.expression))
            if self.IndexCursor < end:
                self.IndexCursor, ExNbr = ControlCursor(self.IndexCursor, self.store_order)
        except Exception:
            pass
        self.iCursor(self.IndexCursor)

    def ChangeDirectionCursor(self, key):
        if key == 'Right':
            end = len(str(self.expression))
            if self.IndexCursor < end:
                try:
                    self.IndexCursor, ExNbr = ControlCursor(self.IndexCursor, self.store_order)
                    self.IndexCursor += self.store_order[ExNbr + 1]
                    self.iCursor(self.IndexCursor)
                except Exception:
                    self.IndexCursor, ExNbr = ControlCursor(self.IndexCursor, self.store_order)
                    self.iCursor(self.IndexCursor)
            else:
                pass

        elif key == 'Left':
            if self.IndexCursor > 0:
                self.IndexCursor, ExNbr = ControlCursor(self.IndexCursor, self.store_order)
                self.IndexCursor -= self.store_order[ExNbr]
                self.iCursor(self.IndexCursor)
            else:
                pass

    def SwitchButtons(self, side):
        page = side
        # buttons to switch between buttons those will be displayed on middle & top frames
        if page == '1st':
            # buttons that will be displayed on top frame ROW 0=========================================================
            for i in range(5):
                self.btn_b[i].destroy()
            big_txt = ['Operation', 'Function', "Simple\nLine\nEquation", 'Line\nEquation\nSolver',
                       'System\nEquation\nSolver']
            big_pad = ['Operation', 'Function', 'Equation', 'Solve', 'Matrices']
            self.btn_a = []
            for i in range(5):
                self.btn_a.append(HoverButton(self.top_frame, **big2_prm, text=big_txt[i]))
                self.btn_a[i].grid(row=0, column=i, sticky=NSEW)
                self.btn_a[i]["command"] = lambda f3=big_pad[i]: self.SwitchFunction(f3, True)

            # buttons that will be displayed on middle frame ROW 0======================================================
            # 2nd
            self.btn_m1[2].configure(text="1ST", command=lambda: self.SwitchButtons("2nd"),
                                     font=('Segoe UI Symbol', 16, 'bold'))
            # ROW 1
            # ========================Trigonometry======================================================================
            Trigonometry_pad = ['cos(', 'sin(', "tan(", 'cosh(', 'sinh(', "tanh("]
            Trigonometry_txt = ['cos', 'sin', "tan", 'cosh', 'sinh', "tanh"]
            for i in range(6):
                self.btn_u[i].configure(
                    text=Trigonometry_txt[i],
                    command=lambda f4=Trigonometry_pad[i]: [self.Input(f4), self.Input(')'),
                                                            self.ChangeDirectionCursor('Left')])

            self.btn_d[3].configure(
                text='∫f(x)',
                command=lambda: [self.Input('integrate('), self.Input(')'), self.ChangeDirectionCursor('Left')])

            self.btn_d[2].configure(
                text='W₀',
                command=lambda: [self.Input('LambertW('), self.Input(')'), self.ChangeDirectionCursor('Left')])

            self.btn[28].configure(text='10ˣ', command=lambda: self.Input('e+'))

            if self.mode == 'Operation' or self.mode == 'Function' or self.mode == 'Equation' or self.mode == 'Solve' \
                    or self.mode == 'Matrices':
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
                self.btn_b[i].grid(row=0, column=i, sticky=NSEW)
                self.btn_b[i]["command"] = lambda f5=big_pad[i]: self.SwitchFunction(f5, True)

            # buttons that will be displayed on middle frame ROW 0======================================================
            # 1st
            self.btn_m1[2].configure(text="2ND", command=lambda: self.SwitchButtons("1st"),
                                     font=('Segoe UI Symbol', 16, 'bold'))
            # ROW 1
            # ========================Trigonometry======================================================================
            Trigonometry_pad = ['acos(', 'asin(', "atan(", 'acosh(', 'asinh(', "atanh("]
            Trigonometry_txt = ['acos', 'asin', "atan", 'acosh', 'asinh', "atanh"]
            for i in range(6):
                self.btn_u[i].configure(
                    text=Trigonometry_txt[i],
                    command=lambda f6=Trigonometry_pad[i]: [self.Input(f6), self.Input(')'),
                                                            self.ChangeDirectionCursor('Left')])

            self.btn_d[3].configure(
                text='d/dx',
                command=lambda: [self.Input('diff('), self.Input(')'), self.ChangeDirectionCursor('Left')])

            self.btn_d[2].configure(
                text='W₋₁',
                command=lambda: [self.Input('LambertW('), self.Input(',-1)'), self.ChangeDirectionCursor('Left')])

            self.btn[28].configure(text='10¯ˣ', command=lambda: self.Input('e-'))

            if self.mode == 'Plot' or self.mode == 'Plot Prm' or self.mode == 'P3DPL' or self.mode == "Plot3D" or \
                    self.mode == 'P3DPS':
                self.SwitchFunction(self.mode, False)

    def SwitchFunction(self, passmode, do_it):
        self.mode = passmode
        self.switched = do_it
        if self.switched:
            if self.mode == 'Operation' or self.mode == 'Solve' or self.mode == 'Matrices':
                self.mathext = ["MathPy 6.1.0 Created by Achraf"]
                self.SwitchWidget('TkAgg')
            else:
                self.SwitchWidget('listbox')
                self.FullTextDisplay.delete(0, END)

        if self.mode == 'Operation':
            if self.switched:
                self.AggSwitchDraw(f'Mode Operation : ')
                self.btn[11].config(state=NORMAL)
                self.btn[17]['state'] = ['disabled']
                self.btn[23].config(state=DISABLED)
                self.btn[2].config(state=NORMAL)

            self.btn_a[0].config(bg='#80000B', relief='sunken')
            self.btn_a[0].DBG = '#80000B'
            for i in range(1, 5):
                self.btn_a[i].config(bg='#212121', relief='raised')
                self.btn_a[i].DBG = '#212121'

        elif self.mode == 'Function':
            if self.switched:
                self.FullTextDisplay.insert(END, 'Mode Function : f(x)')
                self.btn[11]['state'] = ['normal']
                self.btn[2]['state'] = ['disabled']
                self.btn[17]['state'] = ['disabled']
                self.btn[23].config(state=DISABLED)

            self.btn_a[0].config(bg='#212121', relief='raised')
            self.btn_a[0].DBG = '#212121'
            self.btn_a[1].config(bg='#80000B', relief='sunken')
            self.btn_a[1].DBG = '#80000B'
            for i in range(2, 5):
                self.btn_a[i].config(bg='#212121', relief='raised')
                self.btn_a[i].DBG = '#212121'

        elif self.mode == 'Equation':
            if self.switched:
                self.FullTextDisplay.insert(END, 'Mode Simple Line Equation : ax² + bx + c = 0')
                self.btn[11].config(state=DISABLED)
                self.btn[17].config(state=DISABLED)
                self.btn[23].config(state=DISABLED)
                self.btn[2].config(state=DISABLED)

            for i in range(2):
                self.btn_a[i].config(bg='#212121', relief='raised')
                self.btn_a[i].DBG = '#212121'
            self.btn_a[2].config(bg='#80000B', relief='sunken')
            self.btn_a[2].DBG = '#80000B'
            for i in range(3, 5):
                self.btn_a[i].config(bg='#212121', relief='raised')
                self.btn_a[i].DBG = '#212121'

        elif self.mode == 'Solve':
            if self.switched:
                self.AggSwitchDraw('Mode Line Equation Solver : One {eq} : [x] | Constants : (y,z)')
                self.btn[11].config(state=NORMAL)
                self.btn[17].config(state=NORMAL)
                self.btn[23].config(state=NORMAL)
                self.btn[2].config(state=DISABLED)

            for i in range(3):
                self.btn_a[i].config(bg='#212121', relief='raised')
                self.btn_a[i].DBG = '#212121'
            self.btn_a[3].config(bg='#80000B', relief='sunken')
            self.btn_a[3].DBG = '#80000B'
            self.btn_a[4].config(bg='#212121', relief='raised')
            self.btn_a[4].DBG = '#212121'

        elif self.mode == 'Matrices':
            if self.switched:
                self.AggSwitchDraw('Mode System Equation Solver :')
                self.btn[11].config(state=NORMAL)
                self.btn[17].config(state=NORMAL)
                self.btn[23].config(state=NORMAL)
                self.btn[2].config(state=DISABLED)

            for i in range(4):
                self.btn_a[i].config(bg='#212121', relief='raised')
                self.btn_a[i].DBG = '#212121'
            self.btn_a[4].config(bg='#80000B', relief='sunken')
            self.btn_a[4].DBG = '#80000B'

        elif self.mode == 'Plot':
            if self.switched:
                self.FullTextDisplay.insert(END, 'Mode Plot : f(x)')
                self.btn[11]['state'] = ['normal']
                self.btn[17]['state'] = ['disabled']
                self.btn[23].config(state=DISABLED)
                self.btn[2]['state'] = ['disabled']

            self.btn_b[0].config(bg='#80000B', relief='sunken')
            self.btn_b[0].DBG = '#80000B'
            for i in range(1, 5):
                self.btn_b[i].config(bg='#212121', relief='raised')
                self.btn_b[i].DBG = '#212121'

        elif self.mode == 'Plot Prm':
            if self.switched:
                self.FullTextDisplay.insert(END, 'Mode Plot Parametric : f(x)₁ | f(x)₂ ')
                self.btn[11]['state'] = ['normal']
                self.btn[17]['state'] = ['disabled']
                self.btn[23].config(state=DISABLED)
                self.btn[2]['state'] = ['disabled']

            self.btn_b[0].config(bg='#212121', relief='raised')
            self.btn_b[0].DBG = '#212121'
            self.btn_b[1].config(bg='#80000B', relief='sunken')
            self.btn_b[1].DBG = '#80000B'
            for i in range(2, 5):
                self.btn_b[i].config(bg='#212121', relief='raised')
                self.btn_b[i].DBG = '#212121'

        elif self.mode == 'P3DPL':
            if self.switched:
                self.FullTextDisplay.insert(END, 'Mode Plot3D Parametric Line : f(x)₁ | f(x)₂ ')
                self.btn[11]['state'] = ['normal']
                self.btn[17]['state'] = ['disabled']
                self.btn[23].config(state=DISABLED)
                self.btn[2]['state'] = ['disabled']

            for i in range(2):
                self.btn_b[i].config(bg='#212121', relief='raised')
                self.btn_b[i].DBG = '#212121'
            self.btn_b[2].config(bg='#80000B', relief='sunken')
            self.btn_b[2].DBG = '#80000B'
            for i in range(3, 5):
                self.btn_b[i].config(bg='#212121', relief='raised')
                self.btn_b[i].DBG = '#212121'

        elif self.mode == 'Plot3D':
            if self.switched:
                self.FullTextDisplay.insert(END, 'Mode Plot3D : f(x,y)')
                self.btn[11]['state'] = ['normal']
                self.btn[17]['state'] = ['normal']
                self.btn[23].config(state=DISABLED)
                self.btn[2]['state'] = ['disabled']

            for i in range(3):
                self.btn_b[i].config(bg='#212121', relief='raised')
                self.btn_b[i].DBG = '#212121'
            self.btn_b[3].config(bg='#80000B', relief='sunken')
            self.btn_b[3].DBG = '#80000B'
            self.btn_b[4].config(bg='#212121', relief='raised')
            self.btn_b[4].DBG = '#212121'

        elif self.mode == 'P3DPS':
            if self.switched:
                self.FullTextDisplay.insert(END, 'Mode Plot3D Parametric Surface : f(x,y)₁ | f(x,y)₂ ')
                self.btn[11]['state'] = ['normal']
                self.btn[17]['state'] = ['normal']
                self.btn[23].config(state=DISABLED)
                self.btn[2]['state'] = ['disabled']

            for i in range(4):
                self.btn_b[i].config(bg='#212121', relief='raised')
                self.btn_b[i].DBG = '#212121'
            self.btn_b[4].config(bg='#80000B', relief='sunken')
            self.btn_b[4].DBG = '#80000B'

        if self.switched:
            self.Delete()

    def SwitchWidget(self, widget):
        figure = widget
        if figure == 'listbox':
            self.TkAggXY.Destroying()
            self.FullTextDisplay = ScrolledListbox(self.win, width=52, height=12, **ent_prm)
            self.FullTextDisplay.grid(row=3, column=1, rowspan=2, sticky=NSEW)
            self.FullTextDisplay.rowconfigure(0, weight=1)
            self.FullTextDisplay.columnconfigure(0, weight=1)

        elif figure == 'TkAgg':
            self.FullTextDisplay.destroy()
            self.fig = Figure(figsize=(100, 1), facecolor='#F0F0F0')
            self.axes = self.fig.subplots(ncols=1, nrows=0)
            self.TkAggXY = ScrollableTkAggXY(figure=self.fig, master=self.win)
            self.TkAggXY.grid(row=3, column=1, rowspan=2, sticky=NSEW)
            self.TkAggXY.rowconfigure(0, weight=1)
            self.TkAggXY.columnconfigure(0, weight=1)

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
        self.SolutionOS = ''
        self.SolutionTT = ''
        self.xexp = ''
        self.yexp = ''
        self.zexp = ''
        self.fctx = ''
        self.fctx1 = ''
        self.fctx2 = ''
        self.fctxy = ''
        self.fctxy1 = ''
        self.fctxy2 = ''
        self.PlotAddFunc = ''
        self.PlotFirstFunc = ''
        self.store_expression = []
        self.store_order = []
        self.expression = ''
        self.FirstStrVar.set('')
        self.SecondStrVar.set('')
        self.iCursor(0)
        self.IndexCursor = int(self.FirstTextDisplay.index(INSERT))
        self.Figure.clear()
        self.CanvasFigure.draw()

        if self.mode == 'Operation':
            self.VariableTXT('op >')
            self.DrawTexTk('op >')

        elif self.mode == 'Function':
            self.VariableTXT(f'From :')
            self.DrawTexTk('From : A --> To : B | f(x) = Function')

        elif self.mode == 'Equation':
            self.VariableTXT(f'a =')
            self.DrawTexTk('ax² + bx + c = 0')

        elif self.mode == 'Solve':
            self.VariableTXT(f'eq >')
            self.DrawTexTk('eq >')

        elif self.mode == 'Matrices':
            self.VariableTXT('eq₁ >')
            self.DrawTexTk('eq₁ >')

        elif self.mode == 'Plot':
            self.VariableTXT('f(x) =')
            self.DrawTexTk('f(x) = ')

        elif self.mode == "Plot Prm" or self.mode == "P3DPL":
            self.VariableTXT('f(x)₁ =')
            self.DrawTexTk('f(x)₁ = ')

        elif self.mode == 'Plot3D':
            self.VariableTXT('f(x,y) =')
            self.DrawTexTk('f(x,y) = ')

        elif self.mode == "P3DPS":
            self.VariableTXT('f(x,y)₁ =')
            self.DrawTexTk('f(x,y)₁ = ')

        self.equal = False
        self.clear = False
        self.full = None
        self.exist = None

    def Remove(self):
        if self.clear:
            self.Delete()

        try:
            self.expression, self.IndexCursor = RemoveFromString(self.expression, self.IndexCursor, self.store_order,
                                                                 self.store_expression)
        except IndexError:
            pass

        self.ShowInput()

    def KeyboardInput(self, keyword):
        put = keyword.keysym.lower()
        try:
            if self.mode == 'Operation':
                if keyword.keysym == 'Return' or put == 'equal' or keyword.keysym == '=':
                    self.ShowEqual()
                if self.clear:
                    if keyword.keysym == 'Return' or put == 'equal' or keyword.keysym == '=':
                        pass
                    else:
                        self.Delete()
            else:
                if self.clear:
                    self.Delete()
                else:
                    if keyword.keysym == 'Return' or put == 'equal' or keyword.keysym == '=':
                        self.ShowEqual()

            if keyword.keysym == 'BackSpace':
                self.Remove()

            elif keyword.keysym == 'Delete':
                self.Delete()

            elif keyword.keysym == 'E':
                self.Input('E')

            elif keyword.keysym == 'e':
                self.Input('exp('), self.Input(')'), self.ChangeDirectionCursor('Left')

            elif put == 'v':
                self.SwitchButtons("1st"), self.ShowInput()

            elif put == 'b':
                self.SwitchButtons("2nd"), self.ShowInput()

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
                self.Input('('), self.Input(')'), self.ChangeDirectionCursor('Left')

            elif put == 'parenright':
                self.Input(')')

            elif put == 'backslash' or put == 'bar':
                self.Input('sqrt('), self.Input(')'), self.ChangeDirectionCursor('Left')

            elif keyword.keysym == 's':
                self.Input('sin('), self.Input(')'), self.ChangeDirectionCursor('Left')

            elif keyword.keysym == 'c':
                self.Input('cos('), self.Input(')'), self.ChangeDirectionCursor('Left')

            elif keyword.keysym == 't':
                self.Input('tan('), self.Input(')'), self.ChangeDirectionCursor('Left')

            elif keyword.keysym == 'S':
                self.Input('sinh('), self.Input(')'), self.ChangeDirectionCursor('Left')

            elif keyword.keysym == 'C':
                self.Input('cosh('), self.Input(')'), self.ChangeDirectionCursor('Left')

            elif keyword.keysym == 'T':
                self.Input('tanh('), self.Input(')'), self.ChangeDirectionCursor('Left')

            elif keyword.keysym == 'l':
                self.Input('log('), self.Input(')'), self.ChangeDirectionCursor('Left')

            elif keyword.keysym == 'I':
                self.Input('oo')

            elif keyword.keysym == 'i':
                self.Input('integrate('), self.Input(')'), self.ChangeDirectionCursor('Left')

            elif put == 'd':
                self.Input('diff('), self.Input(')'), self.ChangeDirectionCursor('Left')

            elif keyword.keysym == 'w':
                self.Input('LambertW('), self.Input(')'), self.ChangeDirectionCursor('Left')

            elif keyword.keysym == 'W':
                self.Input('LambertW('), self.Input(',-1)'), self.ChangeDirectionCursor('Left')

            elif put == 'j':
                self.Input('1j')

            elif put == 'exclam' or put == 'f':
                self.Input('factorial('), self.Input(')'), self.ChangeDirectionCursor('Left')

            elif put == 'p':
                self.Input('π')

            elif put == 'a' or put == 'x' or put == 'y' or put == 'z' or put == '0' or put == '1' or put == '2' or \
                    put == '3' or put == '4' or put == '5' or put == '6' or put == '7' or put == '8' or put == '9':
                self.Input(put)

            elif keyword.keysym == 'Right':
                self.ChangeDirectionCursor('Right')

            elif keyword.keysym == 'Left':
                self.ChangeDirectionCursor('Left')

            else:
                if keyword.keysym == 'Return' or put == 'equal':
                    pass
                else:
                    self.ShowInput()

        except IndexError:
            self.SecondStrVar.set('IndexError')

    def Input(self, keyword):
        if self.clear:
            self.Delete()

        self.expression, self.IndexCursor = InsertIntoString(self.expression, keyword, self.IndexCursor,
                                                             self.store_order, self.store_expression)

        self.ShowInput()

    @staticmethod
    def DrawAfter(character):
        try:
            simplify = sympify(character)
            LaTex = latex(simplify)
            return r"$%s$" % LaTex
        except None:
            pass
        except Exception:
            pass

    @staticmethod
    def DrawBefore(character):
        try:
            pik = str(character).replace('integrate', 'Integral').replace('diff', 'Derivative')
            simplify = sympify(pik, rational=True, evaluate=False)
            LaTex = latex(simplify)
            return r"$%s$" % LaTex
        except None:
            pass
        except Exception:
            pass

    def DrawTexTk(self, la_text):
        mpl_white_rvb = (255. / 255., 255. / 255., 255. / 255.)
        try:
            self.Figure.clear()
            self.Figure.text(0, 0.4, la_text, color=mpl_white_rvb, fontsize=30)
            self.CanvasFigure.draw()
        except Exception:
            pass

    def VariableTXT(self, label_var):
        self.LabelStrVar.set(label_var)
        self.FirstStrVar.set(self.expression)

    def ShowInput(self):
        try:
            if self.mode == 'Operation':
                self.FirstStrVar.set(self.expression)
                self.DrawTexTk(f'op > {self.DrawBefore(self.expression)} = {self.DrawAfter(eval(self.expression))}')

            elif self.mode == 'Function':
                if self.full is None:
                    self.VariableTXT('From :')
                    self.DrawTexTk(
                        f'From : {self.DrawAfter(self.expression)} --> To : B | f(x) = Function')

                elif not self.full:
                    self.VariableTXT('To :')
                    self.DrawTexTk(
                        f'From : {self.DrawAfter(self.v)} --> To : '
                        f'{self.DrawAfter(self.expression)} | f(x) = Function')

                elif self.full:
                    self.VariableTXT('f(x) =')
                    self.DrawTexTk(
                        f'From : {self.DrawAfter(self.v)} --> To : {self.DrawAfter(self.w)} | '
                        f'f(x) = {self.DrawAfter(self.expression)}')

            elif self.mode == 'Equation':
                if self.full is None:
                    self.VariableTXT('a =')
                    self.DrawTexTk(
                        f'{self.DrawAfter(self.expression)}x² + bx + c = 0')

                elif not self.full:
                    self.VariableTXT('b =')
                    self.DrawTexTk(
                        f'{self.DrawAfter(self.a)}x² + ({self.DrawAfter(self.expression)})x + c = 0')

                elif self.full:
                    self.VariableTXT('c =')
                    self.DrawTexTk(
                        f'{self.DrawAfter(self.a)}x² + ({self.DrawAfter(self.b)})x + '
                        f'({self.DrawAfter(self.expression)}) = 0')

            elif self.mode == 'Solve':
                if self.full is None:
                    self.VariableTXT('eq >')
                    self.DrawTexTk(f'eq > {self.DrawAfter(self.expression)}')
                elif self.full:
                    self.VariableTXT(f'eq > {self.q} =')
                    self.DrawTexTk(
                        f'eq > {self.DrawAfter(self.q)} = '
                        f'{self.DrawAfter(self.expression)}')

            elif self.mode == 'Matrices':
                if self.full is None:
                    self.VariableTXT(f'eq₁ >')
                    self.DrawTexTk(f'eq₁ > {self.DrawAfter(self.expression)}')
                elif not self.full:
                    self.VariableTXT(f'eq₁ > {self.q} = ')
                    self.DrawTexTk(f'eq₁ > {self.DrawAfter(self.q)} = {self.DrawAfter(self.expression)}')

                elif self.full:
                    if self.clear is None:
                        self.VariableTXT(f'eq₂ >')
                        self.DrawTexTk(f'eq₂ > {self.DrawAfter(self.expression)}')
                    elif not self.clear and self.equal is None:
                        self.VariableTXT(f'eq₂ > {self.j} =')
                        self.DrawTexTk(f'eq₂ > {self.DrawAfter(self.j)} = {self.DrawAfter(self.expression)}')

                    elif not self.clear and not self.equal:
                        self.VariableTXT(f'eq₃ >')
                        self.DrawTexTk(f'eq₃ > {self.DrawAfter(self.expression)}')
                    elif not self.clear and self.equal:
                        self.VariableTXT(f'eq₃ > {self.m} =')
                        self.DrawTexTk(f'eq₃ > {self.DrawAfter(self.m)} = {self.DrawAfter(self.expression)}')

            elif self.mode == 'Plot':
                self.VariableTXT(f'f(x) =')
                self.DrawTexTk(f'f(x) = {self.DrawAfter(self.expression)}')

            elif self.mode == "Plot Prm" or self.mode == "P3DPL":
                if self.full is None:
                    self.VariableTXT(f'f(x)₁ =')
                    self.DrawTexTk(f'f(x)₁ = {self.DrawAfter(self.expression)}')

                elif self.full:
                    self.VariableTXT(f'f(x)₂ =')
                    self.DrawTexTk(f'f(x)₁ = {self.DrawAfter(self.fctx1)} | '
                                   f'f(x)₂ = {self.DrawAfter(self.expression)}')

            elif self.mode == "Plot3D":
                self.VariableTXT(f'f(x,y) =')
                self.DrawTexTk(f'f(x,y) = {self.DrawAfter(self.expression)}')

            elif self.mode == "P3DPS":
                if self.full is None:
                    self.VariableTXT(f'f(x,y)₁ =')
                    self.DrawTexTk(f'f(x,y)₁ = {self.DrawAfter(self.expression)}')

                elif self.full:
                    self.VariableTXT(f'f(x,y)₂ =')
                    self.DrawTexTk(f'f(x,y)₁ = {self.DrawAfter(self.fctxy1)} | '
                                   f'f(x,y)₂ = {self.DrawAfter(self.expression)}')

            self.SecondStrVar.set('')
        except Exception:
            pass

        self.iCursor(self.IndexCursor)

    def ResetIndexCursor(self):
        if self.mode == 'Operation':
            pass
        else:
            self.expression = ''
            self.store_expression = []
            self.store_order = []
            self.IndexCursor = 0

    def AggSwitchDraw(self, character):
        self.fig.clear()
        self.mathext.append(character)
        self.axes = self.fig.subplots(ncols=1, nrows=2)
        self.AggDrawMultiLaTex()

    def MultiLaTexDraw(self, character):
        self.fig.clear()
        self.mathext.append(character)
        self.n_lines = len(self.mathext)
        self.axes = self.fig.subplots(ncols=1, nrows=self.n_lines)
        oldSize = self.fig.get_size_inches()
        self.fig.set_size_inches([0.9 + s for s in oldSize])
        self.AggDrawMultiLaTex()

    def AggDrawMultiLaTex(self):
        i_line = 0
        for ax in self.axes.flatten():
            demo = self.mathext[i_line]
            ax.text(0, 0.5, demo, fontsize=20)
            ax.axis('off')
            ax.set_xticklabels("", visible=False)
            ax.set_yticklabels("", visible=False)
            i_line += 1
        self.fig.tight_layout()  # pad=-1, h_pad=-3
        self.TkAggXY.Drawing()

    def VariableEQL(self, label_var, first_var):
        self.LabelStrVar.set(label_var)
        self.FirstStrVar.set(first_var)

    def ShowEqual(self):
        try:
            if self.mode == 'Operation':
                if not self.equal:
                    self.answer = sympify(eval(self.expression))
                    intro = len(str(self.answer))
                    if intro <= 10:
                        self.VariableEQL(f'op > {self.expression} =', f'{self.answer}')
                        self.DrawTexTk(f'op > {self.DrawBefore(self.expression)} = {self.DrawAfter(self.answer)}')
                        self.MultiLaTexDraw(f'op > {self.DrawBefore(self.expression)} = {self.DrawAfter(self.answer)}')
                        self.clear = True
                        self.equal = True
                    else:
                        self.answer = sympify(str(self.answer)).evalf(10)
                        self.VariableEQL(f'op > {self.expression} =', f'{self.answer}')
                        self.DrawTexTk(f'op > {self.DrawBefore(self.expression)} = {self.DrawAfter(self.answer)}')
                        self.MultiLaTexDraw(f'op > {self.DrawBefore(self.expression)} = {self.DrawAfter(self.answer)}')
                        self.clear = True
                        self.equal = True

                elif self.equal:
                    self.answer, self.expression = FullReBuild(self.store_expression, self.callback)
                    self.answer = sympify(self.answer)
                    intro = len(str(self.answer))
                    if intro <= 10:
                        self.VariableEQL(f'op > {self.expression} =', f'{self.answer}')
                        self.DrawTexTk(f'op > {self.DrawBefore(self.expression)} = {self.DrawAfter(self.answer)}')
                        self.MultiLaTexDraw(f'op > {self.DrawBefore(self.expression)} = {self.DrawAfter(self.answer)}')
                    else:
                        self.answer = sympify(str(self.answer)).evalf(10)
                        self.VariableEQL(f'op > {self.expression} =', f'{self.answer}')
                        self.DrawTexTk(f'op > {self.DrawBefore(self.expression)} = {self.DrawAfter(self.answer)}')
                        self.MultiLaTexDraw(f'op > {self.DrawBefore(self.expression)} = {self.DrawAfter(self.answer)}')
                self.callback.append(str(self.answer))

            elif self.mode == 'Function':
                if self.full is None:
                    self.v = int(eval(self.expression))
                    self.FullTextDisplay.insert(END, f'from : {self.expression}')
                    self.VariableEQL(f'To :', "")
                    self.full = False

                elif not self.full:
                    self.w = int(eval(self.expression)) + 1
                    self.FullTextDisplay.insert(END, f'To : {self.expression}')
                    self.VariableEQL(f'f(x) =', '')
                    self.full = True

                elif self.full:
                    if not self.equal:
                        self.fctx = str(eval(self.expression))
                        self.FullTextDisplay.insert(END, f'f(x) = {sympify(self.fctx)}')
                        for x in range(self.v, self.w):
                            sup = sympify(eval(self.fctx)).evalf(3)
                            self.FullTextDisplay.insert(END, f'f({x}) = {sup}')
                        self.PlotFirstFunc = plot(sympify(self.fctx), (self.x, self.v, int(self.w) - 1))
                        self.VariableEQL(f'f(x) =', '')
                        self.equal = True

                    elif self.equal:
                        self.fctx = str(eval(self.expression))
                        self.FullTextDisplay.insert(END, f'f(x) = {self.fctx}')
                        for x in range(self.v, self.w):
                            sup = sympify(eval(self.fctx)).evalf(3)
                            self.FullTextDisplay.insert(END, f'f({x}) = {sup}')
                        self.PlotAddFunc = plot(sympify(self.fctx), (self.x, self.v, int(self.w) - 1), show=False)
                        TwoPlotColor(self.PlotFirstFunc, self.PlotAddFunc)
                        self.VariableEQL(f'f(x) =', '')

            elif self.mode == 'Equation':
                if self.full is None:
                    self.a = self.expression
                    self.VariableEQL(f'b =', '')
                    self.full = False

                elif not self.full:
                    self.b = self.expression
                    self.VariableEQL(f'c =', '')
                    self.full = True

                elif self.full:
                    self.c = self.expression
                    self.VariableEQL(f'a = {self.a} | b = {self.b} | c = {self.c}', '')
                    self.DrawTexTk(f'{self.DrawAfter(self.a)}x² + ({self.DrawAfter(self.b)})x + '
                                   f'({self.DrawAfter(self.c)}) = 0')
                    qe = int(len(EQT(self.a, self.b, self.c)))
                    for eq in range(qe):
                        self.FullTextDisplay.insert(END, EQT(self.a, self.b, self.c)[eq])

                    self.clear = True
                    self.full = None

            elif self.mode == 'Solve':
                if self.full is None:
                    self.q = str(eval(self.expression))
                    self.VariableEQL(f'eq > {self.q} =', '')
                    self.DrawTexTk(f'eq > {self.DrawAfter(self.q)} = ')
                    self.full = True

                elif self.full:
                    self.p = str(eval(self.expression))
                    self.VariableEQL(f'eq > {self.q} = {self.p}', '')
                    try:
                        self.SolutionOS = solvify(Eq(sympify(self.q), sympify(self.p)), self.x, self.C)
                        if self.SolutionOS is None:
                            self.SolutionOS = solvify(Eq(sympify(self.q), sympify(self.p)), self.x, self.R)
                    except Exception:
                        try:
                            self.SolutionOS = solve(Eq(sympify(self.q), sympify(self.p)), self.x)
                        except Exception:
                            self.DrawTexTk('Cannot Solve This Equation')
                    self.DrawTexTk(f'eq > {self.DrawAfter(self.SolutionOS)}')
                    self.MultiLaTexDraw(f'eq > {self.DrawBefore(self.q)} = {self.DrawBefore(self.p)}')
                    self.MultiLaTexDraw(f'{self.DrawAfter(self.SolutionOS)}')
                    for sl in range(len(self.SolutionOS)):
                        self.MultiLaTexDraw(f'> x{self.nb[int(sl) + 1]} = {self.DrawAfter(self.SolutionOS[sl])}')

                    self.clear = True
                    self.full = None

            elif self.mode == 'Matrices':
                if self.full is None:
                    self.q = str(sympify(self.expression))
                    self.VariableEQL(f'eq₁ > {self.q} =', '')
                    self.full = False

                elif not self.full:
                    self.p = str(sympify(self.expression))
                    self.VariableEQL('eq₂ >', '')
                    self.DrawTexTk('eq₂ > ')
                    self.MultiLaTexDraw('New System :')
                    self.MultiLaTexDraw(f' eq₁ | {self.DrawBefore(self.q)} = {self.DrawBefore(self.p)}')
                    self.full = True
                    self.clear = None

                elif self.full:
                    if self.clear is None:
                        self.j = str(sympify(self.expression))
                        self.VariableEQL(f'eq₂ > {self.j} =', '')
                        self.equal = None
                        self.clear = False

                    elif not self.clear:
                        if self.equal is None:
                            self.k = str(sympify(self.expression))
                            self.MultiLaTexDraw(f' eq₂ | {self.DrawBefore(self.j)} = {self.DrawBefore(self.k)}')
                            try:
                                self.SolutionTT = linsolve(
                                    [Eq(sympify(self.q), sympify(self.p)), Eq(sympify(self.j), sympify(self.k))],
                                    [self.x, self.y])
                            except Exception:
                                self.SolutionTT = nonlinsolve(
                                    [Eq(sympify(self.q), sympify(self.p)), Eq(sympify(self.j), sympify(self.k))],
                                    [self.x, self.y])

                            self.SolutionTT = str(self.SolutionTT)
                            self.w = int(len(self.SolutionTT))
                            self.v = 0
                            while self.v < self.w:
                                self.exist = False
                                if self.SolutionTT[self.v] == 'z' or self.SolutionTT == 'EmptySet':
                                    self.VariableEQL('eq₃ >', '')
                                    self.DrawTexTk('eq₃ > ')
                                    self.equal = False
                                    self.exist = True
                                    break
                                self.v += 1

                            if not self.exist:
                                self.MultiLaTexDraw('System of Two Equations : {eq₁,eq₂}_[x,y]')
                                self.DrawTexTk(self.DrawAfter(self.SolutionTT))
                                self.MultiLaTexDraw(self.DrawAfter(self.SolutionTT))
                                self.SolutionTT = str(self.SolutionTT[11:-2])

                                self.w = int(len(self.SolutionTT))
                                self.v = 0
                                while self.v < self.w:
                                    self.xexp = str(self.xexp) + str(self.SolutionTT[self.v])
                                    self.v += 1
                                    if self.SolutionTT[self.v] == ',':
                                        while self.v < self.w:
                                            self.yexp = str(self.yexp) + str(self.SolutionTT[self.v])
                                            self.v += 1

                                self.yexp = str(self.yexp).replace(', ', '')
                                self.VariableEQL(f'x = {self.xexp} | y = {self.yexp}', '')
                                self.MultiLaTexDraw(f'> x = {self.DrawAfter(self.xexp)}')
                                self.MultiLaTexDraw(f'> y = {self.DrawAfter(self.yexp)}')
                                self.clear = True
                                self.full = None

                        elif not self.equal:
                            self.m = str(sympify(self.expression))
                            self.VariableEQL(f'eq₃ > {self.m} =', '')
                            self.equal = True

                        elif self.equal:
                            self.n = str(sympify(self.expression))
                            self.expression = ''
                            self.MultiLaTexDraw(f' eq₃ | {self.DrawBefore(self.m)} = {self.DrawBefore(self.n)}')
                            try:
                                self.SolutionTT = linsolve(
                                    [Eq(sympify(self.q), sympify(self.p)), Eq(sympify(self.j), sympify(self.k)),
                                     Eq(sympify(self.m), sympify(self.n))], [self.x, self.y, self.z])
                            except Exception:
                                self.SolutionTT = nonlinsolve(
                                    [Eq(sympify(self.q), sympify(self.p)), Eq(sympify(self.j), sympify(self.k)),
                                     Eq(sympify(self.m), sympify(self.n))], [self.x, self.y, self.z])

                            self.SolutionTT = str(self.SolutionTT)

                            if self.SolutionTT == 'EmptySet':
                                self.VariableEQL(self.SolutionTT, '')
                                self.DrawTexTk(self.DrawAfter(self.SolutionTT))
                                self.MultiLaTexDraw(self.DrawAfter(self.SolutionTT))

                            else:
                                self.MultiLaTexDraw('System of Three Equations : {eq₁,eq₂,eq₃}_[x,y,z]')
                                self.DrawTexTk(self.DrawAfter(self.SolutionTT))
                                self.MultiLaTexDraw(self.DrawAfter(self.SolutionTT))
                                self.SolutionTT = str(self.SolutionTT[11:-2])

                                self.w = int(len(self.SolutionTT))
                                self.v = 0
                                while self.v < self.w:
                                    self.xexp = str(self.xexp) + str(self.SolutionTT[self.v])
                                    self.v += 1
                                    if self.SolutionTT[self.v] == ',':
                                        while self.v < self.w:
                                            self.yexp = str(self.yexp) + str(self.SolutionTT[self.v])
                                            self.v += 1
                                            if self.SolutionTT[self.v] == ',':
                                                while self.v < self.w:
                                                    self.zexp = str(self.zexp) + str(self.SolutionTT[self.v])
                                                    self.v += 1

                                self.yexp = str(self.yexp).replace(', ', '')
                                self.zexp = str(self.zexp).replace(', ', '')
                                self.VariableEQL(f'x = {self.xexp} | y = {self.yexp} | z = {self.zexp}', '')
                                self.MultiLaTexDraw(f'> x = {self.DrawAfter(self.xexp)}')
                                self.MultiLaTexDraw(f'> y = {self.DrawAfter(self.yexp)}')
                                self.MultiLaTexDraw(f'> z = {self.DrawAfter(self.zexp)}')
                            self.clear = True
                            self.full = None

            elif self.mode == 'Plot':
                if self.full is None:
                    self.fctx = str(eval(self.expression))
                    self.FullTextDisplay.insert(END, f'f(x) = {self.fctx}')
                    self.PlotFirstFunc = plot(sympify(self.fctx), ylim=(-10, 10), xlim=(-10, 10))
                    self.VariableEQL(f'f(x) =', '')
                    self.full = True

                elif self.full:
                    self.fctx = str(eval(self.expression))
                    self.FullTextDisplay.insert(END, f'f(x) = {self.fctx}')
                    self.PlotAddFunc = plot(sympify(self.fctx), ylim=(-10, 10), xlim=(-10, 10), show=False)
                    TwoPlotColor(self.PlotFirstFunc, self.PlotAddFunc)
                    self.VariableEQL(f'f(x) =', '')

            elif self.mode == 'Plot Prm':
                if self.full is None:
                    self.fctx1 = str(eval(self.expression))
                    self.FullTextDisplay.insert(END, f'f(x)₁ = {self.fctx1}')
                    self.DrawTexTk(
                        f'f(x)₁ = {self.DrawAfter(self.fctx1)} | f(x)₂ =')
                    self.VariableEQL(f'f(x)₂ =', '')
                    self.full = True

                elif self.full:
                    self.fctx2 = str(eval(self.expression))
                    self.FullTextDisplay.insert(END, f'f(x)₂ = {self.fctx2}')
                    self.DrawTexTk(
                        f'f(x)₁ = {self.DrawAfter(self.fctx1)} | f(x)₂ = '
                        f'{self.DrawAfter(self.fctx2)}')
                    if not self.equal:
                        self.PlotFirstFunc = plot_parametric(sympify(self.fctx1), sympify(self.fctx2), ylim=(-10, 10),
                                                             xlim=(-10, 10))
                        self.VariableEQL(f'f(x)₁ =', '')
                        self.equal = True
                        self.full = None

                    elif self.equal:
                        self.PlotAddFunc = plot_parametric(sympify(self.fctx1), sympify(self.fctx2), ylim=(-10, 10),
                                                           xlim=(-10, 10), show=False)
                        TwoPlotColor(self.PlotFirstFunc, self.PlotAddFunc)
                        self.VariableEQL(f'f(x)₁ =', '')
                        self.full = None

            elif self.mode == 'P3DPL':
                if self.full is None:
                    self.fctx1 = str(eval(self.expression))
                    self.FullTextDisplay.insert(END, f'f(x)₁ = {self.fctx1}')
                    self.DrawTexTk(
                        f'f(x)₁ = {self.DrawAfter(self.fctx1)} | f(x)₂ = ')
                    self.VariableEQL(f'f(x)₂ =', '')
                    self.full = True

                elif self.full:
                    self.fctx2 = str(eval(self.expression))
                    self.FullTextDisplay.insert(END, f'f(x)₂ = {self.fctx2}')
                    self.DrawTexTk(
                        f'f(x)₁ = {self.DrawAfter(self.fctx1)} | f(x)₂ = '
                        f'{self.DrawAfter(self.fctx2)}')
                    if not self.equal:
                        self.PlotFirstFunc = plot3d_parametric_line(sympify(self.fctx1), sympify(self.fctx2), self.x,
                                                                    ylim=(-10, 10), xlim=(-10, 10))
                        self.VariableEQL(f'f(x)₁ =', '')
                        self.equal = True
                        self.full = None

                    elif self.equal:
                        self.PlotAddFunc = plot3d_parametric_line(sympify(self.fctx1), sympify(self.fctx2), self.x,
                                                                  ylim=(-10, 10), xlim=(-10, 10), show=False)
                        TwoPlotColor(self.PlotFirstFunc, self.PlotAddFunc)
                        self.VariableEQL(f'f(x)₁ =', '')
                        self.full = None

            elif self.mode == 'Plot3D':
                if self.full is None:
                    self.fctxy = str(eval(self.expression))
                    self.FullTextDisplay.insert(END, f'f(x,y) = {self.fctxy}')
                    self.PlotFirstFunc = plot3d(sympify(self.fctxy))
                    self.VariableEQL(f'f(x,y) =', '')
                    self.full = True

                elif self.full:
                    self.fctxy = str(eval(self.expression))
                    self.FullTextDisplay.insert(END, f'f(x,y) = {self.fctxy}')
                    self.PlotAddFunc = plot3d(sympify(self.fctxy), show=False)

                    TwoPlotColor(self.PlotFirstFunc, self.PlotAddFunc)
                    self.VariableEQL(f'f(x,y) =', '')

            elif self.mode == 'P3DPS':
                if self.full is None:
                    self.fctxy1 = str(eval(self.expression))
                    self.FullTextDisplay.insert(END, f'f(x,y)₁ = {self.fctxy1}')
                    self.DrawTexTk(
                        f'f(x,y)₁ = {self.DrawAfter(self.fctxy1)} | f(x,y)₂ = ')
                    self.VariableEQL(f'f(x,y)₂ = ', '')
                    self.full = True

                elif self.full:
                    self.fctxy2 = str(eval(self.expression))
                    self.FullTextDisplay.insert(END, f'f(x,y)₂ = {self.fctxy2}')
                    self.DrawTexTk(f'f(x,y)₁ = {self.DrawAfter(self.fctxy1)} | f(x,y)₂ = '
                                   f'{self.DrawAfter(self.fctxy2)}')
                    if not self.equal:
                        self.PlotFirstFunc = plot3d_parametric_surface(sympify(self.fctxy1), sympify(self.fctxy2),
                                                                       self.x - self.y)
                        self.VariableEQL(f'f(x,y)₁ =', '')
                        self.equal = True
                        self.full = None

                    elif self.equal:
                        self.PlotAddFunc = plot3d_parametric_surface(sympify(self.fctx1), sympify(self.fctx2),
                                                                     self.x - self.y, show=False)
                        TwoPlotColor(self.PlotFirstFunc, self.PlotAddFunc)
                        self.VariableEQL(f'f(x,y)₁ =', '')
                        self.full = None

            self.iCursor(END)

            self.ResetIndexCursor()

            if self.mode == 'Operation' or self.mode == 'Solve' or self.mode == 'Matrices':
                pass
            else:
                self.FullTextDisplay.see(END)

        except ValueError:
            self.SecondStrVar.set('ValueError')
        except SyntaxError:
            self.SecondStrVar.set('SyntaxError')
        except NameError:
            self.SecondStrVar.set('NameError')
        except TypeError:
            self.SecondStrVar.set('TypeError')
        except OverflowError:
            self.SecondStrVar.set('OverflowMathRangeError')
        except IndexError:
            self.SecondStrVar.set('IndexError')

    def Exit(self):
        return self.win.destroy()


if __name__ == "__main__":
    # run calculator
    Calculator()
