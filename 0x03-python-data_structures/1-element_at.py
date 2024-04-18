#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    numofele = len(my_list)
    if idx >= numofele:
        return None
    return (my_list[idx])
