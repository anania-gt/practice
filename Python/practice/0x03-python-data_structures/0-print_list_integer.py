# def print_list_integer(my_list=[]):
#     for i in (my_list):
#         if isinstance(i, int):
#             print("{}".format(i))
# my_list = [1, 2, 3, 4, 5]
# print_list_integer(my_list)

def print_list_integer(my_list=[]):
    for integer in my_list:
        print("{:d}".format(integer))

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
