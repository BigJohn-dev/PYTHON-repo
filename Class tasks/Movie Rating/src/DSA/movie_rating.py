# Movie rating application
import datetime

class Movie_rate:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie_name):
        if movie_name == " ":
            return "No movie added."
        if movie_name not in self.movies:
            self.movies.append({"Movie Name": movie_name, "Time": datetime.datetime.now()})
            return f"New movie {movie_name} has added"
        return f"{movie_name} already exists in storage"

    def rating_movie(self, rating):
        if rating < 1 or rating > 5:
            return "Rating must be between 1 and 5"
        return f"Rating of {self} is: {rating}"

    def view_movies(self):
            if not self.movies:
                return "No movie available in list"
            result = "Your saved movies:\n"
            for i, task in enumerate(self.movies, 1):
                result += f"{i}. {self.movies['movie_name']}"
            return result

    def average_rating(self, rating):
            if rating < 1 or rating > 5:
                return "Rating must be between 1 and 5"