import tkinter as tk

class Spread(tk.Frame):
    def __init__(self, master, r=10, c=10, p=1):
        super(Spread, self).__init__(master)
        self.row = r
        self.column = c
        self.period = p
        self.sheet = [ [ [tk.StringVar(master, '*') for _ in range(self.column) ] for _ in range(self.row) ] for _ in range(self.period + 1) ]

    def get(self, p):
        return self.sheet[p]

    def set(self, sheet, p):
        if (self.row == len(sheet)) and (self.column == len(sheet[0])):
            self.sheet[p] = sheet
        else:
            raise('Setting sheet: size mismatch!')
            
    def resize(r, c, p):
        sheet = [ [ ['*'] * c for _ in range(r) ] for _ in range(p + 1) ]
        for ip in range(min(p + 1, self.period + 1)):
            for ir in range(min(r, self.row)):
                for ic in range(min(c, self.column)):
                    sheet[ip][ir][ic] = self.sheet[ip][ir][ic]
        self.row = r
        self.column = c
        self.period = p
        self.sheet = sheet
