from default_robot import DefaultRobot

# Add inheritance
class Tars(DefaultRobot):

    def __init__(self,legs,hands):
        self.legs = legs
        self.hands = hands
