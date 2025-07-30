# main.py
from lib.models.ingredient import Ingredient
from lib.models.recipe import Recipe
from lib.models.recipe_ingredient import RecipeIngredient

def run():
    r = Recipe.find_by_name("Banana Bread")
    r.add_ingredient_to_recipe("banana", "3 units")

    

if __name__ == "__main__":
    run()



    

