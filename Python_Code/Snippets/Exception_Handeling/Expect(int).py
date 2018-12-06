'''
A module for demonstrating exceptions.
'''

import sys


def convertToInt(user_Input):
    '''   Convert input to an Integer.
    :param
        input: Integers.
    :return:
        "Intified values" when valid or "-1" for exceptions.
    '''

    x = -1
    try:
        x = int(user_Input)
        print(f"Conversion complete: {user_Input}")
    except(ValueError, TypeError) as error:
        print(f"Conversion failed for: {user_Input}")
        print(f"Error message: {error}", file=sys.stderr)
#       Alternative way
#       print("error {}".format(str(error)), file=sys.stderr)
    return user_Input

convertToInt("42")                      # Works.
convertToInt("Sam was holding the cup") # Works; Exception caught as ValueError
convertToInt([3,4,5])                   # Works; Exception caught as TypeError but bad form to do so in python.
# convertToInt([[1,2,3][3,4,5]])          # Does NOT work; Exception identified but not caught as a TypeError
