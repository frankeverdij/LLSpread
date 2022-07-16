import tkinter as tk

class LabelBox(tk.Frame):
    def __init__(self, master):
        super(LabelBox, self).__init__(master, relief=tk.RIDGE, bd=1)
        
        self.G = tk.Label(self, text='Label Sheets:')
        self.S = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.L = tk.Listbox(self, yscrollcommand=self.S.set, width=10, bg='beige')
        self.S.config(command=self.L.yview)
        for i in range(100):
            self.L.insert(tk.END, str(i))
        self.G.pack(side=tk.TOP)
        self.L.pack(side=tk.LEFT, fill=tk.Y)
        self.S.pack(side=tk.RIGHT, fill=tk.Y)
        self.L.config(state = tk.DISABLED)
