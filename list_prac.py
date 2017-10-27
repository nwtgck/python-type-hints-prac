import typing

def f1(float_list: typing.List[float]) -> float:
    return float_list[0]


print(f1([1.0, 2.3, 8.0]))
# print(f1("hello"))         # mypy error (GOOD!): error: Argument 1 to "f1" has incompatible type "str"; expected "List[float]"