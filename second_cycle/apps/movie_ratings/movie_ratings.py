from apps.movie_ratings.users import Users
from apps.movie_ratings.user import User
from apps.movie_ratings.movie import Movie
from apps.movie_ratings.movies import Movies

class MovieRatings(object):
    def __init__(self) -> None:
        self.users_list = Users()
        user = User(1, 'usuarioA', '123')
        self.users_list.add_user(user)
        user = User(2, 'usuarioB', '123')
        self.users_list.add_user(user)
        user = User(3, 'usuarioC', '123')
        self.users_list.add_user(user)
        self.movies_list = Movies()
        movie = Movie(1, 'Pelicula 1')
        self.movies_list.add_movie(movie)
        movie = Movie(2,'Pelicula 2')
        self.movies_list.add_movie(movie)
        movie = Movie(3, 'Pelicula 3')
        self.movies_list.add_movie(movie)
        self.ratings_list = [0,1,2,3,4,5]
        self.ratings_dict = dict()
        for rating in self.ratings_list:
            self.ratings_dict[rating] = rating
        self.movies_dict = dict()
        for movie in self.movies_list.get_movies():
            self.movies_dict[movie.get_id()] = movie
        self.users_dict = dict()
        for user in self.users_list.get_users():
            self.users_dict[user.get_id()] = user
    
    def get_users(self):
        return self.users_dict
        
    def get_movies(self):
        return self.movies_dict
        
    def get_ratings(self):
        return self.ratings_dict
        
    def rate_movie(self, movie_id: int, rate: int, user_id: str):
        if rate not in self.ratings_dict or movie_id not in self.movies_dict:
            return
        self.movies_dict[movie_id].set_rating(rate, user_id)
        
    def get_movie_by_id(self, movie_id):
        return self.movies_dict[movie_id]
        
    def to_string(self):
        s = ""
        for movie in self.movies_list.get_movies():
            s = s + 'Nombre: ' + movie.get_name() + ', Ranting: ' + str(movie.get_rating()) +'.\n'
        return s