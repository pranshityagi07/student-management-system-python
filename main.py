#main.py

from database import Database
from student_manager import StudentManager

def print_menu():
    print()
    print("1. Add New Student        (A)")
    print("2. Update Student         (U)")
    print("3. Delete Student         (D)")
    print("4. Print All Students     (P)")
    print("5. Get Student By ID      (I)")
    print("6. Quit                   (Q)")
    print("==============================")

def main():
    try:
        db = Database("students.db")
        manager = StudentManager(db)
    except Exception as e:
        print(f"Failed to initialize system: {e}")
        return

    print('=' * 30)
    print("Welcome to Student Management System")
    print('=' * 30)

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip().upper()

        try:
            if choice == "A":
                manager.add_student()

            elif choice == "U":
                manager.update_student(input("Enter Student ID: ").strip())

            elif choice == "D":
                manager.delete_student(input("Enter Student ID: ").strip())

            elif choice == "P":
                students = manager.list_students()
                if not students:
                    print("No student found.")
                else:
                    for s in students:
                        print(s)

            elif choice == "I":
                print(manager.get_student(input("Enter Student ID: ").strip()))

            elif choice == "Q":
                print("Exiting Student Management System. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
