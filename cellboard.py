import tkinter as tk

"""
  0 and 1 for Life's normal states, 2 and 3 for cells which disregard rules,
  4 and 5 for unknown cells without and with labels.
"""

class CellBoard(tk.Frame):
    def __init__(self, master):
        super(CellBoard, self).__init__(master)
        self.board = [ [tk.StringVar() for _ in range(10) ] for _ in range(10) ]
        self.state = [ [4]*10 for _ in range(10) ]
        self.statecolor = [ 'black', 'white', 'darkblue', 'yellow', 'grey', 'lightgrey' ]

        for i,row in enumerate(self.board):
            for j,column in enumerate(row):
                self.L = tk.Label(self,textvariable=self.board[i][j],bg=self.statecolor[self.state[i][j]], width=2, height=1)
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
    
        self.board[i][j].set('')
        event.widget.config(bg=self.statecolor[cellstate])
        self.state[i][j] = cellstate

    def on_middleclick(self,i,j,event):
        self.state[i][j] = 5
        self.board[i][j].set('-zz')
        event.widget.config(bg=self.statecolor[self.state[i][j]])
    
    def on_rightclick(self,i,j,event):
        self.state[i][j] = 4
        self.board[i][j].set('')  
        event.widget.config(bg=self.statecolor[self.state[i][j]])

