class Polygon:  
    '''
    This class is defined to help represent a geometric figure known as a polygon
    '''
    __slots__ = ["__name", "__sides"]     # to restrict class Polygon to using only two attributes at a time __name and __sides.

    def __init__(self, name, sides):
        '''
        This function initializes the object of Polygon class.
        name: str
        sides: list of int
        '''
        self.__name = name   # assigning the value of name to the attribute __name
        self.__sides = sides  # assigning the value of sides to the attribute __sides

    def get_name(self):
        '''
        This function is a getter function for the name attribute of the class object that returns the current value of name.
        '''
        return self.__name  # returning value of attribute __name

    def set_name(self, name):
        '''
        This function is a setter function for the name attribute of the class object that sets the value of the name to the given value.
        name: str
        '''
        self.__name = name  # assigning the value of name to __name but name is the new value given

    def get_sides(self):
        '''
        This function is a getter function for the sides attribute of the class obejct that returns the current value of sides in a list.
        '''
        return self.__sides  # returning the value of attribute __sides

    def set_sides(self, sides):
        '''
        This function is a setter function for the sides attribute of the class object that sets the value of the sides to the given value.
        sides: list of int
        '''
        self.__sides = sides  # assigning the value of sides to __sides but sides is the new value given

    def __eq__(self, other):
        '''
        This function checks the equality between two class objects by comparing the attributes.
        '''
        # isinstance checks if two defined objects are instances of the same class
        return isinstance(other, self.__class__) and self.__name == other.__name and self.__sides == other.__sides

    def __ne__(self, other):
        '''
        This function does the opposite of the __eq__ function and checks inequality of two class objects.
        '''
        return not self.__eq__(other)

    def __str__(self):
        '''
        This function returns a string value to a class object if it is printed 
        '''
        return f"{self.__name} with sides: {self.__sides}"  # returning f-string of the name and sides of the polygon

    def calculate_circumference(self):
        '''
        This function helps calculate the circumfrnece of the polygon by adding the values in the list
        '''
        c = 0
        for i in self.__sides:  # iterating through the sides(list of integers) and returning the sum of sides
            c += i
        return c

def main():
    '''
    This function instantiates three Polygon objects: a triangle, a square, and a hexagon with appropriate side lengths 
    and prints each objects string representation and circumference.
    '''
    triangle = Polygon("Triangle", [3, 3, 3])
    square = Polygon("Square", [4, 4, 4, 4])
    hexagon = Polygon("Hexagon", [6, 6, 6, 6, 6, 6])

    print(triangle)  # will print the string representation of triangle class object
    print(f"Circumference: {triangle.calculate_circumference()}")

    print(square)    # will print the string representation of square class object
    print(f"Circumference: {square.calculate_circumference()}")

    print(hexagon)   # will print the string representation of hexagon class object 
    print(f"Circumference: {hexagon.calculate_circumference()}")


if __name__ == "__main__":  # defining main script to check execution of code
    main()