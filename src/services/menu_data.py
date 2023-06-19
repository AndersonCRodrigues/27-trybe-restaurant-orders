import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self._csv_reader(source_path)

    def _csv_reader(self, source_path: str):
        try:
            with open(source_path, encoding="utf-8") as file:
                reader = csv.reader(
                    file, delimiter=",", quotechar='"'
                )
                header, *data = reader

            return self._get_recipes(data)
        except FileNotFoundError:
            print("Arquivo inexistente")

    def _get_recipes(self, data):
        new_set = set()

        for item in data:
            dish_name, dish_price, ingredient_name, ingredient_amount = item[
                :4
            ]

            dish = next((d for d in new_set if d.name == dish_name), None)
            if dish is None:
                dish = Dish(dish_name, float(dish_price))
                new_set.add(dish)

            ingredient = Ingredient(ingredient_name)
            dish.add_ingredient_dependency(ingredient, int(ingredient_amount))

        return new_set
