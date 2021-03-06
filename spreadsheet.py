import tkinter as tk
import re

class Spread(tk.Frame):
    def __init__(self, master):
        super(Spread, self).__init__(master)

    def create(self):
        row = self.master.row.get()
        column = self.master.column.get()
        if (row == 0) or (column == 0):
            raise "Board.new called with zero dimension(s)"
        period = self.master.period.get()

        self.sheet = [ [ [tk.StringVar(self, '*') for _ in range(column) ] for _ in range(row) ] for _ in range(period + 1) ]
        for i in range(period + 1):
            for j in range(row):
                for k in range(column):
                    self.sheet[i][j][k].trace_add('write', self.push_stack)
        print('Create True')
        self.master.unsaved.set(True)

    def remove(self):
        del self.sheet
        self.master.unsaved.set(False)

    def push_stack(self, var, index, mode):
        for i in range(len(self.sheet[0])):
            sheetrow=[]
            for j in range(len(self.sheet[0][0])):
                sheetrow.append( self.sheet[self.master.generation.get()][i][j].get() )
            print(sheetrow)

    def get(self, p, r, c):
        return self.sheet[p][r][c].get()

    def set(self, p, r, c, cell):
        self.sheet[p][r][c].set(cell)
        print('Set True')
        self.master.unsaved.set(True)

    def resize(self):
        sheet = [ [ [tk.StringVar(self.master, '*') for _ in range(self.master.column.get()) ] for _ in range(self.master.row.get()) ] for _ in range(self.master.period.get() + 1) ]
        for i in range(len(sheet)):
            for j in range(len(sheet[0])):
                for k in range(len(sheet[0][0])):
                    sheet[i][j][k].trace_add('write', self.push_stack)
                    try:
                        sheet[i][j][k] = self.sheet[i][j][k]
                    except:
                        pass
        self.sheet = sheet
        print('Resize True')
        self.master.unsaved.set(True)

    def save(self, filename):
        try:
            with open(filename, 'w') as outfile:
                for i in range(len(self.sheet)):
                    for j in range(len(self.sheet[0])):
                        line = ''
                        for k in range(len(self.sheet[0][0])):
                            line += self.sheet[i][j][k].get()
                            line += (self.master.separator.get() if (k< len(self.sheet[0][0])-1) else '')
                        outfile.write(line + '\n')
                    outfile.write('\n')
            print('Save False')
            self.master.unsaved.set(False)
        except:
            print('Spread.save unsuccesful')

    def load(self, filename):
        with open(filename, 'r') as infile:
            input_string = infile.read()

            # From LLS 'src/formatting.py'
            # Remove any comments
            input_string = re.sub('#.*', '', input_string)

            # Remove any trailing or leading whitespace and commas
            input_string = input_string.strip(" ,\t\n")

            # Break down string into list-of-lists-of-lists
            split_by_generation = re.split(
                r"[ ,\t]*\n(?:[ ,\t]*\n)+[ ,\t]*",  # Split on at least two newlines and any spaces, commas or tabs
                input_string
            )
            split_by_line = [
                re.split(
                    r"[ ,\t]*\n[ ,\t]*",  # Split on single newline and any amount of commas or spaces
                    generation
                )
            for generation in split_by_generation]
            grid = [[
                re.split(
                    r"[ ,\t]+",  # Split on any amount of commas or spaces
                    line
                )
            for line in generation] for generation in split_by_line]

            row = len(grid[0])
            column = len(grid[0][0])
            period = len(grid)
            print(period, row, column)

            assert (all(
                len(generation) == len(grid[0])
                for generation in grid)
                    and all(all(
                        len(line) == len(grid[0][0])
                        for line in generation) for generation in grid)), \
                "Search pattern is not cuboidal"

            self.sheet = [ [ [tk.StringVar(self, grid[i][j][k]) for k in range(column) ] for j in range(row) ] for i in range(period) ]
            for i in range(period):
                for j in range(row):
                    for k in range(column):
                        self.sheet[i][j][k].trace_add('write', self.push_stack)

            self.master.period.set(period - 1)
            self.master.row.set(row)
            self.master.column.set(column)
            print('Load False')
            self.master.unsaved.set(False)

    def get_labels(self):
        labeldata = []
        labellist = []
        for i in range(len(self.sheet)):
            for j in range(len(self.sheet[0])):
                for k in range(len(self.sheet[0][0])):
                    var = self.sheet[i][j][k].get()
                    if (var not in ["0","1","0'","1'","*"]):
                        varpos = 1 if var[0] == '-' else 0
                        labellist.append(var[varpos:])
                        labeldata.append(list([var[varpos:], varpos, i]))
        multitons = set(label for label in labellist if labellist.count(label) > 1)
        singletons = set(labellist).difference(multitons)
        labelsingle = list(filter(lambda l : l[0] in singletons, labeldata))
        labelsingle.sort()
        labelmulti = []
        for label in multitons:
            lc = list(filter(lambda l : l[0] == label, labeldata))
            sheets = []
            minus = 0
            for i, entry in enumerate(lc):
                sheets.append(entry[2])
                if (entry[1] == 1):
                    minus = 1
            labelmulti.append([label, minus, sheets])
        labelmulti.sort()
        labeldata = labelsingle + labelmulti
        return labeldata
