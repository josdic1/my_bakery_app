from lib.models import CONN, CURSOR

class Recipe:
    def __init__(self, name, type, steps):
        self.name = name