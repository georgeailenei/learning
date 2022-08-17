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
        movie_genres = ["Action", "Crime", "Drama", "Fantasy", "Horror",
                        "Comedy", "Romance", "Science Fiction", "Sports",
                        "Thriller", "Mystery", "War", "Western"]
        if genre not in movie_genres:
            self.validation_errors.append(f'Movie should have one of the genres: {" ".join(movie_genres)}')

    def check_description_length(self, description):
        if len(description) < 3 or len(description) > 100:
            self.validation_errors.append('Description should have between 3 and 100 characters')

    def validator(self, movie):
        self.validation_errors = []
        self.check_genre(movie.genre)
        self.check_description_length(movie.description)
        self.check_word(movie.title)

        if len(self.validation_errors) > 0:
            raise ValidatorError('\n'.join(self.validation_errors))


class ValidateClient(Validate):
    def check_cnp_length(self, cnp):
        if len(cnp) != 3:
            self.validation_errors.append(f"{cnp} must contain 3 digits.")

    def check_cnp_int(self, cnp):
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        cnp_numbers = [num for num in cnp if num not in numbers]

        if len(cnp_numbers) > 0:
            self.validation_errors.append(f"{cnp} is not an integer")

    def movies_rented(self, client):
        movies_is_available = True if len(client.rented_movies) > 0 else False
        return movies_is_available

    def validator(self, client):
        self.validation_errors = []
        self.check_cnp_length(client.CNP)
        self.check_cnp_int(client.CNP)
        self.check_word(client.name)

        if len(self.validation_errors) > 0:
            raise ValidatorError('\n'.join(self.validation_errors))
