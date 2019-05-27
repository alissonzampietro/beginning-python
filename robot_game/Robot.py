class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def moveUp(self, value):
        self.y += value

    def moveDown(self, value):
        self.y -= value
    
    def moveLeft(self, value):
        self.x -= value

    def moveRight(self, value):
        self.x += value    

        