#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import numbers
import re
from stringvalidated import StringValidated, NumberValidated


class GenericDescriptor:
    def __init__(self, getter, setter):
        self.getter = getter
        self.setter = setter

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return self.getter(instance)

    def __set__(self, instance, value):
        return self.setter(instance, value)


def valid_string(attr_name, empty_allowed=True, regex=None, acceptable=None):
    def decorator(cls):
        name = "__" + attr_name

        def getter(self):
            return getattr(self, name)

        def setter(self, value):
            assert isinstance(value, str), attr_name + " must be a string"
            if not empty_allowed and not value:
                raise ValueError("{0} may not be empty".format(attr_name))
            if (acceptable is not None and value not in acceptable) or (
                regex is not None and not regex.match(value)
            ):
                # fmt: off
                raise ValueError(
                    "{attr_name} cannot be set to {value}".format(**locals()))
                # fmt: on
            setattr(self, name, value)

        setattr(cls, attr_name, GenericDescriptor(getter, setter))
        return cls

    return decorator


def valid_number(attr_name, minimum=None, maximum=None, acceptable=None):
    def decorator(cls):
        name = "__" + attr_name

        def getter(self):
            return getattr(self, name)

        def setter(self, value):
            # fmt: off
            assert isinstance(value, numbers.Number), (attr_name +
                                                       " must be a number")
            if minimum is not None and value < minimum:
                raise ValueError(
                    "{attr_name} {value} is too small".format(**locals()))
            if maximum is not None and value > maximum:
                raise ValueError(
                    "{attr_name} {value} is too big".format(**locals()))
            if acceptable is not None and value not in acceptable:
                raise ValueError(
                    "{attr_name} {value} is unacceptable".format(**locals()))
            # fmt: on
            setattr(self, name, value)

        setattr(cls, attr_name, GenericDescriptor(getter, setter))
        return cls

    return decorator


# fmt: off
@valid_string("name", empty_allowed=False)
@valid_string("productid", empty_allowed=False,
              regex=re.compile(r"[A-Z]{3}\d{4}"))
@valid_string(
    "category", empty_allowed=False,
    acceptable=frozenset(["Consumables", "Hardware", "Software", "Media"]),)
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


class StockLot:
    name = StringValidated()
    productid = StringValidated(regex=r"^[A-Z]{3}\d{4}$")
    category = StringValidated(oneof=frozenset([
        "Consumables", "Hardware", "Software", "Media"]))
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


# fmt: on
if __name__ == "__main__":
    # pc = StockLot("Computer", "EAA5000", "Hardware", 599, 3)
    pc = StockLot("Computer", 0x123, "Hardware", 599, 3)
    assert pc.name == "Computer" and pc.category == "Hardware"
    assert pc.productid == "EAA5000"
    assert pc.price == 599 and pc.quantity == 3 and pc.value == 1797
