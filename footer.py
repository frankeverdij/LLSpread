import tkinter as tk

class Footer(tk.Frame):
    def __init__(self, master):
        super(Footer, self).__init__(master, relief=tk.RIDGE, bd=1)
        
        self.G = tk.Label(self, text='Generation: ')
        self.G.grid(row=0, column=0, ipadx=4, ipady=5, sticky=tk.E)
        self.L = tk.Label(self, textvariable=master.generation, width=3)
        self.L.grid(row=0, column=1, ipadx=4, ipady=5, sticky=tk.W)
        self.S = tk.Scale(self, variable=master.generation, orient=tk.HORIZONTAL, from_=0, to=master.period.get(), showvalue=0)
        self.S.grid(row=0, column=2)
        self.P = tk.Label(self, textvariable=master.period, width=3)
        self.P.grid(row=0, column=3)

    def periodSet(self):
        try:
            self.S.config(to=self.master.period.get())
        except:
            print("Footer: Empty period")
