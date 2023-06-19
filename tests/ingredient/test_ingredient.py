from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import restriction_map  # noqa: F401, E261, E501

# Req 1


def test_ingredient():
    name1 = "farinha"
    name2 = "bacon"

    ingredient1 = Ingredient(name1)
    ingredient2 = Ingredient(name1)
    ingredient3 = Ingredient(name2)

    assert ingredient1.name == name1
    assert ingredient1.__repr__() == f"Ingredient('{name1}')"

    assert ingredient1.__hash__() == ingredient2.__hash__()
    assert ingredient1.__hash__() != ingredient3.__hash__()

    assert ingredient1.__eq__(ingredient2) is True
    assert ingredient1.__eq__(ingredient3) is False

    assert ingredient1.restrictions == restriction_map().get(name1, set)
