#!/usr/bin/env python3

import tkinter as tk
from menubar import *
from cellboard import *
from genslider import *

class App(tk.Tk):
    def __init__(self, master = None):
        super(App, self).__init__(master)
        self.period = 3
        self.generation = 0
        menubar = MenuBar(self)
        board = CellBoard(self)
        slider = GenSlider(self)
        board.new([10,10])

        self.title('TkLife')
        self.config(menu = menubar)
        slider.pack(side=tk.BOTTOM, fill=tk.X)
        board.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
        
    def generationSet(self, genchoice):
        self.generation = genchoice
        print("Chosen generation is", self.generation)
        # board.generationSet(self.generation)

    def periodSet(self, periodchoice):
        self.period = periodchoice
        print("Chosen period is", self.period)
        # slider.periodSet(self.period)

if __name__ == "__main__":
    app = App()
    app.mainloop()
