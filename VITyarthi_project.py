import json, os

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")

def load():
    if os.path.exists(file_path):
        f = open(file_path, "r")
        d = json.load(f)
        f.close()
        return d
    else:
        return {}

def save(d):
    f = open(file_path, "w")
    json.dump(d, f, indent=4)
    f.close()

def show_menu():
    print("\n-------- MENU --------")
    print("1) Add new student")
    print("2) Search by roll no")
    print("3) Edit student info")
    print("4) Add marks")
    print("5) Create new column")
    print("6) Show all records")
    print("7) Remove student")
    print("8) Exit")
    print("----------------------")

def add_student(records):
    rn = input("\nRoll no: ").strip()
    if rn in records:
        print("This roll number is already there!")
        return

    nm = input("Student name: ").strip()
    info = {"Name": nm}

    ch = input("Want to add marks? (y/n): ").strip().lower()
    if ch == "y":
        while True:
            sub = input("  Enter subject (type done to finish): ").strip()
            if sub.lower() == "done":
                break
            m = input("  Marks in " + sub + ": ").strip()
            info[sub] = m

    ch2 = input("Any extra details to add? (y/n): ").strip().lower()
    if ch2 == "y":
        while True:
            fname = input("  Field name (done to stop): ").strip()
            if fname.lower() == "done":
                break
            fval = input("  Enter " + fname + ": ").strip()
            info[fname] = fval

    records[rn] = info
    save(records)
    print("Student added with roll no " + rn)

def search(records):
    rn = input("\nEnter roll no to search: ").strip()
    if rn not in records:
        print("No student found with roll no " + rn)
        return

    stu = records[rn]
    print("\n--- Details for Roll No " + rn + " ---")
    for k in stu:
        print("  " + k + " : " + str(stu[k]))
    print("---" + "-"*25)

def edit(records):
    rn = input("\nRoll no to edit: ").strip()
    if rn not in records:
        print("Roll no not found.")
        return

    stu = records[rn]
    # showing current info
    print("\nCurrent info:")
    keys = list(stu.keys())
    i = 1
    for k in keys:
        print("  " + str(i) + ". " + k + " -> " + str(stu[k]))
        i += 1

    print()
    print("What do you want to do?")
    print("  a) Edit a field")
    print("  b) Remove a field")
    print("  c) Cancel")
    opt = input("Choose: ").strip().lower()

    if opt == "a":
        fn = input("Which field to edit? ").strip()
        # case insensitive match
        matched = ""
        for k in stu:
            if k.lower() == fn.lower():
                matched = k
                break
        if matched == "":
            print("Field '" + fn + "' doesnt exist for this student")
        else:
            nv = input("New value for " + matched + " (was: " + str(stu[matched]) + "): ").strip()
            stu[matched] = nv
            save(records)
            print("Updated!")

    elif opt == "b":
        fn = input("Field to remove: ").strip()
        matched = ""
        for k in list(stu.keys()):
            if k.lower() == fn.lower():
                matched = k
                break
        if matched == "":
            print("Couldnt find that field.")
        else:
            del stu[matched]
            save(records)
            print("Removed " + matched)

def add_marks(records):
    rn = input("\nRoll number: ").strip()
    if rn not in records:
        print("Student not found!")
        return

    print("Adding marks for " + records[rn].get("Name", rn))
    count = 0
    while True:
        sub = input("  Subject (done to finish): ").strip()
        if sub.lower() == "done":
            break
        mrk = input("  Marks: ").strip()
        records[rn][sub] = mrk
        count += 1

    save(records)
    if count > 0:
        print(str(count) + " subject(s) updated.")
    else:
        print("No marks added.")

def new_column(records):
    if len(records) == 0:
        print("\nDatabase is empty, add some students first.")
        return

    col = input("\nNew column name (like Address, Hobbies etc): ").strip()
    if col == "":
        print("Name cant be empty")
        return

    defval = input("Default value for everyone (or just press enter): ").strip()

    print("  1 - Add to all students")
    print("  2 - Add to one student only")
    pick = input("Choose: ").strip()

    if pick == "1":
        c = 0
        for rn in records:
            if col not in records[rn]:
                records[rn][col] = defval
                c = c + 1
        save(records)
        print("Added '" + col + "' to " + str(c) + " students")

    elif pick == "2":
        rn = input("Roll number: ").strip()
        if rn in records:
            v = input("Value for " + col + ": ").strip()
            records[rn][col] = v
            save(records)
            print("Done!")
        else:
            print("Roll no not found")
    else:
        print("Invalid option")

def show_all(records):
    if len(records) == 0:
        print("\nNo records yet.")
        return

    # collect all field names across all students
    all_cols = []
    for rn in records:
        for k in records[rn]:
            if k not in all_cols:
                all_cols.append(k)

    # print header
    print()
    header = "Roll".ljust(10)
    for c in all_cols:
        header = header + c.ljust(15)
    print(header)
    print("-" * len(header))

    # print rows
    for rn in records:
        row = rn.ljust(10)
        for c in all_cols:
            if c in records[rn]:
                row = row + str(records[rn][c]).ljust(15)
            else:
                row = row + "-".ljust(15)
        print(row)
    print()

def remove_student(records):
    rn = input("\nRoll no to remove: ").strip()
    if rn not in records:
        print("Not found.")
        return
    name = records[rn].get("Name", "this student")
    yn = input("Sure you want to delete " + name + "? (y/n): ").strip().lower()
    if yn == "y":
        del records[rn]
        save(records)
        print("Deleted.")
    else:
        print("Cancelled.")


# main program starts here
print("=" * 40)
print("   STUDENT MANAGEMENT SYSTEM")
print("   Made by Viccky")
print("=" * 40)

data = load()

while True:
    show_menu()
    ch = input("Enter choice: ").strip()

    if ch == "1":
        add_student(data)
    elif ch == "2":
        search(data)
    elif ch == "3":
        edit(data)
    elif ch == "4":
        add_marks(data)
    elif ch == "5":
        new_column(data)
    elif ch == "6":
        show_all(data)
    elif ch == "7":
        remove_student(data)
    elif ch == "8":
        print("\nExiting... bye!")
        break
    else:
        print("Wrong choice, try again")
