import sqlite3
from lib.models import CONN, CURSOR


class Recipe:
    def __init__(self, name, type, steps):
        self.name = name
        self.type = type
        self.steps = steps
        self.id = None

    def __repr__(self):
        return f"Recipes: {self.name} | {self.type} | {self.steps}"
    

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if isinstance (value, str) and value.strip():
            self._name = value
        else:
            raise ValueError("name Invalid")
    

    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self,value):
        if isinstance (value, str) and value.strip():
            self._type = value
        else:
            raise ValueError("type Invalid")


    @property
    def steps(self):
        return self._steps

    @steps.setter
    def steps(self,value):
        if isinstance (value, str) and value.strip():
            self._steps = value
        else:
            raise ValueError("steps Invalid")
        
    
    @classmethod
    def _from_db_row(cls, row):
        recipe = cls(row[1], row[2], row[3])
        recipe.id = row[0]
        return recipe
    
    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM recipes")
        rows = CURSOR.fetchall()
        return [cls._from_db_row(row) for row in rows] if rows else []
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM recipes WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        if row:
            return cls._from_db_row(row)
        else:
            return None
        
    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute("SELECT * FROM recipes WHERE name = ?", (name,))
        row = CURSOR.fetchone()
        if row:
                return cls._from_db_row(row)
        else:
            return None
        
    @classmethod
    def add_new(cls, name, type, steps):
        existing = cls.find_by_name(name)
        if existing:
            return existing
        recipe = cls(name, type, steps)
        recipe.save()
        return recipe
    

    def update(self):
        CURSOR.execute("UPDATE recipes SET name = ?, type =? , steps = ? WHERE id = ?", (self._name, self._type, self._steps, self.id,))
        CONN.commit()

    def delete(self):
        CURSOR.execute("DELETE FROM recipes WHERE id = ?",(self.id,))
        CONN.commit()
        self.id = None
    
    def save(self):
        try:
            CURSOR.execute("INSERT INTO recipes (name, type, steps) VALUES (?,?,?)", (self._name, self._type, self._steps))
            self.id = CURSOR.lastrowid
            CONN.commit()
        except sqlite3.IntegrityError:
            print("Name already exists. Use add_new() or choose a different name.")

        
    
        
    
    


