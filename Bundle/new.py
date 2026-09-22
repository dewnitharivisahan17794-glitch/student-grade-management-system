import tkinter as tk
from tkinter import ttk
from Bundle.Place_holder import PLH
import json
from pathlib import Path
from tkinter import messagebox

def new_student():
    sub = tk.Toplevel()
    sub.title('Add Student')
    sub.geometry(f'400x500')
    sub.iconbitmap(r"C:\Users\USER\OneDrive\Documents\GitHub\student grade management system\Bundle\icon.ico")

    name = tk.StringVar()
    student_id = tk.StringVar()
    maths = tk.StringVar()
    english = tk.StringVar()
    programming = tk.StringVar()

    lable2 = ttk.Label(sub, text="", font = "arial 8 italic")
    lable2.pack()
    frame2 = ttk.Frame(sub, width=400, height=500)
    frame2.pack()
    lable1 = ttk.Label(frame2, text="New Student", font="arial 20 bold")
    lable1.pack()
    PLH(frame2, "Name (M.Jhon Smith)", name )
    PLH(frame2, "Student_ID (A1234)", student_id )
    PLH(frame2, "Mathmatics", maths )
    PLH(frame2, "English", english )
    PLH(frame2, "Programming", programming )
    
    lable3 = ttk.Label(frame2, text="Use 0 if the student did not participate.")
    lable3.pack()

    lable4 = ttk.Label(frame2, text="")
    lable4.pack()

    lable5 = ttk.Label(frame2, text="")
    lable5.pack()

    def massage():
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
#
        folder = Path("stdata")
        folder.mkdir(exist_ok= True)
#
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

        file_Path = folder/ f"{id}.json"

        student_Data = {"Name" : Name, "ID" : id, "Maths" : Mathmatics, "Coding" : Programming, "English" : English, "Average" : avg , "Grade" : Grade}

        with open (file_Path, "w") as file:
            json.dump(student_Data, file)

        result = messagebox.askokcancel("Are you sure?", "Sure?")

        if result :
            sub.destroy()

    button1 = ttk.Button(frame2, text="confirm", command=massage )
    button1.pack(side="left", padx=20, pady=20)

    def clear():
        name.set("")
        student_id.set("")
        maths.set("")
        english.set("")
        programming.set("")
        lable4.config(text="")
        lable5.config(text="")

    button2 = ttk.Button(frame2, text="Clear", command=clear)
    button2.pack(side='right', padx=20, pady=20)