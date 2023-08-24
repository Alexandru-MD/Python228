class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_perimetr(self):
        return 2 * (self.width + self.height)


