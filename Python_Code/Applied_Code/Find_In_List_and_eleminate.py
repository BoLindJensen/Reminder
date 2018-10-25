# Lists with no twins

list1 = [1,2,3,4,5,6,7,8,9]
list2 = [9,8,7,6,5,4,3,2,1]
list3 = [2,3,4,5,6,7,8,9,1]
list4 = [3,4,5,1,2,6,7,8,9]

# Twins lists

list5 = [12,12,1234,1234,5,6,7,8,9]
list6 = [1,2,34,34,4567,567,3678,89,89]   #works
list7 = [1,23,23,45,45,456,237,38,39]     #works
list8 = [19,129,3,14,5,6,7,89,19]

list10 = ['',123456789,37,45,45,123456,37,89,19]


# Actual work data
list9 = [4,6,8,2379,379,23,1,5,23]


def find_twins_in_list(input_list):
    saved_input_list = tuple(input_list)

    original_list = input_list
    twin_index_list = []
    twin_index_number_list = []

    for index_number1 in range(len(input_list)):
        # print(f" Index: {index_number1} and Number {input_list[index_number1]}")
        for index_number2 in range(index_number1 + 1, len(input_list)):
            #   print(f" Comparing index1: {index_number1} and index2: {index_number2}")
            #   print(f"BoxValue: {input_list[index_number1]}")
            #   print(f"BoxValue: {input_list[index_number2]}")

            if input_list[index_number1] == input_list[index_number2]:
                if len(str(input_list[index_number1])) == 2:
                    twin_index_list.append(index_number1)
                    twin_index_list.append(index_number2)

                    twin_index_number_list.append(input_list[index_number1])
                    twin_index_number_list.append(input_list[index_number2])

    # Twin number(s) but only, a single time.
    twin_index_number_list= list(set(twin_index_number_list))

    if len(twin_index_list) > 0:
        print(f"-- Twins found in --")
        print(f"Index  : {twin_index_list}")
        print(f"Number(s): {twin_index_number_list}")
    else:
        print("-- No twins found --")
    print(f"Original Input List: {original_list}")

    for index, value in enumerate(original_list):
        print(f" -- Index: {index} Value: {value} Value_Length: {len(str(value))}")
        if len(str(value)) <= 1:
            print("Ignore! (Len is to short")
        elif index not in twin_index_list:
                original_list[index] = shorten_element_in_list(twin_index_number_list, value)
        else:
            print(f"Ignore! Index \"{index}\" as it is a part of the twin_index_list")

    output_list = input_list
    print(f"Input List  : {list(saved_input_list)}")
    print(f"Output List : {output_list}")
    return output_list


def shorten_element_in_list(twin_value_list,a_value):
    # removes single values contained in the twin_value_list from the element.
    #print(f"Argument Twin Value:{twin_value_list}")
    #print(f"Argument value:{a_value}")
    twin_values_var = colapse_list_to_number(twin_value_list)

    l1 = []
    l1 = split_elements(a_value)
    l2 = []
    l2 = split_elements(twin_values_var)

    # l2 = split_elements(emptylist[0])    # FIX THIS only works on index 0 !!!

    #    l1 = [2, 3, 5, 8]
    #    l2 = [2, 3]
    l3 = [x for x in l1 if x not in l2]
    #print(f"List l1 {l1}")
    #print(f"List l2 {l2}")
    #print(f"List l3 {l3}")
    # l3        will        contain[5, 8].
    returnelement = []
    returnelement = colapse_list_to_number(l3)
    return returnelement


def list_2_string(somelist):
# Take a list and make it into a string
    list_2_string_var = ""
    for entity in somelist:
        list_2_string_var += str(entity)

    somelist = list_2_string_var
    return somelist


def colapse_list_to_number(somelist):
    # For each entity in a list, apply them to a temp string.
    tempstring = ""
    for entity in somelist:
        tempstring = tempstring + str(entity)

    #print(f"This is the to colapse_list_to_number function printing the tempstring: {tempstring}")

    # Make sure the string is made into an integer/number
    number = int(tempstring)
    return number


def split_elements(avalue):
    alist = []
    alist.append(avalue)

    # split the list elements into subelements / sub strings
    for li2_index in alist:
        list_2_string = str(li2_index)
        list_2_string.split()

        #print(list_2_string)
        #print(f"Length of string: {len(list_2_string)}")

        split_list = []
        for index in list_2_string:
            split_list.append(int(index))
            # print(index)

        #print(f"Input: {alist} Output: Split List{split_list}")

    return split_list



#find_twins_in_list(list1)
#find_twins_in_list(list5)
find_twins_in_list(list6)
#find_twins_in_list(list7)
#find_twins_in_list(list8)
#find_twins_in_list(list9)
#find_twins_in_list(list10)

