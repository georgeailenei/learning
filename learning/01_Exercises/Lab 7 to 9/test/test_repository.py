import unittest

from domain.entity import Movie
from repository.fileRepository import MoviesFileRepository


# clasa trebuies sa inceapa cu prefixul Test urmat de numele clasei care se testeaza
class TestMoviesFileRepository(unittest.TestCase):

    def setUp(self):
        self.movie1 = Movie(title='Avengers', description='The Avengers were a team of extraordinary individuals.',
                       genre='Action')
        self.movie1.id = 1

        self.movie1.availability = 'NOT AVAILABLE'

        self.movie2 = Movie(title='Batman', description='Is the superhero protector of Gotham City.', genre='Crime')
        self.movie2.id = 2
        self.movie2.availability = 'NOT AVAILABLE'


    # Un nume de test trebuie sa fie format din 3 bucati - ce metoda testam, ce caz testam si ce ne asteptam sa se intample
    def test_get_all_when_initial_file_is_populated_returns_list_with_all_the_moves_as_objects(self):
        # AAA - arange, act, assert
        moviesRepo = MoviesFileRepository('test/movies_test.txt')


        movies = moviesRepo.get_all()

        self.assertListEqual(
            movies,
            [self.movie1, self.movie2]
        )
