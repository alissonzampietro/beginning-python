from Point import Point

class Robot(Point):
    def __init__(self, x, y):
        super(Robot, self).__init__(x,y)
        self.originalX = 10
        self.originalY = 10

    def moveUp(self):
        if(self.y < self.originalY):
            self.y += 1
        else:
            print('Não podes mover mais para cima')

    def moveDown(self):
        if(self.y > 1):
            self.y -= 1
        else:
            print('Não podes mover mais para baixo')
    
    def moveLeft(self):
        if(self.x > 1):
            self.x -= 1
        else:
            print('Não podes mover mais para esquerda')

    def moveRight(self):
        if(self.x < self.originalX):
            self.x += 1
        else:
            print('Não podes mover mais para direita')

    def getPositions(self):
        return [self.x,self.y]

    def getOriginalSizes(self):
        return [self.originalX, self.originalY]