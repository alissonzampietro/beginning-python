class Robot:
    
    ## It's always necessary to set a params in the constructor, cause it represents the self intance o the class
    def __init__(self,x,y):
        self.x = x
        self.y = y

    # If we use the instance
    def show(self):
        print(str(self.x)+str(self.y))