import tkinter as tk
import itertools
from random import randint
from sympy import *
from sympy.abc import x, y, z
from sympy.parsing.sympy_parser import parse_expr
import matplotlib

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.colors import to_hex
# from mpl_toolkits.mplot3d import Axes3D
from sympy.plotting import PlotGrid, plot_backends

delf = ()



def DrawAfter(character):
    try:
      simplify = sympify(character, rational=True, evaluate=True)
      return LaTex(simplify)
    except Exception:
        return character


def DrawAfterNum(character):
    try:
        simplify = sympify(character, rational=True, evaluate=True).evalf()
        return LaTex(simplify)
    except None:
        pass
    except Exception:
        pass


def DrawBefore(character):
    try:
        pik = str(character).replace('integrate', 'Integral').replace('diff', 'Derivative')
        # expression = sympify(pik, rational=True, evaluate=False)
        expression = parse_expr(pik, evaluate=False)
        return LaTex(expression)
    except None:
        pass
    except Exception:
        pass


def LaTex(Math_Expression):
    TEX = '$' + latex(Math_Expression) + '$'
    # TEX = r"$%s$" % latex(Math_Expression)
    # TEX = f'${latex(Math_Expression)}$'
    return TEX


def MultiPlot2D(Plot_First_Func2D, Plot_Add_Func2D, Function2D):
    Plot_First_Func2D.extend(Plot_Add_Func2D)
    RD = randint(1048576, 16777000)
    HX = hex(RD)
    HX = HX[2:8].upper()
    Plot_First_Func2D[-1].line_color = str('#') + str(HX)
    Plot_First_Func2D[-1].label = LaTex(sympify(Function2D))
    return PlotGrid(1, 2, Plot_First_Func2D, Plot_Add_Func2D, legend=True, show=False)


def MultiPlot2D3D(Plot_First_Func2D, Plot_Add_Func2D, Plot_First_Func3D, Plot_Add_Func3D, Function2D):
    RD = randint(1048576, 16777000)
    HX = hex(RD)
    HX = HX[2:8].upper()

    Plot_First_Func2D.extend(Plot_Add_Func2D)
    Plot_First_Func2D[-1].line_color = str('#') + str(HX)
    Plot_First_Func2D[-1].label = LaTex(sympify(Function2D))

    Plot_First_Func3D.extend(Plot_Add_Func3D)
    Plot_First_Func3D[-1].line_color = str('#') + str(HX)
    Plot_First_Func3D[-1].label = LaTex(sympify(Function2D))

    return PlotGrid(1, 2, Plot_First_Func2D, Plot_First_Func3D, legend=True, show=False)


def OnePlotLaTex(Plot_First_Func, FunctionTX):
    Plot_First_Func[-1].label = LaTex(sympify(FunctionTX))
    return Plot_First_Func.show()


def FirstPlotLaTex(Plot_First_Func, FunctionTX):
    Plot_First_Func[-1].label = LaTex(sympify(FunctionTX))
    return Plot_First_Func


def MultiPlot3D(Plot_First_Func3D, Plot_Add_Func3D):
    Plot_First_Func3D.extend(Plot_Add_Func3D)
    return PlotGrid(1, 2, Plot_First_Func3D, Plot_Add_Func3D, show=False)


class HoverButton(tk.Button):
    def __init__(self, master=None, cnf=None, **kwargs):
        if cnf is None:
            cnf = {}
        cnf = tk._cnfmerge((cnf, kwargs))
        super(HoverButton, self).__init__(master=master, cnf=cnf, **kwargs)
        self.DBG = kwargs['background']
        self.ABG = kwargs['activeback']
        self.bind_class(self, "<Enter>", self.Enter)
        self.bind_class(self, "<Leave>", self.Leave)

    def Enter(self, event):
        self['bg'] = self.ABG

    def Leave(self, event):
        self['bg'] = self.DBG


class ManagedEntry(tk.Entry):
    def __init__(self, master=None, cnf=None, **kw):
        if cnf is None:
            cnf = {}
        kw = tk._cnfmerge((kw, cnf))
        self.TextVariable = tk.StringVar()
        super(ManagedEntry, self).__init__(master=master, textvariable=self.TextVariable, cnf={}, **kw)
        self.bind_class(self, "<Button-1>", self.ClickCursor)
        self.bind_class(self, "<Key>", self.Keyboard)
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

    def Keyboard(self, keyword):

        if keyword.keysym == 'Right':
            self.DirectionCursor('Right')

        elif keyword.keysym == 'Left':
            self.DirectionCursor('Left')

    def StringVariable(self):
        self.TextVariable.set(self.expression)
        self.icursor(self.index_cursor)

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
        self.StringVariable()
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

        self.AdditionalInsertionTools(str_to_insert)
        self.StringVariable()
        return self.expression

    def AdditionalInsertionTools(self, string):
        if string[-1:] == '(':
            self.InsertIntoString(')'), self.DirectionCursor('Left')
        if string == ',-1':
            self.DirectionCursor('Left')

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

    def Clear(self):
        self.expression = ''
        self.store_expression = []
        self.store_order = []
        self.index_cursor = int(self.index(tk.INSERT))
        self.index_cursor = 0
        self.StringVariable()


class ScrollableTkAggX(tk.Canvas):
    def __init__(self, figure, height, master, **kw):
        self.height = height
        facecolor = str(to_hex(figure.get_facecolor()))
        # --- create canvas with scrollbar ---
        super(ScrollableTkAggX, self).__init__(master, height=self.height, background=facecolor, **kw)
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

        self.hbar = tk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.xview)
        self.hbar.grid(row=1, column=0, sticky=tk.EW)

        # --- put frame in canvas ---
        self.canvas_frame = self.create_window((0, 0), window=self.fig_wrapper, height=self.height, anchor=tk.NW)
        self.configure(xscrollcommand=self.hbar.set, scrollregion=self.bbox(tk.ALL))

    # expand canvas_frame when canvas changes its size
    def on_configure_x(self, width):
        # when all widgets are in canvas
        self.itemconfigure(self.canvas_frame, width=width)
        # update scrollregion after starting 'mainloop'
        self.configure(scrollregion=self.bbox(tk.ALL))

    def Draw(self, width):
        self.on_configure_x(width)
        self.TkAgg.draw()
        self.xview_moveto(0)


class FigureX(Figure):
    def __init__(self, fontsize, rgbcolor, **kwargs):
        super(FigureX, self).__init__(tight_layout=True, **kwargs)
        self.fontsize = fontsize
        self.mpl_rgb = rgbcolor
        self.size_w = [0]
        self.width = max(self.size_w)

    def DrawOneLaTex(self, la_text):
        self.clear()
        Text = self.text(0, 0.5, la_text, color=self.mpl_rgb, fontsize=self.fontsize)

        Renderer = self.canvas.get_renderer()
        bb = Text.get_window_extent(renderer=Renderer)
        self.width = int(bb.width)

        self.tight_layout(renderer=Renderer)

    def DrawBiLaTex(self, la_text1, la_text2):
        self.size_w = [0]
        self.clear()
        Text1 = self.text(0, 0.75, la_text1, color=self.mpl_rgb, fontsize=self.fontsize)
        Text2 = self.text(0, 0.3, la_text2, color=self.mpl_rgb, fontsize=self.fontsize)

        Renderer = self.canvas.get_renderer()
        bb1 = Text1.get_window_extent(renderer=Renderer)
        bb2 = Text2.get_window_extent(renderer=Renderer)
        self.size_w.append((int(bb1.width) + 1))
        self.size_w.append((int(bb2.width) + 1))
        self.width = max(self.size_w)

        self.tight_layout(renderer=Renderer)

    def DrawTriLaTex(self, la_text1, la_text2, la_text3):
        self.size_w = [0]
        self.clear()
        Text1 = self.text(0, 0.8, la_text1, color=self.mpl_rgb, fontsize=self.fontsize)
        Text2 = self.text(0, 0.5, la_text2, color=self.mpl_rgb, fontsize=self.fontsize)
        Text3 = self.text(0, 0.2, la_text3, color=self.mpl_rgb, fontsize=self.fontsize)

        Renderer = self.canvas.get_renderer()
        bb1 = Text1.get_window_extent(renderer=Renderer)
        bb2 = Text2.get_window_extent(renderer=Renderer)
        bb3 = Text3.get_window_extent(renderer=Renderer)
        self.size_w.append((int(bb1.width) + 1))
        self.size_w.append((int(bb2.width) + 1))
        self.size_w.append((int(bb3.width) + 1))
        self.width = max(self.size_w)

        self.tight_layout(renderer=Renderer)

    def Draw(self, TkAggX):
        TkAggX.Draw(width=self.width)


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

        self.vbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.yview)
        self.vbar.grid(row=0, column=1, sticky=tk.NS)

        self.hbar = tk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.xview)
        self.hbar.grid(row=1, column=0, sticky=tk.EW)

        self.configure(yscrollcommand=self.vbar.set, xscrollcommand=self.hbar.set, scrollregion=self.bbox(tk.ALL))

        # --- put frame in canvas ---
        self.canvas_frame = self.create_window((0, 0), window=self.fig_wrapper, width=600, height=100, anchor=tk.NW)

    # expand canvas_frame when canvas changes its size
    def on_configure(self, width, height):
        # when all widgets are in canvas
        self.itemconfigure(self.canvas_frame, width=width, height=height)
        # update scrollregion after starting 'mainloop'
        self.configure(scrollregion=self.bbox(tk.ALL))
        self.yview_moveto(1)
        self.xview_moveto(0)

    def Draw(self, width, height):
        self.on_configure(width=width, height=height)
        self.TkAgg.draw()


class FigureXY(Figure):
    def __init__(self, fontsize, **kwargs):
        super(FigureXY, self).__init__(tight_layout=True, **kwargs)
        self.fontsize = fontsize
        self.Axes = self.add_subplot(1, 1, 1)
        self.Text = self.Axes.text(0, 1, '', fontsize=self.fontsize)
        self.latex_math = []
        self.size_w = [0]
        self.size_h = 0
        self.width = max(self.size_w)
        self.height = float(self.size_h)

    def DrawLaTex(self, character):
        self.latex_math.append(character)
        self.clear()
        n_lines = len(self.latex_math)
        # Gap between lines in axes coords
        self.Axes = self.add_subplot(1, 1, 1)
        self.Axes.set_ylim((0, n_lines))
        self.Axes.axis('off')
        self.Axes.set_xticklabels("", visible=False)
        self.Axes.set_yticklabels("", visible=False)

        # Plotting features formulae
        for i_line in range(0, n_lines):
            baseline = n_lines - i_line
            demo = self.latex_math[i_line]
            self.Text = self.Axes.text(0, baseline - 0.5, demo, fontsize=self.fontsize)

        Renderer = self.canvas.get_renderer()
        bb = self.Text.get_window_extent(renderer=Renderer)
        self.size_w.append((int(bb.width) + 65))
        self.size_h += (float(bb.height) * 2) + 20

        self.width = max(self.size_w)
        self.height = float(self.size_h)
        try:
            self.tight_layout(renderer=Renderer)
        except Exception:
            pass

    def Draw(self, TkAggXY):
        TkAggXY.Draw(width=self.width, height=self.height)

    def Clear(self):
        self.clear()
        self.latex_math = []
        self.size_w = [0]
        self.size_h = 0


class TkFigurePlot(tk.Frame):
    def __init__(self, figure, master, **kw):
        super(TkFigurePlot, self).__init__(master, **kw)
        self.grid(row=0, column=0, sticky=tk.NSEW)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        self.TkAgg = FigureCanvasTkAgg(figure, master=self)
        self.TkAggWidget = self.TkAgg.get_tk_widget()
        self.TkAggWidget.grid(row=1, column=0, sticky=tk.NSEW)

        self.ToolBarFrame = tk.Frame(self)
        self.ToolBarFrame.grid(row=0, column=0)

        self.ToolBar = NavigationToolbar2Tk(self.TkAgg, self.ToolBarFrame)
        self.ToolBar.update()

    def Draw(self):

        self.ToolBar.update()

        self.TkAgg.draw()


class BackEndPlot(tk.Canvas):
    def __init__(self, master, figsize, **kw):
        self.FigSize = figsize
        super(BackEndPlot, self).__init__(master, **kw)
        self.grid(row=0, column=0, sticky=tk.NSEW)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.Figure = Figure(figsize=self.FigSize, facecolor='#F0F0F0')
        self.TkAgg = TkFigurePlot(figure=self.Figure, master=self)
        self.TkAgg.grid(row=0, column=0, sticky=tk.NSEW)

    def Plot(self, function_to_plot):
        FunctionToPlot = function_to_plot
        # PlotBackEnd = FunctionToPlot.backend(FunctionToPlot)
        PlotBackEnd = plot_backends['matplotlib'](FunctionToPlot)
        PlotBackEnd.process_series()

        self.Figure = PlotBackEnd.fig
        self.Figure.set_size_inches(self.FigSize)
        self.Figure.tight_layout()

        self.TkAgg.destroy()
        self.TkAgg = TkFigurePlot(figure=self.Figure, master=self)
        self.TkAgg.grid(row=0, column=0, sticky=tk.NSEW)

    def Clear(self):
        self.TkAgg.destroy()
        self.Figure = Figure(figsize=self.FigSize, facecolor='#F0F0F0')
        self.TkAgg = TkFigurePlot(figure=self.Figure, master=self)
        self.TkAgg.grid(row=0, column=0, sticky=tk.NSEW)
class BackEndPlotpp(tk.Canvas):
    def __init__(self, master, figsize, **kw):
        self.FigSize = figsize
        super(BackEndPlot, self).__init__(master, **kw)
        self.grid(row=0, column=0, sticky=tk.NSEW)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.Figure = Figure(figsize=self.FigSize, facecolor='#F0F0F0')
        self.TkAgg = TkFigurePlot(figure=self.Figure, master=self)
        self.TkAgg.grid(row=0, column=0, sticky=tk.NSEW)

    def Plot(self, function_to_plot):
        FunctionToPlot = function_to_plot
        # PlotBackEnd = FunctionToPlot.backend(FunctionToPlot)
        PlotBackEnd = plot_backends['matplotlib'](FunctionToPlot)
        self.Figure = PlotBackEnd.fig

        self.TkAgg.destroy()
        self.TkAgg = TkFigurePlot(figure=self.Figure, master=self)
        self.TkAgg.grid(row=0, column=0, sticky=tk.NSEW)

        PlotBackEnd.process_series()

        # PlotBackEnd.process_series._process_series.Axes3D.mouse_init()
        # PlotBackEnd._process_series.Axes3D.mouse_init()

        self.Figure.set_size_inches(self.FigSize)
        self.Figure.tight_layout()

        self.TkAgg.Draw()

    def Clear(self):
        self.TkAgg.destroy()
        self.Figure = Figure(figsize=self.FigSize, facecolor='#F0F0F0')
        self.TkAgg = TkFigurePlot(figure=self.Figure, master=self)
        self.TkAgg.grid(row=0, column=0, sticky=tk.NSEW)


class SmallNumbers:
    def __init__(self, how_much_numbers, place_of_script):
        """

        :param how_much_numbers: input integer or string numbers
                                 to get list of string numbers
        :param place_of_script: sub or super
        """
        try:
            self.how_much_numbers = int(eval(how_much_numbers))
        except TypeError:
            self.how_much_numbers = int(how_much_numbers)

        self.place_of_script = str(place_of_script).lower()

        if self.place_of_script == 'sub':
            self.work_list = ['₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉']
            self.generated_list = ['₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉']

        elif self.place_of_script == 'super':
            self.work_list = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
            self.generated_list = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']

        if self.how_much_numbers >= 10:
            start = 10
            end = 100
            for cmb in range(2, len(str(self.how_much_numbers)) + 1):
                self.ListOfCombinations(is_upper_then=start, is_under_then=end, combinations=cmb)
                start *= 10
                end *= 10

    def __call__(self, call_number, *args, **kwargs):
        return self.generated_list[call_number]

    def ListOfCombinations(self, is_upper_then, is_under_then, combinations):
        multi_work_list = eval(str('self.work_list,') * combinations)
        nbr = 0
        for subset in itertools.product(*multi_work_list):
            if is_upper_then <= nbr < is_under_then:
                self.generated_list.append(''.join(subset))
                if self.how_much_numbers == nbr:
                    break
            nbr += 1


class SystemSolverEntry(tk.Canvas):
    btnb_prm = {'padx': 18,
                'pady': 1,
                'bd': 1,
                'background': '#F0F0F0',
                'fg': 'black',
                'bg': '#F0F0F0',
                'font': ('DejaVu Sans', 7),
                'width': 2,
                'height': 1,
                'activeback': '#B0000B',
                'activebackground': '#80000B',
                'activeforeground': "white",
                'relief': 'flat'}

    def __init__(self, master, line, height, **kwargs):
        self.Master = master
        self.height = height
        super(SystemSolverEntry, self).__init__(master=self.Master, height=self.height, **kwargs)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.canvas = tk.Canvas(master=self, height=self.height)
        self.entry = []
        self.widget = 0
        self.u = int(line)

        self.button3 = HoverButton(master=self, text='3⨯3 {x,y,z}', **self.btnb_prm)
        self.button3.grid(row=1, column=2, sticky=tk.NSEW)

        self.button2 = HoverButton(master=self, text='2⨯2 {x,y}', **self.btnb_prm)
        self.button2.grid(row=1, column=1, sticky=tk.NSEW)

        self.button1 = HoverButton(master=self, text='1⨯1 {x}', **self.btnb_prm)
        self.button1.grid(row=1, column=0, sticky=tk.NSEW)

    def __call__(self, *args, **kwargs):
        # return self.entry[self.widget]
        return self.widget

    def Press(self, event):
        self.widget = event.widget
        # self.widget = int(eval(str(event.widget)[-1:].replace('y', '1'))) - 1

    def CreateGrid(self, line, **kwargs):
        self.u = int(line)
        self.canvas.destroy()
        self.canvas = tk.Canvas(master=self, height=self.height)
        self.canvas.grid(row=0, column=0, columnspan=3, sticky=tk.NSEW)
        if self.u == 1:
            self.canvas.rowconfigure(0, weight=1)
            self.canvas.columnconfigure(0, weight=1)
            self.canvas.columnconfigure(2, weight=1)
        elif self.u == 2:
            self.canvas.rowconfigure(0, weight=1)
            self.canvas.rowconfigure(1, weight=1)
            self.canvas.columnconfigure(0, weight=1)
            self.canvas.columnconfigure(2, weight=1)
        elif self.u == 3:
            self.canvas.rowconfigure(0, weight=1)
            self.canvas.rowconfigure(1, weight=1)
            self.canvas.rowconfigure(2, weight=1)
            self.canvas.columnconfigure(0, weight=1)
            self.canvas.columnconfigure(2, weight=1)

        self.entry = []
        k = 0
        for i in range(self.u):
            for j in range(0, 3, 2):
                self.entry.append(ManagedEntry(self.canvas, **kwargs))
                self.entry[k].grid(row=i, column=j, sticky=tk.NSEW)
                self.entry[k].bind('<Button-1>', self.Press, add="+")
                k += 1

        label = []
        for l0 in range(self.u):
            label.append(tk.Label(self.canvas, text='=', **kwargs))
            label[l0].grid(row=l0, column=1, sticky=tk.NSEW)
            label[l0].configure(justify=tk.CENTER)

        if self.u == 3:
            for m in range(1, 6, 2):
                self.entry[m].configure(width=2)

            self.button3.config(fg="white", bg='#80000B', relief='sunken')
            self.button3.DBG = '#80000B'
            self.button2.config(fg="black", bg='#F0F0F0', relief='flat')
            self.button2.DBG = '#F0F0F0'
            self.button1.config(fg="black", bg='#F0F0F0', relief='flat')
            self.button1.DBG = '#F0F0F0'

        elif self.u == 2:
            for m in range(1, 4, 2):
                self.entry[m].configure(width=2)

            self.button3.config(fg="black", bg='#F0F0F0', relief='flat')
            self.button3.DBG = '#F0F0F0'
            self.button2.config(fg="white", bg='#80000B', relief='sunken')
            self.button2.DBG = '#80000B'
            self.button1.config(fg="black", bg='#F0F0F0', relief='flat')
            self.button1.DBG = '#F0F0F0'

        elif self.u == 1:
            self.entry[1].configure(width=2)

            self.button3.config(fg="black", bg='#F0F0F0', relief='flat')
            self.button3.DBG = '#F0F0F0'
            self.button2.config(fg="black", bg='#F0F0F0', relief='flat')
            self.button2.DBG = '#F0F0F0'
            self.button1.config(fg="white", bg='#80000B', relief='sunken')
            self.button1.DBG = '#80000B'

        self.widget = self.entry[0]

    def Clear(self):
        if self.u == 3:
            for o in range(6):
                self.entry[o].Clear()
        elif self.u == 2:
            for o in range(4):
                self.entry[o].Clear()
        elif self.u == 1:
            for o in range(2):
                self.entry[o].Clear()


class FunctionEntry(tk.Canvas):
    def __init__(self, master, height, **kwargs):
        self.height = height
        super(FunctionEntry, self).__init__(master, height=self.height, **kwargs)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        self.entry = []
        self.widget = []
        self.label = []

    def __call__(self, *args, **kwargs):
        return self.widget

    def CreateGrid(self, **kwargs):
        self.entry = []
        for p in range(2):
            self.entry.append(ManagedEntry(self, width=16, **kwargs))
            self.entry[p].grid(row=p, column=1, sticky=tk.NSEW)
            self.entry[p].bind('<Button-1>', self.Press, add="+")

        self.widget = self.entry[0]

        self.label = []
        for q in range(2):
            self.label.append(tk.Label(self, **kwargs))
            self.label[q].grid(row=q, column=0, sticky=tk.NSEW)

        self.Clear()

    def Press(self, event):
        self.widget = event.widget

    def Clear(self):
        for s in range(2):
            self.entry[s].Clear()


class DrawLaTeX:
    def __init__(self):
        self.last_good_Before = []
        self.last_good_After = []
        self.last_good_AfterNum = []

    def LaTex(self, Math_Expression):
        TEX = '$' + latex(Math_Expression) + '$'
        # TEX = r"$%s$" % latex(Math_Expression)
        # TEX = f'${latex(Math_Expression)}$'
        return TEX

    def Before(self, character):
        try:
            pik = str(character).replace('integrate', 'Integral').replace('diff', 'Derivative')
            # expression = sympify(pik, rational=True, evaluate=False)
            expression = parse_expr(pik, evaluate=False)
            TEX = self.LaTex(expression)
            self.last_good_Before.append(TEX)
            return TEX
        except Exception:
            try:
                return self.last_good_Before[-1]
            except Exception:
                return character

    def After(self, character):
        try:
            simplify = sympify(character, rational=True, evaluate=True)
            TEX = self.LaTex(simplify)
            self.last_good_After.append(TEX)
            return TEX
        except Exception:
            try:
                return self.last_good_After[-1]
            except Exception:
                return character

    def AfterNum(self, character):
        try:
            simplify = sympify(character, rational=True, evaluate=True).evalf()
            TEX = self.LaTex(simplify)
            self.last_good_AfterNum.append(TEX)
            return TEX
        except Exception:
            try:
                return self.last_good_AfterNum[-1]
            except Exception:
                return character

    def Clear(self):
        self.last_good_Before = []
        self.last_good_After = []
        self.last_good_AfterNum = []
