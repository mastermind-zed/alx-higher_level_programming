#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """ function that divides element by element 2 lists. """

     x = []
    y = 0.0
    z = 0
    for i in range(0, list_length):
        y = 0
        try:
            y = my_list_1[i] / my_list_2[i]
            z = 1
        except ZeroDivisionError:
            print("division by 0")
            x += [0]
        except (TypeError):
            print("wrong type")
            x += [0]
        except IndexError:
            print("out of range")
            x += [0]
        finally:
            if z == 1:
                z = 0
                x += [y]
    return x
