from shape import Shape

class Circle(Shape):
    def __init__(self) -> None:
        super().__init__("Circle")
    
    def draw(self):
        print('Drawing a Circle')