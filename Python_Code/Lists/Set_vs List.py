# Set are unique and ordered
s = set()
s.add(2)
s.add(4)
s.add(4)
s.add(5)
s.add(2)
s.add(1)
print(s)
s.pop()
print(s)

print("---")

# List are muteable, and contain just what you put in em in that order
l = []
l.append(1)
l.append(2)
l.append(5)
l.append(6)
l.append(1)
print(l)
l.pop(2) # pop Index 2 (Value 5)
print(l)
l[2] = 33
print(l)









