from repository.repository import Repository


class MoviesRepository(Repository):
    def __init__(self):
        self.database = []
        self.current_id = 1
        self.current_count = 0
        self.current_availability = "Available"
        self.track_rented_movies = {}

    def get(self):
        pass

    def save(self, movie):
        movie.id = self.current_id
        movie.availability = self.current_availability
        self.database.append(movie)
        self.track_rented_movies[movie.title] = self.current_count
        self.current_id += 1

    def add_count(self, movie):
        self.track_rented_movies[movie] += 1

    def update(self, unique_id, new_movie):
        updated_database = []
        for movie in self.database:
            if unique_id == str(movie.id):
                movie.title = new_movie.title
                movie.description = new_movie.description
                movie.genre = new_movie.genre
                updated_database.append(movie)
            else:
                updated_database.append(movie)
        self.remove_all()
        self.save_all(updated_database)

    def get_names(self):
        name_list = [movie.title for movie in self.database]
        return name_list

    def get_movie(self, the_movie):
        for movie in self.get_all():
            if the_movie == movie.title:
                return movie

    def update_status(self, the_movie):
        if the_movie.availability == "Available":
            the_movie.availability = "NOT AVAILABLE"
        elif the_movie.availability == "NOT AVAILABLE":
            the_movie.availability = "Available"
