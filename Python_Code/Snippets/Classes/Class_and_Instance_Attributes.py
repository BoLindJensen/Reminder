list_of_names = []


class PersonClass:
    # Class attributes are defined here.
    #Static variables in python are outside class methods, but inside the class
    #Static variable are the same across all class instances.
    race = "Human"
    country = "Denmark"


      #Constructor
    def __init__(self, name, age=0, name_id=1):

        #instance atributes, availabe to all class methods()  eg. using self.name
        self.name = name
        self.age = age
        self.name_id = name_id

        list_of_names.append(self)


    # Special Attribute to make printing john return the classname. Without it a memory location is returned
    def __str__(self):
        return "PersonClass " + self.name

    # using instance variables
    def get_name_capitalized(self):
        return self.name.capitalize()


    # Using static variable
    def get_race(self):
        return self.race


    def get_race(self):
        return self.race


# Creating different instances of the same class
bo = PersonClass("Bo")
peter = PersonClass("peter ", 32)


# Calling using instancing
print(bo.get_name_capitalized())
print(bo.get_race())

print(peter.get_name_capitalized())
print(peter.get_race())

# Calling class attributes directly without instancing
print(PersonClass.race)


#print("woot",john.get_name_capitalized())

#print(list_of_names)
