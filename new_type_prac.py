# NOTE: Occur a runtime error, "ImportError: cannot import name 'NewType'" in Python 3.5.0
# NOTE: But mypy says nothing (GOOD!)
import typing

WrapInt = typing.NewType("WrapInt", int)

def f1(wi: WrapInt) -> int:
    return wi # NOTE: automatically converted to int


print(f1(WrapInt(10)))
# print(f1(10))          # mypy error(GOOD!): error: Argument 1 to "f1" has incompatible type "int"; expected "WrapInt"