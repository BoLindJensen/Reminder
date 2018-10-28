class EmptyClass:
    #This class does nothing
    pass


# These two instance of the same class are different form each other.

instance1 = EmptyClass()
print(instance1)

instance2 = EmptyClass()
print(instance2)

# Run and look at the memory allocation.
# Ergo; two(or more) instance of the same class are independant from each other
