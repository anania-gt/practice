def search_replace(my_list, search, replace):
    # Create a new list with replaced values
    new_list = [replace if x == search else x for x in my_list]


    return new_list

# Example usage:
my_list = [1, 2, 3, 2, 4, 2]
search = 2
replace = 5
print(search_replace(my_list, search, replace))  # Output: [1, 5, 3, 5, 4, 5]
