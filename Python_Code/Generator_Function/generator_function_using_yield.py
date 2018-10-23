names = []

def read_file(): # Normal function using custom generator function.
    try:
        f = open("names.txt" , "r")
#       instead of using the build in generator .readlines() we create our own, for fun.
        #  for student in f.readlines():

        # To keep getting new results a for loop is needed
        for name in read_students(f):
            names.append(name)
        f.close()
    except Exception:
        print("Error: Cannot read file")


def read_students(f): # Generator function.
    for line in f:
        yield line


read_file()
print(names)
