# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'
#
# print(f"{bcolors.OKGREEN}Error : Test message !{bcolors.ENDC}")

class movie:
    def __init__(self, title, description, genre):
        self.id = None
        self.title = title
        self.description = description
        self.genre = genre
        self.availability = None

    def __repr__(self):
        return f"{self.id} - {self.title} | {self.description} | {self.genre} | {self.availability}"


class client:
    def __init__(self, name, CNP):
        self.id = None
        self.name = name
        self.CNP = CNP
        self.rentedMovies = []

    def __repr__(self):
        return f"{self.id} | {self.name} | {self.CNP} | {self.rentedMovies}"
