import datetime
import unittest

from DSA import movie_rating
from movie_rating import Movie_rate


class Testmovie_rating(unittest.TestCase):

    def test_movies_folder_is_empty(self):
        self.movies = []
        self.assertEqual(0, len(self.movies))

    def test_movies_folder_contains_movies(self):
        self.movies = ['DragonBall']
        self.assertEqual(1, len(self.movies))
        self.movies.append("Snow White")
        self.assertEqual(2, len(self.movies))

    def test_movies_folder_saves_new_movies(self):
        result = Movie_rate.add_movie([datetime], "DragonBall")
        self.assertEqual(result,"New movie DragonBall has added")

    def test_add_movie_duplicate(self):
        self.movies.add_movie("Snow White")
        result = self.Movie_rate.add_movie("Snow White")
        self.assertEqual(result, "Snow White already exists in storage")



if __name__ == '__main__':
    unittest.main()

