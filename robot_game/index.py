from Robot import Robot
from Rewards import Rewards
import getch


while True:
    key = getch.getch()
    print('o numero:'+key)

def checkReward(robot,rewards):
    ok = False
    for reward in rewards:
        if reward.x == robot.x and reward.y == robot.y:
            print('O robo achou a recompensa: %s' % reward.name)
            ok = True
    return ok



# r1 = Robot(5,5)
# r1.moveRight()
# r1.moveRight()
# r1.moveRight()
# r1.moveUp()
# r1.moveLeft()
# r1.showPosition()
r1 = Rewards(1,2,'coins')
r2 = Rewards(2,5,'gold')
rewards = [r1,r2]

robot = Robot(5,5)
robot.moveDown()
robot.moveDown()
robot.moveDown()
robot.moveDown()
robot.moveLeft()
robot.moveLeft()
robot.moveLeft()
print(checkReward(robot, rewards))
