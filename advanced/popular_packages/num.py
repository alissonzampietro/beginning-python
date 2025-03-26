import numpy as np

# generaring random number
print(np.random.randint(10))

# generaring random number between 10 and 100
print(np.random.randint(10, 100))

# getting the value from a Series randomly
print(np.random.choice([1,2,3,4,5]))

# picking 3 random values of the list
print(np.random.choice(["i","love","python", "and", "computers", "datasets", "machine learning"], 3))
