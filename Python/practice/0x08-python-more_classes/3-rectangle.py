class Rectangle:

    def __init__(self,width=0,height=0):
        self.__width = width
        self.__height = height
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self,value):
        if not isinstance(value,int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("width must be positive")
        self.__width = value
    
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value,int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("height must be positive")
        self.__height = value

    
    def area(self):
        return self.__height*self.__width
    
    def perimeter(self):
        
        if self.__height == 0 or self.__width == 0:
            return 0

        return 2*(self.__height*self.__width)
    def __str__(self):
        """Returns the string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = ""
        for _ in range(self.__height):
            rect_str += "#" * self.__width + "\n"
        return rect_str.rstrip()

# Example usage:
rect1 = Rectangle(3, 2)
print(str(rect1))
# Output:
# ###
# ###
print("Area:", rect1.area())  # Output: Area: 6
print("Perimeter:", rect1.perimeter())  # Output: Perimeter: 10

rect2 = Rectangle(0, 2)
print(str(rect2))  # Output: (empty string)
print("Area:", rect2.area())  # Output: Area: 0
print("Perimeter:", rect2.perimeter())  # Output: Perimeter: 0