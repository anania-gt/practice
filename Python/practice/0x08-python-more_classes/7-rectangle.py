class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        return self._width * self._height

    def perimeter(self):
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def __str__(self):
        if self._width == 0 or self._height == 0:
            return ""
        rect_str = ""
        for _ in range(self._height):
            rect_str += str(Rectangle.print_symbol) * self._width + "\n"
        return rect_str.rstrip()

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

# Example usage:
rect1 = Rectangle()
rect1.height = 2
rect1.width = 4
print(rect1)
print(Rectangle.number_of_instances)  # Output: 1

rect2 = Rectangle(2, 2)
print(Rectangle.number_of_instances)  # Output: 2

del rect1
print(Rectangle.number_of_instances)  # Output: 1

del rect2
print(Rectangle.number_of_instances)  # Output: 0
