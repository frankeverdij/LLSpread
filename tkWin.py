#!/usr/bin/env python3

import tkinter as tk
from menubar import *
from cellboard import *
from genslider import *

class App(tk.Tk):
    def __init__(self, master = None):
        super(App, self).__init__(master)
        
        menubar = MenuBar(self)
        self.title('TkLife')
        self.config(menu = menubar)
        board = CellBoard(self)
        board.grid(row=0, column=0, sticky=tk.NW)
        slider = GenSlider(self)
        slider.grid(row=1, column=0, sticky=tk.NW)
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
