# You always need to use "self" to access attributes from the class
class Person:
    
    # Constructor
    def __init__(self, name, age):
        # if you wish create attributes, you should use self
        self.name = name
        self.age = age

    def showName(self):
        print(self.name)