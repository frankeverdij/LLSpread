#!/usr/bin/env python3

import tkinter as tk
from menubar import *
from cellboard import *
from genslider import *

class App(tk.Tk):
    def __init__(self, master = None):
        super(App, self).__init__(master)
        
        menubar = MenuBar(self)
        board = CellBoard(self)
        slider = GenSlider(self)

        self.title('TkLife')
        self.config(menu = menubar)
        slider.pack(side=tk.BOTTOM, fill=tk.X)
        board.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
