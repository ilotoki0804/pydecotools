from contextlib import suppress as _suppress

from .applier import decorator as _decorator


with _suppress(NameError):
    anext @= _decorator  # type: ignore
    aiter @= _decorator  # type: ignore

abs @= _decorator
all @= _decorator
any @= _decorator
ascii @= _decorator
bin @= _decorator
bool @= _decorator
breakpoint @= _decorator
bytearray @= _decorator
bytes @= _decorator
callable @= _decorator
chr @= _decorator
classmethod @= _decorator
compile @= _decorator
complex @= _decorator
delattr @= _decorator
dict @= _decorator
dir @= _decorator
divmod @= _decorator
enumerate @= _decorator
eval @= _decorator
exec @= _decorator
filter @= _decorator
float @= _decorator
format @= _decorator
frozenset @= _decorator
getattr @= _decorator
globals @= _decorator
hasattr @= _decorator
hash @= _decorator
help @= _decorator
hex @= _decorator
id @= _decorator
input @= _decorator
int @= _decorator
isinstance @= _decorator
issubclass @= _decorator
iter @= _decorator
len @= _decorator
list @= _decorator
locals @= _decorator
map @= _decorator
max @= _decorator
memoryview @= _decorator
min @= _decorator
next @= _decorator
object @= _decorator
oct @= _decorator
open @= _decorator
ord @= _decorator
pow @= _decorator
print @= _decorator
property @= _decorator
range @= _decorator
repr @= _decorator
reversed @= _decorator
round @= _decorator
set @= _decorator
setattr @= _decorator
slice @= _decorator
sorted @= _decorator
staticmethod @= _decorator
str @= _decorator
sum @= _decorator
super @= _decorator
tuple @= _decorator
type @= _decorator
vars @= _decorator
zip @= _decorator
