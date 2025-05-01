#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import numbers
import re
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
    StockLot("Printer", "KXV5500", "Vaporware", 129, 2)
    pc = StockLot("Computer", "EAA5000", "Hardware", 599, 3)
    # pc = StockLot("Computer", 0x123, "Hardware", 599, 3)
    print(f"{vars(pc) = }")
    # assert pc.name == "Computer" and pc.category == "Hardware"
    # assert pc.productid == "EAA5000"
    # assert pc.price == 599 and pc.quantity == 3 and pc.value == 1797
