from time import approx
def calculate_circumference(self):
        '''
        This function helps calculate the circumfrnece of the polygon by adding the values in the list
        '''
        c = 0
        for i in self.__sides:  # iterating through the sides(list of integers) and returning the sum of sides
            c += i
        return c


def test_str():
    '''
    This function checks if the string representation gives correct string
    '''
    poly = Polygon("Triangle", [3,3,3])
    should_print = "Triangle with sides: [3, 3, 3]" 
    
    assert str(poly) == should_print  # checks if string of object poly is giving same output 

def test_circumfrence():
    '''
    This function checks if the circumference function returns the correct sum of sides
    '''
    poly = Polygon("Triangle", [3,3,3])
    
    assert poly.calculate_circumference() == approx(9.0)  # approx function from pytest module does floating-point comparison 

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


if __name__ == "__main__":  # defining main script to check execution of code
    main()