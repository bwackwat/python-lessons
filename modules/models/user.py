
class User:
    def __init__(self, name):
        if not len(name):
            raise Exception("Please provide a name.")
        self.name = name
