#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """ function that divides element by element 2 lists. """

     newlist = []
    for y in range(list_length):
        try:
            newlist.append(my_list_1[y] / my_list_2[y])
        except(TypeError, ZeroDivisionError, IndexError) as err:
            if (isinstance(err, ZeroDivisionError)):
                print("division by 0")
            elif (isinstance(err, TypeError)):
                print("wrong type")
            elif (isinstance(err, IndexError)):
                print("out of range")
            newlist.append(0)
        finally:
            pass
    return (newlist)
