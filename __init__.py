from math import log2, log10
from tkinter import _cnfmerge, Button, Listbox, Canvas, Scrollbar, Grid, Pack, Place, HORIZONTAL, VERTICAL, NSEW, NS, EW

from sympy import sinh, cosh, tanh, asinh, acosh, atanh, log, exp, factorial


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


class HoverButton(Button):
    def __init__(self, master=None, cnf=None, *args, **kwargs):
        if cnf is None:
            cnf = {}
        kw = _cnfmerge((kwargs, cnf))
        self.DefaultBackGround = kw['background']
        self.ActiveBack = kw['activeback']
        super(HoverButton, self).__init__(master=master, *args, **kwargs)
        self.bind_class(self, "<Enter>", self.Enter)
        self.bind_class(self, "<Leave>", self.Leave)

    def Enter(self, event):
        self['bg'] = self.ActiveBack

    def Leave(self, event):
        self['bg'] = self.DefaultBackGround


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
