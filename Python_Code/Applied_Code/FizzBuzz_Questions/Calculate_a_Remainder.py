# inputs  (numerator and denominator)

def show_remainder(numerator, denominator):
    remainder = numerator % denominator

    times = int(numerator/denominator)
    print("-- Calculating -- ")
    print(f"{numerator}/{denominator}")
    print(f"Times: {times}")
    if remainder is not 0:
        print(f"Remainder: {remainder}/{denominator}")



show_remainder(2,2)

show_remainder(3,5)

show_remainder(4,2)

show_remainder(5,2)

show_remainder(6,2)

show_remainder(7,2)

show_remainder(8,2)

show_remainder(9,2)

show_remainder(10,2)
