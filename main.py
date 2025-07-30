# main.py
from lib.models.ingredient import Ingredient
from lib.models.recipe import Recipe

def run():
    print("🧪 Ingredients:")
    print(Ingredient.get_all())

    print("🧪 Recipes:")
    print(Recipe.get_all())

if __name__ == "__main__":
    run()

    

