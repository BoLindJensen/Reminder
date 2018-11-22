'''
Python does not have Variables but instead,
Named references to objects,
but it is ok to think of them as variables :)

name = object

ref_name =  1
ref_list = [1,2,3]
'''

a = [1, 2, 3] # list object given the name "a"
b = a       # the same list object given the name "b"
print(id(a))
print(id(b))

# Changing a will change b, and vice versa
print("A before ", a) # [1, 2, 3]
print("B before ", b) # [1, 2, 3]
a[2] = 12

print("A after ", a) # [1, 2, 12]
print("B after ", b) # [1, 2, 12]


print(a is a) # True
print(a is b) # True


print("\n")

p = [1,2,3]
q = [1,2,3]

print(id(p))
print(id(q))

print(p is p) # True
print(p is q) # False