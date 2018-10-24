# Returns all elements of l1 not in l2.

li1 = [12,34,123]
li2 = [123, 12347]

#split the list elements into subelements / sub strings
for li2_index in li2:
    list_2_string = str(li2_index)
    list_2_string.split()

    print(list_2_string)
    print(f"Length of string: {len(list_2_string)}")

    split_list=[]
    for index in list_2_string:
        split_list.append(int(index))
        #print(index)

    print(f"Index {li2} Split List {split_list}")





l1 = [1,2,3,4,5,6,7,8,9]
l2 = [1,2,3,4,5,6,7,8]


#l1 = [1,3,6,8,9]
#l2 = [12,2,3,1,8]



l4 =[1,2,3,4,5,6,7,8,9]

l3 = [x for x in l1 if x not in l2]
# l3 will contain [1, 6].

numbers = ''
for item in l3:
    numbers= str(numbers) + str(item)
print(numbers)

# Apply the numbers string to index 1, remember to make it a int.
l4[0] = int(numbers)

l4[2] = 2222
print(l4)