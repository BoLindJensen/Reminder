# By using ''.join

list1 = ['1', 'A', '2', 'B','3','C']
str1 = ' '.join(list1)
print(f"str1: {str1}")


#Or if the list is of integers, convert the elements before joining them.
list2 = [1, 2, 3, '4', 'B']
str2 = ' '.join(str(e) for e in list2)
print(f"str2: {str2}")
