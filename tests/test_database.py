import pytest

from database import Database

class TestDatabase:

    def test_available_buns_returns_list(self):
        db = Database()
        buns = db.available_buns()
        assert isinstance(buns, list)
        assert len(buns) > 0

    def test_available_ingredients_returns_list(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert isinstance(ingredients, list)
        assert len(ingredients) > 0