class DefaultRobot:
    
    ## It's always necessary to set a params in the constructor, cause it represents the self intance o the class
    def __init__(self,legs,hands):
        self.legs = legs
        self.hands = hands

    # If we use the instance
    def showParts(self):
        # You can get the name of the class using type(self).__name__
        print('The robot '+type(self).__name__+' has '+str(self.hands)+' hand(s) and '+str(self.legs)+' leg(s)', end='')