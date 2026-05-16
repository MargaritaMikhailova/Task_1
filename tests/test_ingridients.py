import pytest

from ingredient import Ingredient
from data import INGREDIENT_CREATION_PARAMS


class TestIngredient:
    @pytest.mark.parametrize("ing_type, name, price", INGREDIENT_CREATION_PARAMS)
    def test_ingredient_creation(self, ing_type, name, price):
        ing = Ingredient(ing_type, name, price)
        assert ing.name == name
        assert ing.price == price
