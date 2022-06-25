#!/usr/bin/env python3

import tkinter as tk
from menubar import *
from board import *
from genslider import *
from spreadsheet import *

class App(tk.Tk):
    def __init__(self, master = None):
        super(App,self).__init__(master)
        self.period = tk.IntVar(master,3)
        self.period.trace_add('write', self.update_period)
        self.generation = tk.IntVar(master,0)
        self.generation.trace_add('write', self.update_generation)

        menubar = MenuBar(self)
        self.board = Board(self,[10,10])
        self.slider = GenSlider(self)
        self.spread = Spread(self,[10,10])

        self.title('TkLife')
        self.config(menu = menubar)
        self.slider.pack(side=tk.BOTTOM, fill=tk.X)
        self.board.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)

    def update_period(self, var, index, mode):
        print("Chosen period is", self.period.get())
        self.slider.periodSet()

    def update_generation(self, var, index, mode):
        print("Chosen generation is", self.generation.get())
        self.board.refresh()

if __name__ == "__main__":
    app = App()
    app.mainloop()
