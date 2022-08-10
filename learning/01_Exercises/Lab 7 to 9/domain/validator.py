class ValidatorError(Exception):
    pass


class Validate:
    def check_word(self, word):
        # The title must contain only letters and spaces. It returns True or False.
        all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z', " ", "."]
        unwanted_letters = [letter for letter in word if letter.lower() not in all_letters]
        if len(unwanted_letters):
            self.validation_errors.append(f'Word {word} contains unwanted characters (only letters allowed)')

    def check_id(self, unique_id):
        try:
            unique_id = int(unique_id)
        except ValidatorError() as e:
            print(e)
        else:
            if isinstance(unique_id, int):
                return True


class ValidateMovie(Validate):
    def check_availability(self, availability):
        is_available = True if availability == "Available" else False
        return is_available

    def check_genre(self, genre):
        # This method checks if the genre given by the user exists.
        movie_genres = ["Action", "Crime", "Drama", "Fantasy", "Horror",
                        "Comedy", "Romance", "Science Fiction", "Sports",
                        "Thriller", "Mystery", "War", "Western"]
        if genre not in movie_genres:
            self.validation_errors.append(f'Movie should have one of the genres: {" ".join(movie_genres)}')

    def check_description_length(self, description):
        # The method returns True or False depending on the description length.
        if len(description) < 3 or len(description) > 100:
            self.validation_errors.append('Description should have between 3 and 100 characters')

    def validator(self, movie):
        self.validation_errors = []

        self.check_genre(movie.genre)
        self.check_description_length(movie.description)
        self.check_word(movie.title)

        if len(self.validation_errors) > 0:
            raise ValidatorError('\n'.join(self.validation_errors))

        # This method check if the genre, length and tittle are correct. returns True or False.


class ValidateClient(Validate):
    def check_cnp_length(self, cnp):
        # The method checks if the CNP is longer or smaller than 3 digits, and it returns True or False.
        length_is_valid = True if len(cnp) == 3 else False
        return length_is_valid

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
        movies_is_available = True if len(client.rented_movies) > 0 else False
        return movies_is_available

    def validator(self, client):
        # This method check if the name and CNP are correct. returns True or False.
        return (
            self.check_cnp_length(client.CNP)
            and self.check_cnp_int(client.CNP)
            and self.check_word(client.name)
        )
    
