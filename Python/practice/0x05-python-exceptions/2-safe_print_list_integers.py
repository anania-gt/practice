def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Counter for the number of integers printed
    try:
        for i in range(x):
            try:
                print("{:d} ".format(my_list[i]), end="")
                count += 1
            except (ValueError, TypeError):
                print(f"{my_list[i]} is not an integer")
    except IndexError:
        pass
    finally:
        print()  # Print a newline at the end
    return count

# Example usage
example_list = [1, 'two', 3, 'four', 5]
elements_to_print = 7
printed_elements = safe_print_list_integers(example_list, elements_to_print)
print(f"Number of integers printed: {printed_elements}")
