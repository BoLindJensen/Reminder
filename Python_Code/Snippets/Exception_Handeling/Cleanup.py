'''
The "finally-block" is executed no matter how the Exception handler try-except block exits,
Thus having a finally block is usefull for cleaning up.
'''
import os
import sys

def make_dir_at(path, dir_name):
    '''
    Crates a directory at path, if mkdir fails to create dir_name, the program exits how it starts.
    aka. there are no unforeseen consequences, if an error is experinced in this try block.
    :param
        path: assign a path.
    :param
        dir_name: Specify a directory name, intended for creation.
    :return
        None
    '''
    original_path = os.getcwd()
    try:
        os.chdir(path)
        os.mkdir(dir_name)
    except OSError as e:
        print("Ups! Something went wrong")
        print(e, file=sys.stderr)
#        raise
    finally:
        os.chdir(original_path)

make_dir_at( "c:/" ,"woot2")

print("Program was executed fully")
