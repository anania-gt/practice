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
    

r=Rectangle(3,5)
print(r.height)
print(r.width)
print(r.area())
print(r.perimeter())