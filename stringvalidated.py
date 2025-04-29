#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import re


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
        if self.regex and re.match(self.regex, value):
            raise ValueError(f"{value!r} doesn't match {self.regex!r}")
        setattr(instance, self.private_name, value)
