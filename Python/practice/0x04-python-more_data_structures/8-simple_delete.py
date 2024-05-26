def remove_key(a_dictionary, key):
    if key in a_dictionary:
        del a_dictionary[key]

# Example usage
a_dictionary = {'a': 1, 'b': 2, 'c': 3}
remove_key(a_dictionary, 'b')
print(a_dictionary)  # Output: {'a': 1, 'c': 3}

remove_key(a_dictionary, 'z')  # Key 'z' does not exist
print(a_dictionary)  # Output: {'a': 1, 'c': 3}


