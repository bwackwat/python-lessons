
class User:
    def __init__(self, name):
        if not len(name):
            raise Exception("Please provide a name.")
        self.name = name

if __name__ == '__main__':
    while True:
        new_name = input("Please enter a name: ")
