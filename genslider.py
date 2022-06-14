import tkinter as tk

class GenSlider(tk.Frame):
    def __init__(self, master):
        super(GenSlider, self).__init__(master, relief=tk.RIDGE, bd=1)
        self.generation = tk.IntVar(0)
        
        self.G = tk.Label(self, text='Generation: ')
        self.G.grid(row=0, column=0, ipadx=4, ipady=5, sticky=tk.E)
        self.L = tk.Label(self, textvariable=self.generation, width=3)
        self.L.grid(row=0, column=1, ipadx=4, ipady=5, sticky=tk.W)
        self.S = tk.Scale(self, variable=self.generation, orient=tk.HORIZONTAL, from_=0, to=10, showvalue=0)
        self.S.grid(row=0, column=2)

