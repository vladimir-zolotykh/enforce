#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""
>>> sock = StockLot("Socket", "KXY5200", "Media", 100, 2)
>>> sock.name
'Socket'
>>> try:
...     sock = StockLot("Socket", "KXY520", "Media", 100, 2)
... except ValueError as e:
...     str(e)
"'KXY520' doesn't match ^[A-Z]{3}\\\\d{4}$"
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
