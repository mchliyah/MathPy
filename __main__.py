import matplotlib

matplotlib.use('TkAgg')  # MUST BE CALLED BEFORE IMPORTING plot
# matplotlib.use('Qt5Agg')  # MUST BE CALLED BEFORE IMPORTING plot
from __jeep_v5__ import *
from tkinter import *
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from sympy import *
from sympy.abc import x, y, z
from sympy.plotting import plot3d, plot3d_parametric_line, plot3d_parametric_surface
from sympy.solvers.solveset import solvify

__author__ = 'Achraf Najmi'
__version__ = '6.2.0_b1'
__name__ = 'MathPy'
"""
# version 6.2
# other improvements
# plotting environment plotted new case of her in window {beta testing}
# add logo in TkAgg_XY
# more improving of getting and setting the result in system equation solver 
# more improving of setting the result in TkAgg_XY
# DrawBefore and DrawAfter move them to jeep v5 as @staticmethod
"""
# noinspection NonAsciiCharacters
π = pi
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
           'font': ('Segoe UI Symbol', 32),
           'relief': 'flat'}


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
        self.TextStrVar = StringVar()
        self.ErrorStrVar = StringVar()
        self.LabelStrVar = StringVar()
        # ROW 0 top canvas==============================================================================================
        top_canvas = Canvas(self.win, relief='flat', bg='#F0F0F0', width=42)
        top_canvas.grid(row=0, column=0, columnspan=2, sticky=NSEW)
        top_canvas.rowconfigure(0, weight=1)
        top_canvas.columnconfigure(1, weight=1)
        # ROW 1 middle top Canvas=======================================================================================
        self.middle_top_canvas = Canvas(self.win, relief='flat', bg='#212121')
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
        # ROW 2 set canvas showing ScrollableTkAggXY & ScrolledListbox==================================================
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
        EqualLabelDisplay = Label(top_canvas, **ent_prm, textvariable=self.LabelStrVar)
        EqualLabelDisplay.grid(row=0, column=0, sticky=NSEW)
        EqualLabelDisplay.configure(anchor='e')
        # Text Display, insertbackground='white'
        self.TextDisplay = Entry(top_canvas, **ent_prm, textvariable=self.TextStrVar, insertwidth=2)
        self.TextDisplay.grid(row=0, column=1, sticky=NSEW)
        self.TextDisplay.configure(takefocus=True)
        self.TextDisplay.bind("<Button-1>", self.Info)
        self.IndexCursor = 0
        # Error Label Display, cursor="arrow"
        ErrorLabelDisplay = Label(top_canvas, **ent_prm, textvariable=self.ErrorStrVar)
        ErrorLabelDisplay.grid(row=0, column=2, sticky=NSEW)
        ErrorLabelDisplay.configure(anchor='e')
        # ROW 1 set MathPlot LaTex Display==============================================================================
        self.FigureX = Figure(figsize=(100, 5), facecolor='#212121')
        self.TkAggX = ScrollableTkAggX(figure=self.FigureX, master=self.middle_top_canvas)
        self.TkAggWidgetX = self.TkAggX.get_tk_widget()
        self.TkAggWidgetX.grid(row=0, column=0, sticky=NSEW)
        self.TkAggWidgetX.rowconfigure(0, weight=1)
        self.TkAggWidgetX.columnconfigure(0, weight=1)
        # buttons that will be fake displayed on middle canvas ROW 0====================================================
        big_txt = ['', '', '', '', '']
        self.btn_b = []
        for k in range(5):
            self.btn_b.append(HoverButton(self.middle_canvas, **big2_prm, text=big_txt[k]))
        # ROW 2 set canvas showing ScrollableTkAggXY & ScrolledListbox==================================================

        # buttons that will be displayed on middle bottom canvas ROW 0==================================================
        txta = ['Û', 'Ü', '1ST']
        self.btn_m1 = []
        for i1 in range(3):
            self.btn_m1.append(HoverButton(self.middle_bottom_canvas, **btn_dif, text=txta[i1]))
            self.btn_m1[i1].grid(row=0, column=i1, sticky=NSEW)
        # Cursor Disposition
        self.btn_m1[0]['command'] = lambda: self.ChangeDirectionCursor('Left')
        self.btn_m1[1]['command'] = lambda: self.ChangeDirectionCursor('Right')

        txtb = ['ANS', 'r', 'Õ']
        self.btn_m2 = []
        i2b = 3
        for i2a in range(3):
            self.btn_m2.append(HoverButton(self.middle_bottom_canvas, **btn_prm, text=txtb[i2a]))
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
            self.btn_u.append(HoverButton(self.middle_bottom_canvas, **btn_prm))
            self.btn_u[i3].grid(row=1, column=i3, sticky=NSEW)
        # ROW 2
        # ========================logarithm=============================================================================
        logarithm_pad = ['log(', 'exp(', 'LambertW(', 'integrate(', 'sqrt(', "fctrl("]
        logarithm_txt = ['log', 'exp', 'W', "∫f(x)", '√n', "n!"]
        self.btn_d = []
        for i4 in range(6):
            self.btn_d.append(HoverButton(self.middle_bottom_canvas, **btn_prm, text=logarithm_txt[i4]))
            self.btn_d[i4].grid(row=2, column=i4, sticky=NSEW)
            self.btn_d[i4].configure(
                command=lambda f0=logarithm_pad[i4]: [self.Input(f0), self.Input(')'),
                                                      self.ChangeDirectionCursor('Left')])
        # buttons that will be displayed on bottom canvas ROW 0=========================================================
        btn = ['π', 'E', "1j", "+", '(', ')', "7", "8", "9", "-", '/100', 'x', "4", "5", "6", "*", "**2", 'y',
               "1", "2", "3", "/", "**", 'z', "0", '', '.', "=", 'e', "oo"]

        btn_txt = ['π', 'e¹', "j", "+", '(', ')', "7", "8", "9", "-", 'n%', 'x', "4", "5", "6", "⨯",
                   u'n\u00B2', 'y', "1", "2", "3", "/", "nˣ", 'z', "0", '', '.', "=", "10ˣ", "∞"]
        self.btn = []
        i5 = 0
        for j in range(5):
            for k in range(6):
                self.btn.append(HoverButton(self.bottom_canvas, **btnb_prm, text=btn_txt[i5]))
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
        # Configuration Master Display==================================================================================
        self.win.rowconfigure(1, weight=1)
        self.win.columnconfigure(1, weight=1)

        self.win.bind_all('<Key>', self.KeyboardInput)
        self.win.iconbitmap('Alecive-Flatwoken-Apps-Libreoffice-Math-B.ico')
        self.win.configure(menu=menubare, bg='#4d4d4d')
        self.win.geometry("1100x680")
        self.win.minsize(width=1100, height=680)
        self.win.resizable(width=True, height=True)
        self.win.title(u"%s v%s" % (__name__, __version__))
        self.win.mainloop()

    def iCursor(self, cursor):
        self.TextDisplay.icursor(cursor)

    def Info(self, event):
        self.IndexCursor = int(self.TextDisplay.index("@%d" % event.x))
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
                self.btn_a.append(HoverButton(self.middle_canvas, **big2_prm, text=big_txt[i]))
                self.btn_a[i].grid(row=0, column=i, sticky=NSEW)
                self.btn_a[i]["command"] = lambda f3=big_pad[i]: self.SwitchFunction(f3, True)

            # buttons that will be displayed on middle bottom canvas ROW 0==============================================
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
            # buttons that will be displayed on middle canvas ROW 0=====================================================
            for i in range(5):
                self.btn_a[i].destroy()
            big_txt = ['Plot\nf(x)', 'Plot\nParametric', 'Plot 3D\nParametric\nLine', "Plot3D\nf(x,y)",
                       'Plot 3D\nParametric\nSurface']
            big_pad = ['Plot', 'Plot Prm', 'P3DPL', "Plot3D", 'P3DPS']
            self.btn_b = []
            for i in range(5):
                self.btn_b.append(HoverButton(self.middle_canvas, **big2_prm, text=big_txt[i]))
                self.btn_b[i].grid(row=0, column=i, sticky=NSEW)
                self.btn_b[i]["command"] = lambda f5=big_pad[i]: self.SwitchFunction(f5, True)

            # buttons that will be displayed on middle bottom canvas ROW 0==============================================
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
            self.east_canvas.destroy()
            if self.mode == 'Operation' or self.mode == 'Solve' or self.mode == 'Matrices':
                self.mathext = [u"    %s v%s Created by %s" % (__name__, __version__, __author__)]
                self.SwitchWidget('TkAgg')
            elif self.mode == 'Plot':
                self.SwitchWidget('plot')
            else:
                self.SwitchWidget('listbox')
                self.FullTextDisplay.delete(0, END)

        if self.mode == 'Operation':
            if self.switched:
                self.MultiLaTexSwitchDraw(f'Mode Operation : ')
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
                self.MultiLaTexSwitchDraw('Mode Line Equation Solver : One {eq} : [x] | Constants : (y,z)')
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
                self.MultiLaTexSwitchDraw('Mode System Equation Solver :')
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
                # self.FullTextDisplay.insert(END, 'Mode Plot : f(x)')
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

        self.TextDisplay.focus_set()

    def SwitchWidget(self, widget):
        figure = widget
        self.east_canvas = Canvas(self.win, relief='flat', bg='#F0F0F0')
        self.east_canvas.grid(row=2, column=1, rowspan=3, sticky=NSEW)
        if figure == 'listbox':
            self.east_canvas.rowconfigure(0, weight=1)
            self.east_canvas.columnconfigure(0, weight=1)

            self.FullTextDisplay = ScrolledListbox(self.east_canvas, width=52, height=8, **ent_prm)
            self.FullTextDisplay.configure(font=('Segoe UI Symbol', 24))
            self.FullTextDisplay.grid(row=0, column=0, sticky=NSEW)
            self.FullTextDisplay.rowconfigure(0, weight=1)
            self.FullTextDisplay.columnconfigure(0, weight=1)

        elif figure == 'TkAgg':
            self.east_canvas.rowconfigure(0, weight=1)
            self.east_canvas.columnconfigure(0, weight=1)

            self.FigureXY = Figure(figsize=(100, 1), facecolor='#F0F0F0')
            self.AxesXY = self.FigureXY.subplots(nrows=2, ncols=1)

            self.TkAggXY = ScrollableTkAggXY(figure=self.FigureXY, master=self.east_canvas)
            self.TkAggWidgetXY = self.TkAggXY.get_tk_widget()
            self.TkAggWidgetXY.grid(row=0, column=0, sticky=NSEW)
            self.TkAggWidgetXY.rowconfigure(0, weight=1)
            self.TkAggWidgetXY.columnconfigure(0, weight=1)

        else:
            self.east_canvas.rowconfigure(1, weight=1)
            self.east_canvas.columnconfigure(0, weight=1)

            self.Figure = Figure(figsize=(6, 4), facecolor='#F0F0F0')

            # self.TkAgg = TkFigureFrame(figure=self.Figure, window=self.east_canvas)
            # self.TkAggWidget = self.TkAgg.get_tk_widget()
            # self.TkAggWidget.grid(row=1, column=0, sticky=NSEW)

            self.TkAgg = FigureCanvasTkAgg(figure=self.Figure, master=self.east_canvas)
            self.TkAggWidget = self.TkAgg.get_tk_widget()
            self.TkAggWidget.grid(row=1, column=0, sticky=NSEW)

            self.ToolBarFrame = Frame(master=self.east_canvas)
            self.ToolBarFrame.grid(row=0, column=0)
            self.ToolBarFrame.columnconfigure(0, weight=1)

            self.ToolBar = NavigationToolbar2Tk(self.TkAgg, self.ToolBarFrame)
            self.ToolBar.update()
            self.ToolBar.grid(row=0, column=0)
            self.ToolBar.columnconfigure(0, weight=1)

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
        self.store_expression = []
        self.store_order = []
        self.expression = ''
        self.TextStrVar.set('')
        self.ErrorStrVar.set('')
        self.iCursor(0)
        self.IndexCursor = int(self.TextDisplay.index(INSERT))
        self.FigureX.clear()
        self.TkAggX.draw()

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

        self.TextDisplay.focus_set()

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
                self.Input('fctrl('), self.Input(')'), self.ChangeDirectionCursor('Left')

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
            self.ErrorStrVar.set('IndexError')

    def Input(self, keyword):
        if self.clear:
            self.Delete()

        self.expression, self.IndexCursor = InsertIntoString(self.expression, keyword, self.IndexCursor,
                                                             self.store_order, self.store_expression)

        self.ShowInput()

    def DrawTexTk(self, la_text):
        mpl_white_rvb = (255. / 255., 255. / 255., 255. / 255.)
        try:
            self.FigureX.clear()
            self.FigureX.text(0, 0.4, la_text, color=mpl_white_rvb, fontsize=30)
            self.TkAggX.draw()
        except Exception:
            pass

    def VariableTXT(self, label_var):
        self.LabelStrVar.set(label_var)
        self.TextStrVar.set(self.expression)

    def ShowInput(self):
        try:
            if self.mode == 'Operation':
                self.TextStrVar.set(self.expression)
                self.DrawTexTk(f'op > {DrawBefore(self.expression)} = {DrawAfter(eval(self.expression))}')

            elif self.mode == 'Function':
                if self.full is None:
                    self.VariableTXT('From :')
                    self.DrawTexTk(
                        f'From : {DrawAfter(self.expression)} --> To : B | f(x) = Function')

                elif not self.full:
                    self.VariableTXT('To :')
                    self.DrawTexTk(
                        f'From : {DrawAfter(self.v)} --> To : '
                        f'{DrawAfter(self.expression)} | f(x) = Function')

                elif self.full:
                    self.VariableTXT('f(x) =')
                    self.DrawTexTk(
                        f'From : {DrawAfter(self.v)} --> To : {DrawAfter(self.w)} | '
                        f'f(x) = {DrawAfter(self.expression)}')

            elif self.mode == 'Equation':
                if self.full is None:
                    self.VariableTXT('a =')
                    self.DrawTexTk(
                        f'{DrawAfter(self.expression)}x² + bx + c = 0')

                elif not self.full:
                    self.VariableTXT('b =')
                    self.DrawTexTk(
                        f'{DrawAfter(self.a)}x² + ({DrawAfter(self.expression)})x + c = 0')

                elif self.full:
                    self.VariableTXT('c =')
                    self.DrawTexTk(
                        f'{DrawAfter(self.a)}x² + ({DrawAfter(self.b)})x + '
                        f'({DrawAfter(self.expression)}) = 0')

            elif self.mode == 'Solve':
                if self.full is None:
                    self.VariableTXT('eq >')
                    self.DrawTexTk(f'eq > {DrawAfter(self.expression)}')
                elif self.full:
                    self.VariableTXT(f'eq > {self.q} =')
                    self.DrawTexTk(
                        f'eq > {DrawAfter(self.q)} = '
                        f'{DrawAfter(self.expression)}')

            elif self.mode == 'Matrices':
                if self.full is None:
                    self.VariableTXT(f'eq₁ >')
                    self.DrawTexTk(f'eq₁ > {DrawAfter(self.expression)}')
                elif not self.full:
                    self.VariableTXT(f'eq₁ > {self.q} = ')
                    self.DrawTexTk(f'eq₁ > {DrawAfter(self.q)} = {DrawAfter(self.expression)}')

                elif self.full:
                    if self.clear is None:
                        self.VariableTXT(f'eq₂ >')
                        self.DrawTexTk(f'eq₂ > {DrawAfter(self.expression)}')
                    elif not self.clear and self.equal is None:
                        self.VariableTXT(f'eq₂ > {self.j} =')
                        self.DrawTexTk(f'eq₂ > {DrawAfter(self.j)} = {DrawAfter(self.expression)}')

                    elif not self.clear and not self.equal:
                        self.VariableTXT(f'eq₃ >')
                        self.DrawTexTk(f'eq₃ > {DrawAfter(self.expression)}')
                    elif not self.clear and self.equal:
                        self.VariableTXT(f'eq₃ > {self.m} =')
                        self.DrawTexTk(f'eq₃ > {DrawAfter(self.m)} = {DrawAfter(self.expression)}')

            elif self.mode == 'Plot':
                self.VariableTXT(f'f(x) =')
                self.DrawTexTk(f'f(x) = {DrawAfter(self.expression)}')

            elif self.mode == "Plot Prm" or self.mode == "P3DPL":
                if self.full is None:
                    self.VariableTXT(f'f(x)₁ =')
                    self.DrawTexTk(f'f(x)₁ = {DrawAfter(self.expression)}')

                elif self.full:
                    self.VariableTXT(f'f(x)₂ =')
                    self.DrawTexTk(f'f(x)₁ = {DrawAfter(self.fctx1)} | '
                                   f'f(x)₂ = {DrawAfter(self.expression)}')

            elif self.mode == "Plot3D":
                self.VariableTXT(f'f(x,y) =')
                self.DrawTexTk(f'f(x,y) = {DrawAfter(self.expression)}')

            elif self.mode == "P3DPS":
                if self.full is None:
                    self.VariableTXT(f'f(x,y)₁ =')
                    self.DrawTexTk(f'f(x,y)₁ = {DrawAfter(self.expression)}')

                elif self.full:
                    self.VariableTXT(f'f(x,y)₂ =')
                    self.DrawTexTk(f'f(x,y)₁ = {DrawAfter(self.fctxy1)} | '
                                   f'f(x,y)₂ = {DrawAfter(self.expression)}')

            self.ErrorStrVar.set('')
        except Exception:
            pass
        self.TextDisplay.focus_set()

        self.iCursor(self.IndexCursor)

    def MultiLaTexSwitchDraw(self, character):
        self.mathext.append(character)

        ico = AnnotationBbox(OffsetImage(plt.imread('Alecive-Flatwoken-Apps-Libreoffice-Math-B.ico'), zoom=0.1),
                             (0.0009, 0.6), frameon=False)
        self.AxesXY[0].add_artist(ico)
        i_line = 0
        for ax in self.AxesXY.flatten():
            demo = self.mathext[i_line]
            ax.text(0, 0.5, demo, fontsize=20)
            ax.axis('off')
            ax.set_xticklabels("", visible=False)
            ax.set_yticklabels("", visible=False)
            i_line += 1
        try:
            self.FigureXY.tight_layout()  # pad=-1, h_pad=-3 h_pad=2
        except Exception:
            pass
        self.TkAggXY.Draw()

    def MultiLaTexEQDraw(self, character):
        self.mathext.append(character)

        n_lines = int(len(self.mathext))
        self.AxesXY = self.FigureXY.add_subplot(n_lines, 1, n_lines)

        demo = self.mathext[-1]
        self.AxesXY.text(0, 0.5, demo, fontsize=20)
        self.AxesXY.axis('off')
        self.AxesXY.set_xticklabels("", visible=False)
        self.AxesXY.set_yticklabels("", visible=False)

        n_axes = len(self.FigureXY.axes)
        for i_axes in range(n_axes):
            self.FigureXY.axes[i_axes].change_geometry(n_axes, 1, i_axes + 1)

        oldSize = self.FigureXY.get_size_inches()
        mac1 = len(self.mathext[-1])
        mac2 = len(self.mathext[-2])
        if mac1 > 20 or mac2 > 30 or mac2 > 20 or mac1 > 30:
            self.FigureXY.set_size_inches(1.35 + oldSize[0], 1.35 + oldSize[1])
        else:
            self.FigureXY.set_size_inches(0.9 + s for s in oldSize)

        try:
            self.FigureXY.tight_layout()  # pad=-1, h_pad=-3 h_pad=2
        except Exception:
            pass

    def VariableEQL(self, label_var, first_var):
        self.LabelStrVar.set(label_var)
        self.TextStrVar.set(first_var)

    def ShowEqual(self):
        try:
            if self.mode == 'Operation':
                if not self.equal:
                    self.answer = sympify(eval(self.expression))
                    self.VariableEQL(f'op > {self.expression} =', f'{self.answer}')
                    self.DrawTexTk(f'op > {DrawBefore(self.expression)} = {DrawAfter(self.answer)}')
                    self.MultiLaTexEQDraw(f'op > {DrawBefore(self.expression)} = {DrawAfter(self.answer)}')
                    self.clear = True
                    self.equal = True

                elif self.equal:
                    self.answer, self.expression = FullReBuild(self.store_expression, self.callback)
                    self.answer = sympify(self.answer)
                    self.VariableEQL(f'op > {self.expression} =', f'{self.answer}')
                    self.DrawTexTk(f'op > {DrawBefore(self.expression)} = {DrawAfter(self.answer)}')
                    self.MultiLaTexEQDraw(f'op > {DrawBefore(self.expression)} = {DrawAfter(self.answer)}')
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
                        TwoPlotMultiColor(self.PlotFirstFunc, self.PlotAddFunc, self.fctx)
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
                    self.DrawTexTk(f'{DrawAfter(self.a)}x² + ({DrawAfter(self.b)})x + '
                                   f'({DrawAfter(self.c)}) = 0')
                    qe = int(len(EQT(self.a, self.b, self.c)))
                    for eq in range(qe):
                        self.FullTextDisplay.insert(END, EQT(self.a, self.b, self.c)[eq])

                    self.clear = True
                    self.full = None

            elif self.mode == 'Solve':
                if self.full is None:
                    self.q = str(eval(self.expression))
                    self.VariableEQL(f'eq > {self.q} =', '')
                    self.DrawTexTk(f'eq > {DrawAfter(self.q)} = ')
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
                    self.DrawTexTk(f'eq > {DrawBefore(self.q)} = {DrawBefore(self.p)}'
                                   f' > Solution : {DrawAfter(self.SolutionOS)}')
                    self.MultiLaTexEQDraw(f'eq > {DrawBefore(self.q)} = {DrawBefore(self.p)}')
                    self.MultiLaTexEQDraw(f'Solution : {DrawAfter(self.SolutionOS)}')
                    for sl in range(len(self.SolutionOS)):
                        self.MultiLaTexEQDraw(f'> x{self.nb[int(sl) + 1]} = {DrawAfter(self.SolutionOS[sl])}')

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
                    self.MultiLaTexEQDraw('New System :')
                    self.MultiLaTexEQDraw(f' eq₁ | {DrawBefore(self.q)} = {DrawBefore(self.p)}')
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
                            self.MultiLaTexEQDraw(f' eq₂ | {DrawBefore(self.j)} = {DrawBefore(self.k)}')
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
                                    self.VariableEQL('eq₃ >', '')
                                    self.DrawTexTk('eq₃ > ')
                                    self.equal = False
                                    self.exist = True
                                    if sol == 'EmptySet':
                                        self.VariableEQL('', '')
                                        self.DrawTexTk(f'Empty Solution : {DrawAfter(self.SolutionTT)}')
                                        self.MultiLaTexEQDraw(f'Empty  Solution : {DrawAfter(self.SolutionTT)}')
                                        self.clear = True
                                        self.full = None
                                    break
                                self.v += 1

                            if not self.exist:
                                self.VariableEQL('System of Two Equations : {eq₁,eq₂}_[x,y]', '')
                                self.DrawTexTk(f'Solution : {DrawAfter(self.SolutionTT)}')
                                self.MultiLaTexEQDraw(f'Solution : {DrawAfter(self.SolutionTT)}')
                                try:
                                    self.xexp, self.yexp = next(iter(self.SolutionTT))
                                    self.MultiLaTexEQDraw(f'> x = {DrawAfter(self.xexp)}')
                                    self.MultiLaTexEQDraw(f'> y = {DrawAfter(self.yexp)}')
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
                                        self.VariableEQL(f'x = {self.xexp} | y = {self.yexp}', '')
                                        self.MultiLaTexEQDraw(f'> x = {DrawAfter(self.xexp)}')
                                        self.MultiLaTexEQDraw(f'> y = {DrawAfter(self.yexp)}')
                                    except Exception:
                                        pass
                                self.clear = True
                                self.full = None

                        elif not self.equal:
                            self.m = str(sympify(self.expression))
                            self.VariableEQL(f'eq₃ > {self.m} =', '')
                            self.equal = True

                        elif self.equal:
                            self.n = str(sympify(self.expression))
                            self.expression = ''
                            self.MultiLaTexEQDraw(f' eq₃ | {DrawBefore(self.m)} = {DrawBefore(self.n)}')
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
                                self.VariableEQL('', '')
                                self.DrawTexTk(f'Empty Solution : {DrawAfter(self.SolutionTT)}')
                                self.MultiLaTexEQDraw(f'Empty  Solution : {DrawAfter(self.SolutionTT)}')

                            else:
                                self.VariableEQL('System of Three Equations : {eq₁,eq₂,eq₃}_[x,y,z]', '')
                                self.DrawTexTk(f'Solution : {DrawAfter(self.SolutionTT)}')
                                self.MultiLaTexEQDraw(f'Solution : {DrawAfter(self.SolutionTT)}')
                                try:
                                    self.xexp, self.yexp, self.zexp = next(iter(self.SolutionTT))
                                    self.MultiLaTexEQDraw(f'> x = {DrawAfter(self.xexp)}')
                                    self.MultiLaTexEQDraw(f'> y = {DrawAfter(self.yexp)}')
                                    self.MultiLaTexEQDraw(f'> z = {DrawAfter(self.zexp)}')
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
                                        self.VariableEQL(f'x = {self.xexp} | y = {self.yexp} | z = {self.zexp}', '')
                                        self.MultiLaTexEQDraw(f'> x = {DrawAfter(self.xexp)}')
                                        self.MultiLaTexEQDraw(f'> y = {DrawAfter(self.yexp)}')
                                        self.MultiLaTexEQDraw(f'> z = {DrawAfter(self.zexp)}')
                                    except Exception:
                                        pass
                            self.clear = True
                            self.full = None

            elif self.mode == 'Plot':
                if self.full is None:
                    self.fctx = str(eval(self.expression))
                    # self.FullTextDisplay.insert(END, f'f(x) = {self.fctx}')
                    self.PlotFirstFunc = plot(sympify(self.fctx), ylim=(-10, 10), xlim=(-10, 10), legend=True,
                                              _backend="matplotlib", show=False)
                    LabelLatexPlot(self.PlotFirstFunc, self.fctx)
                    print(self.PlotFirstFunc._backend.fig, self.PlotFirstFunc[0])
                    print(self.PlotFirstFunc._backend.ax, self.PlotFirstFunc._backend.ax[0])
                    # assert isinstance(self.Figure, (add_artist, self.PlotFirstFun)).__str__(self.PlotFirstFunc.fig)
                    # self.Figure.__repr__(self.PlotFirstFunc.ax)
                    # self.Figure.draw(self.PlotFirstFunc.fig)
                    self.axg = self.Figure._add_axes_internal(self.PlotFirstFunc._backend.fig,
                                                              self.PlotFirstFunc._backend.ax[0])
                    # self.axg = self.Figure.add_subplot(self.PlotFirstFunc._backend.ax[0])
                    self.Figure.tight_layout()
                    self.TkAgg.draw()
                    print(self.axg)
                    self.VariableEQL(f'f(x) =', '')
                    self.full = True

                elif self.full:
                    self.fctx = str(eval(self.expression))
                    # self.FullTextDisplay.insert(END, f'f(x) = {self.fctx}'), show=False
                    self.PlotAddFunc = plot(sympify(self.fctx), ylim=(-10, 10), xlim=(-10, 10), legend=True, show=False)
                    LabelLatexPlot(self.PlotAddFunc, self.fctx)
                    self.PlotFirstFunc = TwoPlotMultiColor(self.PlotFirstFunc, self.PlotAddFunc, self.fctx)
                    self.mpl = self.PlotFirstFunc._backend.ax
                    self.mpl.append(self.PlotAddFunc._backend.ax[0])
                    print(self.PlotFirstFunc._backend.fig)
                    # print(self.PlotFirstFunc._backend.ax, self.PlotFirstFunc._backend.ax[0], self.PlotFirstFunc._backend.ax[1])
                    print(self.mpl[s] for s in range(len(self.mpl)))
                    # print(self.mpl[s] for s in range(2))
                    # print(self.mpl[0], self.mpl[1])

                    # self.axg = self.Figure._add_axes_internal(self.PlotAddFunc._backend.fig, ax=self.PlotFirstFunc._backend.ax[0])
                    self.Figure._remove_ax(self.axg)
                    self.Figure.clear()
                    self.axg = self.Figure._add_axes_internal(self.PlotAddFunc._backend.fig, ax=self.mpl[-1])
                    self.Figure.tight_layout()
                    self.TkAgg.draw()
                    self.VariableEQL(f'f(x) =', '')

            elif self.mode == 'Plot Prm':
                if self.full is None:
                    self.fctx1 = str(eval(self.expression))
                    self.FullTextDisplay.insert(END, f'f(x)₁ = {self.fctx1}')
                    self.DrawTexTk(
                        f'f(x)₁ = {DrawAfter(self.fctx1)} | f(x)₂ =')
                    self.VariableEQL(f'f(x)₂ =', '')
                    self.full = True

                elif self.full:
                    self.fctx2 = str(eval(self.expression))
                    self.FullTextDisplay.insert(END, f'f(x)₂ = {self.fctx2}')
                    self.DrawTexTk(
                        f'f(x)₁ = {DrawAfter(self.fctx1)} | f(x)₂ = '
                        f'{DrawAfter(self.fctx2)}')
                    if not self.equal:
                        self.PlotFirstFunc = plot_parametric(sympify(self.fctx1), sympify(self.fctx2), ylim=(-10, 10),
                                                             xlim=(-10, 10), legend=True, show=False)
                        LabelLatexPlot(self.PlotFirstFunc, (self.fctx1, self.fctx2))
                        self.VariableEQL(f'f(x)₁ =', '')
                        self.equal = True
                        self.full = None

                    elif self.equal:
                        self.PlotAddFunc = plot_parametric(sympify(self.fctx1), sympify(self.fctx2), ylim=(-10, 10),
                                                           xlim=(-10, 10), show=False)
                        TwoPlotMultiColor(self.PlotFirstFunc, self.PlotAddFunc, (self.fctx1, self.fctx2))
                        self.VariableEQL(f'f(x)₁ =', '')
                        self.full = None

            elif self.mode == 'P3DPL':
                if self.full is None:
                    self.fctx1 = str(eval(self.expression))
                    self.FullTextDisplay.insert(END, f'f(x)₁ = {self.fctx1}')
                    self.DrawTexTk(
                        f'f(x)₁ = {DrawAfter(self.fctx1)} | f(x)₂ = ')
                    self.VariableEQL(f'f(x)₂ =', '')
                    self.full = True

                elif self.full:
                    self.fctx2 = str(eval(self.expression))
                    self.FullTextDisplay.insert(END, f'f(x)₂ = {self.fctx2}')
                    self.DrawTexTk(
                        f'f(x)₁ = {DrawAfter(self.fctx1)} | f(x)₂ = '
                        f'{DrawAfter(self.fctx2)}')
                    if not self.equal:
                        self.PlotFirstFunc = plot3d_parametric_line(sympify(self.fctx1), sympify(self.fctx2), self.x
                                                                    , ylim=(-10, 10), xlim=(-10, 10), legend=True
                                                                    , show=False)
                        LabelLatexPlot(self.PlotFirstFunc, (self.fctx1, self.fctx2))
                        self.VariableEQL(f'f(x)₁ =', '')
                        self.equal = True
                        self.full = None

                    elif self.equal:
                        self.PlotAddFunc = plot3d_parametric_line(sympify(self.fctx1), sympify(self.fctx2), self.x,
                                                                  ylim=(-10, 10), xlim=(-10, 10), show=False)
                        TwoPlotMultiColor(self.PlotFirstFunc, self.PlotAddFunc, (self.fctx1, self.fctx2))
                        self.VariableEQL(f'f(x)₁ =', '')
                        self.full = None

            elif self.mode == 'Plot3D':
                if self.full is None:
                    self.fctxy = str(eval(self.expression))
                    self.FullTextDisplay.insert(END, f'f(x,y) = {self.fctxy}')
                    self.PlotFirstFunc = plot3d(sympify(self.fctxy), legend=True)
                    self.VariableEQL(f'f(x,y) =', '')
                    self.full = True

                elif self.full:
                    self.fctxy = str(eval(self.expression))
                    self.FullTextDisplay.insert(END, f'f(x,y) = {self.fctxy}')
                    self.PlotAddFunc = plot3d(sympify(self.fctxy), show=False)

                    TwoPlot3D(self.PlotFirstFunc, self.PlotAddFunc)
                    self.VariableEQL(f'f(x,y) =', '')

            elif self.mode == 'P3DPS':
                if self.full is None:
                    self.fctxy1 = str(eval(self.expression))
                    self.FullTextDisplay.insert(END, f'f(x,y)₁ = {self.fctxy1}')
                    self.DrawTexTk(
                        f'f(x,y)₁ = {DrawAfter(self.fctxy1)} | f(x,y)₂ = ')
                    self.VariableEQL(f'f(x,y)₂ = ', '')
                    self.full = True

                elif self.full:
                    self.fctxy2 = str(eval(self.expression))
                    self.FullTextDisplay.insert(END, f'f(x,y)₂ = {self.fctxy2}')
                    self.DrawTexTk(f'f(x,y)₁ = {DrawAfter(self.fctxy1)} | f(x,y)₂ = '
                                   f'{DrawAfter(self.fctxy2)}')
                    if not self.equal:
                        self.PlotFirstFunc = plot3d_parametric_surface(sympify(self.fctxy1), sympify(self.fctxy2),
                                                                       self.x - self.y, legend=True)
                        self.VariableEQL(f'f(x,y)₁ =', '')
                        self.equal = True
                        self.full = None

                    elif self.equal:
                        self.PlotAddFunc = plot3d_parametric_surface(sympify(self.fctx1), sympify(self.fctx2),
                                                                     self.x - self.y, show=False)
                        TwoPlot3D(self.PlotFirstFunc, self.PlotAddFunc)
                        self.VariableEQL(f'f(x,y)₁ =', '')
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
        self.iCursor(END)

        if self.mode == 'Operation' or self.mode == 'Solve' or self.mode == 'Matrices':
            self.TkAggXY.Draw()

        elif self.mode == 'Plot':
            pass

        else:
            self.FullTextDisplay.see(END)

        if self.mode == 'Operation':
            pass
        else:
            self.expression = ''
            self.store_expression = []
            self.store_order = []
            self.IndexCursor = 0

    def Exit(self):
        return self.win.destroy()


if __name__ == "MathPy":
    # run calculator
    Calculator()
