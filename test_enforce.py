#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import pytest
from enforce import StockItem


def test_ok10():
    pc = StockItem("Computer", "EAA5000", "Hardware", 599, 3)
    assert pc.name == "Computer" and pc.category == "Hardware"
    assert pc.productid == "EAA5000"


def test_nok10():
    with pytest.raises(ValueError):
        e = StockItem("", "ABC1000", "Software", 129, 2)
    assert str(e) == "name may not be empty"
