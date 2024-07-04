students = {}


def add_student(name, age, grade, subjects):

    new_student = {
        'name': name,
        'age': age,
        'grade': grade,
        'subjects': subjects
    }
    students[name] = new_student
    return students


def update_student(name):

    if name in students:
        print("Update the  student's fields...")
        new_age = input('Enter a new age: ')
        new_grade = input('Enter a new grade: ')
        new_subjects = (input('Enter new subjects (comma-separated): ').split(', '))

        if new_age:
            students[name]['age'] = new_age
        if new_grade:
            students[name]['grade'] = float(new_grade)
        if new_subjects:
            students[name]['subjects'] = new_subjects

        return students


def delete_student(name):

    # Check if the student exists
    # Code to delete the student's record
    if name in students:
        del students[name]
        print(f"Deleting {name}'s record...")
    return students


def search_student(name):

    if name in students:
        for name, info in students.items():
            print(f'Name: {name}')
            print(f'Age: {info["age"]}')
            print(f'Grade: {info["grade"]}')
            print(f'Subjects: {", ".join(info["subjects"])}')


def list_all_students():

    if len(students) > 0:
        for name, info in students.items():
            print(f'Name: {name}')
            print(f'Age: {info["age"]}')
            print(f'Grade: {info["grade"]}')
            print(f'Subjects: {", ".join(info["subjects"])}\n')


def main():

    while True:
        # Display menu options
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. List All Students")
        print("6. Exit")

        # Prompt user for their choice
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student's name: ")
            age = int(input("Enter student's age: "))
            grade = float(input("Enter student's grade: "))
            subjects = input("Enter student's subjects (comma-separated): ").split(',')
            add_student(name, age, grade, subjects)

        elif choice == '2':
            name = input("Enter student's name to update: ")
            update_student(name)

        elif choice == '3':
            name = input("Enter student's name to delete: ")
            delete_student(name)

        elif choice == '4':
            name = input("Enter student's name to search: ")
            search_student(name)

        elif choice == '5':
            list_all_students()

        elif choice == '6':
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()