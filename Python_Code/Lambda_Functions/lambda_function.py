# Normal function(s)
def double(x):
    return x * 2

def trible(x):
    return x * 3

def remove_last_letter(string):
    return string[0:-1]


# Lambda function(s)
lambda_double = lambda x: x * 2
lambda_trible = lambda x: x * 3
remove_last_two_letters = lambda string: string[0:-2]


#Input
number = 5
string = "What!?"


#Output
print("Original Number:", number)
print("Double:", double(number))
print("Lambda Double:", lambda_double(number))
print("Trible:",trible(number))
print("Lambda Trible:",lambda_trible(number))

print("\n---\n")
print("Original String:", string)
print("Remove the last letter of a string using a function:", remove_last_letter(string))
print("Remove the last two letters using a Lambda function:", remove_last_two_letters(string))
