#database.py
import sqlite3

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self._create_table()

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def _create_table(self):
        try:
            with self._connect() as conn:
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS students (
                        id TEXT PRIMARY KEY,
                        name TEXT NOT NULL,
                        branch TEXT NOT NULL,
                        year INTEGER NOT NULL
                    )
                """)
        except sqlite3.Error as e:
            raise Exception(f"Database initialization error: {e}")

    def fetch_all(self):
        try:
            with self._connect() as conn:
                return conn.execute("SELECT * FROM students").fetchall()
        except sqlite3.Error as e:
            raise Exception(f"Failed to fetch students: {e}")

    def fetch_by_id(self, student_id):
        try:
            with self._connect() as conn:
                return conn.execute(
                    "SELECT * FROM students WHERE id = ?", (student_id,)
                ).fetchone()
        except sqlite3.Error as e:
            raise Exception(f"Failed to fetch student: {e}")

    def insert(self, student_id, name, branch, year):
        try:
            with self._connect() as conn:
                conn.execute(
                    "INSERT INTO students VALUES (?, ?, ?, ?)",
                    (student_id, name, branch, year)
                )
        except sqlite3.IntegrityError:
            raise ValueError("Student ID already exists.")
        except sqlite3.Error as e:
            raise Exception(f"Insert failed: {e}")

    def update(self, student_id, name, branch, year):
        try:
            with self._connect() as conn:
                conn.execute(
                    "UPDATE students SET name=?, branch=?, year=? WHERE id=?",
                    (name, branch, year, student_id)
                )
        except sqlite3.Error as e:
            raise Exception(f"Update failed: {e}")

    def delete(self, student_id):
        try:
            with self._connect() as conn:
                conn.execute(
                    "DELETE FROM students WHERE id=?", (student_id,)
                )
        except sqlite3.Error as e:
            raise Exception(f"Delete failed: {e}")
