from lib.models import CONN, CURSOR

class Ingredient:
    def __init__(self, name, quantity, unit, recipes_found_in):
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.recipes_found_in = recipes_found_in
        self.id = None

    def __repr__(self):
        return f"Ingredients: {self._name} | {self._quantity} | {self._unit} | {self._recipes_found_in} | {self.id}"


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance (value, str) and value.strip():
            self._name = value
        else:
            raise ValueError ("Invalid Entry - name")
    

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if isinstance (value, str) and value > 0: 
            self._quantity = value
        else:
            raise ValueError ("Invalid Entry - quantity")
        

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        if isinstance (value, str) and value.strip():
            self._unit = value
        else:
            raise ValueError ("Invalid Entry - unit")


    @property
    def recipes_found_in(self):
        return self._recipes_found_in

    @recipes_found_in.setter
    def recipes_found_in(self, value):
        if isinstance (value, str) and value.strip(): 
            self._recipes_found_in = value
        else:
            raise ValueError ("Invalid Entry - recipes_found_in")
    
    @classmethod
    def _row_from_db(cls, row):
        CURSOR.execute("SELECT * FROM ingredients")
        ingredient = cls(row[1], row[2], row[3])
        ingredient.id = row[0]
        return ingredient
    
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM ingredients WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        if row:
            return cls._row_from_db(row)
        else:
            return None
    
    @classmethod
    def 


    
    def save(self):
        CURSOR.execute("INSERT INTO ingredients (name, quantity, unit, recipes_found_in)", (self._name, self._quantity, self._unit, self._recipes_found_in))
        self.id = CURSOR.lastrowid
        CONN.commit()



