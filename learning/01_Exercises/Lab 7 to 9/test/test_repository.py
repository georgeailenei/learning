import unittest
from domain.entity import Client
from repository.clientsRepository import ClientsRepository


class TestClientsRepository(unittest.TestCase):
    # The name of the method must contain 3 segments:
    # 1. the method that we are testing
    # 2. what case we are testing
    # 3. what result we are expecting.

    def setUp(self):
        self.repo = ClientsRepository()
        self.client_01 = Client("George", "234")
        self.client_02 = Client("Jodie", "124")
        self.client_03 = Client("Nick", "442")
        self.repo.save(self.client_01)
        self.repo.save(self.client_02)
        self.repo.save(self.client_03)

    # white-boxing test
    def test_save_when_empty_return_empty_list(self):
        database = self.repo.database
        database.clear()
        self.assertEqual(database, [])

    # white-boxing test
    def test_save_when_saving_new_client_returns_the_right_id(self):
        database = self.repo.database
        self.assertEqual([database[0].id], [self.client_01.id])
        self.assertEqual([database[1].id], [self.client_02.id])
        self.assertEqual([database[2].id], [self.client_03.id])

    # white-boxing test
    def test_save_when_saving_new_client_returns_the_right_rented_movies_count(self):
        database = self.repo.database
        self.assertEqual([database[0].rented_movies], [self.client_01.rented_movies])
        self.assertEqual([database[1].rented_movies], [self.client_02.rented_movies])
        self.assertEqual([database[2].rented_movies], [self.client_03.rented_movies])

    # white-boxing test
    def test_save_when_saving_new_client_returns_zero_to_all_movies_count(self):
        track_clients_movies = self.repo.track_clients_movies
        self.assertEqual(track_clients_movies[self.client_01.name], 0)
        self.assertEqual(track_clients_movies[self.client_02.name], 0)
        self.assertEqual(track_clients_movies[self.client_03.name], 0)

    # white-boxing test
    def test_add_count_when_adding_one_unit_or_more_returns_the_right_count(self):
        track_clients_movies = self.repo.track_clients_movies

        self.assertEqual(track_clients_movies[self.client_01.name], 0)
        self.repo.add_count(self.client_01.name)

        self.assertEqual(track_clients_movies[self.client_01.name], 1)
        self.repo.add_count(self.client_01.name)

        self.assertEqual(track_clients_movies[self.client_01.name], 2)
        self.repo.add_count(self.client_01.name)

        self.assertEqual(track_clients_movies[self.client_01.name], 3)

    # white-boxing test
    def test_update_when_given_a_wrong_id_with_empty_list_returns_empty_list(self):
        self.repo.database.clear()
        self.repo.update("1", self.client_01)
        self.assertEqual(self.repo.database, [])

        self.repo.update("0", self.client_02)
        self.assertEqual(self.repo.database, [])

    # white-boxing test
    def test_update_when_given_a_wrong_id_but_the_list_is_populated_returns_same_list_of_clients(self):

        self.repo.update("0", self.client_01)
        self.assertEqual(self.repo.database, [self.client_01, self.client_02, self.client_03])
        self.repo.update("4", self.client_01)
        self.assertEqual(self.repo.database, [self.client_01, self.client_02, self.client_03])
        self.repo.update("7", self.client_01)
        self.assertEqual(self.repo.database, [self.client_01, self.client_02, self.client_03])

    # white-boxing test
    def test_update_when_given_the_right_id_with_populated_list_returns_updated_name(self):

        update_client = Client("Dan", "222")
        update_client.id = self.client_02.id
        self.repo.update("2", update_client)
        self.assertEqual(str(self.repo.database[1]), str(update_client))

    def test_get_names_when_list_is_empty_return_empty_list(self):
        self.repo.database.clear()
        self.assertEqual(self.repo.get_names(), [])

    def test_get_names_when_list_is_populated_return_the_names_of_clients(self):
        self.assertEqual(self.repo.get_names(), [self.client_01.name, self.client_02.name, self.client_03.name])

    def test_get_client_when_given_name_is_wrong_return_none(self):
        self.assertEqual(self.repo.get_client("nic"), None)
        self.assertEqual(self.repo.get_client("Joe"), None)
        self.assertEqual(self.repo.get_client("Nothing"), None)

    def test_get_client_when_given_name_is_right_return_the_object(self):
        self.assertEqual(self.repo.get_client("George"), self.client_01)
        self.assertEqual(self.repo.get_client("Jodie"), self.client_02)
        self.assertEqual(self.repo.get_client("Nick"), self.client_03)

    def test_save_movie_when_given_name_is_wrong_return_same_string(self):
        self.repo.save_movie("Joe", "Batman")
        self.repo.save_movie("Nicu", "Batman")
        self.repo.save_movie("Rob", "Batman")

        self.assertEqual(self.repo.database[0].rented_movies, self.client_01.rented_movies)
        self.assertEqual(self.repo.database[1].rented_movies, self.client_02.rented_movies)
        self.assertEqual(self.repo.database[2].rented_movies, self.client_03.rented_movies)

    def test_save_movie_when_given_name_is_right_return_client_rented_movies_with_the_movie_name_in(self):
        self.repo.save_movie("George", "Batman")
        self.repo.save_movie("Jodie", "Batman")
        self.repo.save_movie("Nick", "Batman")

        self.assertEqual(self.repo.database[0].rented_movies, self.client_01.rented_movies)
        self.assertEqual(self.repo.database[1].rented_movies, self.client_02.rented_movies)
        self.assertEqual(self.repo.database[2].rented_movies, self.client_03.rented_movies)

    def test_remove_movie_when_given_name_is_wrong_returns_same_string_of_information(self):
        self.repo.save_movie("George", "Batman")
        self.repo.remove_movie("Nimic")
        self.repo.save_movie("Jodie", "Batman")
        self.repo.save_movie("Nick", "Batman")

        self.assertEqual(self.repo.database[0].rented_movies, self.client_01.rented_movies)
        self.assertEqual(self.repo.database[1].rented_movies, self.client_02.rented_movies)
        self.assertEqual(self.repo.database[2].rented_movies, self.client_03.rented_movies)

    def test_remove_movie_when_given_name_is_right_returns_updated_string_of_information(self):
        self.repo.save_movie("George", "Batman")
        self.repo.save_movie("Jodie", "Batman")
        self.repo.save_movie("Nick", "Batman")

        self.repo.remove_movie("Batman")

        self.assertEqual(self.repo.database[0].rented_movies, self.client_01.rented_movies)
        self.assertEqual(self.repo.database[1].rented_movies, self.client_02.rented_movies)
        self.assertEqual(self.repo.database[2].rented_movies, self.client_03.rented_movies)

    def test_movie_count_when_movie_is_not_in_returns_zero(self):
        self.assertEqual(self.repo.get_movie_count("George"), 0)
        self.assertEqual(self.repo.get_movie_count("Jodie"), 0)
        self.assertEqual(self.repo.get_movie_count("Nick"), 0)

    def test_movie_count_when_movie_is_in_the_list_returns_current_count(self):
        self.repo.save_movie("George", "Batman")
        self.repo.save_movie("George", "Avengers")
        self.repo.save_movie("George", "Click")
        self.repo.save_movie("Nick", "Batman")
        self.repo.save_movie("Nick", "NBD")

        self.assertEqual(self.repo.get_movie_count("Nick"), 2)
        self.assertEqual(self.repo.get_movie_count("George"), 3)


if __name__ == "__main__":
    unittest.main()
