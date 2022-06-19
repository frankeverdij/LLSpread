import tkinter as tk

class MenuBar(tk.Menu):
    def __init__(self, master = None):
        super(MenuBar, self).__init__(master)
        self.option_add('*tearOff', False)

        filemenu = FileMenu(self)
        self.add_cascade(label="File", menu = filemenu)
        
        editmenu = EditMenu(self)
        self.add_cascade(label="Edit", menu = editmenu)
        
        helpmenu = HelpMenu(self)
        self.add_cascade(label="Help", menu = helpmenu)
        
    def donothing(self):
        filewin = tk.Toplevel(self.master)
        button = tk.Button(filewin, text="Do nothing button")
        button.pack()
        
    def setDimensions(self):
        dimwin = tk.Toplevel(self.master)
        dimwin.title('Dimensions')
        parambox = tk.Frame(dimwin)
        parambox.pack()

        labelcolumn = tk.Label(parambox, text="Column:")
        labelrow = tk.Label(parambox, text="Row:")
        labelperiod = tk.Label(parambox, text="Period:")
        spincolumn = tk.Spinbox(parambox, from_=0, to=10)
        spinrow = tk.Spinbox(parambox, from_=0, to=10)
        spinperiod = tk.Spinbox(parambox, textvariable=self.master.period, from_=0, to=10)

        button = tk.Button(parambox, text='Ok', command = dimwin.destroy)

        labelcolumn.grid(row=0, column=0)
        labelrow.grid(row=1, column=0)
        labelperiod.grid(row=2, column=0)
        spincolumn.grid(row=0, column=1)
        spinrow.grid(row=1, column=1)
        spinperiod.grid(row=2, column=1)

        button.grid(row=3, column=0, columnspan=2)

    def quit(self):
        self.master.quit()

class FileMenu(tk.Menu):
    def __init__(self, master):
        super(FileMenu, self).__init__(master)
        
        self.add_command(label="New", command = master.donothing)
        self.add_command(label="Open", command = master.donothing)
        self.add_command(label="Save", command = master.donothing)
        self.add_command(label="Save as...", command = master.donothing)
        self.add_command(label="Close", command = master.donothing)
        self.add_separator()
        self.add_command(label="Exit", command = master.quit)
 
class EditMenu(tk.Menu):
    def __init__(self, master):
        super(EditMenu, self).__init__(master)
        
        self.add_command(label="Undo", command = master.donothing)
        self.add_command(label="Redo", command = master.donothing)
        self.add_separator()
        self.add_command(label="Cut", command = master.donothing)
        self.add_command(label="Copy", command = master.donothing)
        self.add_command(label="Paste", command = master.donothing)
        self.add_command(label="Delete", command = master.donothing)
        self.add_command(label="Select All", command = master.donothing)
        self.add_separator()
        self.add_command(label="Set Dimensions", command = master.setDimensions)

class HelpMenu(tk.Menu):
    def __init__(self, master):
        super(HelpMenu, self).__init__(master, name='help')
        
        self.add_command(label="Help Index", command = master.donothing)
        self.add_command(label="About...", command = self.about)

    def about(self):
        win=tk.Toplevel(self.master)
        win.title('about')
        box = tk.Frame(win)
        box.pack()
        label = tk.Label(box, text='TkLifeSearch\n\nFrank Everdij (2021)', padx=10, pady=10)
        label.pack()
        button = tk.Button(box, text='Ok', command = win.destroy)
        button.pack(side='bottom')

