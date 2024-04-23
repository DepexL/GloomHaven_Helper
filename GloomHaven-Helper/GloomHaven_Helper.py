import tkinter as tk
from tkinter import *
from tkinter import ttk

# yey github works =)

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self, text="Welcome to Gloomhaven", font=("Helvetica", 24))
        self.title_label.pack(pady=20) 

        self.exit_button = tk.Button(self, text="Exit", command=self.master.destroy)
        self.exit_button.pack()

myapp = App()

myapp.master.title("My Do-Nothing Application")
myapp.master.maxsize(1000, 400)

myapp.mainloop()
