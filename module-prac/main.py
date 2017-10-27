import my_mod

print(my_mod.my_func("hello"))
# print(my_mod.my_func(1.3))     # mypy error GOOD!: (error: Argument 1 to "my_func" has incompatible type "float"; expected "str")