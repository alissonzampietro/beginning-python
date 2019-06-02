from Robot import Robot
from Rewards import Rewards
import getch
from Drawer import Drawer

r1 = Rewards(1,2,'coins')
r2 = Rewards(2,5,'gold')
rewards = [r1,r2]

robot = Robot(5,5)

Drawer(robot)


def caller(number):
    options = {
        67: robot.moveRight,
        68: robot.moveLeft,
        65: robot.moveUp,
        66: robot.moveDown
    }

    func = options.get(number, '')
    if(func != ''):
        func()
        print(checkReward(robot, rewards))

def checkReward(robot,rewards):
    ok = False
    for reward in rewards:
        if reward.x == robot.x and reward.y == robot.y:
            print('O robo achou a recompensa: %s' % reward.name)
            ok = True
    return ok

while True:
    key = ord(getch.getch())
    caller(key)


# r1 = Robot(5,5)
# r1.moveRight()
# r1.moveRight()
# r1.moveRight()
# r1.moveUp()
# r1.moveLeft()
# r1.showPosition()
