from default_robot import DefaultRobot

# Add inheritance
class Tars(DefaultRobot):

    def __init__(self,legs,hands, head):
        super(Tars, self).__init__(legs, hands)
        self.head = head
    
    def showParts(self):
        super(Tars,self).showParts()
        print(' and '+str(self.head)+' head(s)')

