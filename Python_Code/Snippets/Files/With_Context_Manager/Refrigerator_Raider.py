
from contextlib import closing  # used as a wrapper for context managers

class RefrigeratorRaider:
    '''Raids a refrigerator'''

    def open(self):
        print("Open fridge door.")

    def take(self, food):
        print(f"Finding {food}")
        if food == 'pizza':
            raise RuntimeError("Health Warning!")
        print(f"Taking {food}")

    def close(self):
        print("Closing fridge door.")


def raid(food):
    with closing(RefrigeratorRaider()) as r:        # Get the class into r
        r.open()
        r.take(food)

    #r.close()


raid("milk")

print("---")

raid("pizza")
