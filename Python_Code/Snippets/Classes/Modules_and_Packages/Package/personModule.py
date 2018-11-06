from .namesModule import *


# Original Class
class PersonClass:
    race = "Human"
    country = "Denmark"
    jobstatus = "No job"

    def __init__(self, name, age=2, name_id=1):

        self.name = name
        self.age = age
        self.name_id = name_id

        list_of_names.append(self)

    def __str__(self):
        return "PersonClass " + self.name

    def get_name_capitalized(self):
        return self.name.capitalize()

    def get_age(self):
        return self.age

    def get_race(self):
        return self.race

    def get_country(self):
        return self.country

