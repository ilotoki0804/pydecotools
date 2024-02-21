from src.decotools.builtins import *
from src.decotools.applier import decorator

10 @range @map(lambda x: x + 1) @list @print
# without decorator: print(list(map(lambda x: x + 1, range(10))))

100 @range @map(lambda x: x ** 2) @filter(lambda x: x % 7 != 0) @list @str @bytes(encoding="utf-8") @list @sum @print
# without decorator: print(sum(list(bytes(str(list(filter(lambda x: x % 7 != 0, map(lambda x: x ** 2, range(100))))), encoding="utf-8"))))

100 @range @list @map(str) @decorator @" | ".join @print
# withoud decorator: print("|".join(map(str, list(range(100)))))
