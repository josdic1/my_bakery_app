# main.py
from lib.models.ingredient import Ingredient
from lib.models.recipe import Recipe

def run():
    print("\n🧪 Ingredients:")
    for ing in Ingredient.get_all():
        print(" -", ing)

    print("\n🧪 Recipes:")
    for rec in Recipe.get_all():
        print(" -", rec)

if __name__ == "__main__":
    run()
    