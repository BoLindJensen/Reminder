'''
Zips lists [] into tuples ()

'''


monday =  [1, 2, 3, 4, 4, 8, 10, 12, 13, 9, 7, 6]
tuesday =  [4, 4, 5, 5, 6, 8, 10, 13, 10, 8, 6, 4]
wedensday = [2, 2, 4, 6, 9, 10, 11, 12, 10, 9, 8, 8]



for items in zip(monday, tuesday):
    print(items)



for temps in zip(monday, tuesday, wedensday):
    print("min = {:4.1f}, max={:4.1f}, average={:4.1f}".format(
        min(temps), max(temps), sum(temps)/len(temps)))