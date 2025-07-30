import sqlite3
from lib.models import CONN, CURSOR

class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.id = None

    def __repr__(self):
        return f"Employee: {self.name} | {self.role}"


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance (value, str) and value.strip():
            self._name = value
        else:
            raise ValueError ("name Invalid")


    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        if isinstance (value, str) and value.strip():
            self._role = value
        else:
            raise ValueError ("role Invalid")
    

    @classmethod
    def _from_db_row(cls, row):
        employee = cls(row[1], row[2])
        employee.id = row[0]
        return employee

    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM employees WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        if row:
            return cls._from_db_row(row)
        else:
            return None

    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute("SELECT * FROM employees WHERE name = ?", (name,))
        row = CURSOR.fetchone()
        if row:
            return cls._from_db_row(row)
        else:
            return None

    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM employees")
        rows = CURSOR.fetchall()
        return [cls._from_db_row(row) for row in rows] if rows else []
    

    @classmethod
    def add_new(cls, name, role):
        existing = cls.find_by_name(name)
        if existing:
            return existing
        employee = cls(name, role)
        employee.save()
        return employee
    
    def update(self):
        CURSOR.execute("UPDATE employees SET name = ?, role = ? WHERE id = ?", (self._name, self._role, self.id,))
        CONN.commit()

    def delete(self):
        CURSOR.execute("DELETE FROM employees WHERE id = ?", (self.id,))
        CONN.commit()
        
    def save(self):
        try:
            CURSOR.execute("INSERT INTO employees (name, role) VALUES (?, ?)", (self._name, self._role))
            self.id = CURSOR.lastrowid
            CONN.commit()
        except sqlite3.IntegrityError:
            print("Name already exists. Use add_new() or choose a different name.")


        


