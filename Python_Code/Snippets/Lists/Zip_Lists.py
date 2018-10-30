#zip([1, 2, 3], [4, 6, 8])
# yields:
# [(1, 4), (2, 6), (3, 8)]

list1 = [1, 2, 3]
list2 = [4, 5, 6]
zipped = zip(list1, list2)

#zip() is an iterator
print(zipped) # gives the memory locatin
print("First time", list(zipped)) #exhaustes the iterator
print("again", list(zipped)) # is now empty

for i in zipped:
    print("zipped1 is not shown:" ,i)


zipped2 = zip(list1, list2)
# Exhasustes the zipped2
for i in zipped2:
    print("zipped2: ",i)

# Is now empty
for i in zipped2:
    print("zipped2: ",i)
