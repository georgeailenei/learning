

class movieValidator:
    def checkGenre(self, genre):
        movieGenres = ["Action", "Crime", "Drama", "Fantasy", "Horror",
                       "Comedy", "Romance", "Science Fiction", "Sports",
                       "Thriller", "Mystery", "War", "Western"]
        if genre in movieGenres:
            return True
        else:
            return False


class clientValidator:
    pass
