from Robot import Robot
from Rewards import Rewards
from Drawer import Drawer
import getch
import random

# Set initial position
robot = Robot(3,9)

r1 = Rewards(random.randint(1,10),random.randint(1,10),'Coin')
r2 = Rewards(random.randint(1,10),random.randint(1,10),'Gold')
r3 = Rewards(random.randint(1,10),random.randint(1,10),'Weapon')
rewards = [r1,r2, r3]
print(r1, r2, r3)
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
