def new_in_list(my_list, idx, element):
    if idx<0 or idx>=len(my_list): 
        new_list = my_list.copy()
        print("{}".format(new_list))
    else:
        new_list=my_list.copy()
        new_list[idx] = element
        print("{}".format(new_list))

my_list = [1, 2, 3, 4, 5]
new_in_list(my_list,8,10)