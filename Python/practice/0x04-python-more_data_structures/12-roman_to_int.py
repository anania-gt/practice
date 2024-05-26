def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    
    # Define the mapping of Roman numerals to integers
    roman_to_int_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # Initialize the total value
    total = 0
    prev_value = 0
    
    # Traverse the string in reverse
    for char in reversed(roman_string):
        value = roman_to_int_map.get(char, 0)
        if value >= prev_value:
            total += value
        else:
            total -= value
        prev_value = value
    
    return total

# Example usage
print(roman_to_int("III"))    # Output: 3
print(roman_to_int("IV"))     # Output: 4
print(roman_to_int("IX"))     # Output: 9
print(roman_to_int("LVIII"))  # Output: 58
print(roman_to_int("MCMXCIV"))# Output: 1994
