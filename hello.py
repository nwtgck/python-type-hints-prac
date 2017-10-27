import numbers

def hello() -> str:
    "hello, world"


def add_int(a: int, b: int) -> int:
    return a + b

def add_float(a: float, b: float) -> float:
    return a + b

# (error: Unsupported left operand type for + ("Number"))
# def add_number(a: numbers.Number, b: numbers.Number) -> numbers.Number:
#     return a + b

print(hello())
print(add_int(1, 2))
# print(add_int(1, 2.0)) # mypy error: GOOD! (error: Argument 2 to "add_int" has incompatible type "float"; expected "int")

print(add_float(1, 2))   # No error
print(add_float(1, 2.0))