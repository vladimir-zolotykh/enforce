#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import numbers


def valid_number(
    attr_name, minimum=None, maximum=None, acceptable=None
):
    def decorator(cls):
        name = "__" + attr_name

        def getter(self):
            return getattr(self, name)

        def setter(self, value):
            assert isinstance(value, numbers.Number), (
                attr_name + " must be a number"
            )
            if minimum is not None and value < minimum:
                raise ValueError(
                    "{attr_name} {value} is too small".format(
                        **locals()
                    )
                )
            if maximum is not None and value > maximum:
                raise ValueError(
                    "{attr_name} {value} is too big".format(**locals())
                )
            if acceptable is not None and value not in acceptable:
                raise ValueError(
                    "{attr_name} {value} is unacceptable".format(
                        **locals()
                    )
                )
            setattr(self, name, value)

        setattr(cls, attr_name, GenericDescriptor(getter, setter))
        return cls

    return decorator
