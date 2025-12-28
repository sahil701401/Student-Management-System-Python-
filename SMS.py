import json
import os

# Admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"

# File to store students
STUDENTS_FILE = "students.json"

def load_students():
    if os.path.exists(STUDENTS_FILE):
        with open(STUDENTS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_students(students):
    with open(STUDENTS_FILE, 'w') as f:
        json.dump(students, f, indent=4)

def admin_login():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return True
    return False

def add_student(students):
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    students.append({"id": id, "name": name, "age": age, "grade": grade})
    save_students(students)
    print("Student added successfully!")

def view_students(students):
    if not students:
        print("No students found.")
        return
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

def search_student(students):
    id = input("Enter student ID to search: ")
    for student in students:
        if student['id'] == id:
            print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
            return
    print("Student not found.")

def update_student(students):
    id = input("Enter student ID to update: ")
    for student in students:
        if student['id'] == id:
            student['name'] = input("Enter new name: ")
            student['age'] = input("Enter new age: ")
            student['grade'] = input("Enter new grade: ")
            save_students(students)
            print("Student updated successfully!")
            return
    print("Student not found.")

def delete_student(students):
    id = input("Enter student ID to delete: ")
    for i, student in enumerate(students):
        if student['id'] == id:
            del students[i]
            save_students(students)
            print("Student deleted successfully!")
            return
    print("Student not found.")

def student_view_details():
    students = load_students()
    id = input("Enter your student ID: ")
    for student in students:
        if student['id'] == id:
            print("\nYour Details:")
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Grade: {student['grade']}")
            return
    print("Student not found.")

def admin_menu(students):
    while True:
        print("\nAdmin Menu")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            update_student(students)
        elif choice == '5':
            delete_student(students)
        elif choice == '6':
            break
        else:
            print("Invalid choice.")

def main():
    while True:
        print("\nStudent Management System")
        print("1. Admin Mode")
        print("2. Student Mode")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            if admin_login():
                students = load_students()
                admin_menu(students)
            else:
                print("Invalid credentials.")
        elif choice == '2':
            student_view_details()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
