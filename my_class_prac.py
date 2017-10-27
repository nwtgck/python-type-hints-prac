class Person:
    def __init__(self, name: str, age: int) -> None: # NOTE: The return type of "__init__" must be None
        self.name = name
        self.age  = age


def f1(person: Person) -> int:
    return person.age


print(f1(Person(name="jack", age=4)))
# print(f1(1))                           # mypy error(GOOD!):  error: Argument 1 to "f1" has incompatible type "int"; expected "Person"
