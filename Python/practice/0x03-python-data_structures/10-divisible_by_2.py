def divisible_by_2(my_list=[]):
    # Initialize an empty list to store True/False values
    result_list = []
    
    # Iterate over the elements in the original list
    for num in my_list:
        # Check if the number is divisible by 2
        if num % 2 == 0:
            result_list.append(num)
        
    return result_list

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(divisible_by_2(my_list))  # Output: [False, True, False, True, False, True, False, True, False, True]
