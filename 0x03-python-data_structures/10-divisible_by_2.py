#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    copy = []
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            copy.append(True)
        else:
            copy.append(False)

    return (copy)

