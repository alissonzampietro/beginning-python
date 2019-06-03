from Point import Point

class Rewards(Point):
    # Constructor of the class
    def __init__(self, x, y, name):
        super(Rewards, self).__init__(x,y)
        self.name = name

    # Return the string representation of an object
    def __str__(self):
        # '<%s, %s>: %s' is the same of '<%self.x, %self.y>: %self.name'
        return '<%s, %s>: %s' % (self.x, self.y, self.name)
