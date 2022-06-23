#!/usr/bin/env python3

import tkinter as tk
from menubar import *
from cellboard import *
from genslider import *

class App(tk.Tk):
    def __init__(self, master = None):
        super(App,self).__init__(master)
        self.period = tk.IntVar(master,3)
        self.period.trace_add('write', self.update_period)
        self.generation = tk.IntVar(master,0)
        self.generation.trace_add('write', self.update_generation)

        menubar = MenuBar(self)
        board = CellBoard(self)
        slider = GenSlider(self)
        board.new([10,10])

        self.title('TkLife')
        self.config(menu = menubar)
        slider.pack(side=tk.BOTTOM, fill=tk.X)
        board.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
        
    def update_period(self, var, index, mode):
        print("Chosen period is", self.period.get())
        # slider.periodSet(self.period)

    def update_generation(self, var, index, mode):
        print("Chosen generation is", self.generation.get())
        # board.generationSet(self.generation)

if __name__ == "__main__":
    app = App()
    app.mainloop()
