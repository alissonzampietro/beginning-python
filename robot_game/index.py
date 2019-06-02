from Robot import Robot
from Rewards import Rewards
import getch
from Drawer import Drawer

# Set initial position
robot = Robot(5,5)

r1 = Rewards(1,2,'C')
r2 = Rewards(2,5,'G')
rewards = [r1,r2]
drawer = Drawer(robot, rewards)


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
        drawer.draw(robot)

while True:
    print('\n')
    key = ord(getch.getch())
    caller(key)


# r1 = Robot(5,5)
# r1.moveRight()
# r1.moveRight()
# r1.moveRight()
# r1.moveUp()
# r1.moveLeft()
# r1.showPosition()
