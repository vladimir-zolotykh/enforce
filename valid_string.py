#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


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
                raise ValueError(
                    "{attr_name} cannot be set to " "{value}".format(**locals())
                )
            setattr(self, name, value)
            setattr(cls, attr_name, GenericDescriptor(getter, setter))

        return cls

    return decorator
