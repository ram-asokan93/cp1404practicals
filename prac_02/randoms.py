import random
print(random.randint(5, 20))        # line 1
print(random.randrange(3, 10, 2))     # line 2
print(random.uniform(2.5, 5.5))     # line 3

"""

what did you see on line 1
- The smallest number I could have seen is a 5, and the largest is a 20
what did you see on line 2?
- The smallest was a 3 and the largest is a 9
    I would not have been able to see a 4 on line 2 because the step is 2 and the range starts off on an odd number
what did you see on line 3?
-The smallest number I could have see is a 2.5 and the largest would be a 5.4999999999999...

"""

print(random.randint(1, 100))
