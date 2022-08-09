class ValidatorError(Exception):
    pass


class Validate:
    def check_word(self, word):
        # The title must contain only letters and spaces. It returns True or False.
        all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z', " ", "."]
        unwanted_letters = [letter for letter in word if letter.lower() not in all_letters]
        true_or_false = False if len(unwanted_letters) > 0 else True
        return true_or_false

    def check_id(self, unique_id, id_list):
        true_or_false = False if unique_id not in id_list else True
        return true_or_false


class ValidateMovie(Validate):
    def check_availability(self, availability):
        true_or_false = True if availability == "Available" else False
        return true_or_false

    def check_genre(self, genre):
        # This method checks if the genre given by the user exists.
        movie_genres = ["Action", "Crime", "Drama", "Fantasy", "Horror",
                       "Comedy", "Romance", "Science Fiction", "Sports",
                       "Thriller", "Mystery", "War", "Western"]
        true_or_false = True if genre in movie_genres else False
        return true_or_false

    def check_description_length(self, description):
        # The method returns True or False depending on the description length.
        true_or_false = False if len(description) < 3 or len(description) > 100 else True
        return true_or_false

    def check_title(self, title, movie_names):
        true_or_false = False if title in movie_names else True
        return true_or_false

    def validator(self, movie, movie_names):
        # This method check if the genre, length and tittle are correct. returns True or False.
        return (
            self.check_genre(movie.genre)
            and self.check_description_length(movie.description)
            and self.check_word(movie.title)
            and self.check_title(movie.title, movie_names)
        )


class ValidateClient(Validate):
    def check_cnp_length(self, cnp):
        # The method checks if the CNP is longer or smaller than 3 digits, and it returns True or False.
        true_or_false = True if len(cnp) == 3 else False
        return true_or_false

    def check_cnp_int(self, cnp):
        # The method checks if CNP is an int or not, returns True or False.
        try:
            new_cnp = int(cnp)
            if isinstance(new_cnp, int):
                return True
        # This comment is for me. I would like to write some code that returns some informative errors for the user.
        except ValidatorError():
            print("Ceva Error")

    def movies_rented(self, client):
        true_or_false = True if len(client.rented_movies) > 0 else False
        return true_or_false

    def check_name(self, client, clients_names):
        true_or_false = False if client in clients_names else True
        return true_or_false

    def validator(self, client, clients_names):
        # This method check if the name and CNP are correct. returns True or False.
        return (
            self.check_cnp_length(client.CNP)
            and self.check_cnp_int(client.CNP)
            and self.check_word(client.name)
            and self.check_name(client.name, clients_names)
        )
    
