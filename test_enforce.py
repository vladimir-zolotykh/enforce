#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import pytest
from enforce import StockItem


def test_ok10():
    pc = StockItem("Computer", "EAA5000", "Hardware", 599, 3)
    assert pc.name == "Computer" and pc.category == "Hardware"
    assert pc.productid == "EAA5000"
    assert pc.price == 599 and pc.quantity == 3 and pc.value == 1797


def test_ok15():
    item = StockItem("Toner", "KXV5500", "Media", 10, 100)
    item.quantity += 5
    assert item.quantity == 105 and item.value == 1050


def test_nok10():
    with pytest.raises(ValueError) as e:
        StockItem("", "ABC1000", "Software", 129, 2)
    assert str(e.value) == "name may not be empty"


def test_nok15():
    with pytest.raises(ValueError) as e:
        StockItem("Printer", "KXV5500", "Vaporware", 129, 2)
    assert str(e.value) == "category cannot be set to Vaporware"


def test_nok20():
    with pytest.raises(ValueError) as e:
        StockItem("Cable", "KXB5001", "Media", -12, 2)
    assert str(e.value) == "price -12 is too small"


def test_nok25():
    with pytest.raises(ValueError) as e:
        StockItem("Socket", "KXY520", "Media", 1e7, 2)
    assert str(e.value) == "productid cannot be set to KXY520"


def test_nok30():
    with pytest.raises(ValueError) as e:
        StockItem("Paper", "KXJ5003", "Media", 10, 0)
    assert str(e.value) == "quantity 0 is too small"


def test_nok35():
    with pytest.raises(ValueError) as e:
        StockItem("Ink", "AKX5005", "Media", 10, 1001)
    assert str(e.value) == "quantity 1001 is too big"
