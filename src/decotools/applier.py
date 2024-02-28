from __future__ import annotations

from typing import Callable, TypeVar, Generic

_T, _U, _V, _W = TypeVar("_T"), TypeVar("_U"), TypeVar("_V"), TypeVar("_W")


class DecoratorOperatorMeta(type):
    def __matmul__(cls, other):
        return other(cls)

    def __rmatmul__(cls, other):
        return cls(other)


class decorator(Generic[_T, _U, _V, _W], metaclass=DecoratorOperatorMeta):
    """A decorator for implementing decorator operator."""

    def __init__(self, function_or_object: Callable[[_U], _T] | _W) -> None:
        self.target = function_or_object

    def __call__(self, *args, **kwargs) -> _T:  # noqa: F811
        if not callable(self.target):
            raise TypeError(f"'{type(self.target)}' object is not callable")
        return self.target(*args, **kwargs)

    def __matmul__(self, other: Callable[[Callable[[_U], _T] | _W], _V]) -> _V:
        """__matmul__ is not needed if pipeline implementation is being default.

        ```python
        pipeline_func @ no_pipeline_func
        ==> no_pipeline_func(pipeline_func)
        ```
        """
        return other(self.target)

    def __rmatmul__(self, other: _U) -> _T:
        """
        ```python
        argument @ pipeline_func
        ==> pipeline_func(argument)
        ```
        """
        assert callable(self.target), "The target must be callable."
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
