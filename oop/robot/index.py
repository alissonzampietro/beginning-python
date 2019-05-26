from default_robot import DefaultRobot
from tars import Tars

r1 = DefaultRobot(2,2)
print(type(r1))
r1.showParts()
print(r1.hands)

t1 = Tars(1,2)
t1.showParts()


