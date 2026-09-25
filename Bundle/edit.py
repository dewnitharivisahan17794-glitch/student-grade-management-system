import tkinter as tk
from tkinter import ttk
import json
import os
from tkinter import messagebox , simpledialog
from pathlib import Path

def Edit(id):
    sub = tk.Toplevel()
    sub.title('Edit')
    sub.geometry(f'400x500')
    #sub.iconbitmap(r"C:\Users\USER\OneDrive\Documents\GitHub\student grade management system\Bundle\icon.ico")

    name = tk.StringVar()
    student_id = tk.StringVar()
    maths = tk.StringVar()
    english = tk.StringVar()
    programming = tk.StringVar()

    
    path = Path("stdata/{id}.json")
    with open(path, 'r') as file:
        data = json.load(file)
        p = data.get("Name", "")
        q= data.get("ID", "")
        r = data.get("Maths", "")
        s = data.get("English", "")
        t = data.get("Coding", "")
    lable2 = ttk.Label(sub, text="", font = "arial 8 italic")
    lable2.pack()
    frame2 = ttk.Frame(sub, width=400, height=500)
    frame2.pack()
    lable1 = ttk.Label(frame2, text="Student's Data", font="arial 20 bold")
    lable1.pack()

    entry1=ttk.Entry(frame2, textvariable=name, width=150)
    entry1.pack(padx=10, pady=5)
    entry1.insert(0,p)
    entry2=ttk.Entry(frame2, textvariable=student_id, width=150)
    entry2.pack(padx=10, pady=5)
    entry2.insert(0,q)
    entry2.configure(state="readonly")
    entry3=ttk.Entry(frame2, textvariable=maths, width=150)
    entry3.pack(padx=10, pady=5)
    entry3.insert(0,r)
    entry4=ttk.Entry(frame2, textvariable=english, width=150)
    entry4.pack(padx=10, pady=5)
    entry4.insert(0,s)
    entry5=ttk.Entry(frame2, textvariable=programming, width=150)
    entry5.pack(padx=10, pady=5)
    entry5.insert(0,t)
    
    lable3 = ttk.Label(frame2, text="Use 0 if the student did not participate.")
    lable3.pack()

    lable4 = ttk.Label(frame2, text="")
    lable4.pack()

    lable5 = ttk.Label(frame2, text="")
    lable5.pack()

    def confirm():
        name_value = name.get().strip()
        id_value = student_id.get().strip()

        if name_value in ("", "Name") or id_value in ("", "Student_ID"):
            lable2.config(
                text="Please fill in all required fields.",
                foreground="red"
            )
            

        else:
            lable2.config(text="")

        try:
            Mathmatics =int(maths.get())
            English = int(english.get())
            Programming = int(programming.get())
            subject = [Mathmatics, English, Programming]

            for i in subject:
                if i<0 or i>100:
                    lable5.config(text="Please Enter Marks Between 0 and 100")
                    return
                
            lable5.config(text="")   
            lable4.config(text="")  

        except ValueError as E:
            lable4.config(text= "Please Enter Integer Number")
            return

        id = student_id.get()
        Name = name.get()
        total = Mathmatics + Programming + English
        avg = round(total/3 , 2) 


        if avg >= 75 and avg <= 100 :
            Grade = "A"
        elif avg >=65 and avg <75 :
            Grade = "B"
        elif avg >= 55 and avg < 65 :
            Grade = "C"
        elif avg >= 45 and avg < 35 :
            Grade = "S"
        else:
            Grade = "F"


        student_Data = {"Name" : Name, "ID" : id, "Maths" : Mathmatics, "Coding" : Programming, "English" : English, "Average" : avg , "Grade" : Grade}

        with open (path, "w") as file:
            json.dump(student_Data, file)

        result = messagebox.askokcancel("Are you sure?", "Sure?")

        if result :
            sub.destroy()

    button1 = ttk.Button(frame2, text="confirm", command=confirm )
    button1.pack(side="left", padx=20, pady=20)

    def check_input(*args):
        has_input = any(
            var.get().strip()
            for var in (name, student_id, maths, english, programming)
    )
        button1.config(state="normal" if has_input else "disabled")

    for var in (name, student_id, maths, english, programming):
        var.trace_add("write", check_input) #when variables are changed, this will be called.

    def clear():
        name.set("")
        maths.set("")
        english.set("")
        programming.set("")
        lable4.config(text="")
        lable5.config(text="")
        button1.state(["disabled"])

    button2 = ttk.Button(frame2, text="Clear", command=clear)
    button2.pack(side="left", padx=20, pady=20)

    def delete():
        passkey = simpledialog.askstring("Passkey", "Enter Passkey:", parent=sub, show="*")
        if passkey is None:
            return
        if passkey != "2095":
            messagebox.showerror("Error!", "Incorrect passkey", parent=sub)
            return
        else:
            result2 = messagebox.askokcancel("Are you sure?", "Sure?", parent=sub)
            if result2:

                file_Path = fr"C:\Users\USER\OneDrive\Documents\GitHub\student grade management system\stdata\{id}.json"
                os.remove(file_Path)
                sub.destroy()


    button3 = ttk.Button(frame2, text="Delete", command=delete)
    button3.pack(side="left", padx=20, pady=20)