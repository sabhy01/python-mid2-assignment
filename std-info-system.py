import csv

students = {}

# Grade calculation based on average
def calculate_grade(avg):
    if avg >= 90: return 'A'
    elif avg >= 80: return 'B'
    elif avg >= 70: return 'C'
    elif avg >= 60: return 'D'
    else: return 'F'

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = {}
    for subject in ["Math", "Science", "English"]:
        marks[subject] = int(input(f"Enter marks for {subject}: "))
    avg = sum(marks.values()) / len(marks)
    grade = calculate_grade(avg)
    gpa = avg / 20  # GPA scale out of 5
    students[roll] = {"Name": name, "Marks": marks, "Grade": grade, "GPA": round(gpa, 2)}
    print("Student added successfully.")

def update_student():
    roll = input("Enter Roll No to update: ")
    if roll in students:
        add_student()  # Reuse add_student for update
    else:
        print("Student not found.")

def delete_student():
    roll = input("Enter Roll No to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted.")
    else:
        print("Student not found.")

def view_all_students():
    for roll, data in students.items():
        print(f"\nRoll: {roll}\nName: {data['Name']}\nMarks: {data['Marks']}\nGrade: {data['Grade']}\nGPA: {data['GPA']}")

def find_topper():
    if not students:
        print("No data.")
        return
    topper = max(students.items(), key=lambda x: sum(x[1]['Marks'].values()))
    print(f"Topper: {topper[1]['Name']} with GPA {topper[1]['GPA']}")

def export_to_csv():
    with open("students.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Roll", "Name", "Math", "Science", "English", "Grade", "GPA"])
        for roll, data in students.items():
            writer.writerow([roll, data["Name"], data["Marks"]["Math"], data["Marks"]["Science"],
                             data["Marks"]["English"], data["Grade"], data["GPA"]])
    print("Exported to students.csv")

def import_from_csv():
    try:
        with open("students.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                roll = row["Roll"]
                students[roll] = {
                    "Name": row["Name"],
                    "Marks": {
                        "Math": int(row["Math"]),
                        "Science": int(row["Science"]),
                        "English": int(row["English"])
                    },
                    "Grade": row["Grade"],
                    "GPA": float(row["GPA"])
                }
        print("Imported from students.csv")
    except FileNotFoundError:
        print("CSV file not found.")

def menu():
    while True:
        print("\nStudent Information System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Find Class Topper")
        print("6. Export to CSV")
        print("7. Import from CSV")
        print("8. Exit")

        choice = input("Enter your choice: ")
        if choice == '1': add_student()
        elif choice == '2': update_student()
        elif choice == '3': delete_student()
        elif choice == '4': view_all_students()
        elif choice == '5': find_topper()
        elif choice == '6': export_to_csv()
        elif choice == '7': import_from_csv()
        elif choice == '8': break
        else: print("Invalid choice. Try again.")

# Run the menu
menu()