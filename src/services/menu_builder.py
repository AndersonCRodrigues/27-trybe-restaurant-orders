from typing import Dict, List
from models.dish import Dish

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData


DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4

    def get_main_menu(self, restriction=None) -> List[Dict]:
        menu_list = []

        for dish in self.menu_data.dishes:
            restrictions = dish.get_restrictions()
            ingredients = dish.get_ingredients()

            if restriction is None or restriction not in restrictions:
                recipe = self.build_recipe(dish)
                if self.inventory.check_recipe_availability(recipe):
                    menu_dict = {
                        "dish_name": dish.name,
                        "ingredients": list(ingredients),
                        "price": dish.price,
                        "restrictions": list(restrictions),
                    }
                    menu_list.append(menu_dict)

        return menu_list

    def build_recipe(self, dish: Dish):
        recipe = {}

        for ingredient, amount in dish.recipe.items():
            recipe[ingredient] = amount

        return recipe
