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
"""
import re
from valid_string import valid_string
from valid_number import valid_number


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
