class Account:
    def __init__(self, password, login):
        self.__password = password
        self.login = login
    
    def is_correct_password(self, pw):
        return (self.password == pw)
        