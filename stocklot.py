#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""
>>> pc = StockLot("Computer", "EAA5000", "Hardware", 599, 3)
>>> pc.name == "Computer" and pc.category == "Hardware"
True
>>> pc.price == 599 and pc.quantity == 3 and pc.value == 1797
True
>>> sock = StockLot("Socket", "KXY5200", "Media", 100, 2)
>>> sock.name
'Socket'
>>> try:
...     StockLot("", "ABC1000", "Software", 129, 2)
... except ValueError as e:
...     str(e) == "'name' may not be empty"
True
>>> try:
...     StockLot("Printer", "KXV5500", "Vaporware", 129, 2)
... except ValueError as e:
...     str(e) == ("category: 'Vaporware', Must be one of "
...                "['Consumables', 'Hardware', 'Media', 'Software']")
True
>>> try:
...     sock = StockLot("Socket", "KXY520", "Media", 100, 2)
... except ValueError as e:
...     str(e)
"'KXY520' Is not a valid product ID"
"""
from validator import StringValidated, NumberValidated


class StockLot:
    name = StringValidated()
    productid = StringValidated(regex=r"^[A-Z]{3}\d{4}$")
    category = StringValidated(
        oneof=frozenset(["Consumables", "Hardware", "Media", "Software"])
    )
    price = NumberValidated(1, 1e06)
    quantity = NumberValidated(1, 1000)

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
    # try:
    #     sock = StockLot("Socket", "KXY520", "Media", 100, 2)
    # except ValueError as e:
    #     print(e)
