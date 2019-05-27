from Point import Point

class Rewards(Point):
    def __init__(self, x, y, name):
        super(Rewards, self).__init__(x,y)
        self.name = name
