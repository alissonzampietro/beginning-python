class Account:
    def __init__(self, client, number):
        self.number = number
        self.client = client

    def showGreetingMessage(self):
        print('Welcome Sr. '+self.client)
