#zip([1, 2, 3], [4, 6, 8])
# yields:
# [(1, 4), (2, 6), (3, 8)]

list1 = [1, 2, 3]
list2 = [4, 5, 6]
zipped = zip(list1, list2)

print(zipped)
for i in zipped:
    print(i)
