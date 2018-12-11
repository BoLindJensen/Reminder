'''

with-block ia a resource cleanup method that can be used with context managers.
open() returns a context-manager



'''

import sys


def read_series(filename):
#    try:
#        f = open(filename, mode='rt', encoding='utf-8')
#        return [ int(line.strip()) for line in f]
#    finally:
#        f.close()

# becomes

    with open(filename, mode='rt', encoding='utf-8') as f:
        return [ int(line.strip()) for line in f]



def main(filename):
    series = read_series(filename)
    print(series)


if __name__ == '__main__':
    main(sys.argv[1])