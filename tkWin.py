#!/usr/bin/env python3

import tkinter as tk
from menubar import *
from board import *
from footer import *
from spreadsheet import *

class App(tk.Tk):
    def __init__(self, master = None):
        super(App,self).__init__(master)
        self.row = tk.IntVar(master,10)
        self.column = tk.IntVar(master,10)
        self.period = tk.IntVar(master,1)
        self.generation = tk.IntVar(master,0)
        self.generation.trace_add('write', self.update_generation)
        self.wintitle = tk.StringVar(self,'Untitled')
        self.wintitle.trace_add('write', self.update_title)

        menubar = MenuBar(self)
        self.board = Board(self)
        self.footer = Footer(self)
        self.spread = Spread(self)

        self.spread.create()
        self.board.create()
        self.title('LLSpread')
        self.config(menu = menubar)
        self.footer.pack(side=tk.BOTTOM, fill=tk.X)
        self.board.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)

    def update_dimensions(self):
        print("Chosen dimensions are", self.column.get(), self.row.get())
        print("Chosen period is", self.period.get())
        self.footer.periodSet()
        self.spread.resize()
        self.board.resize()

    def update_title(self, var, index, mode):
        self.title('LLSpread - ' + self.wintitle.get())

    def update_generation(self, var, index, mode):
        print("Chosen generation is", self.generation.get())
        self.board.refresh()

    def load_file(self, filename):
        print("Loading", filename)
        self.spread.load(filename)
        self.footer.periodSet()
        self.board.resize()

if __name__ == "__main__":
    app = App()
    app.mainloop()
