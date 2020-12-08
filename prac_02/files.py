# Question one
NAME_FILE = "name_store.txt"
name = '0'
name_out = open(NAME_FILE, 'w')
while name.isnumeric() is True:
    name = str(input("please enter your name: "))
    if name.isnumeric() is True:
        print("name cannot include numbers!")

print(name, file=name_out)
name_out.close()

# Question two

name_in = open(NAME_FILE, 'r')

print("Your name is {}".format(name_in.read()))
name_in.close()

# Question three
NUM_IN = "numbers.txt"
num_out = open(NUM_IN, 'r')
num1 = int(num_out.readline())
num2 = int(num_out.readline())
num_total = num1 + num2
print('the result is: {}'.format(num_total))
num_out.close()

# Question four
num_read = open(NUM_IN, 'r')
total = 0
for line in num_read:
    num_hold = int(line)
    total += num_hold
num_read.close()
print(total)

