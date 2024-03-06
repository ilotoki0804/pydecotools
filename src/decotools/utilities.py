from __future__ import annotations

from typing import Callable

from .applier import decorator as _decorator, Decorator as _Decorator

NO_DEFAULT = object()


@_decorator
def attr(name: str, default=NO_DEFAULT):
    @_decorator
    def inner(value):
        return getattr(value, name) if default is NO_DEFAULT else getattr(value, name, default)
    return inner


@_decorator
def call(*args, **kwargs):
    @_decorator
    def inner(func):
        return func(*args, **kwargs)
    return inner


@_decorator
def item(item):
    @_decorator
    def inner(value):
        return value[item]
    return inner


@_decorator
def attrchain(name: str, default=NO_DEFAULT):
    """
    `attrchain` is Nonesafe version of `attr`, which means it safely passes None if None is passed as value,
    and returns None if getattr failed.
    """
    @_decorator
    def inner(value):
        if value is None:
            return None
        try:
            return getattr(value, name) if default is NO_DEFAULT else getattr(value, name, default)
        except AttributeError:
            return None
    return inner


@_decorator
def itemchain(item):
    @_decorator
    def inner(value):
        if value is None:
            return None
        try:
            return value[item]
        except Exception:
            return None
    return inner


@_decorator
def nonesafe(func: Callable):
    @_decorator
    def inner(arg, *args, **kwargs):
        return None if arg is None else func(arg, *args, **kwargs)
    return inner


@_decorator
def method(__name: str, /, *args, **kwargs):
    @_decorator
    def inner(value):
        return getattr(value, __name)(*args, **kwargs)
    return inner


@_decorator
def methodchain(__name: str, /, *args, **kwargs):
    @_decorator
    def inner(value):
        if value is None:
            return None
        method = getattr(value, __name, None)
        return None if method is None else method(*args, **kwargs)
    return inner


@_decorator
def debug(value):
    print(repr(value))
    return value


@_decorator
def no_op(value):
    return value
