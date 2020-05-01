from tkinter import _cnfmerge, Button, Listbox, Canvas, Scrollbar, Grid, Pack, Place, HORIZONTAL, VERTICAL, NSEW, NS, EW
from operator import neg
from random import randint
from sympy import sqrt, N
from sympy.plotting import PlotGrid

text = ''
permit = None
delf = ()
nbr = int
n = int
v = int
w = int


def ControlCursor(index, nbr_order):
    global n, nbr
    nbr = 0
    n = 0
    while True:
        nbr += nbr_order[n]
        if index == 0:
            return 0, -1
        elif index <= nbr:
            return nbr, n
        n += 1


def RealStringInsertion(str_now, index, str_order):
    global permit, n
    how = len(str_order)
    now = str(str_now[:index])
    real = ''
    n = 0
    while n < how:
        real += str(str_order[n])
        permit = None
        if now == real:
            permit = True
            break
        n += 1
    return permit, n


def RemoveFromString(str_to_remove, index, nbr_order, str_order):
    global text, permit, n
    end = len(str(str_to_remove))
    permit, n = RealStringInsertion(str_to_remove, index, str_order)
    pro = index - nbr_order[n]
    if index == 0:
        pass
    else:
        if end == index and permit:
            text = str_to_remove[:-nbr_order[n]]
            index -= nbr_order[int(n)]
            str_order.pop(int(n))
            nbr_order.pop(int(n))
        elif pro == 0 and permit:
            text = str_to_remove[nbr_order[n]:]
            index -= nbr_order[int(n)]
            str_order.pop(int(n))
            nbr_order.pop(int(n))
        else:
            if permit:
                text = str_to_remove[:pro] + str_to_remove[index:]
                index -= nbr_order[int(n)]
                str_order.pop(int(n))
                nbr_order.pop(int(n))
            else:
                pass
        return text, index


def InsertIntoString(string, str_to_insert, index, nbr_order, str_order):
    global text, permit, n
    end = len(str(string))
    permit, n = RealStringInsertion(string, index, str_order)
    if index == 0:
        text = string[:index] + str_to_insert + string[index:]
        str_order.insert(0, str(str_to_insert))
        nbr_order.insert(0, len(str(str_to_insert)))
        index += int(len(str(str_to_insert)))
    elif index == end or permit:
        text = string[:index] + str_to_insert + string[index:]
        str_order.insert(int(n) + 1, str(str_to_insert))
        nbr_order.insert(int(n) + 1, len(str(str_to_insert)))
        index += int(len(str(str_to_insert)))
    else:
        text = string
    return text, index


def ReBuild(str_order):
    global v, w
    try:
        expression = ''
        v = int(len(str_order)) - 1
        w = int(len(str_order))
        while True:
            operation = str(str_order[v])
            if operation == '**' or operation == '+' or operation == '-' or operation == '*' or operation == '/' \
                    or operation == '^':
                for y in range(v, w):
                    expression += str(str_order[y])
                return expression
            v -= 1
    except Exception:
        pass


def TwoPlotColorTwoFunc(PlotFirstFunc, PlotAddFunc, callback_function):
    PlotFirstFunc.append(PlotAddFunc[0])
    s = int((len(callback_function) / 2) - 1)
    RD = randint(1048576, 16777000)
    HX = hex(RD)
    HX = HX[2:8].upper()
    PlotFirstFunc[s].line_color = str('#') + str(HX)
    PlotGrid(1, 2, PlotFirstFunc, PlotAddFunc)


def TwoPlotColorOneFunc(PlotFirstFunc, PlotAddFunc, callback_function):
    PlotFirstFunc.append(PlotAddFunc[0])
    s = int(len(callback_function) - 1)
    RD = randint(1048576, 16777000)
    HX = hex(RD)
    HX = HX[2:8].upper()
    PlotFirstFunc[s].line_color = str('#') + str(HX)
    PlotGrid(1, 2, PlotFirstFunc, PlotAddFunc)


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
