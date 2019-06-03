from Robot import Robot
from Rewards import Rewards
from Drawer import Drawer
import getch

# Set initial position
robot = Robot(3,9)

r1 = Rewards(1,2,'Coin')
r2 = Rewards(2,5,'Gold')
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
