
value = 5

print("Type a number divisible by ", value, " to end the loop")

while True:
    respons = input()
    if int(respons) % value == 0:

        print(respons, " is divisible by ", value)
        print("Exiting while loop")

        break
    else:
        print(respons, " is not divisible by ", value)


print("-- End of looping program 7 --")