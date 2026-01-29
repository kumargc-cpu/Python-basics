students = {}

def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
    else:
        for name, marks in students.items():
            print(f"{name} : {marks}")

def main():
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice")

main()
