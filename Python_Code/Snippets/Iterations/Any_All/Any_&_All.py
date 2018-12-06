def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

print(any([False,True,False])) # True

print(all( (True,True,True) )) # True
print(all([False,False,False,True])) # False


print(any(is_prime(x) for x in range(100)))