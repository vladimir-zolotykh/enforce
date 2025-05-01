#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import pytest
from enforce import StockLot


def test_ok10():
    pc = StockLot("Computer", "EAA5000", "Hardware", 599, 3)
    assert pc.name == "Computer" and pc.category == "Hardware"
    assert pc.productid == "EAA5000"
    assert pc.price == 599 and pc.quantity == 3 and pc.value == 1797


def test_nok10():
    with pytest.raises(ValueError) as e:
        StockLot("", "ABC1000", "Software", 129, 2)
    assert str(e.value) == "'name' is empty"


def test_nok15():
    with pytest.raises(ValueError) as e:
        StockLot("Printer", "KXV5500", "Vaporware", 129, 2)
    consumables = frozenset(["Consumables", "Hardware", "Media", "Software"])
    assert str(e.value) == f"'Vaporware' isn't in {consumables}"
