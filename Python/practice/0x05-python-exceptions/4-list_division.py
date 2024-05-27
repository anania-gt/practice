def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
                raise IndexError
            try:
                result.append(my_list_1[i] / my_list_2[i])
            except ZeroDivisionError:
                print("division by 0")
                result.append(0)
            except (TypeError, ValueError):
                print("wrong type")
                result.append(0)
    except IndexError:
        pass
    finally:
        return result

# Example usage:
my_list_1 = [10, 20, 30]
my_list_2 = [2, 0, 'a']
list_length = 5
result = list_division(my_list_1, my_list_2, list_length)
print(result)
