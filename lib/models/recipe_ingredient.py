import sqlite3
from lib.models import CONN, CURSOR
from lib.models.ingredient import Ingredient

class RecipeIngredient:
    def __init__(self, recipe_id, ingredient_id, quantity):
        self.recipe_id = recipe_id
        self.ingredient_id = ingredient_id
        self.quantity = quantity
        self.id = None

    def __repr__(self):
        return f"RecipeIngredients: {self.recipe_id} | {self.ingredient_id} | {self.quantity}"


    @property
    def recipe_id(self):
        return self._recipe_id

    @recipe_id.setter
    def recipe_id(self, value):
        if isinstance (value, int) and value > 0:
            self._recipe_id = value
        else:
            raise ValueError ("Invalid Entry - recipe_id")
    

    @property
    def ingredient_id(self):
        return self._ingredient_id

    @ingredient_id.setter
    def ingredient_id(self, value):
        if isinstance (value, int) and value > 0: 
            self._ingredient_id = value
        else:
            raise ValueError ("Invalid Entry - ingredient_id")
        
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if isinstance (value, int) and value > 0: 
            self._quantity = value
        else:
            raise ValueError ("Invalid Entry - quantity")
        
    @classmethod
    def _row_from_db(cls, row):
        recipe_ingredient = cls(row[1], row[2], row[3])
        recipe_ingredient.id = row[0]
        return recipe_ingredient

    @classmethod
    def find_ingredient(cls):
        print(Ingredient.get_all())

    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM recipe_ingredients")
        rows = CURSOR.fetchall()
        return [cls._row_from_db(row) for row in rows] if rows else []
    
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM recipe_ingredients WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        if row:
            return cls._row_from_db(row)
        else:
            return None
    
    @classmethod
    def find_by_recipe_and_ingredient(cls, recipe_id, ingredient_id, quantity):
        CURSOR.execute("SELECT * FROM recipe_ingredients WHERE recipe_id = ? AND ingredient_id =? AND quantity = ?", (recipe_id, ingredient_id,quantity,))
        row = CURSOR.fetchone()
        if row:
            return cls._row_from_db(row)
        else:
            return None

    @classmethod
    def add_new(cls, recipe_id, ingredient_id, quantity):
        existing = cls.find_by_recipe_and_ingredient(recipe_id, ingredient_id, quantity)
        if existing:
            return existing
        recipe_ingredient = cls(recipe_id, ingredient_id, quantity)
        recipe_ingredient.save()
        return recipe_ingredient
    
    def update(self):
        CURSOR.execute("UPDATE recipe_ingredients SET recipe_id  = ?, ingredient_id = ?, quantity = ? WHERE id = ?", (self._recipe_id, self._ingredient_id, self._quantity, self.id,))
        CONN.commit()

    def delete(self):
        CURSOR.execute("DELETE FROM recipe_ingredients WHERE id = ?", (self.id,))
        CONN.commit()

    def save(self):
        try:
            CURSOR.execute("INSERT INTO recipe_ingredients (recipe_id, ingredient_id, quantity) VALUES (?, ?, ?)", (self._recipe_id, self._ingredient_id, self._quantity,))
            self.id = CURSOR.lastrowid
            CONN.commit()
        except sqlite3.IntegrityError:
            print("Recipe-ingredient combination already exists")



