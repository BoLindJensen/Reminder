list_of_names = []


class PersonClass:
      #Constructor
    def __init__(self, name, name_id=1):
        name_dic = {"name": name, "name_id": name_id}
        list_of_names.append(name_dic)

    # Special Attribute to make printing john return the classname. Without it a memory location is returned
    def __str__(self):
        return "PersonClass"


john = PersonClass("John")

print(john)

#print(list_of_names)
