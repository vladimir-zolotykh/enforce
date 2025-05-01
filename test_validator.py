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
    assert str(e.value) == (
        "category: 'Vaporware', Must be one of "
        "[Constraint: ['Consumables', 'Hardware', 'Media', 'Software']]"
    )


def test_nok20():
    with pytest.raises(ValueError) as e:
        StockLot("Cable", "KXB5001", "Media", -12, 2)
    assert str(e.value) == "-12 is less than 1"


def test_nok25():
    with pytest.raises(ValueError) as e:
        StockLot("Socket", "KXY520", "Media", 1e7, 2)
    assert str(e.value) == "'KXY520' doesn't match ^[A-Z]{3}\\d{4}$"


def test_nok30():
    with pytest.raises(ValueError) as e:
        StockLot("Paper", "KXJ5003", "Media", 10, 0)
    assert str(e.value) == "0 is less than 1"


def test_nok35():
    with pytest.raises(ValueError) as e:
        StockLot("Ink", "AKX5005", "Media", 10, 1001)
    assert str(e.value) == "1001 is bigger that 1000"
