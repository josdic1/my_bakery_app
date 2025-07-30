# main.py
from lib.models.ingredient import Ingredient
from lib.models.recipe import Recipe
from lib.models.recipe_ingredient import RecipeIngredient

def run():
    print(RecipeIngredient.get_all())



if __name__ == "__main__":
    run()



    

