
# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

# L3 returns all elements of L1 not in L2.

L1 = [1,2,6,8]
L2 = [2,3,5,8]

L3 = [x for x in L1 if x not in L2]
print(L3) #L3 will contain [1, 6].
