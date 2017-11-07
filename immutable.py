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

#error about tuples
my_tuple = (1, [1,2])

my_tuple[1] =+ [3,4]  #this will raise an error
#however the value of my_tuple is still changed...