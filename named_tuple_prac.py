import typing

# NOTE: Use 3.6.3 to use syntax bellow
# class Person(typing.NamedTuple):
#     name: str
#     age : int


Person = typing.NamedTuple("Person", [('name', str), ('age', int)]) # (from: https://stackoverflow.com/a/34269877/2885946)


def f1(person: Person) -> int:
    return person.age

def f2(i: int) -> None:
    pass


person = Person(name="jack", age=4)
print(f1(person))
# print(f1(2)) # mypy error(GOOD!): error: Argument 1 to "f1" has incompatible type "int"; expected "Person"


f2(person.age)