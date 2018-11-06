from Package.personModule import PersonClass
from .namesModule import *



# Inherit / derive functionality from original class using () after your new class
# So DerivedClass(Parrent)
class ProgrammerClass(PersonClass):

    def __init__(self, name, twc = 0, age=2, name_id=1):

        self.name = name
        self.age = age
        self.name_id = name_id
        self.time_with_company = twc

        list_of_names.append(self)

    # Overwrite variable
    jobstatus = "Programmer"

    # Define new variable
#    timeWithCompany = "10 months"
    happy = True


    # Define new methods(functionality)
    def get_jobstatus(self):
        return self.jobstatus + ", been with the company for " + str(self.time_with_company) + "."

    def is_happy(self):
        return "Is happy: " + str(self.happy) + ""

    #Polymorphism, take the old and add on to it
    def get_age(self):
        #              = parrentclass . method()
        original_value = super().get_age()
        computerYearFactor = 19
        return str(original_value * computerYearFactor) + " computer years"


   # Overwriting a function
    def get_country(self):
        return "Country has no meaning to a programmer, cyberspace is the place to be."

