from __future__ import annotations

from typing import Callable, TypeVar, Generic

_TargetReturn = TypeVar("_TargetReturn")
_TargetInput = TypeVar("_TargetInput")
_OtherReturn = TypeVar("_OtherReturn")


class DecoratorOperatorMeta(type):
    def __matmul__(cls, other):
        return other(cls)

    def __rmatmul__(cls, other):
        return cls(other)


class decorator(Generic[_TargetReturn, _TargetInput, _OtherReturn], metaclass=DecoratorOperatorMeta):
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


@decorator
def smart_partial(f: Callable, /, *, skip_trying: bool = False):
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

smart_partial @= smart_partial  # noqa: E305
