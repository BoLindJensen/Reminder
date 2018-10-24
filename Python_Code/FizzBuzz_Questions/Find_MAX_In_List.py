unorderd_list = [5, 1, 3, 3,3, 4, 7, 5, 6, 17, 8,8,8,8, 8, 7, 2, 9, 6,9 ,3,1]

ordered_list = set(unorderd_list)

maxvalue = 0
for element in unorderd_list:
    print(element)
    if element > maxvalue:
        maxvalue = element


print(f"Input List{unorderd_list}")
print(f"Max Value: {maxvalue}")


build_in_max_value = max(unorderd_list)
print(f"Showing build in max: {build_in_max_value}")

