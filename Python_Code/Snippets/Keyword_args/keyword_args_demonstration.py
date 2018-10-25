def simple_var_args(name, *args):
    print("I am demonstrating a 'Simple Argument List' ")
    print(name)
    print(args)

simple_var_args("Bo Jensen", "Loves pythons", None, 2 , True, "False")


print("\n----\n")

def keyword_var_args(name, **kwargs):
    print("I Am demonstrating 'Keyword Arguments' ")
    print(name)
    print(kwargs["description"],kwargs["address"],kwargs["country"],kwargs["udacity_subscriber"] )


keyword_var_args("Bo Jensen", country="Denmark", address="Vestre Alle", description="Super Cool Guy",udacity_subscriber=True , random="Not added")
