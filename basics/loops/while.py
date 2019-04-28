import random

top = 200

number = random.randint(1,top)
trials = 0

while number < top:
    if number % 2 == 0:
        # Can pass second argument to define how shown structure will behave
        print(number, end=' ')
    number += 1
    trials += 1

print('Was lefting just '+str(trials)+' to '+str(top))