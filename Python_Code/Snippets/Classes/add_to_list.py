list_of_names = []

# Using a class
class PersonClass:
    def add_person(self, name, name_id=1):
        name_dic = {"name": name, "name_id": name_id}
        list_of_names.append(name_dic)
    pass

person_Instance = PersonClass()

person_Instance.add_person("Bo")  # Assigning a number is optional.
person_Instance.add_person("Lise", 123)


print(list_of_names)
