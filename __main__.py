import sys
import matplotlib

# matplotlib.use('TkAgg')  # MUST BE CALLED BEFORE IMPORTING plot
matplotlib.use('Qt5Agg')  # MUST BE CALLED BEFORE IMPORTING plot
from __jeep_v9_2__ import *
from tkinter import *
from sympy import *
from sympy.abc import x, y, z
import sympy.plotting as plt
from sympy.solvers.solveset import solvify

"""
# version 6.3.0
# change position of setting (__author__, __version__, __name__, btn_prm, btn_dif, btnb_prm, big2_prm, ent_prm)
# improve classes of [ScrollableTkAgg {X & XY}, ScrolledListbox, TkFigurePlot, BackEndPlot] by changing self to a Canvas
# add StringVar() in text_variable and add bind Right & Left in Keyboard to class of ManagedEntry and delete them from
class of calculator
# more improving scrollbar for FigureX in ScrollableTkAggX and more speed on draw for FigureXY in ScrollableTkAggXY
# optimization in operation mode
"""
# noinspection NonAsciiCharacters
π = pi


class Calculator:
    __author__ = 'Achraf Najmi'
    __version__ = '6.3.0_b3.2'
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
                'font': ('DejaVu Sans', 12),
                'width': 5,
                'height': 1,
                'relief': 'raised',
                'activeback': '#49000A',
                'activebackground': '#80000B',
                'activeforeground': "white"}
    ent_prm = {'fg': 'black',
               'bg': '#F0F0F0',
               'font': ('DejaVu Sans', 32),
               'relief': 'flat'}

    def __init__(self):
        self.win = Tk()
        self.little_nbr = ['₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉',
                           '⏨', '₁₁', '₁₂', '₁₃', '₁₄', '₁₅', '₁₆', '₁₇', '₁₈', '₁₉',
                           '₂₀', '₂₁', '₂₂', '₂₃', '₂₄', '₂₅', '₂₆', '₂₇', '₂₈', '₂₉',
                           '₃₀', '₃₁', '₃₂', '₃₃', '₃₄', '₃₅', '₃₆', '₃₇', '₃₈', '₃₉',
                           '₄₀', '₄₁', '₄₂', '₄₃', '₄₄', '₄₅', '₄₆', '₄₇', '₄₈', '₄₉',
                           '₅₀', '₅₁', '₅₂', '₅₃', '₅₄', '₅₅', '₅₆', '₅₇', '₅₈', '₅₉',
                           '₆₀', '₆₁', '₆₂', '₆₃', '₆₄', '₆₅', '₆₆', '₆₇', '₆₈', '₆₉',
                           '₇₀', '₇₁', '₇₂', '₇₃', '₇₄', '₇₅', '₇₆', '₇₇', '₇₈', '₇₉',
                           '₈₀', '₈₁', '₈₂', '₈₃', '₈₄', '₈₅', '₈₆', '₈₇', '₈₈', '₈₉',
                           '₉₀', '₉₁', '₉₂', '₉₃', '₉₄', '₉₅', '₉₆', '₉₇', '₉₈', '₉₉']
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
        self.ErrorStrVar = StringVar()
        self.LabelStrVar = StringVar()
        # ROW 0 top canvas==============================================================================================
        top_canvas = Canvas(self.win, relief='flat', bg='#F0F0F0', width=42)
        top_canvas.grid(row=0, column=0, columnspan=2, sticky=NSEW)
        top_canvas.rowconfigure(0, weight=1)
        top_canvas.columnconfigure(1, weight=1)
        # ROW 1 middle top Canvas=======================================================================================
        self.middle_top_canvas = Canvas(self.win, relief='flat', background='#212121')
        self.middle_top_canvas.grid(row=1, column=0, columnspan=2, sticky=NSEW)
        self.middle_top_canvas.rowconfigure(0, weight=1)
        self.middle_top_canvas.columnconfigure(0, weight=1)
        # ROW 2 set canvas showing top buttons==========================================================================
        self.middle_canvas = Canvas(self.win, relief='flat')
        self.middle_canvas.grid(row=2, column=0, sticky=NSEW)
        self.middle_canvas.rowconfigure(0, weight=1)
        self.middle_canvas.columnconfigure(0, weight=1)
        self.middle_canvas.columnconfigure(1, weight=1)
        self.middle_canvas.columnconfigure(2, weight=1)
        self.middle_canvas.columnconfigure(3, weight=1)
        self.middle_canvas.columnconfigure(4, weight=1)
        # ROW 2 set canvas switching ScrollableTkAggXY & ScrolledListbox & FigureCanvasTkAgg & NavigationToolbar2Tk=====
        self.east_canvas = Canvas(self.win, relief='flat', bg='#F0F0F0')
        self.east_canvas.grid(row=2, column=1, rowspan=3, sticky=NSEW)
        self.east_canvas.rowconfigure(0, weight=1)
        self.east_canvas.columnconfigure(0, weight=1)
        # ROW 3 set canvas showing middle bottom buttons================================================================
        self.middle_bottom_canvas = Canvas(self.win, relief='flat')
        self.middle_bottom_canvas.grid(row=3, column=0, sticky=NSEW)
        self.middle_bottom_canvas.rowconfigure(0, weight=1)
        self.middle_bottom_canvas.rowconfigure(1, weight=1)
        self.middle_bottom_canvas.rowconfigure(2, weight=1)
        self.middle_bottom_canvas.columnconfigure(0, weight=1)
        self.middle_bottom_canvas.columnconfigure(1, weight=1)
        self.middle_bottom_canvas.columnconfigure(2, weight=1)
        self.middle_bottom_canvas.columnconfigure(3, weight=1)
        self.middle_bottom_canvas.columnconfigure(4, weight=1)
        self.middle_bottom_canvas.columnconfigure(5, weight=1)
        # ROW 4 set canvas showing bottom buttons=======================================================================
        self.bottom_canvas = Canvas(self.win, relief='flat')
        self.bottom_canvas.grid(row=4, column=0, sticky=NSEW)
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
        EqualLabelDisplay = Label(top_canvas, **self.ent_prm, textvariable=self.LabelStrVar)
        EqualLabelDisplay.grid(row=0, column=0, sticky=NSEW)
        EqualLabelDisplay.configure(anchor='e')
        # Text Display, insertbackground='white'
        self.TextDisplay = ManagedEntry(top_canvas, **self.ent_prm, insertwidth=2)
        self.TextDisplay.grid(row=0, column=1, sticky=NSEW)
        # Error Label Display, cursor="arrow", cursor="hand1"
        ErrorLabelDisplay = Label(top_canvas, **self.ent_prm, textvariable=self.ErrorStrVar)
        ErrorLabelDisplay.grid(row=0, column=2, sticky=NSEW)
        ErrorLabelDisplay.configure(anchor='e')
        # ROW 1 set MathPlot LaTex Display==============================================================================
        mpl_white_rgb = (255. / 255., 255. / 255., 255. / 255.)
        self.FigureX = FigureX(figsize=(1, 1), facecolor='#212121', rgbcolor=mpl_white_rgb, fontsize=32)
        self.TkAggX = ScrollableTkAggX(figure=self.FigureX, master=self.middle_top_canvas)
        self.TkAggX.configure(relief='flat', background='#212121')
        self.TkAggX.grid(row=0, column=0, sticky=NSEW)
        # buttons that will be fake displayed on middle canvas ROW 0====================================================
        big_txt = ['', '', '', '', '']
        self.btn_b = []
        for k in range(5):
            self.btn_b.append(HoverButton(self.middle_canvas, **self.big2_prm, text=big_txt[k]))
        # ROW 2 set canvas showing ScrolledListbox======================================================================
        self.FullTextDisplay = ScrolledListbox(self.east_canvas, width=52, height=8, **self.ent_prm)
        self.FullTextDisplay.configure(font=('DejaVu Sans', 22))
        self.FullTextDisplay.grid(row=0, column=0, sticky=NSEW)
        # ROW 2 set canvas showing ScrollableTkAggXY====================================================================
        self.FigureXY = FigureXY(figsize=(1, 1), fontsize=20, facecolor='#F0F0F0')
        self.TkAggXY = ScrollableTkAggXY(figure=self.FigureXY, master=self.east_canvas)
        self.TkAggXY.grid(row=0, column=0, sticky=NSEW)
        # ROW 2 set canvas showing BackEndPlot==========================================================================
        self.BackEndPlot = BackEndPlot(master=self.east_canvas, figsize=(6, 3))
        self.BackEndPlot.grid(row=0, column=0, sticky=NSEW)
        # buttons that will be displayed on middle bottom canvas ROW 0==================================================
        txta = ['Û', 'Ü', '1ST']
        self.btn_m1 = []
        for i1 in range(3):
            self.btn_m1.append(HoverButton(self.middle_bottom_canvas, **self.btn_dif, text=txta[i1], cursor="hand2"))
            self.btn_m1[i1].grid(row=0, column=i1, sticky=NSEW)
        # Cursor Disposition
        self.btn_m1[0]['command'] = lambda: self.TextDisplay.DirectionCursor('Left')
        self.btn_m1[1]['command'] = lambda: self.TextDisplay.DirectionCursor('Right')

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
            self.btn_d[i4].configure(
                command=lambda f0=logarithm_pad[i4]: [self.Input(f0), self.Input(')'),
                                                      self.TextDisplay.DirectionCursor('Left')])
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
        # (
        self.btn[4]['command'] = lambda f2=btn[4]: [self.Input(f2), self.Input(')'),
                                                    self.TextDisplay.DirectionCursor('Left')]
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
        self.SwitchButtons('1st'), self.SwitchMode('Operation', True)
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
                         command=lambda: [self.SwitchButtons('1st'), self.SwitchMode("Operation", True)])
        Mode.add_command(label='Function',
                         command=lambda: [self.SwitchButtons('1st'), self.SwitchMode('Function', True)])
        Mode.add_command(label="Simple Line Equation",
                         command=lambda: [self.SwitchButtons('1st'), self.SwitchMode('Equation', True)])
        Mode.add_command(label='Line Equation Solver',
                         command=lambda: [self.SwitchButtons('1st'), self.SwitchMode('Solve', True)])
        Mode.add_command(label='System Equation Solver',
                         command=lambda: [self.SwitchButtons('1st'), self.SwitchMode('Matrices', True)])
        Mode.add_separator()
        Mode.add_command(label='Plot',
                         command=lambda: [self.SwitchButtons('2nd'), self.SwitchMode('Plot', True)])
        Mode.add_command(label='Plot Parametric',
                         command=lambda: [self.SwitchButtons('2nd'), self.SwitchMode('Plot Prm', True)])
        Mode.add_command(label='Plot 3D',
                         command=lambda: [self.SwitchButtons('2nd'), self.SwitchMode('Plot3D', True)])
        Mode.add_command(label='Plot 3D Parametric Line',
                         command=lambda: [self.SwitchButtons('2nd'), self.SwitchMode('P3DPL', True)])
        Mode.add_command(label='Plot 3D Parametric Surface',
                         command=lambda: [self.SwitchButtons('2nd'), self.SwitchMode('P3DPS', True)])
        # Configuration Master Display==================================================================================
        self.win.rowconfigure(1, weight=1)
        self.win.columnconfigure(1, weight=1)

        self.win.bind_all('<Key>', self.KeyboardInput)
        self.win.iconbitmap('Alecive-Flatwoken-Apps-Libreoffice-Math-B.ico')
        self.win.configure(menu=menubare, bg='#4d4d4d')
        self.win.geometry("1100x680")
        self.win.minsize(width=420, height=680)
        self.win.resizable(width=True, height=True)
        self.win.title(u"%s v%s" % (self.__name__, self.__version__))
        self.win.update()
        self.win.mainloop()

    def SwitchButtons(self, side):
        page = side
        # buttons to switch between buttons those will be displayed on middle bottom & middle canvas
        if page == '1st':
            # buttons that will be displayed on middle canvas ROW 0=====================================================
            for i in range(5):
                self.btn_b[i].destroy()
            big_txt = ['Operation', 'Function', "Simple\nLine\nEquation", 'Line\nEquation\nSolver',
                       'System\nEquation\nSolver']
            big_pad = ['Operation', 'Function', 'Equation', 'Solve', 'Matrices']
            self.btn_a = []
            for i in range(5):
                self.btn_a.append(HoverButton(self.middle_canvas, **self.big2_prm, text=big_txt[i], cursor="hand2"))
                self.btn_a[i].grid(row=0, column=i, sticky=NSEW)
                self.btn_a[i]["command"] = lambda f3=big_pad[i]: self.SwitchMode(f3, True)

            # buttons that will be displayed on middle bottom canvas ROW 0==============================================
            # 2nd
            self.btn_m1[2].configure(text="1ST", command=lambda: self.SwitchButtons("2nd"),
                                     font=('DejaVu Sans', 17))
            # ROW 1
            # ========================Trigonometry======================================================================
            Trigonometry_pad = ['cos(', 'sin(', "tan(", 'cosh(', 'sinh(', "tanh("]
            Trigonometry_txt = ['cos', 'sin', "tan", 'cosh', 'sinh', "tanh"]
            for i in range(6):
                self.btn_u[i].configure(
                    text=Trigonometry_txt[i],
                    command=lambda f4=Trigonometry_pad[i]: [self.Input(f4), self.Input(')'),
                                                            self.TextDisplay.DirectionCursor('Left')])

            self.btn_d[3].configure(
                text='∫f(x)',
                command=lambda: [self.Input('integrate('), self.Input(')'), self.TextDisplay.DirectionCursor('Left')])

            self.btn_d[2].configure(
                text='W₀',
                command=lambda: [self.Input('LambertW('), self.Input(')'), self.TextDisplay.DirectionCursor('Left')])

            self.btn[28].configure(text='10ˣ', command=lambda: self.Input('e+'))

            if self.mode == 'Operation' or self.mode == 'Function' or self.mode == 'Equation' or self.mode == 'Solve' \
                    or self.mode == 'Matrices':
                self.SwitchMode(self.mode, False)

        elif page == '2nd':
            # buttons that will be displayed on middle canvas ROW 0=====================================================
            for i in range(5):
                self.btn_a[i].destroy()
            big_txt = ['Plot\nf(x)', 'Plot\nParametric', 'Plot 3D\nParametric\nLine', "Plot3D\nf(x,y)",
                       'Plot 3D\nParametric\nSurface']
            big_pad = ['Plot', 'Plot Prm', 'P3DPL', "Plot3D", 'P3DPS']
            self.btn_b = []
            for i in range(5):
                self.btn_b.append(HoverButton(self.middle_canvas, **self.big2_prm, text=big_txt[i], cursor="hand2"))
                self.btn_b[i].grid(row=0, column=i, sticky=NSEW)
                self.btn_b[i]["command"] = lambda f5=big_pad[i]: self.SwitchMode(f5, True)

            # buttons that will be displayed on middle bottom canvas ROW 0==============================================
            # 1st
            self.btn_m1[2].configure(text="2ND", command=lambda: self.SwitchButtons("1st"),
                                     font=('DejaVu Sans', 17))
            # ROW 1
            # ========================Trigonometry======================================================================
            Trigonometry_pad = ['acos(', 'asin(', "atan(", 'acosh(', 'asinh(', "atanh("]
            Trigonometry_txt = ['acos', 'asin', "atan", 'acosh', 'asinh', "atanh"]
            for i in range(6):
                self.btn_u[i].configure(
                    text=Trigonometry_txt[i],
                    command=lambda f6=Trigonometry_pad[i]: [self.Input(f6), self.Input(')'),
                                                            self.TextDisplay.DirectionCursor('Left')])

            self.btn_d[3].configure(
                text='d/dx',
                command=lambda: [self.Input('diff('), self.Input(')'), self.TextDisplay.DirectionCursor('Left')])

            self.btn_d[2].configure(
                text='W₋₁',
                command=lambda: [self.Input('LambertW('), self.Input(',-1)'), self.TextDisplay.DirectionCursor('Left')])

            self.btn[28].configure(text='10¯ˣ', command=lambda: self.Input('e-'))

            if self.mode == 'Plot' or self.mode == 'Plot Prm' or self.mode == 'P3DPL' or self.mode == "Plot3D" or \
                    self.mode == 'P3DPS':
                self.SwitchMode(self.mode, False)

    def SwitchMode(self, passmode, do_it):
        self.mode = passmode
        self.switched = do_it
        if self.switched:
            if self.mode == 'Operation' or self.mode == 'Solve' or self.mode == 'Matrices':
                self.SwitchWidget('TkAgg')
            elif self.mode == 'Equation' or self.mode == 'Function':
                self.SwitchWidget('listbox')
                self.FullTextDisplay.delete(0, END)
            else:
                self.SwitchWidget('plot')

        if self.mode == 'Operation':
            if self.switched:
                self.FigureXY.DrawLaTex(f'Mode Operation : ')
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
                self.FigureXY.DrawLaTex('Mode Line Equation Solver : One {eq} : [x] | Constants : (y,z)')
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
                self.FigureXY.DrawLaTex('Mode System Equation Solver :')
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
            if self.mode == 'Operation' or self.mode == 'Solve' or self.mode == 'Matrices':
                self.FigureXY.Draw(self.TkAggXY)

        self.TextDisplay.focus_set()

    def SwitchWidget(self, widget):
        figure = widget
        self.east_canvas.destroy()
        self.east_canvas = Canvas(self.win, relief='flat', bg='#F0F0F0')
        self.east_canvas.grid(row=2, column=1, rowspan=3, sticky=NSEW)
        self.east_canvas.rowconfigure(0, weight=1)
        self.east_canvas.columnconfigure(0, weight=1)

        if figure == 'listbox':
            self.FullTextDisplay = ScrolledListbox(self.east_canvas, width=52, height=8, **self.ent_prm)
            self.FullTextDisplay.configure(font=('DejaVu Sans', 22))
            self.FullTextDisplay.grid(row=0, column=0, sticky=NSEW)

        elif figure == 'TkAgg':
            self.FigureXY.Clear()
            self.TkAggXY = ScrollableTkAggXY(figure=self.FigureXY, master=self.east_canvas)
            self.TkAggXY.grid(row=0, column=0, sticky=NSEW)

        elif figure == 'plot':
            self.BackEndPlot = BackEndPlot(master=self.east_canvas, figsize=(6, 3))
            self.BackEndPlot.grid(row=0, column=0, sticky=NSEW)

        self.TextDisplay.focus_set()

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
        self.ErrorStrVar.set('')
        self.FigureX.clear()
        self.TextDisplay.ResetClear()

        if self.mode == 'Operation':
            self.LabelStrVar.set('op >')
            self.FigureX.DrawTexTk('op >')

        elif self.mode == 'Function':
            self.LabelStrVar.set(f'From :')
            self.FigureX.DrawTexTk('From : A --> To : B | f(x) = Function')

        elif self.mode == 'Equation':
            self.LabelStrVar.set(f'a =')
            self.FigureX.DrawTexTk('ax² + bx + c = 0')

        elif self.mode == 'Solve':
            self.LabelStrVar.set(f'eq >')
            self.FigureX.DrawTexTk('eq >')

        elif self.mode == 'Matrices':
            self.LabelStrVar.set('eq₁ >')
            self.FigureX.DrawTexTk('eq₁ >')

        elif self.mode == 'Plot':
            self.LabelStrVar.set('f(x) =')
            self.FigureX.DrawTexTk('f(x) = ')

        elif self.mode == "Plot Prm" or self.mode == "P3DPL":
            self.LabelStrVar.set('f(x)₁ =')
            self.FigureX.DrawTexTk('f(x)₁ = ')

        elif self.mode == 'Plot3D':
            self.LabelStrVar.set('f(x,y) =')
            self.FigureX.DrawTexTk('f(x,y) = ')

        elif self.mode == "P3DPS":
            self.LabelStrVar.set('f(x,y)₁ =')
            self.FigureX.DrawTexTk('f(x,y)₁ = ')

        self.equal = False
        self.clear = False
        self.full = None
        self.exist = None

        self.TextDisplay.focus_set()

        self.FigureX.Draw(self.TkAggX)

    def Remove(self):
        if self.clear:
            self.Delete()

        try:
            self.TextDisplay.RemoveFromString()
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
                self.Input('exp('), self.Input(')'), self.TextDisplay.DirectionCursor('Left')

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
                self.Input('('), self.Input(')'), self.TextDisplay.DirectionCursor('Left')

            elif put == 'parenright':
                self.Input(')')

            elif put == 'backslash' or put == 'bar':
                self.Input('sqrt('), self.Input(')'), self.TextDisplay.DirectionCursor('Left')

            elif keyword.keysym == 's':
                self.Input('sin('), self.Input(')'), self.TextDisplay.DirectionCursor('Left')

            elif keyword.keysym == 'c':
                self.Input('cos('), self.Input(')'), self.TextDisplay.DirectionCursor('Left')

            elif keyword.keysym == 't':
                self.Input('tan('), self.Input(')'), self.TextDisplay.DirectionCursor('Left')

            elif keyword.keysym == 'S':
                self.Input('sinh('), self.Input(')'), self.TextDisplay.DirectionCursor('Left')

            elif keyword.keysym == 'C':
                self.Input('cosh('), self.Input(')'), self.TextDisplay.DirectionCursor('Left')

            elif keyword.keysym == 'T':
                self.Input('tanh('), self.Input(')'), self.TextDisplay.DirectionCursor('Left')

            elif keyword.keysym == 'l':
                self.Input('log('), self.Input(')'), self.TextDisplay.DirectionCursor('Left')

            elif keyword.keysym == 'I':
                self.Input('oo')

            elif keyword.keysym == 'i':
                self.Input('integrate('), self.Input(')'), self.TextDisplay.DirectionCursor('Left')

            elif put == 'd':
                self.Input('diff('), self.Input(')'), self.TextDisplay.DirectionCursor('Left')

            elif keyword.keysym == 'w':
                self.Input('LambertW('), self.Input(')'), self.TextDisplay.DirectionCursor('Left')

            elif keyword.keysym == 'W':
                self.Input('LambertW('), self.Input(',-1)'), self.TextDisplay.DirectionCursor('Left')

            elif put == 'j':
                self.Input('1j')

            elif put == 'exclam' or put == 'f':
                self.Input('fctrl('), self.Input(')'), self.TextDisplay.DirectionCursor('Left')

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

        self.TextDisplay.InsertIntoString(keyword)

        self.ShowInput()

    def ShowInput(self):
        try:
            if self.mode == 'Operation':
                self.LabelStrVar.set('op >')
                self.answer = sympify(self.TextDisplay.expression, evaluate=True)

                expr_str = DrawBefore(self.TextDisplay.expression)
                result_expr = DrawAfter(self.answer)
                result_num = DrawAfterNum(self.answer)

                norm = str(result_expr).replace('$', '')
                dot_zero = str(result_num).replace('.0', '').replace('$', '')

                if expr_str == result_expr and str('log') in str(self.TextDisplay.expression) \
                        or str('exp') in str(self.TextDisplay.expression):
                    self.FigureX.DrawTexTk(f'op > {self.TextDisplay.expression} = {result_expr} = {result_num}')

                elif dot_zero == norm or result_expr == result_num:
                    self.FigureX.DrawTexTk(f'op > {expr_str} = {result_expr}')
                else:
                    self.FigureX.DrawTexTk(f'op > {expr_str} = {result_expr} = {result_num}')

            elif self.mode == 'Function':
                if self.full is None:
                    self.LabelStrVar.set('From :')
                    self.FigureX.DrawTexTk(
                        f'From : {DrawAfter(self.TextDisplay.expression)} --> To : B | f(x) = Function')

                elif not self.full:
                    self.LabelStrVar.set('To :')
                    self.FigureX.DrawTexTk(
                        f'From : {DrawAfter(self.v)} --> To : '
                        f'{DrawAfter(self.TextDisplay.expression)} | f(x) = Function')

                elif self.full:
                    self.LabelStrVar.set('f(x) =')
                    self.FigureX.DrawTexTk(
                        f'From : {DrawAfter(self.v)} --> To : {DrawAfter(self.w)} | '
                        f'f(x) = {DrawAfter(self.TextDisplay.expression)}')

            elif self.mode == 'Equation':
                if self.full is None:
                    self.LabelStrVar.set('a =')
                    self.FigureX.DrawTexTk(
                        f'{DrawAfter(self.TextDisplay.expression)}x² + bx + c = 0')

                elif not self.full:
                    self.LabelStrVar.set('b =')
                    self.FigureX.DrawTexTk(
                        f'{DrawAfter(self.a)}x² + ({DrawAfter(self.TextDisplay.expression)})x + c = 0')

                elif self.full:
                    self.LabelStrVar.set('c =')
                    self.FigureX.DrawTexTk(
                        f'{DrawAfter(self.a)}x² + ({DrawAfter(self.b)})x + '
                        f'({DrawAfter(self.TextDisplay.expression)}) = 0')

            elif self.mode == 'Solve':
                if self.full is None:
                    self.LabelStrVar.set('eq >')
                    self.FigureX.DrawTexTk(f'eq > {DrawAfter(self.TextDisplay.expression)}')
                elif self.full:
                    self.LabelStrVar.set(f'eq > {self.q} =')
                    self.FigureX.DrawTexTk(
                        f'eq > {DrawAfter(self.q)} = '
                        f'{DrawAfter(self.TextDisplay.expression)}')

            elif self.mode == 'Matrices':
                if self.full is None:
                    self.LabelStrVar.set(f'eq₁ >')
                    self.FigureX.DrawTexTk(f'eq₁ > {DrawAfter(self.TextDisplay.expression)}')
                elif not self.full:
                    self.LabelStrVar.set(f'eq₁ > {self.q} = ')
                    self.FigureX.DrawTexTk(f'eq₁ > {DrawAfter(self.q)} = {DrawAfter(self.TextDisplay.expression)}')

                elif self.full:
                    if self.clear is None:
                        self.LabelStrVar.set(f'eq₂ >')
                        self.FigureX.DrawTexTk(f'eq₂ > {DrawAfter(self.TextDisplay.expression)}')
                    elif not self.clear and self.equal is None:
                        self.LabelStrVar.set(f'eq₂ > {self.j} =')
                        self.FigureX.DrawTexTk(f'eq₂ > {DrawAfter(self.j)} = {DrawAfter(self.TextDisplay.expression)}')

                    elif not self.clear and not self.equal:
                        self.LabelStrVar.set(f'eq₃ >')
                        self.FigureX.DrawTexTk(f'eq₃ > {DrawAfter(self.TextDisplay.expression)}')
                    elif not self.clear and self.equal:
                        self.LabelStrVar.set(f'eq₃ > {self.m} =')
                        self.FigureX.DrawTexTk(f'eq₃ > {DrawAfter(self.m)} = {DrawAfter(self.TextDisplay.expression)}')

            elif self.mode == 'Plot':
                self.LabelStrVar.set(f'f(x) =')
                self.FigureX.DrawTexTk(f'f(x) = {DrawAfter(self.TextDisplay.expression)}')

            elif self.mode == "Plot Prm" or self.mode == "P3DPL":
                if self.full is None:
                    self.LabelStrVar.set(f'f(x)₁ =')
                    self.FigureX.DrawTexTk(f'f(x)₁ = {DrawAfter(self.TextDisplay.expression)}')

                elif self.full:
                    self.LabelStrVar.set(f'f(x)₂ =')
                    self.FigureX.DrawTexTk(f'f(x)₁ = {DrawAfter(self.fctx1)} | '
                                           f'f(x)₂ = {DrawAfter(self.TextDisplay.expression)}')

            elif self.mode == "Plot3D":
                self.LabelStrVar.set(f'f(x,y) =')
                self.FigureX.DrawTexTk(f'f(x,y) = {DrawAfter(self.TextDisplay.expression)}')

            elif self.mode == "P3DPS":
                if self.full is None:
                    self.LabelStrVar.set(f'f(x,y)₁ =')
                    self.FigureX.DrawTexTk(f'f(x,y)₁ = {DrawAfter(self.TextDisplay.expression)}')

                elif self.full:
                    self.LabelStrVar.set(f'f(x,y)₂ =')
                    self.FigureX.DrawTexTk(f'f(x,y)₁ = {DrawAfter(self.fctxy1)} | '
                                           f'f(x,y)₂ = {DrawAfter(self.TextDisplay.expression)}')

            self.ErrorStrVar.set('')

            self.FigureX.Draw(self.TkAggX)
        except Exception:
            pass
        self.TextDisplay.focus_set()

        self.TextDisplay.icursor(self.TextDisplay.index_cursor)

    def VariableEQL(self, label_var):
        self.TextDisplay.StringVariable('')
        self.LabelStrVar.set(label_var)

    def ShowEqual(self):
        try:
            if self.mode == 'Operation':
                if not self.equal:
                    self.answer = sympify(self.TextDisplay.expression, evaluate=True)
                    self.VariableEQL(f'op > {self.TextDisplay.expression} = {self.answer}')
                    expr_str = DrawBefore(self.TextDisplay.expression)
                    result_expr = DrawAfter(self.answer)
                    result_num = DrawAfterNum(self.answer)
                    norm = str(result_expr).replace('$', '')
                    dot_zero = str(result_num).replace('.0', '').replace('$', '')

                    if expr_str == result_expr and str('log') in str(self.TextDisplay.expression) \
                            or str('exp') in str(self.TextDisplay.expression):
                        self.FigureX.DrawTexTk(f'op > {self.TextDisplay.expression} = {result_expr} = {result_num}')
                        self.FigureXY.DrawLaTex(f'op > {self.TextDisplay.expression}')
                        self.FigureXY.DrawLaTex(f'= {result_expr}')
                        self.FigureXY.DrawLaTex(f'= {result_num}')

                    elif dot_zero == norm or result_expr == result_num:
                        self.FigureX.DrawTexTk(
                            f'op > {expr_str} = {result_expr}')
                        self.FigureXY.DrawLaTex(f'op > {expr_str}')
                        self.FigureXY.DrawLaTex(f'= {result_expr}')
                    else:
                        self.FigureX.DrawTexTk(
                            f'op > {expr_str} = {result_expr}'
                            f' = {result_num}')
                        self.FigureXY.DrawLaTex(f'op > {expr_str}')
                        self.FigureXY.DrawLaTex(f'= {result_expr}')
                        self.FigureXY.DrawLaTex(f'= {result_num}')
                    self.clear = True
                    self.equal = True

                elif self.equal:
                    self.answer = self.TextDisplay.FullReBuild(self.callback)
                    self.answer = sympify(self.answer, evaluate=True)
                    self.VariableEQL(f'op > {self.TextDisplay.expression} = {self.answer}')
                    expr_str = DrawBefore(self.TextDisplay.expression)
                    result_expr = DrawAfter(self.answer)
                    result_num = DrawAfterNum(self.answer)
                    norm = str(result_expr).replace('$', '')
                    dot_zero = str(result_num).replace('.0', '').replace('$', '')

                    if expr_str == result_expr and str('log') in str(self.TextDisplay.expression) \
                            or str('exp') in str(self.TextDisplay.expression):
                        self.FigureX.DrawTexTk(f'op > {self.TextDisplay.expression} = {result_expr}')
                        self.FigureXY.DrawLaTex(f'op > {self.TextDisplay.expression}')
                        self.FigureXY.DrawLaTex(f'= {result_expr}')

                    elif dot_zero == norm or result_expr == result_num:
                        self.FigureX.DrawTexTk(
                            f'op > {expr_str} = {result_expr}')
                        self.FigureXY.DrawLaTex(f'op > {expr_str}')
                        self.FigureXY.DrawLaTex(f'= {result_expr}')
                    else:
                        self.FigureX.DrawTexTk(
                            f'op > {expr_str} = {result_expr}'
                            f' = {result_num}')
                        self.FigureXY.DrawLaTex(f'op > {expr_str}')
                        self.FigureXY.DrawLaTex(f'= {result_expr}')
                        self.FigureXY.DrawLaTex(f'= {result_num}')
                self.callback.append(str(self.answer))

            elif self.mode == 'Function':
                if self.full is None:
                    self.v = int(eval(self.TextDisplay.expression))
                    self.FullTextDisplay.insert(END, f'from : {self.TextDisplay.expression}')
                    self.VariableEQL(f'To :')
                    self.full = False

                elif not self.full:
                    self.w = int(eval(self.TextDisplay.expression)) + 1
                    self.FullTextDisplay.insert(END, f'To : {self.TextDisplay.expression}')
                    self.VariableEQL(f'f(x) =')
                    self.full = True

                elif self.full:
                    if not self.equal:
                        self.fctx = str(eval(self.TextDisplay.expression))
                        self.FullTextDisplay.insert(END, f'f(x) = {sympify(self.fctx)}')
                        for x in range(self.v, self.w):
                            sup = sympify(eval(self.fctx)).evalf(3)
                            self.FullTextDisplay.insert(END, f'f({x}) = {sup}')
                        self.PlotFirstFunc = plt.plot(sympify(self.fctx), (self.x, self.v, int(self.w) - 1), show=False,
                                                      legend=True)
                        OnePlotLaTex(self.PlotFirstFunc, self.fctx)
                        self.VariableEQL(f'f(x) =')
                        self.equal = True

                    elif self.equal:
                        self.fctx = str(eval(self.TextDisplay.expression))
                        self.FullTextDisplay.insert(END, f'f(x) = {self.fctx}')
                        for x in range(self.v, self.w):
                            sup = sympify(eval(self.fctx)).evalf(3)
                            self.FullTextDisplay.insert(END, f'f({x}) = {sup}')
                        self.PlotAddFunc = plt.plot(sympify(self.fctx), (self.x, self.v, int(self.w) - 1), legend=True,
                                                    show=False)
                        TwoPlotMultiColor(self.PlotFirstFunc, self.PlotAddFunc, self.fctx)
                        self.VariableEQL(f'f(x) =')

            elif self.mode == 'Equation':
                if self.full is None:
                    self.a = self.TextDisplay.expression
                    self.VariableEQL(f'b =')
                    self.full = False

                elif not self.full:
                    self.b = self.TextDisplay.expression
                    self.VariableEQL(f'c =')
                    self.full = True

                elif self.full:
                    self.c = self.TextDisplay.expression
                    self.VariableEQL(f'a = {self.a} | b = {self.b} | c = {self.c}')
                    self.FigureX.DrawTexTk(f'{DrawAfter(self.a)}x² + ({DrawAfter(self.b)})x + '
                                           f'({DrawAfter(self.c)}) = 0')
                    qe = int(len(EQT(self.a, self.b, self.c)))
                    for eq in range(qe):
                        self.FullTextDisplay.insert(END, EQT(self.a, self.b, self.c)[eq])

                    self.clear = True
                    self.full = None

            elif self.mode == 'Solve':
                if self.full is None:
                    self.q = str(eval(self.TextDisplay.expression))
                    self.VariableEQL(f'eq > {self.q} =')
                    self.FigureX.DrawTexTk(f'eq > {DrawAfter(self.q)} = ')
                    self.full = True

                elif self.full:
                    self.p = str(eval(self.TextDisplay.expression))
                    self.VariableEQL(f'eq > {self.q} = {self.p}')
                    # try:
                    #     self.SolutionOS = solvify(Eq(sympify(self.q), sympify(self.p)), self.x, self.C)
                    #     print('complex')
                    #     if self.SolutionOS is None:
                    #         self.SolutionOS = solvify(Eq(sympify(self.q), sympify(self.p)), self.x, self.R)
                    #         print('real')
                    # except Exception:
                    try:
                        self.SolutionOS = solve(Eq(sympify(self.q), sympify(self.p)), self.x)
                        print('all')
                    except Exception:
                        self.FigureX.DrawTexTk('Cannot Solve This Equation')
                    self.FigureX.DrawTexTk(
                        f'eq > {DrawBefore(self.q)} = {DrawBefore(self.p)} > Solution : {DrawAfter(self.SolutionOS)}')
                    self.FigureXY.DrawLaTex(f'eq > {DrawBefore(self.q)} = {DrawBefore(self.p)}')
                    self.FigureXY.DrawLaTex(f'Solution : {DrawAfter(self.SolutionOS)}')
                    much_x = len(self.SolutionOS)
                    # print(str(much_x)[1:2])
                    for sl in range(much_x):
                        self.FigureXY.DrawLaTex(
                            f'> x{self.little_nbr[sl]} = {DrawAfter(self.SolutionOS[sl])}')

                    self.clear = True
                    self.full = None

            elif self.mode == 'Matrices':
                if self.full is None:
                    self.q = str(sympify(self.TextDisplay.expression))
                    self.VariableEQL(f'eq₁ > {self.q} =')
                    self.full = False

                elif not self.full:
                    self.p = str(sympify(self.TextDisplay.expression))
                    self.VariableEQL('eq₂ >')
                    self.FigureX.DrawTexTk('eq₂ > ')
                    self.FigureXY.DrawLaTex('New System :')
                    self.FigureXY.DrawLaTex(f' eq₁ | {DrawBefore(self.q)} = {DrawBefore(self.p)}')
                    self.full = True
                    self.clear = None

                elif self.full:
                    if self.clear is None:
                        self.j = str(sympify(self.TextDisplay.expression))
                        self.VariableEQL(f'eq₂ > {self.j} =')
                        self.equal = None
                        self.clear = False

                    elif not self.clear:
                        if self.equal is None:
                            self.k = str(sympify(self.TextDisplay.expression))
                            self.FigureXY.DrawLaTex(f' eq₂ | {DrawBefore(self.j)} = {DrawBefore(self.k)}')
                            try:
                                self.SolutionTT = linsolve(
                                    [Eq(sympify(self.q), sympify(self.p)), Eq(sympify(self.j), sympify(self.k))],
                                    [self.x, self.y])
                            except Exception:
                                self.SolutionTT = nonlinsolve(
                                    [Eq(sympify(self.q), sympify(self.p)), Eq(sympify(self.j), sympify(self.k))],
                                    [self.x, self.y])
                            sol = str(self.SolutionTT)
                            self.w = int(len(sol))
                            self.v = 0
                            while self.v < self.w:
                                self.exist = False
                                if sol[self.v] == 'z' or sol == 'EmptySet':
                                    self.VariableEQL('eq₃ >')
                                    self.FigureX.DrawTexTk('eq₃ > ')
                                    self.equal = False
                                    self.exist = True
                                    if sol == 'EmptySet':
                                        self.VariableEQL('Empty Solution : ∅')
                                        self.FigureX.DrawTexTk(f'Empty Solution : {DrawAfter(self.SolutionTT)}')
                                        self.FigureXY.DrawLaTex(f'Empty Solution : {DrawAfter(self.SolutionTT)}')
                                        self.clear = True
                                        self.full = None
                                    break
                                self.v += 1

                            if not self.exist:
                                self.VariableEQL('System of Two Equations : {eq₁,eq₂}_[x,y]')
                                self.FigureX.DrawTexTk(f'Solution : {DrawAfter(self.SolutionTT)}')
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
                                        self.VariableEQL(f'x = {self.xexp} | y = {self.yexp}')
                                    except Exception:
                                        pass
                                try:
                                    self.FigureXY.DrawLaTex(f'> x = {DrawAfter(self.xexp)}')
                                    self.FigureXY.DrawLaTex(f'> y = {DrawAfter(self.yexp)}')
                                except Exception:
                                    pass
                                self.clear = True
                                self.full = None

                        elif not self.equal:
                            self.m = str(sympify(self.TextDisplay.expression))
                            self.VariableEQL(f'eq₃ > {self.m} =')
                            self.equal = True

                        elif self.equal:
                            self.n = str(sympify(self.TextDisplay.expression))
                            self.FigureXY.DrawLaTex(f' eq₃ | {DrawBefore(self.m)} = {DrawBefore(self.n)}')
                            try:
                                self.SolutionTT = linsolve(
                                    [Eq(sympify(self.q), sympify(self.p)), Eq(sympify(self.j), sympify(self.k)),
                                     Eq(sympify(self.m), sympify(self.n))], [self.x, self.y, self.z])
                            except Exception:
                                self.SolutionTT = nonlinsolve(
                                    [Eq(sympify(self.q), sympify(self.p)), Eq(sympify(self.j), sympify(self.k)),
                                     Eq(sympify(self.m), sympify(self.n))], [self.x, self.y, self.z])

                            sol = str(self.SolutionTT)
                            if sol == 'EmptySet':
                                self.VariableEQL('Empty Solution : ∅')
                                self.FigureX.DrawTexTk(f'Empty Solution : {DrawAfter(self.SolutionTT)}')
                                self.FigureXY.DrawLaTex(f'Empty  Solution : {DrawAfter(self.SolutionTT)}')

                            else:
                                self.VariableEQL('System of Three Equations : {eq₁,eq₂,eq₃}_[x,y,z]')
                                self.FigureX.DrawTexTk(f'Solution : {DrawAfter(self.SolutionTT)}')
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
                                        self.VariableEQL(f'x = {self.xexp} | y = {self.yexp} | z = {self.zexp}')
                                    except Exception:
                                        pass
                                try:
                                    self.FigureXY.DrawLaTex(f'> x = {DrawAfter(self.xexp)}')
                                    self.FigureXY.DrawLaTex(f'> y = {DrawAfter(self.yexp)}')
                                    self.FigureXY.DrawLaTex(f'> z = {DrawAfter(self.zexp)}')
                                except Exception:
                                    pass
                            self.clear = True
                            self.full = None

            elif self.mode == 'Plot':
                if self.full is None:
                    self.fctx = str(eval(self.TextDisplay.expression))
                    self.PlotFirstFunc = plt.plot(sympify(self.fctx), ylim=(-10, 10), xlim=(-10, 10), legend=True,
                                                  show=False)
                    self.PlotFirstFunc = FirstPlotLaTex(self.PlotFirstFunc, self.fctx)
                    self.BackEndPlot.Plot(self.PlotFirstFunc)
                    self.VariableEQL(f'f(x) =')
                    self.full = True

                elif self.full:
                    self.fctx = str(eval(self.TextDisplay.expression))
                    self.PlotAddFunc = plt.plot(sympify(self.fctx), ylim=(-10, 10), xlim=(-10, 10), legend=True,
                                                show=False)
                    self.PlotAddFunc = MultiPlot2D(self.PlotFirstFunc, self.PlotAddFunc, self.fctx)
                    self.BackEndPlot.Plot(self.PlotAddFunc)
                    self.VariableEQL(f'f(x) =')

            elif self.mode == 'Plot Prm':
                if self.full is None:
                    self.fctx1 = str(eval(self.TextDisplay.expression))
                    self.FigureX.DrawTexTk(f'f(x)₁ = {DrawAfter(self.fctx1)} | f(x)₂ =')
                    self.VariableEQL(f'f(x)₂ =')
                    self.full = True

                elif self.full:
                    self.fctx2 = str(eval(self.TextDisplay.expression))
                    self.FigureX.DrawTexTk(f'f(x)₁ = {DrawAfter(self.fctx1)} | f(x)₂ = {DrawAfter(self.fctx2)}')
                    if not self.equal:
                        self.PlotFirstFunc = plt.plot_parametric(sympify(self.fctx1), sympify(self.fctx2), legend=True,
                                                                 ylim=(-10, 10), xlim=(-10, 10), show=False)
                        self.PlotFirstFunc = FirstPlotLaTex(self.PlotFirstFunc, (self.fctx1, self.fctx2))
                        self.BackEndPlot.Plot(self.PlotFirstFunc)
                        self.VariableEQL(f'f(x)₁ =')
                        self.equal = True
                        self.full = None

                    elif self.equal:
                        self.PlotAddFunc = plt.plot_parametric(sympify(self.fctx1), sympify(self.fctx2), ylim=(-10, 10),
                                                               xlim=(-10, 10), legend=True, show=False)
                        self.PlotAddFunc = MultiPlot2D(self.PlotFirstFunc, self.PlotAddFunc, (self.fctx1, self.fctx2))
                        self.BackEndPlot.Plot(self.PlotAddFunc)
                        self.VariableEQL(f'f(x)₁ =')
                        self.full = None

            elif self.mode == 'P3DPL':
                if self.full is None:
                    self.fctx1 = str(eval(self.TextDisplay.expression))
                    self.FigureX.DrawTexTk(f'f(x)₁ = {DrawAfter(self.fctx1)} | f(x)₂ = ')
                    self.VariableEQL(f'f(x)₂ =')
                    self.full = True

                elif self.full:
                    self.fctx2 = str(eval(self.TextDisplay.expression))
                    self.FigureX.DrawTexTk(
                        f'f(x)₁ = {DrawAfter(self.fctx1)} | f(x)₂ = '
                        f'{DrawAfter(self.fctx2)}')
                    if not self.equal:
                        self.PlotFirstFunc = plt.plot3d_parametric_line(sympify(self.fctx1), sympify(self.fctx2),
                                                                        self.x, legend=True, show=False)
                        self.PlotFirstFunc = FirstPlotLaTex(self.PlotFirstFunc, (self.fctx1, self.fctx2))
                        self.BackEndPlot.Plot(self.PlotFirstFunc)
                        self.VariableEQL(f'f(x)₁ =')
                        self.equal = True
                        self.full = None

                    elif self.equal:
                        self.PlotAddFunc = plt.plot3d_parametric_line(sympify(self.fctx1), sympify(self.fctx2), self.x,
                                                                      legend=True, show=False)
                        self.PlotAddFunc = MultiPlot2D(self.PlotFirstFunc, self.PlotAddFunc, (self.fctx1, self.fctx2))
                        self.BackEndPlot.Plot(self.PlotAddFunc)
                        self.VariableEQL(f'f(x)₁ =')
                        self.full = None

            elif self.mode == 'Plot3D':
                if self.full is None:
                    self.fctxy = str(eval(self.TextDisplay.expression))
                    self.PlotFirstFunc = plt.plot3d(sympify(self.fctxy), show=False)
                    self.BackEndPlot.Plot(self.PlotFirstFunc)
                    self.VariableEQL(f'f(x,y) =')
                    self.full = True

                elif self.full:
                    self.fctxy = str(eval(self.TextDisplay.expression))
                    self.PlotAddFunc = plt.plot3d(sympify(self.fctxy), show=False)
                    self.PlotAddFunc = MultiPlot3D(self.PlotFirstFunc, self.PlotAddFunc)
                    self.BackEndPlot.Plot(self.PlotAddFunc)
                    self.VariableEQL(f'f(x,y) =')

            elif self.mode == 'P3DPS':
                if self.full is None:
                    self.fctxy1 = str(eval(self.TextDisplay.expression))
                    self.FigureX.DrawTexTk(f'f(x,y)₁ = {DrawAfter(self.fctxy1)} | f(x,y)₂ = ')
                    self.VariableEQL(f'f(x,y)₂ = ')
                    self.full = True

                elif self.full:
                    self.fctxy2 = str(eval(self.TextDisplay.expression))
                    self.FigureX.DrawTexTk(f'f(x,y)₁ = {DrawAfter(self.fctxy1)} | f(x,y)₂ = {DrawAfter(self.fctxy2)}')
                    if not self.equal:
                        self.PlotFirstFunc = plt.plot3d_parametric_surface(sympify(self.fctxy1), sympify(self.fctxy2),
                                                                           self.x - self.y, show=False)
                        self.BackEndPlot.Plot(self.PlotFirstFunc)
                        self.VariableEQL(f'f(x,y)₁ =')
                        self.equal = True
                        self.full = None

                    elif self.equal:
                        self.PlotAddFunc = plt.plot3d_parametric_surface(sympify(self.fctx1), sympify(self.fctx2),
                                                                         self.x - self.y, show=False)
                        self.PlotAddFunc = MultiPlot3D(self.PlotFirstFunc, self.PlotAddFunc)
                        self.BackEndPlot.Plot(self.PlotAddFunc)
                        self.VariableEQL(f'f(x,y)₁ =')
                        self.full = None

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

        if self.mode == 'Operation' or self.mode == 'Solve' or self.mode == 'Matrices':
            self.FigureXY.Draw(self.TkAggXY)

        elif self.mode == 'Equation' or self.mode == 'Function':
            self.FullTextDisplay.see(END)

        else:
            pass

        if self.mode == 'Operation':
            pass
        else:
            self.TextDisplay.ResetClear()
        self.TextDisplay.focus_set()


if __name__ == "__main__":
    # run calculator
    Calculator()
