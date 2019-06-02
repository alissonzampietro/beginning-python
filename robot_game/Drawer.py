class Drawer:
    def __init__(self, Robot, Rewards):
        self.robot = Robot
        self.rewards = Rewards
        self.originalSizes = self.robot.getOriginalSizes()
        self.draw(self.robot)

    def draw(self, robot):
        character = '|'
        actualPosition = robot.getPositions()
        print(self.originalSizes, actualPosition)
        
        # for x in range(1, self.originalSizes[0]):
        #     for y in range(1, self.originalSizes[1]):
        #         character = '|'
        #         if(actualPosition[0] == x and actualPosition[1] == y):
        #             character = '\o'
        #         for reward in self.rewards:
        #             if reward.x == robot.x and reward.y == robot.y:
        #                 character = reward.name
                
        #         print(' '+character+' ', end='')
        #     print('','\n')
