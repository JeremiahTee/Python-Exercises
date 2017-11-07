"""
mutable: list, dict, set

immutable: int str tuple
"""

x = "Hello, "
print(id(x))
x += "word"
print(id(x))
print('They are different strings; therefore, different memory addresses')

print()

list = [1,2,3]
print(id(x))
list += [4,5,6]

print(list)
print(id(x))

print('Lists are \'immutable\'. After adding elements to the list, list has same address')