# database.py
import sqlite3

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self._create_table()

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def _create_table(self):
        with self._connect() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    branch TEXT NOT NULL,
                    year INTEGER NOT NULL
                )
            """)

    def fetch_all(self):
        with self._connect() as conn:
            return conn.execute("SELECT * FROM students").fetchall()

    def fetch_by_id(self, student_id):
        with self._connect() as conn:
            return conn.execute(
                "SELECT * FROM students WHERE id = ?", (student_id,)
            ).fetchone()

    def insert(self, student_id, name, branch, year):
        with self._connect() as conn:
            conn.execute(
                "INSERT INTO students VALUES (?, ?, ?, ?)",
                (student_id, name, branch, year)
            )

    def update(self, student_id, name, branch, year):
        with self._connect() as conn:
            conn.execute(
                "UPDATE students SET name=?, branch=?, year=? WHERE id=?",
                (name, branch, year, student_id)
            )

    def delete(self, student_id):
        with self._connect() as conn:
            conn.execute(
                "DELETE FROM students WHERE id=?", (student_id,)
            )
