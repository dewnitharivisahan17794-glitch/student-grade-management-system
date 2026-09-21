import tkinter as tk
from tkinter import ttk
from Bundle.Place_holder import PLH
from Bundle.new import new_student
from pathlib import Path
import json

root = tk.Tk()
title = root.title("SMng")
icon = root.iconbitmap(r"C:\Users\USER\OneDrive\Documents\GitHub\student grade management system\Bundle\icon.ico")
geometry = root.geometry(f'700x700')
search_Name = tk.StringVar()
search_ID = tk.StringVar()
lable = ttk.Label(root, text = "STUDENT MANAGER", foreground="Red", font="arial 30 bold ")
lable.pack()

frame1 = ttk.Frame(root, width=400, height=150, relief='groove') 
frame1.pack(pady=20)
frame1.pack_propagate(False)

PLH(frame1, "Student_ID", search_ID)
PLH(frame1, 'Student Name', search_Name)

def view_all():
    canves = tk.Canvas(root, width=650, height=400, background='White')
    canves.pack(after=frame1)
    frame3 = ttk.Frame(canves)
    frame3.pack()
    scroll_bar = ttk.Scrollbar(frame3, orient= 'vertical', command=canves.yview)
    scroll_bar.pack(side='right', fill='y')
    frame3.bind('<Configure>', lambda e: canves.configure(scrollregion=canves.bbox("all")))

    table = ttk.Treeview(frame3, columns=('id', 'name', 'maths', 'english', 'programming', 'avg', 'grade'), show='headings')
    table.pack()
    table.heading('id',text = "ID")
    table.heading('name',text = "Name")
    table.heading('maths',text = "Maths")
    table.heading('english',text = "English")
    table.heading('programming',text = "Coding")
    table.heading('avg',text = "Average")
    table.heading('grade', text="Grade")

    table.column('id', width=60,stretch = False)
    table.column('english', width=60,stretch = False)
    table.column('maths', width=60,stretch = False)
    table.column('programming', width=60,stretch = False)
    table.column('avg', width=60,stretch = False)
    table.column('grade', width=60,stretch = False)

    for file_path in Path("stdata").glob("*.json"):
        with open(file_path, "r") as file:
            data = json.load(file)

            table.insert("", 
                         'end', 
                         values=(
                             data.get("ID", ""),
                            data.get("Name", ""), 
                            data.get("Maths", ""), 
                            data.get("English", ""), 
                            data.get("Coding", ""), 
                            data.get("Average", ""), 
                            data.get("Grade", "")))
            

button1 = ttk.Button(frame1, text='All Students', command=view_all)
button1.pack(side='left', pady=10, padx=10)

button2 = ttk.Button(frame1, text='Add New Student', command=new_student )
button2.pack(side='right', pady=10, padx=10)

button3 = ttk.Button(frame1, text='Search' )
button3.pack(side='bottom', pady=20, padx=10)

root.mainloop()