#!/usr/bin/env python3
#shebang

'''
By Austin Bingham & Robert Smallshire
from http://sixty-north.com
austin@sixty_north.com

Retrieve and print words from a URL provided as an argument

Usage:
    python3 URLOpen.py <URL>

'''
# This script open a weppage, with a txt story spanning multiple lines, anc collects them in a list
import sys
from urllib.request import urlopen
# url = 'http://sixty-north.com/c/t.txt'

def fetch_words(url):
    """ Fetches a list of words form a URL

    :param
        url: The URL of the UTF-8 text document.
    :return:
        A list of strings containing the words from the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:

    #       line_words = line.split()  # Returnes 'Byte data'
            line_words = line.decode('utf-8').split()

            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    ''' Prints items one per line
    :param
        items: An iterable series of printable items.
    '''
    for item in items:
        print(item)


def main(url):
    ''' Print each word from a text document from a URL.
    :param
        url: The URL of a UTF-8 text document
    '''

    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1]) # The 0th arg is the module filename
    print("my name is: ", sys.argv[0])



'''
Python 3 source encoding is UTF-8
bytes is a sequence of bytes, str is a sequence of Unicode codepoints
bytes literals are prefixed with a lowercase b

Convert str to bytes with encode()
Convert bytes to str with decode()

'''
