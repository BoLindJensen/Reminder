'''
The function open() opens a file.

file: path to file (required)
mode: read/write/append,  binary/text
encoding: text encoding eg. utf-8. It is a good idea to always specify this, as you never know what other file systems use as their default

Modes:
'r' Read
'w' Write
'x' eXclusive creation, fails if the file already exists.
'a' Append to the file if it exists.
'b' Binary mode
't' Text mode (Default)
'+' open a disk file for updating(reading and writing)
'U' Universal new lines mode(legasy code)

check:
http://docs.python.org/3/library/codecs.html#standard-encodings


'''

import sys
print(sys.getdefaultencoding())

my_filename = "text.txt"


# Make the file
f = open(my_filename , mode='wt', encoding ='utf-8')
#print(help(f))

# Write something into the file
f.write("This is a long message,")
f.write(" that continues. \n")
f.write("Now it ends.")
f.close()
#print(f)

# Open a file
g = open(my_filename, mode= 'rt', encoding= 'utf-8')
# Read 16 chars of the file
print(g.read(16))
# Read everything from last read
print(g.read())
print(g.read()) # no more information in file.

print(g.seek(0)) # return cartridge to 0

print(g.readline())
print(g.readline())

print(g.seek(0)) # return cartridge to 0
print(g.readlines()) # Give a list


g.close() # and we are done with the file

# append to a file.
h = open(my_filename, mode= 'at', encoding= 'utf-8')

h.writelines(
    ['\n'
     'Added lines \n'
     'Remember the newlines character, '
     'if you need it \n' 
     '...'])
h.close()




