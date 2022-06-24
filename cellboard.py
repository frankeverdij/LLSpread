import tkinter as tk

"""
  0 and 1 for Life's normal states, 2 and 3 for cells which disregard rules,
  4 and 5 for unknown cells without and with labels.
"""
fieldcolor = [ 'white', 'black', 'white', 'black', 'black', 'black' ]
fieldvalue = {"0": 0 , "1": 1, "0'": 2, "1'": 3, "*": 4, " ": 5}
statecolor = [ 'black', 'white', 'black', 'white', 'grey', 'lightgrey' ]

class CellBoard(tk.Frame):
    def __init__(self, master, paramlist = None):
        super(CellBoard, self).__init__(master)
        if (paramlist):
            self.new(paramlist)

    def new(self, paramlist):
        self.row = paramlist[0]
        self.column = paramlist[1]
        self.field = [ [tk.StringVar() for _ in range(self.column) ] for _ in range(self.row) ]
        self.state = [ [4] * self.column for _ in range(self.row) ]
        self.i_saved = -1
        self.j_saved = -1

        self.focus_set()
        self.bind('<Key>', lambda e: self.on_keyhandler(e))

        for i,row in enumerate(self.field):
            for j,column in enumerate(row):
                self.field[i][j].set('   ')
                self.L = tk.Label(self, textvariable=self.field[i][j], relief=tk.RAISED, bg=statecolor[self.state[i][j]], width=3, height=1)
                self.L.grid(row=i,column=j, ipadx=4, ipady=5)
                self.L.bind('<Button-1>',lambda e,i=i,j=j: self.on_leftclick(i,j,e))
                self.L.bind('<Button-2>',lambda e,i=i,j=j: self.on_middleclick(i,j,e))
                self.L.bind('<Button-3>',lambda e,i=i,j=j: self.on_rightclick(i,j,e))

    def idx(self,label):
        return fieldvalue.get(label, 5)

    def load_sheet(self, sheet):
        pass

    def save_sheet(self, sheet):
        pass

    def resize_board(self, paramlist):
        difrow = paramlist[0] - self.row
        difcolumn = paramlist[1] - self.column
        if (difrow == 0) and (difcolumn == 0):
            return
        for label in self.grid_slaves():
            if int(label.grid_info()["row"]) > paramlist[0]:
                label.grid_forget()
            if int(label.grid_info()["column"]) > paramlist[1]:
                label.grid_forget()

    def on_leftclick(self,i,j,event):
        cellstate = self.state[i][j]
        if (cellstate < 5):
            if cellstate == 4:
                cellstate = 0
            else: 
                cellstate += 1
                cellstate = cellstate % 4
        else:
            return
        if (cellstate == 2 or cellstate == 3):
            self.field[i][j].set(' # ')
        else:
            self.field[i][j].set('   ')
        event.widget.config(bg=statecolor[cellstate], fg=fieldcolor[cellstate])
        self.state[i][j] = cellstate

    def widget_raise(self):
        for label in self.grid_slaves():
            label.config(relief=tk.RAISED)

    def on_middleclick(self,i,j,event):
        self.widget_raise()
        event.widget.config(bg=statecolor[5], fg=fieldcolor[5])
        if (self.state[i][j] < 5):
            self.field[i][j].set('   ')
            self.i_saved = i
            self.j_saved = j
            event.widget.config(relief=tk.RIDGE)
        else:
            if (self.i_saved < 0):
                self.i_saved = i
                self.j_saved = j
                event.widget.config(relief=tk.RIDGE)
            else:
                self.i_saved = -1
        self.state[i][j] = 5

    def on_rightclick(self,i,j,event):
        if (self.state[i][j] == 4):
            self.i_saved = -1
            self.on_middleclick(i,j,event)
            return

        self.state[i][j] = 4
        self.field[i][j].set('   ')
        event.widget.config(bg=statecolor[self.state[i][j]], fg=fieldcolor[self.state[i][j]], relief=tk.RAISED)

    def on_keyhandler(self,event):
        if (self.i_saved < 0):
            return

        i = self.i_saved
        j = self.j_saved
        if (self.state[i][j] == 5):
            var = self.field[i][j].get()
            if (event.keysym == 'Escape'):
                self.i_saved = -1
                self.widget_raise()
                return

            if (event.char == '-'):
                if (var[0] == '-'):
                    var = ' ' + var[1:]
                else:
                    if not var.isspace():
                        var = event.char + var[1:]
                    else:
                        return

            if event.char.isalpha():
                if (var[1] == ' '):
                    var = var[0] + event.char + ' '
                else:
                    if (var[2] == ' '):
                        var = var[0:2] + event.char
                    else:
                        var = var[0] + event.char + ' '
            self.field[i][j].set(var)

