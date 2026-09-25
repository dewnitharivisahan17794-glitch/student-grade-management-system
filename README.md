# Student Grade Management System

A simple **Student Grade Management System** built with **Python and Tkinter**.

This project is designed to practice building a desktop GUI application using Tkinter while working with student information, marks, calculations, and CRUD operations.

## 📌 Project Features

- Add new students
- View all students
- Search students by ID
- Update student information
- Delete students
- Calculate average marks automatically
- Calculate grades automatically
- Input validation
- Display student data using `ttk.Treeview`
- Clear input fields
- Show success and error messages using `messagebox`

## 🛠️ Technologies

- Python
- Tkinter
- ttk
- JSON *(Bonus)*

## 📋 Requirements

### Student Information

The application should collect:

- Student ID
- Name
- Age
- Mathematics marks
- English marks
- Programming marks

### Main Functions

The application should provide the following buttons:

- **Add Student**
- **View Students**
- **Search**
- **Update**
- **Delete**
- **Clear**

### Student Table

Use a `ttk.Treeview` to display:

| ID | Name  |  Maths | English | Programming | Average | Grade |
|---|---|---|---|---|---|---|---|

### 🎓 Grade System

| Average | Grade |
|---|---|
| 75 - 100 | A |
| 65 - 74 | B |
| 55 - 64 | C |
| 40 - 54 | S |
| Below 40 | F |

## ✅ Validation Requirements

- Student ID must be unique.
- Marks must be between `0` and `100`.
- Required fields should not be empty.
- Appropriate error messages should be displayed for invalid input.
- Confirmation should be requested before deleting a student.

## 🔄 Expected Behaviour

1. User enters student information.
2. User clicks **Add Student**.
3. The application validates the information.
4. The student's average and grade are calculated automatically.
5. The student is displayed in the `Treeview`.
6. Clicking a student row should load its information into the input fields.
7. The user can then update or delete the selected student.

## ⭐ Bonus Features

After completing the basic version, add:

- Save student data to a JSON file.
- Load saved data when the application starts.
- Automatically save data when the application closes.
- Search students by name.
- Add a scrollbar to the `Treeview`.

## 🎯 Learning Goals

This project is intended to practice:

- Tkinter GUI development
- `Entry`, `Button`, `Label`
- `ttk.Treeview`
- Functions
- Conditional statements
- Loops
- Lists and dictionaries
- Input validation
- CRUD operations
- `messagebox`
- File handling
- JSON

## 🚀 Future Improvements

Possible future improvements include:

- Student login system
- Separate dashboard
- Better UI design
- SQLite database
- Export student results
- Student report generation

## 📂 Project Status

**Status:** In Development 🚧

The project is being developed as part of Python GUI project practice using Tkinter.

## My Notes.

This project was given by chatGPT,
And also NOT  copy and paste work.
***This is my own work.***
icon from Here: https://icons8.com/icons/set/system
