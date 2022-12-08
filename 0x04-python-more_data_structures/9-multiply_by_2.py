#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dico = a_dictionary.copy()
    list_keys = list(new_dico.keys())

    for i in list_keys:
        new_dico[i] *= 2

    return (new_dico)
