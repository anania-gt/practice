class Square:
    def __init__(self,size):
        self.size = size


    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self,value):

        if not isinstance(value,int):
            raise TypeError("Value must be an integer")
        
        if value < 0:
            raise ValueError("Value must be greater than zero")

        self.__size=value

    def area(self):
        return self.__size**2
    

s = Square(3)
print(s.size)  # Output: 3
print(s.area())