class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_perimetr(self):
        return 2 * (self.width + self.height)


# print(__name__)
__author__ = "Alexandru"

if __name__ == '__main__':
    print(f'Module {__name__} (author: {__author__})')
    r1 = Rectangle(10, 20)
    r2 = Rectangle(30, 40)
    print('r1', r1.get_perimetr())
    print('r2', r2.get_perimetr())