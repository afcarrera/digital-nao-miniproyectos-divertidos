class Movie(object):
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
        self.rating = 0.0
        self.total_rating = 0.0
        self.rated_by = set()
        
    def set_rating(self, rating: int, usr_id: str):
        if usr_id not in self.rated_by:
            self.rated_by.add(usr_id)
            self.total_rating = (self.total_rating + rating) 
            self.rating = (self.total_rating) / len(self.rated_by)
        
    def get_rating(self):
        return self.rating
    
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
        