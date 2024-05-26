def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary):
        print(f"{key}: {a_dictionary[key]}")
    for value in a_dictionary.values():
        print(value)

# Example usage
example_dict = {'b': 2, 'a': 1, 'c': 3,'d':None}
print_sorted_dictionary(example_dict)
