for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print('\n')

num = int(input("enter number of stars you would like: "))

for line in range(num):
    for i in range(line+1):
        print('*', end='')
    print()
