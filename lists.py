# Summary of Lists

#Lists are sequences, supports all sequences operations
L = [123, 'spam', 1.23] # three different-type objects
print(len(L))

print(L[0])
print(L[:-1]) # slicing a list returns a new list

L + [4, 5, 6]
L * 2

L.append('NI')
L.pop(2) # delete item in the middle, and return it
del L[1] # also works

# Lists are more powerful than arrays in other languages
# List don't have type constraints and they have no fixed size


# L[99] Error, can't reference items that aren't present

M = ['aa', 'cc', 'dd', 'bb']
M.sort()
M.reverse()

# Code can span lines if bracketed
M = [[1,2,3],
    [4,5,6,],
    [7,8,9]]

M[1] # get row 2
M[1][2] # get row 2 then item 3 within the row

# List comprehension
col2 = [row[1] for row in M] # Collect the items in column 2
# More specific: "Give me row[1] for each row in matrix M, in a new list
print(col2) # this prints [2, 5, 8]

[row[1] + 1 for row in M] # Add 1 to each item in column 2

[row[1] for row in M if row[1] % 2 == 0] # filter out odd items in column 2

list(range(4)) # [0, 1, 2, 3]
list(range(-6, 7, 2)) # -6 to +6 in 2

[[x ** 2, x ** 3] for x in range(4)] # [square, cube] for 0, 1, 2, 3
[[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0]

