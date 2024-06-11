class Square:

    def __init__(self,size=0, position=(0,0)):
        self.size = size
        self.position = position
    
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

    @property
    def position(self):
        """Getter method for position"""
        return self._position

    @position.setter
    def position(self, value):
        """Setter method for position with validation"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #"""
        if self.__size == 0:
            print("")
            return

        # Print the newlines for the vertical position
        for _ in range(self._position[1]):
            print("")

        # Print the square
        for _ in range(self.__size):
            print(" " * self._position[0] + "#" * self.__size)

s = Square(3, (1, 2))
s.my_print()
print("Area:", s.area())  # Output: Area: 9

s.size = 5
s.position = (2, 1)
s.my_print()
print("Area:", s.area())  # Output: Area: 25

s.size = 0
s.my_print()