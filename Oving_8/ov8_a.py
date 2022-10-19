from matplotlib.pyplot import polar


class contry:
    def __init__(self, name, population = None, area = None):
        self.name = name
        self.population = population or None
        self.area = area