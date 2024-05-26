def uniq_add(my_list=[]):
    unique_integers = set(my_list)  # Convert the list to a set to remove duplicates
    total_sum = sum(unique_integers)  # Sum the unique integers
    return total_sum

# Example usage
print(uniq_add([1, 2, 3, 2, 4, 3, 5]))  # Output: 15
