unorderd_list = [5, 1, 3, 3,3, 4, 7, 5, 6, -17, 8,8,8,-18, 8, 7, 2, 9, 6,9 ,3,1]
print(f"Input List{unorderd_list}")


ordered_list = set(unorderd_list)
minvalue = 100000

for element in ordered_list:
    print(element)
    if element < minvalue:
        print(f"Assigning new Min: {element} Replacing: {minvalue}")
        minvalue = element


print("\n----\n")
print(f"Min Value found using own method : {minvalue}")

build_in_min_value = min(unorderd_list)
print(f"Using Python Build-in function: {build_in_min_value}")

