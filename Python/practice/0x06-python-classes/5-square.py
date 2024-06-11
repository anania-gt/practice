class Square:

    def __init__(self,size=0):
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
    
    def my_print(self):
        """Prints the square with the character #"""

        if self.__size == 0:
            print("")
        else:
            for x in range(self.__size):
                print("#" * self.__size)
    
s = Square(3)
print(s.size)  # Output: 3
print(s.area())
s.my_print()