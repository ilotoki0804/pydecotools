# sourcery skip: avoid-builtin-shadow
from contextlib import suppress as _suppress
import builtins

from .applier import decorator as _decorator, DecoratorMeta as _DecoratorMeta


with _suppress(NameError):
    anext = _decorator(builtins.anext)  # type: ignore
    aiter = _decorator(builtins.aiter)  # type: ignore

# classes
class list(builtins.list, metaclass=_DecoratorMeta):
    pass
class bytearray(builtins.bytearray, metaclass=_DecoratorMeta):
    pass
class bytes(builtins.bytes, metaclass=_DecoratorMeta):
    pass
class classmethod(builtins.classmethod, metaclass=_DecoratorMeta):
    pass
class complex(builtins.complex, metaclass=_DecoratorMeta):
    pass
class dict(builtins.dict, metaclass=_DecoratorMeta):
    pass
class enumerate(builtins.enumerate, metaclass=_DecoratorMeta):
    pass
class filter(builtins.filter, metaclass=_DecoratorMeta):
    pass
class float(builtins.float, metaclass=_DecoratorMeta):
    pass
class frozenset(builtins.frozenset, metaclass=_DecoratorMeta):
    pass
class int(builtins.int, metaclass=_DecoratorMeta):
    pass
class map(builtins.map, metaclass=_DecoratorMeta):
    pass
class object(builtins.object, metaclass=_DecoratorMeta):
    pass
class property(builtins.property, metaclass=_DecoratorMeta):
    pass
class reversed(builtins.reversed, metaclass=_DecoratorMeta):
    pass
class set(builtins.set, metaclass=_DecoratorMeta):
    pass
class staticmethod(builtins.staticmethod, metaclass=_DecoratorMeta):
    pass
class str(builtins.str, metaclass=_DecoratorMeta):
    pass
class super(builtins.super, metaclass=_DecoratorMeta):
    pass
class tuple(builtins.tuple, metaclass=_DecoratorMeta):
    pass
class type(builtins.type, metaclass=_DecoratorMeta):
    pass
class zip(builtins.zip, metaclass=_DecoratorMeta):
    pass

# classes cannot be subclassed
bool = _decorator(builtins.bool)
memoryview = _decorator(builtins.memoryview)
range = _decorator(builtins.range)
slice = _decorator(builtins.slice)

# functions
abs = _decorator(builtins.abs)
all = _decorator(builtins.all)
any = _decorator(builtins.any)
ascii = _decorator(builtins.ascii)
bin = _decorator(builtins.bin)
breakpoint = _decorator(builtins.breakpoint)
callable = _decorator(builtins.callable)
chr = _decorator(builtins.chr)
compile = _decorator(builtins.compile)
delattr = _decorator(builtins.delattr)
dir = _decorator(builtins.dir)
divmod = _decorator(builtins.divmod)
eval = _decorator(builtins.eval)
exec = _decorator(builtins.exec)
format = _decorator(builtins.format)
getattr = _decorator(builtins.getattr)
globals = _decorator(builtins.globals)
hasattr = _decorator(builtins.hasattr)
hash = _decorator(builtins.hash)
help = _decorator(builtins.help)
hex = _decorator(builtins.hex)
id = _decorator(builtins.id)
input = _decorator(builtins.input)
isinstance = _decorator(builtins.isinstance)
issubclass = _decorator(builtins.issubclass)
iter = _decorator(builtins.iter)
len = _decorator(builtins.len)
locals = _decorator(builtins.locals)
max = _decorator(builtins.max)
min = _decorator(builtins.min)
next = _decorator(builtins.next)
oct = _decorator(builtins.oct)
open = _decorator(builtins.open)
ord = _decorator(builtins.ord)
pow = _decorator(builtins.pow)
print = _decorator(builtins.print)
repr = _decorator(builtins.repr)
round = _decorator(builtins.round)
setattr = _decorator(builtins.setattr)
sorted = _decorator(builtins.sorted)
sum = _decorator(builtins.sum)
vars = _decorator(builtins.vars)
