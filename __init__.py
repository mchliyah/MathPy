from tkinter import *
from tkinter import _cnfmerge as cnfmerge


class HoverButton(Button):
    def __init__(self, master=None, cnf=None, **kw):
        if cnf is None:
            cnf = {}
        kw = cnfmerge((kw, cnf))
        self.DefaultBackGround = kw['background']
        self.ActiveBack = kw['activeback']
        super(HoverButton, self).__init__(master=master, **kw)
        self.bind_class(self, "<Enter>", self.Enter)
        self.bind_class(self, "<Leave>", self.Leave)

    def Enter(self, event):
        self['bg'] = self.ActiveBack

    def Leave(self, event):
        self['bg'] = self.DefaultBackGround


class ScrolledListbox(Listbox):
    def __init__(self, master=None, **kw):
        self.canvas = Canvas(master)
        self.canvas['bg'] = kw['bg']
        Listbox.__init__(self, self.canvas, **kw)

        self.vbar = Scrollbar(self.canvas, orient="vertical")
        self.vbar.pack(side=RIGHT, fill=Y, expand=True)

        self.hbar = Scrollbar(self.canvas, orient="horizontal")
        self.hbar.pack(side=BOTTOM, fill=X, expand=True)

        kw.update(
            {'yscrollcommand': self.vbar.set, 'xscrollcommand': self.hbar.set, 'scrollregion': (0, 0, 1000, 1000)})
        self.vbar['command'] = self.yview
        self.hbar['command'] = self.xview

        self.pack(side=LEFT and TOP, fill=BOTH, expand=True)

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
