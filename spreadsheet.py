import tkinter as tk

class Spread(tk.Frame):
    def __init__(self, master):
        super(Spread, self).__init__(master)

    def create(self):
        row = self.master.row.get()
        column = self.master.column.get()
        if (row == 0) or (column == 0):
            raise "Board.new called with zero dimension(s)"
        self.period = self.master.period.get()

        self.sheet = [ [ [tk.StringVar(self.master, '*') for _ in range(column) ] for _ in range(row) ] for _ in range(self.period + 1) ]
        for i in range(self.period + 1):
            for j in range(row):
                for k in range(column):
                    self.sheet[i][j][k].trace_add('write', self.push_stack)

    def push_stack(self, var, index, mode):
        for i in range(len(self.sheet[0])):
            sheetrow=[]
            for j in range(len(self.sheet[0][0])):
                sheetrow.append( self.sheet[self.master.generation.get()][i][j].get() )
            print(sheetrow)

    def get(self, p):
        return self.sheet[p]

    def set(self, sheet, p):
        if (len(self.sheet[0]) == len(sheet[0])) and (len(self.sheet[0][0]) == len(sheet[0][0])):
            self.sheet[p] = sheet
        else:
            raise('Setting sheet: size mismatch!')
            
    def resize(self):
        newcolumn = self.master.column.get()
        difcolumn = newcolumn - len(self.sheet[0][0])
        if (difcolumn > 0):
            for i in range(self.period + 1):
                for j in range(len(self.sheet[0])):
                    for k in range(newcolumn - difcolumn, newcolumn):
                        self.sheet[i][j].append(tk.StringVar(self.master,'*'))
                        self.sheet[i][j][k].trace_add('write', self.push_stack)

