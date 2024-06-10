def replace_in_list(my_list, idx, element):
    if idx<0 or idx >=len(my_list):
        print("{}".format(my_list))
    else:
        my_list[idx]=element
        print("{}".format(my_list))

my_list = [1, 2, 3, 4, 5]
replace_in_list(my_list,2,10)