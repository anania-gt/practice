def multiply_list_map(my_list=[], number=0):
    new_list = list(map(lambda x: x*number, my_list))
    return new_list


example_list = [1, 2, 3, 4, 5]
multiplied_list = multiply_list_map(example_list, 3)
print(multiplied_list)  # Output: [3, 6, 9, 12, 15]
