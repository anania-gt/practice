def delete_at(my_list=[], idx=0):
    if idx >= len(my_list) or idx < 0:
        return my_list
    else:
        my_list.remove(my_list[idx])
        return my_list
my_list = [1, 2, 3, 4, 5]
print(delete_at(my_list,4))