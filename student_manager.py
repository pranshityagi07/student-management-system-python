#student_manager.py

class StudentManager:
    def __init__(self, database):
        self.db = database

    def add_student(self):
        student_id = input("Enter ID: ").strip()
        if self.db.fetch_by_id(student_id):
            raise ValueError("Student already exists.")

        name = input("Enter name: ").strip()
        branch = input("Enter branch: ").strip()

        try:
            year = int(input("Enter year: "))
        except ValueError:
            raise ValueError("Year must be a valid number.")

        self.db.insert(student_id, name, branch, year)
        print("Student added successfully.")

    def update_student(self, student_id):
        if not self.db.fetch_by_id(student_id):
            raise ValueError("Student not found.")

        name = input("Enter new name: ").strip()
        branch = input("Enter new branch: ").strip()

        try:
            year = int(input("Enter new year: "))
        except ValueError:
            raise ValueError("Year must be a valid number.")

        self.db.update(student_id, name, branch, year)
        print("Student updated successfully.")

    def delete_student(self, student_id):
        if not self.db.fetch_by_id(student_id):
            raise ValueError("Student not found.")

        self.db.delete(student_id)
        print("Student deleted successfully.")

    def list_students(self):
        return self.db.fetch_all()

    def get_student(self, student_id):
        student = self.db.fetch_by_id(student_id)
        if not student:
            raise ValueError("Student not found.")
        return student
