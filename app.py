import tkinter as tk
from tkinter import ttk

root = tk.Tk()
title = root.title("SMng")
icon = root.iconbitmap(r"C:\Users\USER\OneDrive\Documents\GitHub\student grade management system\icon.ico")
geometry = root.geometry(f'700x700')
lable = ttk.Label(root, text = "STUDENT MANAGER", foreground="Red", font="arial 30 bold ")
lable.pack()
root.mainloop()