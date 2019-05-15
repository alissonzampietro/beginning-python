from account import Account

class CheckingAccount(Account):
    def __init__(self, client, number, limit = 0):
        Account.__init__(self, client, number)
        self.limit = limit
    
        