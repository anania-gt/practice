def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print(value)
            return True
        else:
            raise ValueError
    except ValueError:
        print(f"{value} is not a valid integer")
        return False

# Example usage
print(safe_print_integer(42))     # Should print: 42 and return True
#print(safe_print_integer("hello")) # Should print: hello is not a valid integer and return False
