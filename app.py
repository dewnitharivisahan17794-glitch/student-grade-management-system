import tkinter as tk
from tkinter import ttk
from Bundle.Place_holder import PLH
from Bundle.new import new_student
from Bundle.edit import  Edit
from pathlib import Path
import json
import os

root = tk.Tk()
title = root.title("SMng")
icon = root.iconbitmap(r"C:\Users\USER\OneDrive\Documents\GitHub\student grade management system\Bundle\icon.ico")
geometry = root.geometry(f'700x700')
search_Name = tk.StringVar()
search_ID = tk.StringVar()
lable = ttk.Label(root, text = "STUDENT MANAGER", foreground="Red", font="arial 30 bold ")
lable.pack()

frame1 = ttk.Frame(root, width=400, height=170, relief='groove') 
frame1.pack(pady=20)
frame1.pack_propagate(False)

k = PLH(frame1, "Student_ID (A1234)", search_ID)
lable1 = ttk.Label(frame1, text="", font="Arial 8 italic", foreground='#800000')
lable1.pack()
p = PLH(frame1, 'Student Name (M.Jhon Smith)', search_Name)
lable2 = ttk.Label(frame1, text="", font="Arial 8 italic", foreground='#800000')
lable2.pack()
def view_all():
   
    frame3 = ttk.Frame(root)
    frame3.pack(after=frame1)
    table = ttk.Treeview(frame3, columns=('id', 'name', 'maths', 'english', 'programming', 'avg', 'grade'), show='headings')

    scroll_bar = ttk.Scrollbar(frame3, orient='vertical', command=table.yview)

    table.configure(yscrollcommand=scroll_bar.set)

    button4 = ttk.Button(frame3, text="Close", command=lambda: frame3.destroy())
    button4.pack(pady=10)

    table.pack(side='left', fill='both', expand=True)
    scroll_bar.pack(side='right', fill='y')

    

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


def search():
    lable1.configure(text="")
    lable2.configure(text="")

    id = search_ID.get()
    path =Path("stdata")
    exists = os.path.exists(path)
    if(exists):
        with open(path, "r") as file:
            data = json.load(file)
            name = data.get("Name", "")
        if name != search_Name.get():
            lable2.configure(text="*Student ID or Student Name doesn't match.")
        else:
            frame2 = ttk.Frame(root, width=400, height=200, relief='groove')
            frame2.pack(pady=20, after=frame1)
            frame2.pack_propagate(False)
            letterbox = ttk.Label(frame2, text="", font="Arial 9", background="White" )
            letterbox.pack(padx=20, pady=10, fill="both")
            maths = data.get("Maths", "") 
            english = data.get("English", "") 
            coding = data.get("Coding", "") 
            avg = data.get("Average", "") 
            grade = data.get("Grade", "")
            letterbox.configure(text=f"ID = {id}\nName = {name}\nMathmatics = {maths}\nEnglish = {english}\nProgramming = {coding}\nAverage = {avg}\nGrade = {grade}\n")
            edit = ttk.Button(frame2, text="Edit", command=lambda:Edit(id))
            edit.pack(side='left',padx = 10)
            def close():
                frame2.destroy()
                search_Name.set("")
                search_ID.set("")
                
            close = ttk.Button(frame2, text = "Close", command=close)
            close.pack(side= 'right', padx=10)
    else:
        lable1.configure(text="*Student ID doesn't Exists")




button1 = ttk.Button(frame1, text='All Students', command=view_all)
button1.pack(side='left', pady=10, padx=20)

button3 = ttk.Button(frame1, text='Search' , command=search)
button3.pack(side='left', pady=10, padx=20)

button2 = ttk.Button(frame1, text='Add New Student', command=new_student )
button2.pack(side='left', pady=10, padx=20)

root.mainloop()