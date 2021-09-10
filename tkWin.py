#!/usr/bin/env python3

import tkinter as tk

class MenuBar(tk.Menu):
    def __init__(self, master = None):
        super(MenuBar, self).__init__(master)
        
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
        
    def quit(self):
        self.master.quit()

class FileMenu(tk.Menu):
    def __init__(self, master):
        super(FileMenu, self).__init__(master, tearoff = False)
        
        self.add_command(label="New", command = master.donothing)
        self.add_command(label="Open", command = master.donothing)
        self.add_command(label="Save", command = master.donothing)
        self.add_command(label="Save as...", command = master.donothing)
        self.add_command(label="Close", command = master.donothing)
        self.add_separator()
        self.add_command(label="Exit", command = master.quit)
 
class EditMenu(tk.Menu):
    def __init__(self, master):
        super(EditMenu, self).__init__(master, tearoff = False)
        
        self.add_command(label="Undo", command = master.donothing)
        self.add_command(label="Redo", command = master.donothing)
        self.add_separator()
        self.add_command(label="Cut", command = master.donothing)
        self.add_command(label="Copy", command = master.donothing)
        self.add_command(label="Paste", command = master.donothing)
        self.add_command(label="Delete", command = master.donothing)
        self.add_command(label="Select All", command = master.donothing)

class HelpMenu(tk.Menu):
    def __init__(self, master):
        super(HelpMenu, self).__init__(master, tearoff = False)
        
        self.add_command(label="Help Index", command = master.donothing)
        self.add_command(label="About...", command = master.donothing)

class App(tk.Tk):
    def __init__(self, master = None):
        super(App, self).__init__(master)
        
        menubar = MenuBar(self)
        self.config(menu = menubar)

if __name__ == "__main__":
    app = App()
    app.mainloop()
