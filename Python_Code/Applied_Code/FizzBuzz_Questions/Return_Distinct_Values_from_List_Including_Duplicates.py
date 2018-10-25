#Return distinct values from a list which includes duplicates
#  (i.e. "1 3 5 3 7 3 1 1 5" -> "1 3 5 7")
random_list = [1,3,5,3,7,3,1,1,5]

ordered_list = list(set(random_list))

print(f"Original List: {random_list}")
print(f"Ordered List using 'List(Set())': {ordered_list}")


another_ordered_list = []
duplicate_list = []

for element in random_list:
    if element not in another_ordered_list:
        another_ordered_list.append(element)

print(f"Ordered List using 'not in, for loop': {another_ordered_list}")
