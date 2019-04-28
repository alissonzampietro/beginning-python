import random

num = random.randint(1,200)

# Function xrange is unavailable from version 3
for x in range(10):
    if(x == 5):
        print('Middle')
    print(x)