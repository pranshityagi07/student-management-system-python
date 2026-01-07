# main.py

from database import Database
from student_manager import StudentManager

def main():
    db = Database("students.db")
    manager = StudentManager(db)

    while True:
        print("\nA-Add U-Update D-Delete P-Print I-Id Q-Quit")
        choice = input("Choice: ").upper()

        try:
            if choice == "A":
                manager.add_student()
            elif choice == "U":
                manager.update_student(input("ID: "))
            elif choice == "D":
                manager.delete_student(input("ID: "))
            elif choice == "P":
                for s in manager.list_students():
                    print(s)
            elif choice == "I":
                print(manager.get_student(input("ID: ")))
            elif choice == "Q":
                break
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
