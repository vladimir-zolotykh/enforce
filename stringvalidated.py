#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import re
from numbers import Number


class StringValidated:
    def __init__(self, oneof=None, regex=None):
        self.oneof = oneof
        self.regex = regex

    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        if not instance:
            return self
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError(f"{value!r} isn't of type `str'")
        if self.oneof and value not in self.oneof:
            raise ValueError(f"{value!r} isn't in {self.oneof!r}")
        if self.regex and not re.match(self.regex, value):
            raise ValueError(f"{value!r} doesn't match {self.regex!r}")
        setattr(instance, self.private_name, value)


class NumberValidated:
    def __init__(self, minvalue=0, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        if not instance:
            return self
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{value!r} isn't int or float")
        if value < self.minvalue:
            raise ValueError(f"{value!r} is less than {self.minvalue}")
        if isinstance(self.maxvalue, Number) and value > self.maxvalue:
            raise ValueError(f"{value!r} is bigger that {self.maxvalue}")
        setattr(instance, self.private_name, value)
