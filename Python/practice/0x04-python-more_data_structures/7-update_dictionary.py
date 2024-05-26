def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value

# Example usage
a_dictionary = {'a': 1, 'b': 2, 'c': 3}
update_dictionary(a_dictionary, "z", "2")
print(a_dictionary)  # Output: {'a': 1, 'b': 2, 'c': 3, 'z': '2'}

update_dictionary(a_dictionary, "b", 5)
print(a_dictionary)  # Output: {'a': 1, 'b': 5, 'c': 3, 'z': '2'}

