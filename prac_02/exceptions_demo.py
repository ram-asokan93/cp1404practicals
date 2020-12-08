denominator = 0
while denominator == 0:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
        continue
    if denominator == 0:
        print("Denominator cannot be zero!")
    else:
        break
fraction = numerator / denominator
print(fraction)

print("Finished.")

"""
1. When will a ValueError occur?
-- a ValueError will occur when an invalid value is provided when a 
    specific value type is asked for
        (for example, in this case, if a str or float is 
         entered when asked for a numerator/denominator,
         a ValueError will be returned)
2. When will a ZeroDivisionError occur?
-- when a float or integer is attempted to be divided by '0' 
    a ZeroDivisionError will occur

3. Could you change the code to avoid the possibility of a ZeroDivisionError
-- to accomplish this we must make it so that the division 
    does not take place when '0' is entered as the denominator 
"""