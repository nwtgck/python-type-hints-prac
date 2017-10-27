import typing

def f1(i_or_s: typing.Union[int, str]) -> bool:
    return type(i_or_s) == int


def f2(i_or_s_or_f: typing.Union[int, str, float]) -> bool:
    return type(i_or_s_or_f) == int

print(f1(1))
print(f1("hello"))
# print(f1(1.2))     # mypy error (GOOD!): error: Argument 1 to "f1" has incompatible type "float"; expected "Union[int, str]"



print(f2(1))
print(f2("hello"))
print(f2(1.2))
print(f2(True))                        # no error (NOT GOOD)
# print(f2({1: "apple", 2: "orange"})) # mypy error (GOOD!): error: Argument 1 to "f2" has incompatible type "Dict[int, str]"; expected "Union[int, str, float]"