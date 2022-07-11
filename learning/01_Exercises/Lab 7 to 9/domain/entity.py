
class movies:
    def __init__(self, title, description, gender):
        self.id = None
        self.title = title
        self.description = description
        self.gender = gender

    def __repr__(self):
        return f"{self.id} | {self.title} | {self.description} | {self.gender}"


class client:
    def __init__(self, name, CNP):
        self.id = None
        self.name = name
        self.CNP = CNP

    def __repr__(self):
        return f"{self.id} | {self.name} | {self.CNP}"
