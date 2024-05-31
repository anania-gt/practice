class Square:
    """Class that defines a square by its size."""
    
    def __init__(self, size=0):
        """
        Initialize a new Square.
        
        Parameters:
        size (int): The size of the square. Default is 0.
        
        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """
        self.size = size  # This will use the setter for validation

    @property
    def size(self):
        """Getter for the size property."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size property with validation.
        
        Parameters:
        value (int): The new size of the square.
        
        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        """Calculate the area of the square.
        
        Returns:
        int: The area of the square.
        """
        return self.__size ** 2

# Example Usage
try:
    s = Square(5)
    print(s.size)       # Output: 5
    print(s.area())     # Output: 25

    s.size = 10
    print(s.size)       # Output: 10
    print(s.area())     # Output: 100

    s.size = -3         # Raises ValueError: size must be >= 0
except (TypeError, ValueError) as e:
    print(e)
