class Magic:
    # Constructor of the class
    ## You can realize that are passed two params in the constructor of the class
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # With __str__ you can change what is showed in the properties of the class
    def __str__(self):
        return 'a Beautiful class'





m = Magic(1,2)

print(m)

# Here you can get the orignial property of the class
print(m.__repr__())