from tkinter import _cnfmerge
from tkinter import *
from operator import neg
from random import randint
from sympy import *
from sympy.abc import x, y, z
from sympy.plotting import PlotGrid
import tkinter as tk
from tkinter import Scrollbar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

delf = ()


def fctrl(arg):
    return factorial(arg).evalf()


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


def TwoPlotMultiColor(Plot_First_Func, Plot_Add_Func, Function):
    Plot_First_Func.extend(Plot_Add_Func)
    RD = randint(1048576, 16777000)
    HX = hex(RD)
    HX = HX[2:8].upper()
    Plot_First_Func[-1].line_color = str('#') + str(HX)
    Plot_First_Func[-1].label = LaTex(sympify(Function))
    PlotGrid(1, 2, Plot_First_Func, Plot_Add_Func, legend=True)
    return Plot_First_Func


def LabelLatexPlot(Plot_First_Func, Function):
    Plot_First_Func[-1].label = LaTex(sympify(Function))
    Plot_First_Func.show()


def TwoPlot3D(Plot_First_Func, Plot_Add_Func):
    Plot_First_Func.extend(Plot_Add_Func)
    PlotGrid(1, 2, Plot_First_Func, Plot_Add_Func, legend=True)
    return Plot_First_Func


def EQT(nbr_a, nbr_b, nbr_c):
    global delf
    a = float(eval(nbr_a))
    b = float(eval(nbr_b))
    c = float(eval(nbr_c))
    d = float((b ** 2) - 4 * a * c)
    nd = neg(d)
    nb = neg(b)
    if a > 0 or a < 0:
        delf = (
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


class TextManager:
    def __init__(self):
        self.text = ''
        self.expression = ''
        self.answer = ''
        # store expressions & order
        self.store_expression = []
        self.store_order = []
        self.permit = None
        self.nbr = int
        self.n = int
        self.v = int
        self.w = int

    def ControlCursor(self, index):
        self.nbr = 0
        self.n = 0
        while True:
            self.nbr += self.store_order[self.n]
            if index == 0:
                return 0, -1
            elif index <= self.nbr:
                return self.nbr, self.n
            self.n += 1

    def RealStringInsertion(self, str_now, index):
        how = len(self.store_expression)
        now = str(str_now[:index])
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

    def RemoveFromString(self, remove_from_str, index):
        end = len(str(remove_from_str))
        self.permit, self.n = self.RealStringInsertion(remove_from_str, index)
        pro = index - self.store_order[self.n]
        if index == 0:
            pass
        else:
            if end == index and self.permit:
                self.text = remove_from_str[:-self.store_order[self.n]]
                index -= self.store_order[int(self.n)]
                self.store_expression.pop(int(self.n))
                self.store_order.pop(int(self.n))
            elif pro == 0 and self.permit:
                self.text = remove_from_str[self.store_order[self.n]:]
                index -= self.store_order[int(self.n)]
                self.store_expression.pop(int(self.n))
                self.store_order.pop(int(self.n))
            else:
                if self.permit:
                    self.text = remove_from_str[:pro] + remove_from_str[index:]
                    index -= self.store_order[int(self.n)]
                    self.store_expression.pop(int(self.n))
                    self.store_order.pop(int(self.n))
                else:
                    pass
            return self.text, index

    def InsertIntoString(self, insert_into_str, str_to_insert, index):
        end = len(str(insert_into_str))
        self.permit, self.n = self.RealStringInsertion(insert_into_str, index)
        if index == 0:
            self.text = insert_into_str[:index] + str_to_insert + insert_into_str[index:]
            self.store_expression.insert(0, str(str_to_insert))
            self.store_order.insert(0, len(str(str_to_insert)))
            index += int(len(str(str_to_insert)))
        elif index == end or self.permit:
            self.text = insert_into_str[:index] + str_to_insert + insert_into_str[index:]
            self.store_expression.insert(int(self.n) + 1, str(str_to_insert))
            self.store_order.insert(int(self.n) + 1, len(str(str_to_insert)))
            index += int(len(str(str_to_insert)))
        else:
            self.text = insert_into_str
        return self.text, index

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
                    character = str('(') + str(call_back[-1]) + str(')') + str(self.expression)
                    self.answer = eval(character)
                    return self.answer, character
                elif operation == 'e+' or operation == 'e-':
                    for y in range(self.v, self.w):
                        self.expression += str(self.store_expression[y])
                    character = str(call_back[-1]) + str(self.expression)
                    self.answer = eval(character)
                    return self.answer, character
                self.v -= 1
        except Exception:
            try:
                self.expression = str(self.store_expression[0]) + str(call_back[-1]) + str(')')
                self.answer = eval(self.expression)
                return self.answer, self.expression
            except Exception:
                self.v = int(len(self.store_expression)) - 1
                while self.v >= 0:
                    operation = int(len(self.store_expression[self.v]))
                    if operation > 3:
                        self.expression = str(self.store_expression[self.v]) + str(call_back[-1]) + str(')')
                        self.answer = eval(self.expression)
                        return self.answer, self.expression
                    self.v -= 1
                self.expression = str(call_back[-1])
                self.answer = eval(self.expression)
                return self.answer, self.expression

    def ResetClear(self):
        self.store_expression = []
        self.store_order = []


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


class ScrollableTkAggX(FigureCanvasTkAgg):
    def __init__(self, figure, master, *args, **kwargs):
        # --- create canvas with scrollbar ---
        self.canvas = tk.Canvas(master)
        self.canvas.grid(row=0, column=0, sticky=tk.NSEW)
        self.canvas.rowconfigure(0, weight=1)
        self.canvas.columnconfigure(0, weight=1)

        self.fig_wrapper = tk.Frame(self.canvas)
        self.fig_wrapper.grid(row=0, column=0, sticky=tk.NSEW)
        self.fig_wrapper.rowconfigure(0, weight=1)
        self.fig_wrapper.columnconfigure(0, weight=1)

        super(ScrollableTkAggX, self).__init__(figure, master=self.fig_wrapper, *args, **kwargs)
        self.tkagg = self.get_tk_widget()
        self.tkagg.grid(row=0, column=0, sticky=tk.NSEW)

        self.hbar = Scrollbar(self.canvas, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.hbar.grid(row=1, column=0, sticky=tk.EW)

        self.canvas.configure(xscrollcommand=self.hbar.set, scrollregion=self.canvas.bbox(tk.ALL))

        # when all widgets are in canvas
        self.canvas.bind('<Configure>', self.on_configure)
        # --- put frame in canvas ---
        self.canvas_frame = self.canvas.create_window((0, 0), window=self.fig_wrapper, anchor=tk.NW)

    # expand canvas_frame when canvas changes its size
    def on_configure(self, event):
        # when all widgets are in canvas
        canvas_height = event.height
        self.canvas.itemconfigure(self.canvas_frame, height=canvas_height - 20)
        # update scrollregion after starting 'mainloop'
        self.canvas.configure(scrollregion=self.canvas.bbox(tk.ALL))


class ScrollableTkAggXY(FigureCanvasTkAgg):
    def __init__(self, figure, master, *args, **kwargs):
        # --- create canvas with scrollbar ---
        self.canvas = tk.Canvas(master)
        self.canvas.grid(row=0, column=0, sticky=tk.NSEW)
        self.canvas.rowconfigure(0, weight=1)
        self.canvas.columnconfigure(0, weight=1)

        self.fig_wrapper = tk.Frame(self.canvas)
        self.fig_wrapper.grid(row=0, column=0, sticky=tk.NSEW)
        self.fig_wrapper.rowconfigure(0, weight=1)
        self.fig_wrapper.columnconfigure(0, weight=1)

        super(ScrollableTkAggXY, self).__init__(figure, master=self.fig_wrapper, *args, **kwargs)
        self.tkagg = self.get_tk_widget()
        self.tkagg.grid(row=0, column=0, sticky=tk.NSEW)

        self.vbar = Scrollbar(self.canvas, orient=tk.VERTICAL, command=self.canvas.yview)
        self.vbar.grid(row=0, column=1, sticky=tk.NS)

        self.hbar = Scrollbar(self.canvas, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.hbar.grid(row=1, column=0, sticky=tk.EW)

        self.canvas.configure(yscrollcommand=self.vbar.set, xscrollcommand=self.hbar.set,
                              scrollregion=self.canvas.bbox(tk.ALL))

        # --- put frame in canvas ---
        self.canvas_frame = self.canvas.create_window((0, 0), window=self.fig_wrapper, anchor=tk.NW)

    # expand canvas_frame when canvas changes its size
    def on_configure(self):
        # when all widgets are in canvas
        Size = self.get_width_height()
        self.canvas.itemconfigure(self.canvas_frame, height=int(Size[1]))
        # update scrollregion after starting 'mainloop'
        self.canvas.configure(scrollregion=self.canvas.bbox(tk.ALL))
        self.canvas.yview_moveto(1)
        self.canvas.xview_moveto(0)

    def Draw(self):
        self.draw()
        self.on_configure()


class TkFigureFrame(FigureCanvasTkAgg):
    def __init__(self, figure, window, *args, **kwargs):
        self.canvas = Canvas(master=window)
        self.canvas.rowconfigure(0, weight=1)
        self.canvas.columnconfigure(0, weight=1)

        super(TkFigureFrame, self).__init__(figure=figure, master=self.canvas, *args, **kwargs)
        self.TkAggWidget = self.get_tk_widget()
        self.TkAggWidget.grid(row=1, column=0, sticky=NSEW)

        self.ToolBarFrame = Frame(master=self.canvas)
        self.ToolBarFrame.grid(row=0, column=0)
        self.ToolBarFrame.columnconfigure(0, weight=1)

        self.ToolBar = NavigationToolbar2Tk(self, self.ToolBarFrame)
        self.ToolBar.update()
        self.ToolBar.grid(row=0, column=0)
        self.ToolBar.columnconfigure(0, weight=1)
