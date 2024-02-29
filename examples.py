from src.decotools.builtins import *
from src.decotools.applier import *
from src.decotools.itertools import *

10 @range @map.partial(lambda x: x + 1) @list @print
# without decorator: print(list(map(lambda x: x + 1, range(10))))

100 @range @map.partial(lambda x: x ** 2) @filter.partial(lambda x: x % 7 != 0) @list @str @bytes.partial(encoding="utf-8") @list @sum @print
# without decorator: print(sum(list(bytes(str(list(filter(lambda x: x % 7 != 0, map(lambda x: x ** 2, range(100))))), encoding="utf-8"))))

100 @range @list @map.partial(str) @decorator @" | ".join @print
# without decorator: print(" | ".join(map(str, list(range(100)))))
