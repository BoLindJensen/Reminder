'''

Showing the functionality of packages and modules

'''


from Package import programmerModule as pm

#from Package.programmerModule import ProgrammerClass
#could do #from .programmer import *
# to import every class from file


martin = pm.ProgrammerClass("martin", "1 Month", 30, 2)
print(martin.get_name_capitalized())
print(martin.get_jobstatus())
print(martin.is_happy())
print(martin.get_country())
print(martin.get_age())