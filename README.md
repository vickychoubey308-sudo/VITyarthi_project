# Student Management System

A terminal based student record manager made in pure Python. Search any student by roll number, add/edit marks, and create new fields like Address, Hobbies etc.

## Features

- Add new student with roll number, name, marks and extra details
- Search student by roll number to see all info
- Edit or remove any field of a student
- Add subject wise marks anytime
- Create new columns (Address, Hobbies, Phone etc) for one or all students
- View all students in a table
- Delete a student
- Data saved in data.json automatically

## Requirements

- Python 3.x (no external libraries)

## How to Run

### Option 1 - Double click
Just double click **RUN_PROGRAM.bat** and the program will open in terminal.

### Option 2 - Terminal
```
cd C:\Users\Lalit\Documents\StudentManager
python student_manager.py
```

## Files

```
StudentManager/
├── student_manager.py    # main code
├── RUN_PROGRAM.bat       # double click to run
├── README.md             # this file
├── sample_output.txt     # example of how it looks
└── data.json             # created automatically when you add first student
```

## Note
Delete data.json to reset all records.
