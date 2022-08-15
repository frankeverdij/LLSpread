import tkinter as tk

class LabelBox(tk.Frame):
    def __init__(self, master):
        super(LabelBox, self).__init__(master, relief=tk.RIDGE, bd=1)
        
        self.G = tk.Button(self, text='Get Labels', command = self.get_labels)
        self.S = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.L = tk.Listbox(self, yscrollcommand=self.S.set, width=10, bg='beige')
        self.S.config(command=self.L.yview)
        self.G.pack(side=tk.TOP)
        self.L.pack(side=tk.LEFT, fill=tk.Y)
        self.S.pack(side=tk.RIGHT, fill=tk.Y)

    def get_labels(self):
        labels = self.master.get_labels()
        self.L.delete(0, tk.END)
        if (labels):
            for index, labelentry in enumerate(labels):
                color = 'cyan' if (labelentry[1] == 1) else 'beige'
                if type(labelentry[2]) is not list:
                    color = 'red'
                labelline = labelentry[0] + ' ' + str(labelentry[2])
                self.L.insert(tk.END, labelline)
                self.L.itemconfigure(tk.END, background=color)
