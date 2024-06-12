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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1,Rectangle):
            raise TypeError("rect_1 must be a Rectangle")
        if not isinstance(rect_2,Rectangle):
            raise TypeError("rect_2 must be a Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2
    @classmethod
    def square(cls, size=0):
        new_rect = Rectangle(size, size)
        return new_rect

# Example usage:
rect1 = Rectangle()
rect1.height = 2
rect1.width = 4
print(rect1)
print(Rectangle.number_of_instances)  # Output: 1

rect2 = Rectangle(2, 2)
print(Rectangle.number_of_instances)  # Output: 2

print(Rectangle.bigger_or_equal(rect1, rect2)) 
print(Rectangle.bigger_or_equal(rect1, rect2))
print(Rectangle.square(2))

del rect1
print(Rectangle.number_of_instances)  # Output: 1

del rect2
print(Rectangle.number_of_instances)  # Output: 0

