from src.decotools.builtins import *
from src.decotools.applier import *
from src.decotools.itertools import *
from src.decotools.utilities import *


print(10 @range @map.partial(lambda x: x + 1) @list)
# without decorator:
print(list(map(lambda x: x + 1, range(10))))


print(
    100
    @range
    @map.partial(lambda x: x ** 2)
    @filter.partial(lambda x: x % 7 != 0)
    @list
    @str
    @bytes.partial(encoding="utf-8")
    @list
    @sum
)
# without decorator:
print(sum(list(bytes(str(list(filter(lambda x: x % 7 != 0, map(lambda x: x ** 2, range(100))))), encoding="utf-8"))))


print(
    100
    @range
    @list
    @map.partial(str)
    @decorator(" | ".join)
)
# without decorator:
print(" | ".join(map(str, list(range(100)))))


class CallableClass(Decorator):
    def __init__(self, prevalue, value):
        self.value = value

    def print(self):
        print(self.value)

    def __call__(self, arg):
        print(self.value, arg)

callableobj = "hello" @CallableClass.partial("prevalue")
"printit" @callableobj

print("hello world" @getattr.supply("split") @call())
print(["hello", "world"] @decorator(chain.from_iterable) @decorator("".join))  # type: ignore
