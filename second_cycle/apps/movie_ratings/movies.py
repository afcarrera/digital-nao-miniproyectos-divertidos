class Movies(object):
    def __init__(self) -> None:
        self.movies_list = []
        
    def add_movie(self, movie):
        self.movies_list.append(movie)
        
    def get_movies(self):
        return self.movies_list