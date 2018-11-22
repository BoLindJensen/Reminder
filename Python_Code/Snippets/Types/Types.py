

# Python build-in Collection types
# ---BEGIN ---


#  a String (homogenious immutable* sequences of Unicode codepoints)
#                     * cannot modify contents
my_string = "a text string"
print(type(my_string))
print(my_string)

my_multiline_string = """
multi 
line 
string
"""
print(my_multiline_string)

my_raw_string = r'c:\some\location\on\the\computer'
print(my_raw_string)

joinedString = ":".join(["What","a","String"])
print(joinedString)
print(joinedString.split(":"))



#  A Byte (Immutable sequence of bytes)
my_byte = b'data'
print(type(my_byte))
print(my_byte)


# A List (muteable sequence of objects)
my_list = [1,2,3]
print(type(my_list))
for item in my_list:
    print(item)

# A Tuple   (Heterogeneous immutable sequence of objects, cannot replace, remove or add once created)
my_tuple = (1 ,2, 3)
print(type(my_tuple))
for item in my_tuple:
    print(item)

# A Set
my_set = {1,2,3}
print(type(my_set))
for item in my_set:
    print(item)

# A Range arithmetic progression og integers
my_range = range(6)  # Stop - value  (number excluded)
print(type(my_range))
for number in my_range:
    print(number)


my_startStopRange = range(2,6) # Start, Stop  -values
print(type(my_startStopRange))
for number in my_startStopRange:
    print(number)


my_stepRange = range(2, 8, 2) # Start, Stop, Step  -values
print(type(my_stepRange))
for number in my_stepRange:
    print(number)


values = [1, 5, 10, 200, 40000]
for v in enumerate(values):
    print(v)
#using tuple unpacking
for i, v in enumerate(values):
    print("I= {}, V = {}".format(i, v))


# A Dictionary (mutable mapping of keys to values(associative array))
my_dict = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3',
            }

# Adding key value pair to dictionary
my_dict['key4'] = 'value4'

print(type(my_dict))
print(my_dict)

for item in my_dict:
   print(item , my_dict[item])


# Python Collection build-in types
# ---END ---


# Python Scalar build-in types
# ---BEGIN ---

# An signed Integer  (arbitrary precision integer)
my_int = 42
print(type(my_int))
print(my_int)

# a 64-bit floating point numbers
my_float = 4.2
print(type(my_float))
print(my_float)

# a Boolean logical value
my_bool = False
print(type(my_bool))
print(my_bool)

# a None type used for placeholders
my_nontype = None
print(my_nontype is None)
print(type(my_nontype))
print(my_nontype)

# Python Scalar build-in types
# ---END  ---
