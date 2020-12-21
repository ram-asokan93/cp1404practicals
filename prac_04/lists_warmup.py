numbers = [3, 1, 4, 1, 5, 9, 2]

"""
Answers to questions:

numbers[0]
output: 3

numbers[-1]
output: 2

numbers[3]
output: 1

numbers[:-1]
output: [3, 1, 4, 1, 5, 9]

numbers[3:4]
output: 1

5 in numbers
output: True

7 in numbers
output: False

"3" in numbers
output: False

numbers + [6, 5, 3]
output: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
"""

numbers[0] = "ten"
numbers[-1] = 1
print(numbers[2:])
if 9 in numbers:
    print("9 is an element in numbers list")
else:
    print("9 is not an element in list")
# or #
# print("9 an element in numbers:", 9 in numbers)



