def best_score(a_dictionary):
    best_key = None
    max_value = float('-inf')  # Initialize max_value to negative infinity
    
    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            best_key = key
    
    return best_key

# Example usage
example_dict = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
result = best_score(example_dict)
print(result)  # Output: 'Bob'
