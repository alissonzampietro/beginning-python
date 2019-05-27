from Point import Point

class Robot(Point):
    def __init__(self, x, y):
        super(Robot, self).__init__(x,y)
        print(x,y)

    def moveUp(self):
        if(self.y < 10):
            self.y += 1
        else:
            print('Não podes mover mais para cima')

    def moveDown(self):
        if(self.y > 0):
            self.y -= 1
        else:
            print('Não podes mover mais para baixo')
    
    def moveLeft(self):
        if(self.x > 0):
            self.x -= 1
        else:
            print('Não podes mover mais para esquerda')

    def moveRight(self):
        if(self.x < 10):
            self.x += 1
        else:
            print('Não podes mover mais para direita')

    def showPosition(self):
        print(self.x,self.y)

        