from polygon import Polygon

def test_polygon_initialization():
    '''
    This function tests if the attributes of __init__() function are initialized porperly
    '''
    poly = Polygon("Pentagon", [5,5,5,5,5])

    assert poly.get_name() == "Pentagon"
    assert poly.get_sides() == [5,5,5,5,5]  # to check if name and sides are working correctly in Polygon class

def test_get_name():
    '''
    This function checks if the function get_name() returns the name correctly
    '''
    poly = Polygon("Triangle", [3,3,3])

    assert poly.get_name() == "Triangle"  # checks if value of name is returned properly

def test_set_name():
    '''
    This function checks if the set_name() function sets new value of name correctly
    '''
    poly = Polygon("Hexagon", [6,6,6,6,6,6])
    poly.set_name("Rectangle")

    assert poly.get_name() == "Rectangle"  # checks if value of name is changed properly

def test_get_sides():
    '''
    This function checks if the get_sides() function returns the value sides correctly
    '''
    poly = Polygon("Heptagon", [7,7,7,7,7,7,7])

    assert poly.get_sides() == [7,7,7,7,7,7,7]  # checks if value of sides is returned properly

def test_set_sides():
    '''
    This function checks if the set_sides() function sets the new value of sides correctly
    '''
    poly = Polygon("Octagon", [8,8,8,8,8,8,8,8])
    poly.set_sides([7,7,7,7,7,7,7])

    assert poly.get_sides() == [7,7,7,7,7,7,7]  # checks if the value of sides is changed properly

def test_equality():
    '''
    This function checks if equality operator is correctly defined
    '''
    poly1 = Polygon("Rectangle", [4,4,4,4])
    poly2 = Polygon("Rectangle", [4,4,4,4])

    assert poly1 == poly2  # checking betweeen 2 objects if they are equal

def test_inequality():
    '''
    This function checks if inequality operator is correctly defined
    '''
    poly1 = Polygon("Rectangle", [4,4,4,4])
    poly2 = Polygon("Triangle", [3,3,3])

    assert poly1 != poly2  # checking between 2 objects if they are not equal