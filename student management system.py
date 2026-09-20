students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        course = input("Enter course: ")

        student = {
            "name": name,
            "age": age,
            "course": course
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == 2:
        if len(students) == 0:
            print("No students found.")
        else:
            print("\nStudent Details")

            for student in students:
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Course:", student["course"])
                print("--------------------")

    elif choice == 3:
        search_name = input("Enter student name to search: ")
        found = False

        for student in students:
            if student["name"].lower() == search_name.lower():
                print("Student Found!")
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Course:", student["course"])
                found = True

        if not found:
            print("Student not found.")

    elif choice == 4:
        delete_name = input("Enter student name to delete: ")
        found = False

        for student in students:
            if student["name"].lower() == delete_name.lower():
                students.remove(student)
                print("Student deleted successfully!")
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == 5:
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice.")
