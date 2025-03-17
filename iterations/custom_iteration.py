class TestingIterator:
    def __init__(self, initial, max):
        self.initial = initial
        self.max = max
    
    def __iter__(self):
        self.n = self.initial
        return self
    
    def __next__(self):
        if self.n >= self.max:
            raise StopIteration
        self.n *= self.initial
        return self.n 

# For will iterate over all iterable objects. 
# However, you can create your custom one using __iter__ and __next__
for i in TestingIterator(2, 600):
    print(i)

print('------------------------------')

# You can also use the iterator in a while loop
instance = TestingIterator(2, 600)
iterator = iter(instance)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

