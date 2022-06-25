import tkinter as tk

class Spread(tk.Frame):
    def __init__(self, master, paramlist):
        super(Spread, self).__init__(master)

        self.row = paramlist[0]
        self.column = paramlist[1]
        self.period = master.period.get()

        self.sheet = [ [ [tk.StringVar(self.master, '*') for _ in range(self.column) ] for _ in range(self.row) ] for _ in range(self.period + 1) ]
        for i in range(self.period + 1):
            for j in range(self.row):
                for k in range(self.column):
                    self.sheet[i][j][k].trace_add('write', self.push_stack)

    def push_stack(self, var, index, mode):
        for i in range(self.row):
            sheetrow=[]
            for j in range(self.column):
                sheetrow.append( self.sheet[self.master.generation.get()][i][j].get() )
            print(sheetrow)

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
