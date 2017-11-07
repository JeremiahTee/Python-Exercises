#Write a program that creates a dictionary with 10 keys: 2,3,5,7,11,13,17,19,23,29
#Value of each key should be a list of the numbers between 1 and 1000 that are divisible by it

keys = [2,3,5,7,11,13,17,19,23,29]
dictionary = {}

for key in keys:
    new_list = []
    for i in range(1,1001):
        if i % key == 0:
            new_list.append(i)
    dictionary[key] = new_list

for key in dictionary:
    print(str(key) + " : " + str(dictionary[key]))