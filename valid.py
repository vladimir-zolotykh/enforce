#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""
>>> pc = StockItem("Computer", "EAA5000", "Hardware", 599, 3)
>>> pc.name == "Computer" and pc.category == "Hardware"
True
>>> pc.productid == "EAA5000"
True
>>> pc.price == 599 and pc.quantity == 3 and pc.value == 1797
True
>>> error = None
>>> try:
...     StockItem("", "ABC1000", "Software", 129, 2)
... except ValueError as e:
...     error = str(e)
>>> error == "name may not be empty"
True
>>> try:
...     StockItem("Printer", "KXV5500", "Vaporware", 129, 2)
... except ValueError as e:
...     error = str(e)
>>> error == "category cannot be set to Vaporware"
True
>>> try:
...     StockItem("Cable", "KXB5001", "Media", -12, 2)
... except ValueError as e:
...     error = str(e)
>>> error == "price -12 is too small"
True
>>> try:
...     StockItem("Socket", "KXY520", "Media", 1e7, 2)
... except ValueError as e:
...     error = str(e)
>>> error == "productid cannot be set to KXY520"
True
>>> try:
...     StockItem("Socket", "KXY5020", "Media", 1e7, 2)
... except ValueError as e:
...     error = str(e)
>>> error == "price 10000000.0 is too big"
True
>>> try:
...     StockItem("Paper", "KXJ5003", "Media", 10, 0)
... except ValueError as e:
...     error = str(e)
>>> error == "quantity 0 is too small"
True
>>> try:
...     StockItem("Ink", "AKX5005", "Media", 10, 1001)
... except ValueError as e:
...     error = str(e)
>>> error == "quantity 1001 is too big"
True
>>> item = StockItem("Toner", "KXV5500", "Media", 10, 100)
>>> item.quantity += 5
>>> item.quantity == 105 and item.value == 1050
True
>>> try:
...     item.quantity = "one"
... except AssertionError as e:
...     error = str(e)
>>> error == "quantity must be a number"
True
"""

import re
from valid_string import valid_string
from valid_number import valid_number

error = None


@valid_string("name", empty_allowed=False)
@valid_string("productid", empty_allowed=False, regex=re.compile(r"[A-Z]{3}\d{4}"))
@valid_string(
    "category",
    empty_allowed=False,
    acceptable=frozenset(["Consumables", "Hardware", "Software", "Media"]),
)
@valid_number("price", minimum=0, maximum=1e6)
@valid_number("quantity", minimum=1, maximum=1000)
class StockItem:
    def __init__(self, name, productid, category, price, quantity):
        self.name = name
        self.productid = productid
        self.category = category
        self.price = price
        self.quantity = quantity

    @property
    def value(self):
        return self.price * self.quantity


if __name__ == "__main__":
    import doctest

    doctest.testmod()
