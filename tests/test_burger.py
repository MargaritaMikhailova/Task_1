import pytest

from unittest.mock import Mock
from burger import Burger

class TestBurger:

    def test_initial_state(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self):
        burger = Burger()
        ing1 = Mock()
        ing2 = Mock()
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        assert len(burger.ingredients) == 2

    def test_remove_ingredient(self):
        burger = Burger()
        ing1 = Mock()
        ing2 = Mock()
        burger.ingredients = [ing1, ing2]
        burger.remove_ingredient(0)
        assert burger.ingredients == [ing2]

    def test_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 10.0
        burger.set_buns(mock_bun)

        ing = Mock()
        ing.get_price.return_value = 5.0
        burger.add_ingredient(ing)

        assert burger.get_price() == 25.0  
