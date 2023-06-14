class User(object):
    def __init__(self, id, name, password) -> None:
        self.id = id
        self.name = name
        self.password = password
    
    def get_id(self):
        return self.id
        
    def get_name(self):
        return self.name