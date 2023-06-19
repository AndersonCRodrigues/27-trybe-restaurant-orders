from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
import pytest  # noqa: F401, E261, E501


# Req 2
def test_dish():
    name1 = "Lasanha"
    name2 = "Salada"
    price = 25.99

    dish1 = Dish(name1, price)
    dish2 = Dish(name1, price)
    dish3 = Dish(name2, 12.50)

    indredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("camarão")

    assert dish1.name == "Lasanha"
    assert dish1.price == 25.99
    assert dish1.__repr__() == f"Dish('{name1}', R${price:.2f})"

    assert dish1.__eq__(dish2) is True
    assert dish1.__eq__(dish3) is False

    assert dish1.__hash__() == dish2.__hash__()
    assert dish1.__hash__() != dish3.__hash__()

    dish1.add_ingredient_dependency(indredient1, 10)
    dish1.add_ingredient_dependency(ingredient2, 5)

    assert dish1.get_ingredients() == {indredient1, ingredient2}

    restriction = dish1.get_restrictions()

    assert dish1.get_restrictions()
    assert isinstance(restriction, set)

    with pytest.raises(TypeError):
        Dish("Pizza", "invalid price")

    with pytest.raises(ValueError):
        Dish("Burger", 0)
