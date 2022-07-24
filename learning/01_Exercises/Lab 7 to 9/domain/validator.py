class ValidatorError(Exception):
    pass


class movieValidator:
    def checkGenre(self, genre):
        # This method checks if the genre given by the user exists.
        movieGenres = ["Action", "Crime", "Drama", "Fantasy", "Horror",
                       "Comedy", "Romance", "Science Fiction", "Sports",
                       "Thriller", "Mystery", "War", "Western"]

        # The method returns True or False.
        if genre in movieGenres:
            return True
        else:
            return False

    def checkDescriptionLength(self, description):
        # The method returns True or False depending on the description length.
        if len(description) < 3 or len(description) > 10:
            return False
        else:
            return True

    def validator(self, movie):
        # The method checks if the length and the genre are correct, and it returns True or False.
        return self.checkGenre(movie.genre) and self.checkDescriptionLength(movie.description)


class clientValidator:
    def checkCnpLength(self, CNP):
        # The method checks if the CNP is longer or smaller than 3 digits, and it returns True or False.
        if len(CNP) == 3:
            return True
        else:
            return False

    def checkCnpInt(self, CNP):
        # The method checks if CNP is an int or not, returns True or False.
        try:
            newCNP = int(CNP)
            if isinstance(newCNP, int):
                return True
        # This comment is for me. I would like to write some code that returns some informative errors for the user.
        except ValidatorError():
            print("Ceva Error")

    def validator(self, Client):
        return self.checkCnpLength(Client.CNP) and self.checkCnpInt(Client.CNP)
