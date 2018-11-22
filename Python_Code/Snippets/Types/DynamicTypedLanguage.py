'''
Python is a "dynamic typed" language, which means that the type is figured out at runtime.
but it is also "strongly typed" which translates to you cannot match different types.

So the same "add()" function definition can be used for a multitude of things.
'''

def add(a, b):
    return a + b


if __name__ == '__main__':
    print(add(2, 3.2)) # int + float is ok

    try:
        print(add(2, "3.2")) # integer + string gives a TypeError
    except TypeError:
        print("Ups we got an TypeError (Strongly Typed remember)")

    print(add(2, 3)) # adding ints = 5
    print(add(4.33, 6.12)) # adding floats = 10.45
    print(add("water", "park")) # concatinating  strings to "waterpark"
    print(add([1, 4], [2, 33, 80])) # Concatinating lists to one list [1, 4, 2, 33, 80]

