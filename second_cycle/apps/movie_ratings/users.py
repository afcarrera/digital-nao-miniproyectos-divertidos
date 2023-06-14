class Users(object):
    def __init__(self) -> None:
        self.users_list = []
    
    def add_user(self, user):
        self.users_list.append(user)
        
    def get_users(self):
        return self.users_list