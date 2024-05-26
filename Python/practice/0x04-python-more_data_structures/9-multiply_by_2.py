def multiply_by_2(a_dictionary):
    new_dict = {}
    for key in a_dictionary:
        new_dict[key]=a_dictionary[key]*2
    print (new_dict)
a_dictionary = {'a': 1, 'b': 2, 'c': 3}
multiply_by_2(a_dictionary)