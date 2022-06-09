import tkinter as tk

"""
  0 and 1 for Life's normal states, 2 and 3 for cells which disregard rules,
  4 and 5 for unknown cells without and with labels.
"""

class CellBoard(tk.Frame):
    def __init__(self, master):
        super(CellBoard, self).__init__(master)
        self.field = [ [tk.StringVar() for _ in range(10) ] for _ in range(10) ]
        self.fieldcolor = [ 'white', 'black', 'white', 'black', 'black', 'black' ]
        self.state = [ [4]*10 for _ in range(10) ]
        self.statecolor = [ 'black', 'white', 'black', 'white', 'grey', 'lightgrey' ]
        self.i_saved = -1
        self.j_saved = -1

        self.focus_set()
        self.bind('<Key>', lambda e: self.on_keyhandler(e))

        for i,row in enumerate(self.field):
            for j,column in enumerate(row):
                self.field[i][j].set('   ')
                self.L = tk.Label(self, textvariable=self.field[i][j], bg=self.statecolor[self.state[i][j]], width=3, height=1)
                self.L.grid(row=i,column=j)
                self.L.bind('<Button-1>',lambda e,i=i,j=j: self.on_leftclick(i,j,e))
                self.L.bind('<Button-2>',lambda e,i=i,j=j: self.on_middleclick(i,j,e))
                self.L.bind('<Button-3>',lambda e,i=i,j=j: self.on_rightclick(i,j,e))

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
        event.widget.config(bg=self.statecolor[cellstate], fg=self.fieldcolor[cellstate])
        self.state[i][j] = cellstate

    def on_middleclick(self,i,j,event):
        current_state = self.state[i][j]
        if (current_state < 5):
            self.field[i][j].set('   ')
            self.i_saved = i
            self.j_saved = j
        else:
            if (self.i_saved < 0):
                self.i_saved = i
                self.j_saved = j
            else:
                self.i_saved = -1
        self.state[i][j] = 5
        event.widget.config(bg=self.statecolor[self.state[i][j]], fg=self.fieldcolor[self.state[i][j]])

    def on_rightclick(self,i,j,event):
        self.state[i][j] = 4
        self.field[i][j].set('   ')
        event.widget.config(bg=self.statecolor[self.state[i][j]], fg=self.fieldcolor[self.state[i][j]])

    def on_keyhandler(self,event):
        if (self.i_saved < 0):
            return

        i = self.i_saved
        j = self.j_saved
        if (self.state[i][j] == 5):
            var = self.field[i][j].get()
            if (event.keysym == 'Escape'):
                self.i_saved = -1
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

