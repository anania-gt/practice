def safe_print_list(my_list=[], x=0):
    counter=0
    try:
         for i in range(x) :
              print(f"{my_list[i]} ",end="")
              counter+=1

    except IndexError:
         print("Index out of range")
    
    finally:
         print()
    return counter

example_list = [1, 'two', 3, 'four', 5]
elements_to_print = 2
printed_elements = safe_print_list(example_list, elements_to_print)
print(f"Number of elements printed: {printed_elements}")