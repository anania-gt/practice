def no_c(my_string):
    new_string = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string

# Example usage:
original_string = "Helloc, WorldC! This is a test string."
print(no_c(original_string))  # Output: "Hello, World! This is a test string."
