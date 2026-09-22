import tkinter as tk
from tkinter import ttk

def PLH(parent, text, var):
    style=ttk.Style()
    style.configure("Placeholder.TEntry", forground="Gray")
    style.configure("Nomal.TEntry", forground="Black")

    style.map(
        "Placeholder.TEntry",
        foreground=[("!disabled", "gray")])

    style.map(
        "Normal.TEntry",
        foreground=[("!disabled", "black")])
    
    
    entry=ttk.Entry(parent, textvariable=var, style="Placeholder.TEntry", width=150)
    entry.pack(padx=10, pady=5)
    entry.insert(0,text)

    def forcus_in(event):
        if entry.get()==text:
            entry.delete(0,tk.END)
            entry.configure(style="Nomal.TEntry")

    def forcus_out(event):
        if entry.get()=="":
            entry.insert(0,text)
            entry.configure(style="Placeholder.TEntry")
            
    entry.bind("<FocusIn>", forcus_in)
    entry.bind("<FocusOut>", forcus_out)
