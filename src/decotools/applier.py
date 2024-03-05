from __future__ import annotations

from typing import Any, Callable, TypeVar, Generic

_TargetReturn = TypeVar("_TargetReturn")
_TargetInput = TypeVar("_TargetInput")
_OtherReturn = TypeVar("_OtherReturn")
_T = TypeVar("_T")


class DecoratorMeta(type):
    """Make classes decoratable."""

    def __matmul__(cls: type[_T], other) -> _T:
        return other(cls)

    def __rmatmul__(cls: type[_T], other) -> _T:
        return cls(other)

    def partial(cls: type[_T], *args, **kwargs) -> decorator[Any, _T, Any]:
        @decorator
        def inner(*inner_args, **inner_kwargs) -> _T:
            return cls(*args, *inner_args, **kwargs, **inner_kwargs)
        return inner

    def supply(cls: type[_T], *args, **kwargs) -> decorator[Any, _T, Any]:
        @decorator
        def inner(*inner_args, **inner_kwargs) -> _T:
            return cls(*inner_args, *args, **kwargs, **inner_kwargs)
        return inner


class Decorator(metaclass=DecoratorMeta):
    def __matmul__(self, other):
        return other(self)

    def __rmatmul__(self, other):
        return self(other)  # type: ignore

    def partial(self, *args, **kwargs):
        @decorator
        def inner(*inner_args, **inner_kwargs):
            return self(*args, *inner_args, **kwargs, **inner_kwargs)  # type: ignore
        return inner

    def supply(self, *args, **kwargs):
        @decorator
        def inner(*inner_args, **inner_kwargs):
            return self(*inner_args, *args, **kwargs, **inner_kwargs)  # type: ignore
        return inner


class decorator(Generic[_TargetInput, _TargetReturn, _OtherReturn], metaclass=DecoratorMeta):
    """A decorator for implementing decorator operator."""

    def __init__(self, func: Callable[[_TargetInput], _TargetReturn] | Callable[..., _TargetReturn]) -> None:
        self.target = func

    def __call__(self, *args, **kwargs) -> _TargetReturn:  # noqa: F811
        return self.target(*args, **kwargs)

    def __matmul__(
        self,
        other: Callable[[Callable[[_TargetInput], _TargetReturn] | Callable[..., _TargetReturn]], _OtherReturn]
    ) -> _OtherReturn:
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

    def supply(self, *args, **kwargs):
        @decorator
        def inner(*inner_args, **inner_kwargs):
            return self.target(*inner_args, *args, **kwargs, **inner_kwargs)
        return inner


@decorator
def decorator_flow(func: Callable[..., _TargetReturn]):
    """Make a function which not designed for decorators follow the decorator flow."""
    @decorator
    def wrapper(*args, **kwargs):
        @decorator
        def inner(*inner_args, **inner_kwargs):
            return func(*args, *inner_args, **kwargs, **inner_kwargs)
        return inner
    return wrapper


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
