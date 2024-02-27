from contextlib import suppress as _suppress

from .applier import smart_partial as _smart_partial


with _suppress(NameError):
    anext @= _smart_partial  # type: ignore
    aiter @= _smart_partial  # type: ignore

abs @= _smart_partial
all @= _smart_partial
any @= _smart_partial
ascii @= _smart_partial
bin @= _smart_partial
bool @= _smart_partial
breakpoint @= _smart_partial
bytearray @= _smart_partial
bytes @= _smart_partial
callable @= _smart_partial
chr @= _smart_partial
classmethod @= _smart_partial
compile @= _smart_partial
complex @= _smart_partial
delattr @= _smart_partial
dict @= _smart_partial
dir @= _smart_partial
divmod @= _smart_partial
enumerate @= _smart_partial
eval @= _smart_partial
exec @= _smart_partial
filter @= _smart_partial
float @= _smart_partial
format @= _smart_partial
frozenset @= _smart_partial
getattr @= _smart_partial
globals @= _smart_partial
hasattr @= _smart_partial
hash @= _smart_partial
help @= _smart_partial
hex @= _smart_partial
id @= _smart_partial
input @= _smart_partial
int @= _smart_partial
isinstance @= _smart_partial
issubclass @= _smart_partial
iter @= _smart_partial
len @= _smart_partial
list @= _smart_partial
locals @= _smart_partial
map @= _smart_partial
max @= _smart_partial
memoryview @= _smart_partial
min @= _smart_partial
next @= _smart_partial
object @= _smart_partial
oct @= _smart_partial
open @= _smart_partial
ord @= _smart_partial
pow @= _smart_partial
print @= _smart_partial
property @= _smart_partial
range @= _smart_partial
repr @= _smart_partial
reversed @= _smart_partial
round @= _smart_partial
set @= _smart_partial
setattr @= _smart_partial
slice @= _smart_partial
sorted @= _smart_partial
staticmethod @= _smart_partial
str @= _smart_partial
sum @= _smart_partial
super @= _smart_partial
tuple @= _smart_partial
type @= _smart_partial
vars @= _smart_partial
zip @= _smart_partial
