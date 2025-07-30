import sqlite3
from lib.models import CONN, CURSOR

class Ingredient:
    def __init__(self, name):
        self.name = name
        self.id = None

    def __repr__(self):
        return f"Ingredients: {self.name} | {self.id}"


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance (value, str) and value.strip():
            self._name = value
        else:
            raise ValueError ("Invalid Entry - name")
    

    @classmethod
    def _row_from_db(cls, row):
        ingredient = cls(row[1])
        ingredient.id = row[0]
        return ingredient


    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM ingredients")
        rows = CURSOR.fetchall()
        return [cls._row_from_db(row) for row in rows] if rows else []
    
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM ingredients WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        if row:
            return cls._row_from_db(row)
        else:
            return None
    
    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute("SELECT * FROM ingredients WHERE name = ?", (name,))
        row = CURSOR.fetchone()
        if row:
            return cls._row_from_db(row)
        else:
            return None
    

    @classmethod
    def add_new(cls, name):
        existing = cls.find_by_name(name)
        if existing:
            return existing
        ingredient = cls(name)
        ingredient.save()
        return ingredient
    
    def update(self):
        CURSOR.execute("UPDATE ingredients SET name  = ? WHERE id = ?", (self._name, self.id,))
        CONN.commit()

    def delete(self):
        CURSOR.execute("DELETE FROM ingredients WHERE id = ?", (self.id,))
        CONN.commit()

    def save(self):
        try:
            CURSOR.execute("INSERT INTO ingredients (name) VALUES (?)", (self._name,))
            self.id = CURSOR.lastrowid
            CONN.commit()
        except sqlite3.IntegrityError:
            print("Name already exists. Use add_new() or choose a different name.")


