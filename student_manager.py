# student_manager.py

class StudentManager:
    def __init__(self, database):
        self.db = database

    def add_student(self):
        student_id = input("Enter ID: ")
        if self.db.fetch_by_id(student_id):
            raise ValueError("Student already exists")

        name = input("Enter name: ")
        branch = input("Enter branch: ")
        year = int(input("Enter year: "))

        self.db.insert(student_id, name, branch, year)

    def update_student(self, student_id):
        if not self.db.fetch_by_id(student_id):
            raise ValueError("Student not found")

        name = input("Enter new name: ")
        branch = input("Enter new branch: ")
        year = int(input("Enter new year: "))

        self.db.update(student_id, name, branch, year)

    def delete_student(self, student_id):
        if not self.db.fetch_by_id(student_id):
            raise ValueError("Student not found")

        self.db.delete(student_id)

    def list_students(self):
        return self.db.fetch_all()

    def get_student(self, student_id):
        student = self.db.fetch_by_id(student_id)
        if not student:
            raise ValueError("Student not found")
        return student
