from repository.moviesRepository import moviesRepository


class clientsRepository(moviesRepository):
    def __init__(self):
        super().__init__()
        self.database = []
        self.currentID = 1
