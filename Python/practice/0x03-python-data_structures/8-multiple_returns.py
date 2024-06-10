def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])

# Example usage:
sentence = "Hello, world!"
print(multiple_returns(sentence))  # Output: (13, 'H')

empty_sentence = ""
print(multiple_returns(empty_sentence))  # Output: (0, None)
