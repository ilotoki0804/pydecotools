from __future__ import annotations

from typing import Callable, TypeVar, Generic

_TargetReturn = TypeVar("_TargetReturn")
_TargetInput = TypeVar("_TargetInput")
_OtherReturn = TypeVar("_OtherReturn")


class DecoratorMeta(type):
    def __matmul__(cls, other):
        return other(cls)

    def __rmatmul__(cls, other):
        return cls(other)

    def partial(cls, *args, **kwargs):
        @decorator
        def inner(*inner_args, **inner_kwargs):
            return cls(*args, *inner_args, **kwargs, **inner_kwargs)
        return inner


class Decorator(metaclass=DecoratorMeta):
    """Decorator maker for classes.

    ```python
    from decotools import Decorator

    class MyDecorator(Decorator):
        def __init__(self, arg, kwarg=None):
            ...

        def __call__(self, arg, kwarg=None):
            ...

    "hello" @MyDecorator  # equivalent to `MyDecorator("hello")`
    "hello" @MyDecorator.partial(kwarg=123)  # equivalent to `MyDecorator("hello", kwarg=123)`
    "hello" @MyDecorator("arg")  # equivalent to `MyDecorator("arg")("hello")
    ```
    """
    def __matmul__(self, other):
        return other(self)

    def __rmatmul__(self, other):
        return self(other)  # type: ignore


class decorator(Generic[_TargetReturn, _TargetInput, _OtherReturn], metaclass=DecoratorMeta):
    """A decorator for implementing decorator operator."""

    def __init__(self, func: Callable[[_TargetInput], _TargetReturn]) -> None:
        self.target = func

    def __call__(self, *args, **kwargs) -> _TargetReturn:  # noqa: F811
        return self.target(*args, **kwargs)

    def __matmul__(self, other: Callable[[Callable[[_TargetInput], _TargetReturn]], _OtherReturn]) -> _OtherReturn:
        """
        ```python
        decoratable_func @ normal_func
        ==> normal_func(decoratable_func)
        ```
        """
        return other(self.target)

    def __rmatmul__(self, other: _TargetInput) -> _TargetReturn:
        """
        ```python
        argument @ decoratable_func
        ==> decoratable_func(argument)
        ```
        """
        return self.target(other)

    def partial(self, *args, **kwargs):
        @decorator
        def inner(*inner_args, **inner_kwargs):
            return self.target(*args, *inner_args, **kwargs, **inner_kwargs)
        return inner


@decorator
def smart_partial(f: Callable | None = None, /, *, skip_trying: bool = False) -> Callable:
    if f is None:
        return lambda f: smart_partial(f, skip_trying=skip_trying)

    @decorator
    def wrapper(*args, **kwargs):
        try:
            if skip_trying:
                raise TypeError("argument")
            return f(*args, **kwargs)
        except TypeError as e:
            if "argument" not in e.args[0]:
                # Error message must have `argument` if the error is related to parameter incomplete error.
                raise

            # Parameter was incomplete
            @decorator
            def inner(*inner_args, **inner_kwargs):
                return f(*args, *inner_args, **kwargs, **inner_kwargs)
            return inner
    return wrapper
