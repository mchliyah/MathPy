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
        self.frame = Frame(master)
        self.vbar = Scrollbar(self.frame)
        self.vbar.pack(side=RIGHT, fill=Y)

        kw.update({'yscrollcommand': self.vbar.set})
        Listbox.__init__(self, self.frame, **kw)
        self.pack(side=LEFT, fill=BOTH, expand=True)
        self.vbar['command'] = self.yview

        # Copy geometry methods of self.frame without overriding Listbox
        # methods -- hack!
        listbox_meths = vars(Listbox).keys()
        methods = vars(Pack).keys() | vars(Grid).keys() | vars(Place).keys()
        methods = methods.difference(listbox_meths)

        for m in methods:
            if m[0] != '_' and m != 'config' and m != 'configure':
                setattr(self, m, getattr(self.frame, m))

    def __str__(self):
        return str(self.frame)
