class Polygon:
    def __init__(self, name, sides):
       
        self.name = name
        self.sides = sides

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_sides(self):
        return self.sides

    def set_sides(self, sides):
        self.sides = sides

    def __eq__(self, other):
        if not isinstance(other, Polygon):
            return False
        return self.name == other.name and self.sides == other.sides

    def __ne__(self, other):
        return not self.__eq__(other)

    
    def __str__(self):
        return f"{self.name} sides: {self.sides}"

    
    def calculate_circumference(self):
        return sum(self.sides)


def main():
    
    
    triangle = Polygon("triangle", [2, 3, 4])
    square = Polygon("square", [7, 7, 7, 7])
    hexagon = Polygon("hexagon", [3, 3, 3, 3, 3, 3])

    
    for polygon in [triangle, square, hexagon]:
        print(polygon)
        print(f"circumference : {polygon.calculate_circumference()}\n")


if __name__ == "__main__":
    main()
