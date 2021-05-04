import bootstrap

class Model:
    def __init__(self):
        self.connection = bootstrap.get_connection()
        self.cursor = bootstrap.get_cursor()

