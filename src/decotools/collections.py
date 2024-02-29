from collections import (
    ChainMap,
    Counter,
    OrderedDict,
    UserDict,
    UserList,
    UserString,
    defaultdict,
    deque,
    namedtuple,
)

from .applier import decorator as _decorator

ChainMap @= _decorator
Counter @= _decorator
OrderedDict @= _decorator
UserDict @= _decorator
UserList @= _decorator
UserString @= _decorator
defaultdict @= _decorator
deque @= _decorator
namedtuple @= _decorator
