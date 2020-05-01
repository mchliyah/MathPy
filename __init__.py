import tkinter as tk
from tkinter import *
from tkinter import Scrollbar
from tkinter import _cnfmerge
from operator import neg
from random import randint
from sympy import *
from sympy.abc import x, y, z
from sympy.plotting import PlotGrid, plot_backends
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.colors import to_hex

delf = ()


def fctrl(nbr):
    return factorial(nbr).evalf()


def DrawAfter(character):
    try:
        simplify = sympify(character, rational=True)
        return LaTex(simplify)
    except None:
        pass
    except Exception:
        pass


def DrawBefore(character):
    try:
        pik = str(character).replace('integrate', 'Integral').replace('diff', 'Derivative')
        simplify = sympify(pik, rational=True, evaluate=False)
        return LaTex(simplify)
    except None:
        pass
    except Exception:
        pass


def LaTex(Math_Expression):
    # return r"$%s$" % latex(Math_Expression)
    return f'${latex(Math_Expression)}$'


def TwoPlotMultiColor(Plot_First_Func2D, Plot_Add_Func2D, Function2D):
    Plot_First_Func2D.extend(Plot_Add_Func2D)
    RD = randint(1048576, 16777000)
    HX = hex(RD)
    HX = HX[2:8].upper()
    Plot_First_Func2D[-1].line_color = str('#') + str(HX)
    Plot_First_Func2D[-1].label = LaTex(sympify(Function2D))
    PlotGrid(1, 2, Plot_First_Func2D, Plot_Add_Func2D, legend=True)


def MultiPlot2D(Plot_First_Func2D, Plot_Add_Func2D, Function2D):
    Plot_First_Func2D.extend(Plot_Add_Func2D)
    RD = randint(1048576, 16777000)
    HX = hex(RD)
    HX = HX[2:8].upper()
    Plot_First_Func2D[-1].line_color = str('#') + str(HX)
    Plot_First_Func2D[-1].label = LaTex(sympify(Function2D))
    return Plot_First_Func2D


def OnePlotLaTex(Plot_First_Func, FunctionTX):
    Plot_First_Func[-1].label = LaTex(sympify(FunctionTX))
    Plot_First_Func.show()


def FirstPlotLaTex(Plot_First_Func, FunctionTX):
    Plot_First_Func[-1].label = LaTex(sympify(FunctionTX))
    return Plot_First_Func


def MultiPlot3D(Plot_First_Func3D, Plot_Add_Func3D):
    Plot_First_Func3D.extend(Plot_Add_Func3D)
    return Plot_First_Func3D


def EQT(nbr_a, nbr_b, nbr_c):
    global delf
    delf = ()
    a = float(eval(nbr_a))
    b = float(eval(nbr_b))
    c = float(eval(nbr_c))
    d = float((b ** 2) - 4 * a * c)
    nd = neg(d)
    nb = neg(b)
    delf += ('____________________________________________',
             '',
             f"eq > {eval(str(a * x ** 2 + b * x + c))} = 0")
    if a > 0 or a < 0:
        delf += (
            f'The Equation Have Two Solutions For x :',
            f'  ∆ =  b² - 4ac',
            f'  ∆ = {b}² - (4 ⨯ {a} ⨯ {c})',
            f'      = {b ** 2} - ({4 * a * c})',
            f'      = {d}')
        if d == 0:
            delf += (
                f'∆=0 : x = -b / 2a',
                f' x₁ = x₂ = ({N(neg(b), 3)}) / (2 ⨯ {a})',
                f' x₁ = x₂ = {N(neg(b) / (2 * a), 3)}')
        elif d >= 0:
            delf += (
                f'∆>0 : x = (-b ± √∆) / 2a',
                f' x₁ = ({nb} + √{d}) / (2 ⨯ {a})',
                f'     = {N((nb + sqrt(d)) / (2 * a), 3)}',
                f' x₂ = ({nb} - √{d}) / (2 ⨯ {a})',
                f'     = {N((nb - sqrt(d)) / (2 * a), 3)}')
        elif d <= 0:
            delf += (
                f'      = {nd}i²',
                f'∆<0 : x = (-b ± i√∆) / 2a',
                f' x₁ = ({nb} + i√({nd})) / (2 ⨯ {a})',
                f'     = {N((nb + sqrt(nd) * 1j) / (2 * a), 3)}',
                f' x₂ = ({nb} - i√({nd})) / (2 ⨯ {a})',
                f'     = {N((nb - sqrt(nd) * 1j) / (2 * a), 3)}',
                f'  z = a ± ib',
                f'  a = {N(nb / (2 * a), 3)}',
                f'  b = ± {N(sqrt(nd) / (2 * a), 3)}')
    elif a == 0:
        if b == 0 and c == 0:
            delf += ('', "Empty Solution {{∅}}")
        elif b == 0:
            delf += ('', "Empty Solution {{∅}}")
        elif c == 0:
            delf += (
                f'The Equation Have One Solution For x :',
                f'  {b}x = 0',
                f'  x = 0',)
        else:
            delf += (
                f'The Equation Have One Solution For x :',
                f'  {b}x = {neg(c)}',
                f'  x = {neg(c)} / {b}',
                f'  x = {neg(c) / b}')
    return delf


class ManagedEntry(Entry):
    def __init__(self, master=None, cnf=None, **kw):
        if cnf is None:
            cnf = {}
        kw = _cnfmerge((kw, cnf))
        self.TextVariable = StringVar()
        super(ManagedEntry, self).__init__(master=master, textvariable=self.TextVariable, cnf={}, **kw)
        self.bind_class(self, "<Button-1>", self.ClickCursor)
        self.index_cursor = 0
        self.expression = ''
        self.answer = ''
        # store expressions & order
        self.store_expression = []
        self.store_order = []
        self.permit = None
        self.ind_nbr = int
        self.ex_nbr = int
        self.n = int
        self.v = int
        self.w = int

    def StringVariable(self, text):
        self.TextVariable.set(text)

    def ClickCursor(self, event):
        self.index_cursor = int(self.index("@%d" % event.x))
        try:
            end = len(str(self.expression))
            if self.index_cursor < end:
                self.index_cursor, self.ex_nbr = self.ControlCursor()
        except Exception:
            pass
        self.icursor(self.index_cursor)

    def DirectionCursor(self, key):
        if key == 'Right':
            end = len(str(self.expression))
            if self.index_cursor < end:
                try:
                    self.index_cursor, self.ex_nbr = self.ControlCursor()
                    self.index_cursor += self.store_order[self.ex_nbr + 1]
                    self.icursor(self.index_cursor)
                except Exception:
                    self.index_cursor, self.ex_nbr = self.ControlCursor()
                    self.icursor(self.index_cursor)
            else:
                pass

        elif key == 'Left':
            if self.index_cursor > 0:
                self.index_cursor, self.ex_nbr = self.ControlCursor()
                self.index_cursor -= self.store_order[self.ex_nbr]
                self.icursor(self.index_cursor)
            else:
                pass

    def ControlCursor(self):
        self.ind_nbr = 0
        self.ex_nbr = 0
        while True:
            self.ind_nbr += self.store_order[self.ex_nbr]
            if self.index_cursor == 0:
                return 0, -1
            elif self.index_cursor <= self.ind_nbr:
                return self.ind_nbr, self.ex_nbr
            self.ex_nbr += 1

    def RealStringInsertion(self, str_now):
        how = len(self.store_expression)
        now = str(str_now[:self.index_cursor])
        real = ''
        self.n = 0
        while self.n < how:
            real += str(self.store_expression[self.n])
            self.permit = None
            if now == real:
                self.permit = True
                break
            self.n += 1
        return self.permit, self.n

    def RemoveFromString(self):
        end = len(str(self.expression))
        self.permit, self.n = self.RealStringInsertion(self.expression)
        pro = self.index_cursor - self.store_order[self.n]
        if self.index_cursor == 0:
            pass
        else:
            if end == self.index_cursor and self.permit:
                self.expression = self.expression[:-self.store_order[self.n]]
                self.index_cursor -= self.store_order[int(self.n)]
                self.store_expression.pop(int(self.n))
                self.store_order.pop(int(self.n))
            elif pro == 0 and self.permit:
                self.expression = self.expression[self.store_order[self.n]:]
                self.index_cursor -= self.store_order[int(self.n)]
                self.store_expression.pop(int(self.n))
                self.store_order.pop(int(self.n))
            else:
                if self.permit:
                    self.expression = self.expression[:pro] + self.expression[self.index_cursor:]
                    self.index_cursor -= self.store_order[int(self.n)]
                    self.store_expression.pop(int(self.n))
                    self.store_order.pop(int(self.n))
                else:
                    pass
            self.StringVariable(self.expression)
            return self.expression

    def InsertIntoString(self, str_to_insert):
        end = len(str(self.expression))
        self.permit, self.n = self.RealStringInsertion(self.expression)
        if self.index_cursor == 0:
            self.expression = self.expression[:self.index_cursor] + str_to_insert + self.expression[self.index_cursor:]
            self.store_expression.insert(0, str(str_to_insert))
            self.store_order.insert(0, len(str(str_to_insert)))
            self.index_cursor += int(len(str(str_to_insert)))
        elif self.index_cursor == end or self.permit:
            self.expression = self.expression[:self.index_cursor] + str_to_insert + self.expression[self.index_cursor:]
            self.store_expression.insert(int(self.n) + 1, str(str_to_insert))
            self.store_order.insert(int(self.n) + 1, len(str(str_to_insert)))
            self.index_cursor += int(len(str(str_to_insert)))
        else:
            self.expression = self.expression
        self.StringVariable(self.expression)
        return self.expression

    def FullReBuild(self, call_back):
        try:
            self.expression = ''
            self.v = int(len(self.store_expression)) - 1
            self.w = int(len(self.store_expression))
            while True:
                operation = str(self.store_expression[self.v])
                if operation == '**' or operation == '+' or operation == '-' or operation == '*' or operation == '/' \
                        or operation == '**2' or operation == '^':
                    for y in range(self.v, self.w):
                        self.expression += str(self.store_expression[y])
                    self.expression = str('(') + str(call_back[-1]) + str(')') + str(self.expression)
                    self.answer = eval(self.expression)
                    return self.answer
                elif operation == 'e+' or operation == 'e-':
                    for y in range(self.v, self.w):
                        self.expression += str(self.store_expression[y])
                    self.expression = str(call_back[-1]) + str(self.expression)
                    self.answer = eval(self.expression)
                    return self.answer
                self.v -= 1
        except Exception:
            try:
                self.expression = str(self.store_expression[0]) + str(call_back[-1]) + str(')')
                self.answer = eval(self.expression)
                return self.answer
            except Exception:
                self.v = int(len(self.store_expression)) - 1
                while self.v >= 0:
                    operation = int(len(self.store_expression[self.v]))
                    if operation > 3:
                        self.expression = str(self.store_expression[self.v]) + str(call_back[-1]) + str(')')
                        self.answer = eval(self.expression)
                        return self.answer
                    self.v -= 1
                self.expression = str(call_back[-1])
                self.answer = eval(self.expression)
                return self.answer

    def Reset(self):
        self.icursor(0)
        self.expression = ''
        self.store_expression = []
        self.store_order = []
        self.index_cursor = int(self.index(INSERT))

    def Clear(self):
        self.StringVariable('')
        self.icursor(0)
        self.expression = ''
        self.store_expression = []
        self.store_order = []
        self.index_cursor = 0


class HoverButton(Button):
    def __init__(self, master=None, cnf=None, *args, **kwargs):
        if cnf is None:
            cnf = {}
        kw = _cnfmerge((kwargs, cnf))
        self.DBG = kw['background']
        self.ABG = kw['activeback']
        super(HoverButton, self).__init__(master=master, *args, **kwargs)
        self.bind_class(self, "<Enter>", self.Enter)
        self.bind_class(self, "<Leave>", self.Leave)

    def Enter(self, event):
        self['bg'] = self.ABG

    def Leave(self, event):
        self['bg'] = self.DBG


class ScrolledListbox(Listbox):
    def __init__(self, master, *args, **kwargs):
        self.canvas = Canvas(master)
        self.canvas.rowconfigure(0, weight=1)
        self.canvas.columnconfigure(0, weight=1)

        Listbox.__init__(self, self.canvas, *args, **kwargs)
        self.grid(row=0, column=0, sticky=NSEW)

        self.vbar = Scrollbar(self.canvas, orient=VERTICAL)
        self.hbar = Scrollbar(self.canvas, orient=HORIZONTAL)

        self.configure(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)

        self.vbar.grid(row=0, column=1, sticky=NS)
        self.vbar.configure(command=self.yview)
        self.hbar.grid(row=1, column=0, sticky=EW)
        self.hbar.configure(command=self.xview)

        # Copy geometry methods of self.canvas without overriding Listbox
        # methods -- hack!
        listbox_meths = vars(Listbox).keys()
        methods = vars(Pack).keys() | vars(Grid).keys() | vars(Place).keys()
        methods = methods.difference(listbox_meths)

        for m in methods:
            if m[0] != '_' and m != 'config' and m != 'configure':
                setattr(self, m, getattr(self.canvas, m))

    def __str__(self):
        return str(self.canvas)


class ScrollableTkAggX(tk.Canvas):
    def __init__(self, figure, master, **kw):
        # --- create canvas with scrollbar ---
        facecolor = str(to_hex(figure.get_facecolor()))
        super(ScrollableTkAggX, self).__init__(master, background=facecolor, **kw)
        self.grid(row=0, column=0, sticky=tk.NSEW)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.fig_wrapper = tk.Frame(self, background=facecolor)
        self.fig_wrapper.grid(row=0, column=0, sticky=tk.NSEW)
        self.fig_wrapper.rowconfigure(0, weight=1)
        self.fig_wrapper.columnconfigure(0, weight=1)

        self.TkAgg = FigureCanvasTkAgg(figure, master=self.fig_wrapper)
        self.TkAggWidget = self.TkAgg.get_tk_widget()
        self.TkAggWidget.configure(background=facecolor)
        self.TkAggWidget.grid(row=0, column=0, sticky=tk.NSEW)

        self.hbar = Scrollbar(self, orient=tk.HORIZONTAL, command=self.xview)
        self.hbar.grid(row=1, column=0, sticky=tk.EW)

        self.configure(xscrollcommand=self.hbar.set, scrollregion=self.bbox(tk.ALL))

        # when all widgets are in canvas
        self.bind('<Configure>', self.on_configure)
        # --- put frame in canvas ---
        self.canvas_frame = self.create_window((0, 0), window=self.fig_wrapper, anchor=tk.NW)

    # expand canvas_frame when canvas changes its size
    def on_configure(self, event):
        # when all widgets are in canvas
        canvas_height = event.height
        self.itemconfigure(self.canvas_frame, height=canvas_height - 20)
        # update scrollregion after starting 'mainloop'
        self.configure(scrollregion=self.bbox(tk.ALL))

    def Draw(self):
        self.TkAgg.draw()
        self.xview_moveto(0)


class ScrollableTkAggXY(tk.Canvas):
    def __init__(self, figure, master, **kw):
        # --- create canvas with scrollbar ---
        super(ScrollableTkAggXY, self).__init__(master, **kw)
        self.grid(row=0, column=0, sticky=tk.NSEW)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.fig_wrapper = tk.Frame(self)
        self.fig_wrapper.grid(row=0, column=0, sticky=tk.NSEW)
        self.fig_wrapper.rowconfigure(0, weight=1)
        self.fig_wrapper.columnconfigure(0, weight=1)

        self.TkAgg = FigureCanvasTkAgg(figure, master=self.fig_wrapper)
        self.TkAggWidget = self.TkAgg.get_tk_widget()
        self.TkAggWidget.grid(row=0, column=0, sticky=tk.NSEW)

        self.vbar = Scrollbar(self, orient=tk.VERTICAL, command=self.yview)
        self.vbar.grid(row=0, column=1, sticky=tk.NS)

        self.hbar = Scrollbar(self, orient=tk.HORIZONTAL, command=self.xview)
        self.hbar.grid(row=1, column=0, sticky=tk.EW)

        self.configure(yscrollcommand=self.vbar.set, xscrollcommand=self.hbar.set, scrollregion=self.bbox(tk.ALL))

        # --- put frame in canvas ---
        self.canvas_frame = self.create_window((0, 0), window=self.fig_wrapper, anchor=tk.NW)

    # expand canvas_frame when canvas changes its size
    def on_configure(self):
        # when all widgets are in canvas
        Size = self.TkAgg.get_width_height()
        self.itemconfigure(self.canvas_frame, height=int(Size[1]))
        # update scrollregion after starting 'mainloop'
        self.configure(scrollregion=self.bbox(tk.ALL))
        self.yview_moveto(1)
        self.xview_moveto(0)

    def Draw(self):
        self.TkAgg.draw()
        self.on_configure()


class FigureXY(Figure):
    def __init__(self, fontsize, **kwargs):
        super(FigureXY, self).__init__(**kwargs)
        self.fontsize = fontsize
        self.AxesXY = self.add_subplot(1, 1, 1)
        self.latex_math = []

    def TextMath(self):
        demo = self.latex_math[-1]
        self.AxesXY.text(0, 0.5, demo, fontsize=self.fontsize)
        self.AxesXY.axis('off')
        self.AxesXY.set_xticklabels("", visible=False)
        self.AxesXY.set_yticklabels("", visible=False)

    def AddFirstLaTex(self, character):
        self.latex_math.append(character)
        self.TextMath()
        try:
            self.tight_layout()  # pad=-1, h_pad=-3 h_pad=2
        except Exception:
            pass

    def AddMultiLaTex(self, character):
        self.latex_math.append(character)

        n_lines = int(len(self.latex_math))
        self.AxesXY = self.add_subplot(n_lines, 1, n_lines)

        self.TextMath()

        n_axes = len(self.axes)
        for i_axes in range(n_axes):
            self.axes[i_axes].change_geometry(n_axes, 1, i_axes + 1)

        oldSize = self.get_size_inches()
        mac1 = len(self.latex_math[-1])
        mac2 = len(self.latex_math[-2])
        if mac1 > 20 or mac2 > 30 or mac2 > 20 or mac1 > 30:
            self.set_size_inches(1.35 + oldSize[0], 1.35 + oldSize[1])
        else:
            self.set_size_inches(0.7 + s for s in oldSize)

        try:
            self.tight_layout()  # pad=-1, h_pad=-3 h_pad=2
        except Exception:
            pass


class TkFigurePlot(tk.Canvas):
    def __init__(self, figure, master, **kw):
        super(TkFigurePlot, self).__init__(master, **kw)
        self.grid(row=0, column=0, sticky=tk.NSEW)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        self.TkAgg = FigureCanvasTkAgg(figure, master=self)
        self.TkAggWidget = self.TkAgg.get_tk_widget()
        self.TkAggWidget.grid(row=1, column=0, sticky=NSEW)

        self.ToolBarFrame = Frame(self)
        self.ToolBarFrame.grid(row=0, column=0)

        self.ToolBar = NavigationToolbar2Tk(self.TkAgg, self.ToolBarFrame)
        self.ToolBar.update()

    def Destroy(self):
        self.ToolBarFrame.destroy()
        self.TkAggWidget.destroy()

    def Draw(self):
        self.TkAgg.draw()


class BackEndPlot(tk.Canvas):
    def __init__(self, master, **kw):
        super(BackEndPlot, self).__init__(master, **kw)
        self.grid(row=0, column=0, sticky=NSEW)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.Figure = Figure(figsize=(6, 3), facecolor='#F0F0F0')
        self.TkAgg = TkFigurePlot(figure=self.Figure, master=self)
        self.TkAgg.grid(row=0, column=0, sticky=NSEW)

    def Plot(self, function_to_plot):
        FunctionToPlot = function_to_plot
        # PlotBackEnd = FunctionToPlot.backend(FunctionToPlot)
        PlotBackEnd = plot_backends['matplotlib'](FunctionToPlot)
        PlotBackEnd.process_series()

        AXg = PlotBackEnd.ax[0]

        self.Figure = PlotBackEnd.fig
        self.Figure._remove_ax(AXg)
        self.Figure.add_axes(AXg)
        self.Figure.set_size_inches(6, 3)
        self.Figure.tight_layout()

        self.TkAgg.Destroy()
        self.TkAgg = TkFigurePlot(figure=self.Figure, master=self)
        self.TkAgg.grid(row=0, column=0, sticky=NSEW)
        self.TkAgg.Draw()
