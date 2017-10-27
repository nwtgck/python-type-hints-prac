import typing

def f1(callable: typing.Callable[[int], str]) -> str:
    return callable(1)


# def f2(callable: typing.Callable[[int], str]) -> str:
#     return callable("hello") # mypy error(GOOD!): error: Argument 1 has incompatible type "str"; expected "int"

print(f1(lambda i: "hello"))

# print(f1(lambda i: 1.3))
# => mypy error(GOOD!):
# error: Argument 1 to "f1" has incompatible type "Callable[[int], float]"; expected "Callable[[int], str]"
# error: Incompatible return value type (got "float", expected "str")