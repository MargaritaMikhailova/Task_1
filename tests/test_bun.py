import pytest

from bun import Bun
from data import *


class TestBun:
    @pytest.mark.parametrize("name, price", BUN_PARAMS)
    def test_bun_init_and_getters(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name
        assert bun.price == price

    @pytest.mark.parametrize("name, price", BUN_PARAMS)
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
