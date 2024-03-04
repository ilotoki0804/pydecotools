from __future__ import annotations

from contextlib import suppress as _suppress
from itertools import (
    count,
    cycle,
    repeat,
    accumulate,
    chain as _chain,
    compress,
    dropwhile,
    filterfalse,
    groupby,
    islice as _islice,
    starmap,
    takewhile,
    tee,
    zip_longest,
    product,
    permutations,
    combinations,
    combinations_with_replacement,
)

from .applier import (
    decorator as _decorator,
    DecoratorMeta as _DecoratorMeta,
)


class chain(_chain, metaclass=_DecoratorMeta):
    pass


chain.from_iterable @= _decorator


@_decorator
def islice(*args):
    @_decorator
    def wrapper(iterable):
        return _islice(iterable, *args)
    return wrapper


count @= _decorator
cycle @= _decorator
repeat @= _decorator
accumulate @= _decorator
compress @= _decorator
dropwhile @= _decorator
filterfalse @= _decorator
groupby @= _decorator
starmap @= _decorator
takewhile @= _decorator
tee @= _decorator
zip_longest @= _decorator
product @= _decorator
permutations @= _decorator
combinations @= _decorator
combinations_with_replacement @= _decorator

with _suppress(ImportError):
    from itertools import pairwise  # type: ignore
    pairwise @= _decorator

with _suppress(ImportError):
    from itertools import batched  # type: ignore
    batched @= _decorator
