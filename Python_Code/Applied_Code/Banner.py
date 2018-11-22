

def banner(message, border = '-'):
    line = border * len(message)  # using the repetition operation and not a multiplier.
    print(line)
    print(message)
    print(line)



banner('Hello world')
banner('Hi Stars', '*')
banner(border ="/", message="This is a long message")