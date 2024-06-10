def max_integer(my_list=[]):
    # Check if the list is empty
    if len(my_list) == 0:
        return None
    
    # Initialize the maximum value with the first element of the list
    max_value = my_list[0]
    
    # Iterate over the list to find the maximum value
    for num in my_list:
        if num > max_value:
            max_value = num
    
    return max_value

# Example usage:
my_list = [1, 5, 3, 9, 2]
print(max_integer(my_list))  # Output: 9

empty_list = []
print(max_integer(empty_list))  # Output: None
