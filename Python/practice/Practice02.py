class Person:
    def __init__(self, name):
        self._name = name  # Note the use of a private attribute (by convention)

    @property
    def name(self):
        """Getter method."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter method."""
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value

    @name.deleter
    def name(self):
        """Deleter method."""
        del self._name

# Example Usage:
p = Person("Alice")
print(p.name)  # Uses the getter method
p.name = "Bob"  # Uses the setter method
print(p.name)
del p.name  # Uses the deleter method
