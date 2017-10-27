
import typing

def f1(i2s_dict: typing.Dict[int, str], key: int) -> str:
    return i2s_dict[key]


print(f1({1: "apple", 2: "orange"}, 2))
# print(f1({1: "apple", 2: "orange"}, "hello")) # mypy error (GOOD!): error: Argument 2 to "f1" has incompatible type "str"; expected "int"
# print(f1({1: "apple", 2.0: "orange"}, 2))     # mypy error (GOOD!): error: Dict entry 1 has incompatible type "float": "str"; expected "int": "str"