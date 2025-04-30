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
