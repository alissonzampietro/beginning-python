class Drawer:
    def __init__(self, Robot):
        self.robot = Robot
        self.originalSizes = self.robot.getOrigalSizes()
        self.draw()

    def draw(self):
        actualPosition = self.robot.getPositions()
        for x in range(0, self.originalSizes[0]):
            for y in range(0, self.originalSizes[1]):
                if(actualPosition[0] == x and actualPosition[1] == y):
                    print(' O ', end='')
                else:
                    print(' X ', end='')
            print('','\n')
