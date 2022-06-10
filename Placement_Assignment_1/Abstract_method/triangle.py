from shape import Shape

class Triangle(Shape):
    def __init__(self) -> None:
        super().__init__("Triangle")
    
    def draw(self):
        print('Drawing a Triangle')