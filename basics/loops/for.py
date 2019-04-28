import random

num = random.randint(1,200)

# Function xrange is unavailable from version 3
for x in range(10):
    if(x == 5):
        print('Middle', end=' ')
    print(x, end=' ')

print('\n')

# Define range and quantity between values
for x in range(1,10,2):
    print(x, end=' ')