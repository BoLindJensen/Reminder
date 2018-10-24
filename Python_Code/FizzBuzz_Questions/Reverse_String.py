some_string ="This_Is_A_String"
print(f"Input string: {some_string}")


# revers using python string opperation
reversestring = some_string[::-1]
print(f"Reverse string using build in python: {reversestring}")


# Build it yourselfe...
reverse_string = ""
length_of_string = len(some_string)
while length_of_string != 0:
    reverse_string = reverse_string + some_string[length_of_string-1]
    length_of_string -= 1

print(f"Reverse string build with own code: {reverse_string}")

