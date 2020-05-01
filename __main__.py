from __jeep_v10_2__ import *
from tkinter import *
from sympy import *
from sympy.abc import x, y, z
import sympy.plotting as plt

"""
# version 7.0.0
# add multi entry for system equation solver and mix it by linear equation solver, it has tree modes functions such as
(3⨯3 {x,y,z} | 2⨯2 {x,y} | 1⨯1 {x}), optimizing and adapting and creating space for this class in script
# add double entry for Plot 3D Parametric Surface & Line and for Plot 2D Parametric this last was mix it by Plot 3D 
Parametric Line, optimizing and adapting and creating space for this class in script
# delete four modes (Function, Simple Equation, Linear Equation Solver, Plot 3D Parametric Line)
# optimizing and adapting and redesigning all
# set the primary entry static height
# switching modes are more organized for call widgets
# reduce conditions in definition of delete and switch mode
# fix the setting zero in Equation Solver
"""
# noinspection NonAsciiCharacters
π = pi


class Calculator:
    __author__ = 'Achraf Najmi'
    __version__ = '7.0.0 beta 2.1'
    __name__ = 'MathPy'
    btn_prm = {'padx': 18,
               'pady': 1,
               'bd': 1,
               'background': '#666666',
               'fg': 'white',
               'bg': '#666666',
               'font': ('DejaVu Sans', 17),
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
               'font': ('Wingdings', 18),
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
                'font': ('DejaVu Sans', 17),
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
                'font': ('DejaVu Sans', 10),
                'width': 4,
                'height': 1,
                'relief': 'raised',
                'activeback': '#49000A',
                'activebackground': '#80000B',
                'activeforeground': "white"}
    ent_prm = {'fg': 'black',
               'bg': '#F0F0F0',
               'font': ('DejaVu Sans', 32),
               'relief': 'flat'}
    mlt_ent_prm = {'fg': 'black',
                   'bg': '#F0F0F0',
                   'font': ('DejaVu Sans', 20),
                   'relief': 'flat'}

    def __init__(self):
        self.win = Tk()
        self.win.geometry("1100x683")
        self.win.minsize(width=420, height=683)
        self.win.resizable(width=True, height=True)
        self.win.title(u"%s v%s" % (self.__name__, self.__version__))
        self.little_tuple = {'(': '₍', ')': '₎'}
        self.btn_u = []
        self.btn_a = []
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
        self.PlotSecondFunc = ''
        self.PlotAddFunc = ''
        self.PlotAdd2Func = ''
        # used to switch modes
        self.mode = ''
        # default variable
        self.equal = False
        self.clear = False
        # string variable for text input
        self.ErrorStrVar = StringVar()
        self.LabelStrVar = StringVar()
        # ROW 0 top canvas==============================================================================================
        self.top_canvas = Canvas(self.win, relief='flat', bg='#F0F0F0', width=42)
        self.top_canvas.grid(row=0, column=0, columnspan=2, sticky=NSEW)
        self.top_canvas.rowconfigure(0, weight=1)
        self.top_canvas.columnconfigure(1, weight=1)
        # ROW 1 middle top Canvas=======================================================================================
        self.middle_top_canvas = Canvas(self.win, relief='flat', background='#212121', height=211)
        self.middle_top_canvas.grid(row=1, column=0, columnspan=2, rowspan=1, sticky=NSEW)
        # ROW 2 set canvas switching ScrollableTkAggXY & FigureCanvasTkAgg & NavigationToolbar2Tk-----------------------
        self.east_canvas = Canvas(self.win, relief='flat', bg='#F0F0F0')
        self.east_canvas.grid(row=2, column=1, rowspan=4, sticky=NSEW)
        self.east_canvas.rowconfigure(0, weight=1)
        self.east_canvas.columnconfigure(0, weight=1)
        self.empty_canvas = Canvas(self.win, relief='flat')
        self.empty_canvas.grid(row=2, column=0, sticky=NSEW)
        # ROW 3 set canvas showing top buttons==========================================================================
        self.middle_canvas = Canvas(self.win, relief='flat')
        self.middle_canvas.grid(row=3, column=0, sticky=NSEW)
        self.middle_canvas.rowconfigure(0, weight=1)
        self.middle_canvas.columnconfigure(0, weight=1)
        self.middle_canvas.columnconfigure(1, weight=1)
        self.middle_canvas.columnconfigure(2, weight=1)
        self.middle_canvas.columnconfigure(3, weight=1)
        self.middle_canvas.columnconfigure(4, weight=1)
        self.middle_canvas.columnconfigure(5, weight=1)
        # ROW 4 set canvas showing middle bottom buttons================================================================
        self.middle_bottom_canvas = Canvas(self.win, relief='flat')
        self.middle_bottom_canvas.grid(row=4, column=0, sticky=NSEW)
        self.middle_bottom_canvas.rowconfigure(0, weight=1)
        self.middle_bottom_canvas.rowconfigure(1, weight=1)
        self.middle_bottom_canvas.rowconfigure(2, weight=1)
        self.middle_bottom_canvas.columnconfigure(0, weight=1)
        self.middle_bottom_canvas.columnconfigure(1, weight=1)
        self.middle_bottom_canvas.columnconfigure(2, weight=1)
        self.middle_bottom_canvas.columnconfigure(3, weight=1)
        self.middle_bottom_canvas.columnconfigure(4, weight=1)
        self.middle_bottom_canvas.columnconfigure(5, weight=1)
        # ROW 5 set canvas showing bottom buttons=======================================================================
        self.bottom_canvas = Canvas(self.win, relief='flat')
        self.bottom_canvas.grid(row=5, column=0, sticky=NSEW)
        self.bottom_canvas.rowconfigure(0, weight=1)
        self.bottom_canvas.rowconfigure(1, weight=1)
        self.bottom_canvas.rowconfigure(2, weight=1)
        self.bottom_canvas.rowconfigure(3, weight=1)
        self.bottom_canvas.rowconfigure(4, weight=1)
        self.bottom_canvas.columnconfigure(0, weight=1)
        self.bottom_canvas.columnconfigure(1, weight=1)
        self.bottom_canvas.columnconfigure(2, weight=1)
        self.bottom_canvas.columnconfigure(3, weight=1)
        self.bottom_canvas.columnconfigure(4, weight=1)
        self.bottom_canvas.columnconfigure(5, weight=1)
        # Equal Label Display===========================================================================================
        # Text Display, insertbackground='white'
        self.TextDisplay = ManagedEntry(self.top_canvas, **self.ent_prm, insertwidth=2)
        # Error Label Display, cursor="arrow", cursor="hand1"
        self.ErrorLabelDisplay = Label(self.top_canvas, **self.ent_prm, textvariable=self.ErrorStrVar)

        self.SSE = SystemSolverEntry(self.top_canvas, line=3, height=267)
        self.FE = FunctionEntry(self.top_canvas, height=267)

        # region ---------------------------------- ROW 1 set MathPlot LaTex Display -----------------------------------
        mpl_white_rgb = ((255. / 255.), (255. / 255.), (255. / 255.))
        self.FigureX = FigureX(figsize=(1, 1), facecolor='#212121', rgbcolor=mpl_white_rgb, fontsize=32)
        self.TkAggX = ScrollableTkAggX(figure=self.FigureX, master=self.win, height=211)
        self.TkAggX.configure(relief='flat', background='#212121')

        # ROW 2 set canvas showing BackEndPlot==========================================================================
        self.BackEndPlot = BackEndPlot(master=self.east_canvas, figsize=(6, 3))

        # ROW 2 set canvas showing ScrollableTkAggXY====================================================================
        self.FigureXY = FigureXY(figsize=(1, 1), fontsize=20, facecolor='#F0F0F0')
        self.TkAggXY = ScrollableTkAggXY(figure=self.FigureXY, master=self.east_canvas)

        # region ------------------------ buttons that will be fake displayed on middle canvas ROW 0 -------------------
        big_txt = ['Operation', 'System\nEquation\nSolver', 'Plot\nf(x)', "Plot3D\nf(x,y)",
                   'Plot\nParametric\n2D_3D Line', 'Plot 3D\nParametric\nSurface']
        big_pad = ['Operation', 'SystemSolver', 'Plot', "Plot3D", 'PP2D3DL', 'P3DPS']
        self.btn_a = []
        for i in range(6):
            self.btn_a.append(HoverButton(self.middle_canvas, **self.big2_prm, text=big_txt[i], cursor="hand2"))
            self.btn_a[i].grid(row=0, column=i, sticky=NSEW)
            self.btn_a[i]["command"] = lambda f3=big_pad[i]: self.SwitchMode(f3)

        # buttons that will be displayed on middle bottom canvas ROW 0==================================================
        txta = ['Û', 'Ü', '1ST']
        self.btn_m1 = []
        for i1 in range(3):
            self.btn_m1.append(HoverButton(self.middle_bottom_canvas, **self.btn_dif, text=txta[i1], cursor="hand2"))
            self.btn_m1[i1].grid(row=0, column=i1, sticky=NSEW)
        # Cursor Disposition
        self.btn_m1[0].bind("<Button>", lambda event, direction='Left': self.LiveSSEControlCursor(event, direction))
        self.btn_m1[1].bind("<Button>", lambda event, direction='Right': self.LiveSSEControlCursor(event, direction))

        txtb = ['ANS', 'r', 'Õ']
        self.btn_m2 = []
        i2b = 3
        for i2a in range(3):
            self.btn_m2.append(HoverButton(self.middle_bottom_canvas, **self.btn_prm, text=txtb[i2a], cursor="hand2"))
            self.btn_m2[i2a].grid(row=0, column=i2b, sticky=NSEW)
            i2b += 1
        # Answer Stored
        self.btn_m2[0].configure(bg='#20B645', activebackground='#00751E', font=('DejaVu Sans', 17),
                                 command=lambda: self.Input(str(self.callback[-1])))
        self.btn_m2[0].ABG = '#009C27'
        self.btn_m2[0].DBG = '#20B645'
        # Clear
        self.btn_m2[1].configure(width=1, bg='firebrick2', activebackground='firebrick4', font=('Marlett', 20),
                                 command=lambda: self.Delete())
        self.btn_m2[1].ABG = 'firebrick3'
        self.btn_m2[1].DBG = 'firebrick2'
        # Remove
        self.btn_m2[2].configure(width=1, bg='Royalblue2', activebackground='Royalblue4', font=('Wingdings', 19),
                                 command=lambda: self.Remove())
        self.btn_m2[2].ABG = 'Royalblue3'
        self.btn_m2[2].DBG = 'Royalblue2'
        # ========================Trigonometry==========================================================================
        self.btn_u = []
        for i3 in range(6):
            self.btn_u.append(HoverButton(self.middle_bottom_canvas, **self.btn_prm, cursor="hand2"))
            self.btn_u[i3].grid(row=1, column=i3, sticky=NSEW)
        # ROW 2
        # ========================logarithm=============================================================================
        logarithm_pad = ['log(', 'exp(', 'LambertW(', 'integrate(', 'sqrt(', "fctrl("]
        logarithm_txt = ['log', 'exp', 'W', "∫f(x)", '√n', "n!"]
        self.btn_d = []
        for i4 in range(6):
            self.btn_d.append(
                HoverButton(self.middle_bottom_canvas, **self.btn_prm, text=logarithm_txt[i4], cursor="hand2"))
            self.btn_d[i4].grid(row=2, column=i4, sticky=NSEW)
            self.btn_d[i4].configure(command=lambda f0=logarithm_pad[i4]: self.Input(f0))
        # buttons that will be displayed on bottom canvas ROW 0=========================================================
        btn = ['π', 'E', "1j", "+", '(', ')', "7", "8", "9", "-", '/100', 'x', "4", "5", "6", "*", "**2", 'y',
               "1", "2", "3", "/", "**", 'z', "0", '', '.', "=", 'e', "oo"]

        btn_txt = ['π', 'e¹', "j", "+", '(', ')', "7", "8", "9", "-", 'n%', 'x', "4", "5", "6", "⨯",
                   u'n\u00B2', 'y', "1", "2", "3", "/", "nˣ", 'z', "0", '', '.', "=", "10ˣ", "∞"]
        self.btn = []
        i5 = 0
        for j in range(5):
            for k in range(6):
                self.btn.append(HoverButton(self.bottom_canvas, **self.btnb_prm, text=btn_txt[i5], cursor="hand2"))
                self.btn[i5].grid(row=j, column=k, sticky=NSEW)
                self.btn[i5].configure(command=lambda f1=btn[i5]: self.Input(f1))
                i5 += 1
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

        # =================================================================================
        self.DLTX = []
        for l5 in range(6):
            self.DLTX.append(DrawLaTeX())

        # run button switcher and display switcher mode=================================================================
        self.SwitchButtons('1st'), self.SwitchMode('Operation')
        # Switch Menu In Bare Display===================================================================================
        menubare = Menu(self.win)
        File = Menu(menubare, tearoff=0)
        Mode = Menu(menubare, tearoff=0)
        menubare.add_cascade(label="File", menu=File)
        menubare.add_cascade(label="Mode", menu=Mode)
        File.add_command(label='1st Page             V', command=lambda: self.SwitchButtons("1st"))
        File.add_command(label='2nd Page           B', command=lambda: self.SwitchButtons("2nd"))
        File.add_separator()
        File.add_command(label="Close         Alt+F4", command=lambda: sys.exit())
        Mode.add_command(label="Operation",
                         command=lambda: [self.SwitchButtons('1st'), self.SwitchMode('Operation')])
        Mode.add_command(label='System Equation Solver',
                         command=lambda: [self.SwitchButtons('1st'), self.SwitchMode('SystemSolver')])
        Mode.add_command(label='Plot',
                         command=lambda: [self.SwitchButtons('2nd'), self.SwitchMode('Plot')])
        Mode.add_command(label='Plot 3D',
                         command=lambda: [self.SwitchButtons('2nd'), self.SwitchMode('Plot3D')])
        Mode.add_command(label='Plot Parametric 2D_3D Line',
                         command=lambda: [self.SwitchButtons('2nd'), self.SwitchMode('PP2D3DL')])
        Mode.add_command(label='Plot 3D Parametric Surface',
                         command=lambda: [self.SwitchButtons('2nd'), self.SwitchMode('P3DPS')])
        # Configuration Master Display==================================================================================
        self.win.rowconfigure(2, weight=1)
        self.win.columnconfigure(1, weight=1)

        self.win.bind_all('<Key>', self.KeyboardInput)
        self.win.iconbitmap('Alecive-Flatwoken-Apps-Libreoffice-Math-B.ico')
        self.win.configure(menu=menubare, bg='#212121')
        self.win.update()
        self.win.mainloop()

    def SwitchButtons(self, side):
        page = side
        # buttons to switch between buttons those will be displayed on middle bottom & middle canvas
        if page == '1st':
            # buttons that will be displayed on middle bottom canvas ROW 0==============================================
            # 2nd
            self.btn_m1[2].configure(text="1ST", command=lambda: self.SwitchButtons("2nd"), font=('DejaVu Sans', 17))
            # ROW 1
            # ========================Trigonometry======================================================================
            Trigonometry_pad = ['cos(', 'sin(', "tan(", 'cosh(', 'sinh(', "tanh("]
            Trigonometry_txt = ['cos', 'sin', "tan", 'cosh', 'sinh', "tanh"]

            for i in range(6):
                self.btn_u[i].configure(text=Trigonometry_txt[i], command=lambda f4=Trigonometry_pad[i]: self.Input(f4))

            self.btn_d[3].configure(text="∫f(x)", command=lambda: self.Input('integrate('))

            self.btn_d[2].configure(text='W₀', command=lambda: self.Input('LambertW('))

            self.btn[28].configure(text='10ˣ', command=lambda: self.Input('e+'))

        elif page == '2nd':
            # buttons that will be displayed on middle bottom canvas ROW 0==============================================
            # 1st
            self.btn_m1[2].configure(text="2ND", command=lambda: self.SwitchButtons("1st"), font=('DejaVu Sans', 17))

            # ========================Trigonometry======================================================================
            Trigonometry_pad = ['acos(', 'asin(', "atan(", 'acosh(', 'asinh(', "atanh("]
            Trigonometry_txt = ['acos', 'asin', "atan", 'acosh', 'asinh', "atanh"]

            for i in range(6):
                self.btn_u[i].configure(text=Trigonometry_txt[i], command=lambda f6=Trigonometry_pad[i]: self.Input(f6))

            self.btn_d[3].configure(text='d/dx', command=lambda: self.Input('diff('))

            self.btn_d[2].configure(text='W₋₁', command=lambda: [self.Input('LambertW('), self.Input(',-1')])

            self.btn[28].configure(text='10¯ˣ', command=lambda: self.Input('e-'))

    def SwitchMode(self, passmode):
        pass_mode = self.mode
        self.mode = passmode

        # Switching ScrollableTkAggXY & BackEndPlot ====================================================================
        if self.mode == 'Operation' or self.mode == 'SystemSolver':
            if pass_mode == 'Operation' or pass_mode == 'SystemSolver':
                self.FigureXY.Clear()
            else:
                self.SwitchEqualWidget('TkAggXY')

        else:
            if pass_mode == 'P3DPS' or pass_mode == 'PP2D3DL' or pass_mode == 'Plot3D' or pass_mode == 'Plot':
                self.BackEndPlot.Clear()
            else:
                self.SwitchEqualWidget('PlotTkAgg')

        # Switching Entry Widgets ======================================================================================
        if self.mode == 'SystemSolver':
            if pass_mode == 'SystemSolver':
                pass
            else:
                self.SwitchEntryWidget('MultiEntry')

        elif self.mode == 'PP2D3DL' or self.mode == "P3DPS":
            if pass_mode == 'PP2D3DL' or pass_mode == "P3DPS":
                pass
            else:
                self.SwitchEntryWidget('DoubleEntry')

        else:
            if pass_mode == 'Operation' or pass_mode == 'Plot' or pass_mode == 'Plot3D':
                pass
            else:
                self.SwitchEntryWidget('SingleEntry')

        # Switching Modes ==============================================================================================
        if self.mode == 'Operation':
            self.FigureXY.DrawLaTex(f'Mode Operation : ')
            self.btn[17]['state'] = ['disabled']
            self.btn[23].config(state=DISABLED)

            self.btn_a[0].config(bg='#80000B', relief='sunken')
            self.btn_a[0].DBG = '#80000B'
            for i in range(1, 6):
                self.btn_a[i].config(bg='#212121', relief='raised')
                self.btn_a[i].DBG = '#212121'

        elif self.mode == 'SystemSolver':
            self.FigureXY.DrawLaTex('Mode System Equation Solver :')
            self.btn[17].config(state=NORMAL)
            self.btn[23].config(state=NORMAL)

            self.btn_a[0].config(bg='#212121', relief='raised')
            self.btn_a[0].DBG = '#212121'
            self.btn_a[1].config(bg='#80000B', relief='sunken')
            self.btn_a[1].DBG = '#80000B'
            for i in range(2, 6):
                self.btn_a[i].config(bg='#212121', relief='raised')
                self.btn_a[i].DBG = '#212121'

        elif self.mode == 'Plot':
            self.btn[17]['state'] = ['disabled']
            self.btn[23].config(state=DISABLED)

            for i in range(2):
                self.btn_a[i].config(bg='#212121', relief='raised')
                self.btn_a[i].DBG = '#212121'
            self.btn_a[2].config(bg='#80000B', relief='sunken')
            self.btn_a[2].DBG = '#80000B'
            for i in range(3, 6):
                self.btn_a[i].config(bg='#212121', relief='raised')
                self.btn_a[i].DBG = '#212121'

        elif self.mode == 'Plot3D':
            self.btn[17]['state'] = ['normal']
            self.btn[23].config(state=DISABLED)

            for i in range(3):
                self.btn_a[i].config(bg='#212121', relief='raised')
                self.btn_a[i].DBG = '#212121'
            self.btn_a[3].config(bg='#80000B', relief='sunken')
            self.btn_a[3].DBG = '#80000B'
            for i in range(4, 6):
                self.btn_a[i].config(bg='#212121', relief='raised')
                self.btn_a[i].DBG = '#212121'

        elif self.mode == 'PP2D3DL':
            self.btn[17]['state'] = ['disabled']
            self.btn[23].config(state=DISABLED)

            for i in range(4):
                self.btn_a[i].config(bg='#212121', relief='raised')
                self.btn_a[i].DBG = '#212121'
            self.btn_a[4].config(bg='#80000B', relief='sunken')
            self.btn_a[4].DBG = '#80000B'
            self.btn_a[5].config(bg='#212121', relief='raised')
            self.btn_a[5].DBG = '#212121'

        elif self.mode == 'P3DPS':
            self.btn[17]['state'] = ['normal']
            self.btn[23].config(state=DISABLED)

            for i in range(5):
                self.btn_a[i].config(bg='#212121', relief='raised')
                self.btn_a[i].DBG = '#212121'
            self.btn_a[5].config(bg='#80000B', relief='sunken')
            self.btn_a[5].DBG = '#80000B'

        self.Delete()

    def SwitchEqualWidget(self, widget):
        figure = widget
        self.east_canvas.destroy()
        self.east_canvas = Canvas(self.win, relief='flat', bg='#F0F0F0')
        self.east_canvas.grid(row=2, column=1, rowspan=4, sticky=NSEW)
        self.east_canvas.rowconfigure(0, weight=1)
        self.east_canvas.columnconfigure(0, weight=1)

        if figure == 'TkAggXY':
            self.FigureXY.Clear()
            self.TkAggXY = ScrollableTkAggXY(figure=self.FigureXY, master=self.east_canvas)
            self.TkAggXY.grid(row=0, column=0, sticky=NSEW)

        elif figure == 'PlotTkAgg':
            self.BackEndPlot = BackEndPlot(master=self.east_canvas, figsize=(6, 3))
            self.BackEndPlot.grid(row=0, column=0, sticky=NSEW)

    def SwitchEntryWidget(self, widget):
        figure = widget
        self.middle_top_canvas.destroy()
        self.TkAggX.destroy()

        self.ErrorLabelDisplay.destroy()
        self.top_canvas.destroy()
        try:
            self.SSE.destroy()
        except Exception:
            pass
        try:
            self.FE.destroy()
        except Exception:
            pass

        if figure == 'MultiEntry':
            self.top_canvas = Canvas(self.win, relief='flat', bg='#F0F0F0', height=267)
            self.top_canvas.grid(row=0, column=0, rowspan=2, sticky=NSEW)

            self.SSE = SystemSolverEntry(self.win, line=3, height=267)
            self.SSE.grid(row=0, column=0, rowspan=2, sticky=NSEW)
            self.SSE.CreateGrid(line=3, **self.mlt_ent_prm)
            self.SSE.button3['command'] = lambda: [self.SSE.CreateGrid(line=3, **self.mlt_ent_prm), self.Delete()]
            self.SSE.button2['command'] = lambda: [self.SSE.CreateGrid(line=2, **self.mlt_ent_prm), self.Delete()]
            self.SSE.button1['command'] = lambda: [self.SSE.CreateGrid(line=1, **self.mlt_ent_prm), self.Delete()]

            self.middle_top_canvas = Canvas(self.win, relief='flat', background='#212121', height=267)
            self.middle_top_canvas.grid(row=0, column=1, columnspan=1, rowspan=2, sticky=NSEW)

            self.ErrorLabelDisplay = Label(self.middle_top_canvas, **self.mlt_ent_prm, textvariable=self.ErrorStrVar)
            self.ErrorLabelDisplay.grid(row=0, column=1, sticky=NSEW)

            self.TkAggX = ScrollableTkAggX(figure=self.FigureX, master=self.win, height=267)
            self.TkAggX.configure(relief='flat', background='#212121')
            self.TkAggX.grid(row=0, column=1, columnspan=1, rowspan=2, sticky=NSEW)

            self.FigureX.fontsize = 20

        elif figure == 'DoubleEntry':
            self.top_canvas = Canvas(self.win, relief='flat', bg='#F0F0F0', height=267)
            self.top_canvas.grid(row=0, column=0, rowspan=2, sticky=NSEW)

            self.FE = FunctionEntry(self.win, height=267)
            self.FE.grid(row=0, column=0, rowspan=2, sticky=NSEW)
            self.FE.CreateGrid(**self.mlt_ent_prm)

            self.middle_top_canvas = Canvas(self.win, relief='flat', background='#212121', height=267)
            self.middle_top_canvas.grid(row=0, column=1, columnspan=1, rowspan=2, sticky=NSEW)

            self.ErrorLabelDisplay = Label(self.middle_top_canvas, **self.mlt_ent_prm, textvariable=self.ErrorStrVar)
            self.ErrorLabelDisplay.grid(row=0, column=1, sticky=NSEW)

            self.TkAggX = ScrollableTkAggX(figure=self.FigureX, master=self.win, height=267)
            self.TkAggX.configure(relief='flat', background='#212121')
            self.TkAggX.grid(row=0, column=1, columnspan=1, rowspan=2, sticky=NSEW)

            self.FigureX.fontsize = 20

        elif figure == 'SingleEntry':
            self.top_canvas = Canvas(self.win, relief='flat', bg='#F0F0F0', width=42)
            self.top_canvas.grid(row=0, column=0, columnspan=2, sticky=NSEW)
            self.top_canvas.rowconfigure(0, weight=1)
            self.top_canvas.columnconfigure(1, weight=1)

            EqualLabelDisplay = Label(self.top_canvas, **self.ent_prm, textvariable=self.LabelStrVar)
            EqualLabelDisplay.grid(row=0, column=0, sticky=NSEW)
            EqualLabelDisplay.configure(anchor='e')
            # Text Display, insertbackground='white'
            self.TextDisplay = ManagedEntry(self.top_canvas, **self.ent_prm, insertwidth=2)
            self.TextDisplay.grid(row=0, column=1, sticky=NSEW)
            # Error Label Display, cursor="arrow", cursor="hand1"
            self.ErrorLabelDisplay = Label(self.top_canvas, **self.ent_prm, textvariable=self.ErrorStrVar)
            self.ErrorLabelDisplay.grid(row=0, column=2, sticky=NSEW)
            self.ErrorLabelDisplay.configure(anchor='e')

            self.middle_top_canvas = Canvas(self.win, relief='flat', background='#212121', height=211)
            self.middle_top_canvas.grid(row=1, column=0, columnspan=2, rowspan=1, sticky=NSEW)

            self.TkAggX = ScrollableTkAggX(figure=self.FigureX, master=self.win, height=211)
            self.TkAggX.configure(relief='flat', background='#212121')
            self.TkAggX.grid(row=1, column=0, columnspan=2, rowspan=1, sticky=NSEW)
            self.FigureX.fontsize = 32

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
        self.equal = False
        self.clear = False
        self.ErrorStrVar.set('')
        self.FigureX.clear()
        for l5 in range(6):
            self.DLTX[l5].Clear()

        if self.mode == 'Operation':
            self.TextDisplay.Clear()
            self.LabelStrVar.set('op>')
            self.FigureX.DrawOneLaTex('op>')
            self.FigureXY.Draw(self.TkAggXY)
            self.TextDisplay.focus_set()

        elif self.mode == 'SystemSolver':
            self.SSE.Clear()
            if self.SSE.u == 3:
                self.FigureX.DrawTriLaTex('eq₁>  =', 'eq₂>  =', 'eq₃>  =')
            elif self.SSE.u == 2:
                self.FigureX.DrawBiLaTex('eq₁>  =', 'eq₂>  =')
            elif self.SSE.u == 1:
                self.FigureX.DrawOneLaTex('eq₁>  =')
            self.FigureXY.Draw(self.TkAggXY)
            self.SSE().focus_set()

        elif self.mode == 'Plot':
            self.TextDisplay.Clear()
            self.BackEndPlot.Clear()
            self.LabelStrVar.set('f(x) =')
            self.FigureX.DrawOneLaTex('f(x) = ')
            self.TextDisplay.focus_set()

        elif self.mode == 'Plot3D':
            self.TextDisplay.Clear()
            self.BackEndPlot.Clear()
            self.LabelStrVar.set('f(x,y) =')
            self.FigureX.DrawOneLaTex('f(x,y) = ')
            self.TextDisplay.focus_set()

        elif self.mode == "PP2D3DL":
            self.FE.Clear()
            self.BackEndPlot.Clear()
            self.FE.label[0]['text'] = 'f(x)₁ = '
            self.FE.label[1]['text'] = 'f(x)₂ = '
            self.FigureX.DrawBiLaTex('f(x)₁ =', 'f(x)₂ =')
            self.FE().focus_set()

        elif self.mode == "P3DPS":
            self.FE.Clear()
            self.BackEndPlot.Clear()
            self.FE.label[0]['text'] = 'f(x,y)₁ = '
            self.FE.label[1]['text'] = 'f(x,y)₂ = '
            self.FigureX.DrawBiLaTex('f(x,y)₁ =', 'f(x,y)₂ =')
            self.FE().focus_set()

        self.FigureX.Draw(self.TkAggX)

    def Remove(self):
        if self.clear:
            self.Delete()

        try:
            if self.mode == 'SystemSolver':
                self.SSE().RemoveFromString()
            elif self.mode == 'PP2D3DL' or self.mode == "P3DPS":
                self.FE().RemoveFromString()
            else:
                self.TextDisplay.RemoveFromString()
        except IndexError:
            pass

        self.ShowInput()

    def LiveSSEControlCursor(self, event, direction):
        if self.mode == 'SystemSolver':
            self.SSE().DirectionCursor(direction)
        elif self.mode == 'PP2D3DL' or self.mode == "P3DPS":
            self.FE().DirectionCursor(direction)
        else:
            self.TextDisplay.DirectionCursor(direction)

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
                self.Input('exp(')

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
                self.Input('(')

            elif put == 'parenright':
                self.Input(')')

            elif put == 'backslash' or put == 'bar':
                self.Input('sqrt(')

            elif keyword.keysym == 's':
                self.Input('sin(')

            elif keyword.keysym == 'c':
                self.Input('cos(')

            elif keyword.keysym == 't':
                self.Input('tan(')

            elif keyword.keysym == 'S':
                self.Input('sinh(')

            elif keyword.keysym == 'C':
                self.Input('cosh(')

            elif keyword.keysym == 'T':
                self.Input('tanh(')

            elif keyword.keysym == 'l':
                self.Input('log(')

            elif keyword.keysym == 'I':
                self.Input('oo')

            elif keyword.keysym == 'i':
                self.Input('integrate(')

            elif put == 'd':
                self.Input('diff(')

            elif keyword.keysym == 'w':
                self.Input('LambertW(')

            elif keyword.keysym == 'W':
                self.Input('LambertW('), self.Input(',-1')

            elif put == 'j':
                self.Input('1j')

            elif put == 'exclam' or put == 'f':
                self.Input('fctrl(')

            elif put == 'p':
                self.Input('π')

            elif put == 'a' or put == 'x' or put == 'y' or put == 'z' or put == '0' or put == '1' or put == '2' or \
                    put == '3' or put == '4' or put == '5' or put == '6' or put == '7' or put == '8' or put == '9':
                self.Input(put)

            else:
                if keyword.keysym == 'Return' or put == 'equal':
                    pass
                else:
                    self.ShowInput()

        except IndexError:
            self.ErrorStrVar.set('IndexError')

    def Input(self, keyword):
        if self.clear:
            self.Delete()

        if self.mode == 'SystemSolver':
            self.SSE().InsertIntoString(keyword)
        elif self.mode == 'PP2D3DL' or self.mode == "P3DPS":
            self.FE().InsertIntoString(keyword)
        else:
            self.TextDisplay.InsertIntoString(keyword)

        self.ShowInput()

    def ShowInput(self):
        try:
            if self.mode == 'Operation':
                self.LabelStrVar.set('op>')
                self.answer = sympify(self.TextDisplay.expression, evaluate=True)

                expr_str = self.DLTX[0].Before(self.TextDisplay.expression)
                result_expr = self.DLTX[1].After(self.answer)
                result_num = self.DLTX[2].AfterNum(self.answer)
                dot_zero = str(result_num).replace('.0', '')

                if expr_str == result_expr and str('log') in str(self.TextDisplay.expression) \
                        or str('exp') in str(self.TextDisplay.expression):
                    self.FigureX.DrawBiLaTex(f'op> {self.TextDisplay.expression}', f' = {result_expr} = {result_num}')

                elif dot_zero == result_expr or result_expr == result_num:
                    self.FigureX.DrawOneLaTex(f'op> {expr_str} = {result_expr}')
                else:
                    self.FigureX.DrawBiLaTex(f'op> {expr_str}', f' = {result_expr} = {result_num}')

            elif self.mode == 'SystemSolver':
                if self.SSE.u == 3:
                    self.FigureX.DrawTriLaTex(f'eq₁> {self.DLTX[0].After(self.SSE.entry[0].expression)}'
                                              f' = {self.DLTX[1].After(self.SSE.entry[1].expression)}',
                                              f'eq₂> {self.DLTX[2].After(self.SSE.entry[2].expression)}'
                                              f' = {self.DLTX[3].After(self.SSE.entry[3].expression)}',
                                              f'eq₃> {self.DLTX[4].After(self.SSE.entry[4].expression)}'
                                              f' = {self.DLTX[5].After(self.SSE.entry[5].expression)}')
                elif self.SSE.u == 2:
                    self.FigureX.DrawBiLaTex(f'eq₁> {self.DLTX[0].After(self.SSE.entry[0].expression)}'
                                             f' = {self.DLTX[1].After(self.SSE.entry[1].expression)}',
                                             f'eq₂> {self.DLTX[2].After(self.SSE.entry[2].expression)}'
                                             f' = {self.DLTX[3].After(self.SSE.entry[3].expression)}')
                elif self.SSE.u == 1:
                    self.FigureX.DrawOneLaTex(f'eq₁> {self.DLTX[0].After(self.SSE.entry[0].expression)}'
                                              f' = {self.DLTX[1].After(self.SSE.entry[1].expression)}')

            elif self.mode == 'Plot':
                self.LabelStrVar.set(f'f(x) =')
                self.FigureX.DrawOneLaTex(f'f(x) = {self.DLTX[0].After(self.TextDisplay.expression)}')

            elif self.mode == "Plot3D":
                self.LabelStrVar.set(f'f(x,y) =')
                self.FigureX.DrawOneLaTex(f'f(x,y) = {self.DLTX[0].After(self.TextDisplay.expression)}')

            elif self.mode == "PP2D3DL":
                self.FigureX.DrawBiLaTex(f'f(x)₁ = {self.DLTX[0].After(self.FE.entry[0].expression)}',
                                         f'f(x)₂ = {self.DLTX[1].After(self.FE.entry[1].expression)}')

            elif self.mode == "P3DPS":
                self.FigureX.DrawBiLaTex(f'f(x,y)₁ = {self.DLTX[0].After(self.FE.entry[0].expression)}',
                                         f'f(x,y)₂ = {self.DLTX[1].After(self.FE.entry[1].expression)}')

            self.ErrorStrVar.set('')

            self.FigureX.Draw(self.TkAggX)
        except Exception:
            pass
        if self.mode == 'SystemSolver':
            self.SSE().focus_set()
        elif self.mode == 'PP2D3DL' or self.mode == "P3DPS":
            self.FE().focus_set()
        else:
            self.TextDisplay.focus_set()

    def VariableEQL(self, label_var):
        if self.mode == 'SystemSolver' or self.mode == 'PP2D3DL' or self.mode == "P3DPS":
            pass
        else:
            self.TextDisplay.StringVariable('')
            self.LabelStrVar.set(label_var)

    def ShowEqual(self):
        try:
            if self.mode == 'Operation':
                if not self.equal:
                    self.answer = sympify(self.TextDisplay.expression, evaluate=True)
                    self.VariableEQL(f'op> {self.TextDisplay.expression} = {self.answer}')
                    expr_str = DrawBefore(self.TextDisplay.expression)
                    result_expr = DrawAfter(self.answer)
                    result_num = DrawAfterNum(self.answer)
                    dot_zero = str(result_num).replace('.0', '')

                    if expr_str == result_expr and str('log') in str(self.TextDisplay.expression) \
                            or str('exp') in str(self.TextDisplay.expression):
                        self.FigureX.DrawBiLaTex(f'op> {self.TextDisplay.expression}',
                                                 f' = {result_expr} = {result_num}')
                        self.FigureXY.DrawLaTex(f'op> {self.TextDisplay.expression}')
                        self.FigureXY.DrawLaTex(f'= {result_expr}')
                        self.FigureXY.DrawLaTex(f'= {result_num}')

                    elif dot_zero == result_expr or result_expr == result_num:
                        self.FigureX.DrawOneLaTex(f'op> {expr_str} = {result_expr}')
                        self.FigureXY.DrawLaTex(f'op> {expr_str} = {result_expr}')
                    else:
                        self.FigureX.DrawBiLaTex(f'op> {expr_str}', f' = {result_expr} = {result_num}')
                        self.FigureXY.DrawLaTex(f'op> {expr_str}')
                        self.FigureXY.DrawLaTex(f'= {result_expr}')
                        self.FigureXY.DrawLaTex(f'= {result_num}')
                    self.clear = True
                    self.equal = True

                elif self.equal:
                    self.answer = self.TextDisplay.FullReBuild(self.callback)
                    self.answer = sympify(self.answer, evaluate=True)
                    self.VariableEQL(f'op> {self.TextDisplay.expression} = {self.answer}')
                    expr_str = DrawBefore(self.TextDisplay.expression)
                    result_expr = DrawAfter(self.answer)
                    result_num = DrawAfterNum(self.answer)
                    dot_zero = str(result_num).replace('.0', '')

                    if expr_str == result_expr and str('log') in str(self.TextDisplay.expression) \
                            or str('exp') in str(self.TextDisplay.expression):
                        self.FigureX.DrawBiLaTex(f'op> {self.TextDisplay.expression}',
                                                 f' = {result_expr} = {result_num}')
                        self.FigureXY.DrawLaTex(f'op> {self.TextDisplay.expression}')
                        self.FigureXY.DrawLaTex(f'= {result_expr}')
                        self.FigureXY.DrawLaTex(f'= {result_num}')

                    elif dot_zero == result_expr or result_expr == result_num:
                        self.FigureX.DrawOneLaTex(f'op> {expr_str} = {result_expr}')
                        self.FigureXY.DrawLaTex(f'op> {expr_str} = {result_expr}')
                    else:
                        self.FigureX.DrawBiLaTex(f'op> {expr_str} ', f' = {result_expr} = {result_num}')
                        self.FigureXY.DrawLaTex(f'op> {expr_str}')
                        self.FigureXY.DrawLaTex(f'= {result_expr}')
                        self.FigureXY.DrawLaTex(f'= {result_num}')
                self.callback.append(str(self.answer))

            elif self.mode == 'SystemSolver':
                self.q = str(sympify(self.SSE.entry[0].expression))
                self.p = str(sympify(self.SSE.entry[1].expression))
                if self.SSE.u == 3:
                    self.j = str(sympify(self.SSE.entry[2].expression))
                    self.k = str(sympify(self.SSE.entry[3].expression))
                    self.m = str(sympify(self.SSE.entry[4].expression))
                    self.n = str(sympify(self.SSE.entry[5].expression))
                    try:
                        self.SolutionTT = linsolve(
                            [Eq(sympify(self.q), sympify(self.p)), Eq(sympify(self.j), sympify(self.k)),
                             Eq(sympify(self.m), sympify(self.n))], [self.x, self.y, self.z])
                        sol = str(self.SolutionTT)
                        if sol == 'EmptySet':
                            pass
                        else:
                            self.FigureXY.DrawLaTex('System Linear of Three Equations : {eq₁,eq₂,eq₃}_[x,y,z]')
                    except Exception:
                        try:
                            self.SolutionTT = nonlinsolve(
                                [Eq(sympify(self.q), sympify(self.p)), Eq(sympify(self.j), sympify(self.k)),
                                 Eq(sympify(self.m), sympify(self.n))], [self.x, self.y, self.z])
                            sol = str(self.SolutionTT)
                            if sol == 'EmptySet':
                                pass
                            else:
                                self.FigureXY.DrawLaTex('System Nonlinear of Three Equations : {eq₁,eq₂,eq₃}_[x,y,z]')
                        except Exception:
                            self.FigureX.DrawOneLaTex('Cannot Solve This System')

                    sol = str(self.SolutionTT)
                    if sol == 'EmptySet':
                        self.FigureX.DrawOneLaTex(f'Empty Solution : {DrawAfter(self.SolutionTT)}')

                    else:
                        self.FigureX.DrawTriLaTex(
                            f'eq₁> {DrawBefore(self.q)} = {DrawBefore(self.p)}',
                            f'eq₂> {DrawBefore(self.j)} = {DrawBefore(self.k)} Solution : {DrawAfter(self.SolutionTT)}',
                            f'eq₃> {DrawBefore(self.m)} = {DrawBefore(self.n)}')
                        self.FigureXY.DrawLaTex(f'eq₁> {DrawBefore(self.q)} = {DrawBefore(self.p)}')
                        self.FigureXY.DrawLaTex(f'eq₂> {DrawBefore(self.j)} = {DrawBefore(self.k)}')
                        self.FigureXY.DrawLaTex(f'eq₃> {DrawBefore(self.m)} = {DrawBefore(self.n)}')
                        self.FigureXY.DrawLaTex(f'Solution : {DrawAfter(self.SolutionTT)}')
                        try:
                            self.xexp, self.yexp, self.zexp = next(iter(self.SolutionTT))
                        except Exception:
                            try:
                                sol = str(self.SolutionTT[11:-2])

                                self.w = int(len(sol))
                                self.v = 0
                                while self.v < self.w:
                                    self.xexp = str(self.xexp) + str(sol[self.v])
                                    self.v += 1
                                    if sol[self.v] == ',':
                                        while self.v < self.w:
                                            self.yexp = str(self.yexp) + str(sol[self.v])
                                            self.v += 1
                                            if sol[self.v] == ',':
                                                while self.v < self.w:
                                                    self.zexp = str(self.zexp) + str(sol[self.v])
                                                    self.v += 1

                                self.yexp = str(self.yexp).replace(', ', '')
                                self.zexp = str(self.zexp).replace(', ', '')
                            except Exception:
                                pass
                        try:
                            self.FigureXY.DrawLaTex(f'> x = {DrawAfter(self.xexp)}')
                            self.FigureXY.DrawLaTex(f'> y = {DrawAfter(self.yexp)}')
                            self.FigureXY.DrawLaTex(f'> z = {DrawAfter(self.zexp)}')
                        except Exception:
                            pass

                elif self.SSE.u == 2:
                    self.j = str(sympify(self.SSE.entry[2].expression))
                    self.k = str(sympify(self.SSE.entry[3].expression))
                    try:
                        self.SolutionTT = linsolve(
                            [Eq(sympify(self.q), sympify(self.p)), Eq(sympify(self.j), sympify(self.k))],
                            [self.x, self.y])
                        sol = str(self.SolutionTT)
                        if sol == 'EmptySet':
                            pass
                        else:
                            self.FigureXY.DrawLaTex('System Linear of Two Equations : {eq₁,eq₂}_[x,y]')
                    except Exception:
                        try:
                            self.SolutionTT = nonlinsolve(
                                [Eq(sympify(self.q), sympify(self.p)), Eq(sympify(self.j), sympify(self.k))],
                                [self.x, self.y])
                            sol = str(self.SolutionTT)
                            if sol == 'EmptySet':
                                pass
                            else:
                                self.FigureXY.DrawLaTex('System Nonlinear of Two Equations : {eq₁,eq₂}_[x,y]')
                        except Exception:
                            self.FigureX.DrawOneLaTex('Cannot Solve This System')
                    sol = str(self.SolutionTT)
                    if sol == 'EmptySet':
                        self.FigureX.DrawTriLaTex(f'eq₁> {DrawBefore(self.q)} = {DrawBefore(self.p)}',
                                                  f'eq₂> {DrawBefore(self.j)} = {DrawBefore(self.k)}',
                                                  f'Empty Solution : {DrawAfter(self.SolutionTT)}')

                    else:
                        self.FigureX.DrawTriLaTex(f'eq₁> {DrawBefore(self.q)} = {DrawBefore(self.p)}',
                                                  f'eq₂> {DrawBefore(self.j)} = {DrawBefore(self.k)}',
                                                  f'Solution : {DrawAfter(self.SolutionTT)}')
                        self.FigureXY.DrawLaTex(f'eq₁> {DrawBefore(self.q)} = {DrawBefore(self.p)}')
                        self.FigureXY.DrawLaTex(f'eq₂> {DrawBefore(self.j)} = {DrawBefore(self.k)}')
                        self.FigureXY.DrawLaTex(f'Solution : {DrawAfter(self.SolutionTT)}')
                        try:
                            self.xexp, self.yexp = next(iter(self.SolutionTT))
                        except Exception:
                            try:
                                sol = str(self.SolutionTT[11:-2])

                                self.w = int(len(sol))
                                self.v = 0
                                while self.v < self.w:
                                    self.xexp = str(self.xexp) + str(sol[self.v])
                                    self.v += 1
                                    if sol[self.v] == ',':
                                        while self.v < self.w:
                                            self.yexp = str(self.yexp) + str(sol[self.v])
                                            self.v += 1

                                self.yexp = str(self.yexp).replace(', ', '')
                            except Exception:
                                pass
                        try:
                            self.FigureXY.DrawLaTex(f'> x = {DrawAfter(self.xexp)}')
                            self.FigureXY.DrawLaTex(f'> y = {DrawAfter(self.yexp)}')
                        except Exception:
                            pass

                elif self.SSE.u == 1:
                    try:
                        self.SolutionOS = solve(Eq(sympify(self.q), sympify(self.p)), self.x)
                    except Exception:
                        self.FigureX.DrawOneLaTex('Cannot Solve This Equation')

                    self.FigureX.DrawBiLaTex(f'eq₁> {DrawBefore(self.q)} = {DrawBefore(self.p)}',
                                             f'Solution : {DrawAfter(self.SolutionOS)}')
                    self.FigureXY.DrawLaTex('Linear and Polynomial Equations : {eq₁}_[x] | Constants : (y)_(z)')
                    self.FigureXY.DrawLaTex(f'eq₁> {DrawBefore(self.q)} = {DrawBefore(self.p)}')
                    self.FigureXY.DrawLaTex(f'Solution : {DrawAfter(self.SolutionOS)}')

                    much_sol = len(self.SolutionOS)
                    small_numbers = SmallNumbers(much_sol)
                    for sl in range(much_sol):
                        self.FigureXY.DrawLaTex(f'> x{small_numbers(sl + 1)} = {DrawAfter(self.SolutionOS[sl])}')

            elif self.mode == 'Plot':
                self.fctx = str(eval(self.TextDisplay.expression))
                if not self.equal:
                    self.PlotFirstFunc = plt.plot(sympify(self.fctx), ylim=(-10, 10), xlim=(-10, 10), legend=True,
                                                  show=False)
                    self.PlotFirstFunc = FirstPlotLaTex(self.PlotFirstFunc, self.fctx)
                    self.BackEndPlot.Plot(self.PlotFirstFunc)
                    self.VariableEQL(f'f(x) =')
                    self.equal = True

                elif self.equal:
                    self.PlotAddFunc = plt.plot(sympify(self.fctx), ylim=(-10, 10), xlim=(-10, 10), legend=True,
                                                show=False)
                    self.PlotAddFunc = MultiPlot2D(self.PlotFirstFunc, self.PlotAddFunc, self.fctx)
                    self.BackEndPlot.Plot(self.PlotAddFunc)
                    self.VariableEQL(f'f(x) =')

            elif self.mode == 'Plot3D':
                self.fctxy = str(eval(self.TextDisplay.expression))
                if not self.equal:
                    self.PlotFirstFunc = plt.plot3d(sympify(self.fctxy), show=False)
                    self.BackEndPlot.Plot(self.PlotFirstFunc)
                    self.VariableEQL(f'f(x,y) =')
                    self.equal = True

                elif self.equal:
                    self.PlotAddFunc = plt.plot3d(sympify(self.fctxy), show=False)
                    self.PlotAddFunc = MultiPlot3D(self.PlotFirstFunc, self.PlotAddFunc)
                    self.BackEndPlot.Plot(self.PlotAddFunc)
                    self.VariableEQL(f'f(x,y) =')

            elif self.mode == 'PP2D3DL':
                self.fctx1 = str(eval(self.FE.entry[0].expression))
                self.fctx2 = str(eval(self.FE.entry[1].expression))
                self.FigureX.DrawBiLaTex(f'f(x)₁ = {DrawAfter(self.fctx1)}', f'f(x)₂ = {DrawAfter(self.fctx2)}')
                if not self.equal:
                    self.PlotFirstFunc = plt.plot_parametric(sympify(self.fctx1), sympify(self.fctx2), legend=True,
                                                             ylim=(-10, 10), xlim=(-10, 10), show=False)
                    self.PlotSecondFunc = plt.plot3d_parametric_line(sympify(self.fctx1), sympify(self.fctx2),
                                                                     self.x, legend=True, show=False)
                    self.PlotFirstFunc = FirstPlotLaTex(self.PlotFirstFunc, (self.fctx1, self.fctx2))
                    self.PlotSecondFunc = FirstPlotLaTex(self.PlotSecondFunc, (self.fctx1, self.fctx2))
                    MIX = PlotGrid(1, 2, self.PlotFirstFunc, self.PlotSecondFunc, legend=True, show=False)
                    self.BackEndPlot.Plot(MIX)
                    self.equal = True

                elif self.equal:
                    self.PlotAddFunc = plt.plot_parametric(sympify(self.fctx1), sympify(self.fctx2), ylim=(-10, 10),
                                                           xlim=(-10, 10), legend=True, show=False)
                    self.PlotAdd2Func = plt.plot3d_parametric_line(sympify(self.fctx1), sympify(self.fctx2),
                                                                   self.x, legend=True, show=False)
                    MIX = MultiPlot2D3D(self.PlotFirstFunc, self.PlotAddFunc, self.PlotSecondFunc, self.PlotAdd2Func,
                                        (self.fctx1, self.fctx2))
                    self.BackEndPlot.Plot(MIX)

            elif self.mode == 'P3DPS':
                self.fctxy1 = str(eval(self.FE.entry[0].expression))
                self.fctxy2 = str(eval(self.FE.entry[1].expression))
                self.FigureX.DrawBiLaTex(f'f(x)₁ = {DrawAfter(self.fctxy1)}', f'f(x)₂ = {DrawAfter(self.fctxy2)}')
                if not self.equal:
                    self.PlotFirstFunc = plt.plot3d_parametric_surface(sympify(self.fctxy1), sympify(self.fctxy2),
                                                                       self.x - self.y, show=False)
                    self.BackEndPlot.Plot(self.PlotFirstFunc)
                    self.VariableEQL(f'f(x,y)₁ =')
                    self.equal = True

                elif self.equal:
                    self.PlotAddFunc = plt.plot3d_parametric_surface(sympify(self.fctx1), sympify(self.fctx2),
                                                                     self.x - self.y, show=False)
                    self.PlotAddFunc = MultiPlot3D(self.PlotFirstFunc, self.PlotAddFunc)
                    self.BackEndPlot.Plot(self.PlotAddFunc)
                    self.VariableEQL(f'f(x,y)₁ =')

            self.ApplyAfterEqual()

        except ValueError:
            self.ErrorStrVar.set('ValueError')
        except SyntaxError:
            self.ErrorStrVar.set('SyntaxError')
        except NameError:
            self.ErrorStrVar.set('NameError')
        except TypeError:
            self.ErrorStrVar.set('TypeError')
        except OverflowError:
            self.ErrorStrVar.set('OverflowMathRangeError')
        except IndexError:
            self.ErrorStrVar.set('IndexError')

    def ApplyAfterEqual(self):
        self.FigureX.Draw(self.TkAggX)

        if self.mode == 'Operation' or self.mode == 'SystemSolver':
            self.FigureXY.Draw(self.TkAggXY)

        if self.mode == 'Plot' or self.mode == 'Plot3D':
            self.TextDisplay.Clear()

        if self.mode == 'SystemSolver':
            self.SSE().focus_set()
        elif self.mode == 'PP2D3DL' or self.mode == "P3DPS":
            self.FE().focus_set()
        else:
            self.TextDisplay.focus_set()


if __name__ == "__main__":
    # run calculator
    Calculator()
