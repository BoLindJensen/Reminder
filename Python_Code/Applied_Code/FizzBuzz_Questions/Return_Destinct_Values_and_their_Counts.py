# Return distinct values and their counts (
# (i.e. "1 3 5 3 7 3 1 1 5" -> "1 3 5 7")
# i.e. the list above becomes "1(3) 3(3) 5(2) 7(1)")
from collections import Counter
original_list = [1, 3, 5, 3, 7, 3, 1, 1, 5]
print(f"Original list: {original_list}")


#Find using build in functions Counter()
print(f"Using build in functions {Counter(original_list)}")

#Find using list comprehension
dictionary = dict((x,original_list.count(x)) for x in original_list)
print(f"List Comprehension: {dictionary}")

#Find using loop
counted_list = {}
for element in original_list:
    if element in counted_list:
        counted_list[element] = counted_list[element] + 1
    else:
        counted_list[element] = 1

print(f"Found using for loop: {counted_list}")


   # if element not in new_list:
    #    new_list.append(element)


#def occurDict(items):
#    d = {}
#    for i in items:
#        if i in d:
#            d[i] = d[i]+1
#        else:
#            d[i] = 1
#    return d

#print(occurDict([1,2,3,4,1,1]))


#Given a string of expressions (only variables, +, and -) and a set of variable/value pairs (i.e. a=1, b=7, c=3, d=14) return the result of the expression ("a + b+c -d" would be -3).