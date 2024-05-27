class Square:
    """"""
    def __init__(self,size=0):
        if type(size) is not int:
            raise TypeError
        if size < 0:
            raise ValueError
        self.__size = size