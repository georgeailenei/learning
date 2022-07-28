class ValidatorError(Exception):
    pass


class validate:
    def checkWord(self, word):
        # The title must contain only letters and spaces. It returns True or False.
        allLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z', " ", "."]
        unwantedLetters = [letter for letter in word if letter.lower() not in allLetters]
        trueOrFalse = False if len(unwantedLetters) > 0 else True
        return trueOrFalse

    def checkID(self, ID, idList):
        trueOrFalse = False if ID not in idList else True
        return trueOrFalse


class movieValidator(validate):
    def checkAvailability(self, availability):
        trueOrFalse = True if availability == "Available" else False
        return trueOrFalse

    def checkGenre(self, genre):
        # This method checks if the genre given by the user exists.
        movieGenres = ["Action", "Crime", "Drama", "Fantasy", "Horror",
                       "Comedy", "Romance", "Science Fiction", "Sports",
                       "Thriller", "Mystery", "War", "Western"]
        trueOrFalse = True if genre in movieGenres else False
        return trueOrFalse

    def checkDescriptionLength(self, description):
        # The method returns True or False depending on the description length.
        trueOrFalse = False if len(description) < 3 or len(description) > 100 else True
        return trueOrFalse

    def validator(self, movie):
        # This method check if the genre, length and tittle are correct. returns True or False.
        return self.checkGenre(movie.genre) and self.checkDescriptionLength(movie.description) and self.checkWord(movie.title)


class clientValidator(validate):
    def checkCnpLength(self, CNP):
        # The method checks if the CNP is longer or smaller than 3 digits, and it returns True or False.
        trueOrFalse = True if len(CNP) == 3 else False
        return trueOrFalse

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
        # This method check if the name and CNP are correct. returns True or False.
        return self.checkCnpLength(Client.CNP) and self.checkCnpInt(Client.CNP) and self.checkWord(Client.name)
