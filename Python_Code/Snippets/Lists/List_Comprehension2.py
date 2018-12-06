'''
Python Comprehension works on list[], set{}, dictionaries{key:value}

List Comprehension style is Declarative and Functional
it is readable, expressive, and effective.

[ expr(item) for item in items ]
[ expr(item) for item in iterable ]
[ expr(item) for item in iterable if predicate(item) ]

'''

words = "What is this list comprehension i hear so much about, what can it help me with?"
words_list = words.split()

# This List comprehension

print([len(word) for word in words_list])

# Is the same as this foreach loop.

word_lengths = []
for word in words_list:
    word_lengths.append(len(word))

print(word_lengths)



from math import sqrt
def is_prime(x):
    if x < 2:
        return False
    for i in range(2,int(sqrt(x)) +1):
        if x % i == 0:
            return False
        return True

print([x for x in range(101)])

print("Using is_prime() function as optional filter clause")
print([x for x in range(101) if is_prime(x)])
