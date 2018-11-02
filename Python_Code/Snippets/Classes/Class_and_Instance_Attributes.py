list_of_names = []


class PersonClass:
    # Class attributes are defined here.
    # Static variables in python are outside class methods, but inside the class
    # Static variable are the same across all class instances.
    race = "Human"
    country = "Denmark"


    # Constructor
    def __init__(self, name, age=0, name_id=1):

        #instance atributes, availabe to all class methods()  eg. using self.name
        self.name = name
        self.age = age
        self.name_id = name_id

        list_of_names.append(self)


    # Special Attribute to make printing john return the classname. Without it a memory location is returned
    def __str__(self):
        return "PersonClass " + self.name

    #user made up methods()
    # Using instance variables
    def get_name_capitalized(self):
        return self.name.capitalize()


    def get_age(self):
        return self.age


    # Using static variable
    def get_race(self):
        return self.race


    def get_country(self):
        return self.country


# Creating different instances of the same class
bo = PersonClass("Bo")
peter = PersonClass("peter", 32)


# Calling attributes using instancing.
print("Calling using instancing:")
print(bo.get_name_capitalized() + " is " + bo.get_race())
print(peter.get_name_capitalized() + " is " + peter.get_race())

# Calling class attributes directly.
print("\nCalling class attributes 'race' directly without instancing anything:")
print(PersonClass.race)

# Change it.
print("\nChange PersonClass.race:")
PersonClass.race = "Alien"
print(PersonClass.race)
