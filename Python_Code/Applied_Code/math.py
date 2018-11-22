import math
from math import factorial

math.sqrt(81)


# Item picker
# number of items
n = 5
# keep on hand
k = 3


# Floating division
result = math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
print(type(result))
print(result)


# Integer division & direct use
result = factorial(n) // (factorial(k) * factorial(n-k))
print(type(result))
print(result)
