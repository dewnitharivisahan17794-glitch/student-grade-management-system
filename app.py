import tkinter as tk
from tkinter import ttk
from Place_holder import PLH
from new import new_student

root = tk.Tk()
title = root.title("SMng")
icon = root.iconbitmap(r"C:\Users\USER\OneDrive\Documents\GitHub\student grade management system\icon.ico")
geometry = root.geometry(f'500x500')
search_Name = tk.StringVar()
search_ID = tk.StringVar()
lable = ttk.Label(root, text = "STUDENT MANAGER", foreground="Red", font="arial 30 bold ")
lable.pack()

frame1 = ttk.Frame(root, width=400, height=150, relief='groove') 
frame1.pack(pady=20)
frame1.pack_propagate(False)

PLH(frame1, "Student_ID", search_ID)
PLH(frame1, 'Student Name', search_Name)

button1 = ttk.Button(frame1, text='All Students')
button1.pack(side='left', pady=10, padx=10)

button2 = ttk.Button(frame1, text='Add New Student', command=new_student )
button2.pack(side='right', pady=10, padx=10)

button3 = ttk.Button(frame1, text='Search' )
button3.pack(side='bottom', pady=20, padx=10)

root.mainloop()