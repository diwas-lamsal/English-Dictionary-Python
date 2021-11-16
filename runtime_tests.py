# This file performs tests on the data structures and algorithms

import global_variables as gb
import helpers as hp
import matplotlib.pyplot as plt
import timeit
import math
import random

from timeit import timeit
import string


# ------------------------------------------------------------------------------------------------------- #
# ------------------------------------- TESTING SEARCH -------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------- #

def plot_search_runtime(lo=100, hi=200, search_exist=True):
    sl_arr = []
    sl_bin_arr = []
    sd_arr = []

    global my_list, search_term, my_dict

    for n in range(lo, hi):
        my_list = []
        my_list[:] = gb.data_list[:n][:]

        word_list = []
        for row in my_list:
            word_list.append(row[0])

        my_dict = dict((k, gb.data_dict[k]) for k in word_list if k in gb.data_dict)

        if search_exist:
            search_term = random.choice(word_list)
        else:
            search_term = ''.join(random.choice(string.ascii_lowercase) for i in range(5))

        list_search_linear = timeit('hp.search_list(my_list,search_term)', number=1, globals=globals())
        list_search_binary = timeit('hp.search_list_binary(my_list,search_term)', number=1, globals=globals())
        dict_search = timeit('hp.search_dict(my_dict, search_term)', number=1, globals=globals())

        sl_arr.append(list_search_linear)
        sl_bin_arr.append(list_search_binary)
        sd_arr.append(dict_search)

    plt.plot(sl_arr, label="Linear search on List")
    plt.plot(sl_bin_arr, label="Binary search on List")
    plt.plot(sd_arr, label="Search on Dictionary")
    plt.legend()
    if search_exist:
        plt.title("Search of existing words")
    else:
        plt.title("Search of nonexistent words")
    plt.show()


# ------------------------------------------------------------------------------------------------------- #

# plot_search_runtime(lo=100, hi=400, search_exist=True)


# ------------------------------------------------------------------------------------------------------- #


# ------------------------------------------------------------------------------------------------------- #
# ------------------------------------- TESTING INSERT -------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------- #

def plot_insert_runtime(lo=100, hi=len(gb.data_list) - 1, word_exist=True):
    li_sort = []
    li_no_sort = []
    di = []

    global my_list, word, my_dict, meaning, word_type

    for n in range(lo, hi):
        my_list = []
        my_list[:] = gb.data_list[:n][:]

        word_list = []
        for row in my_list:
            word_list.append(row[0])

        my_dict = dict((k, gb.data_dict[k]) for k in word_list if k in gb.data_dict)

        # Generate random
        if word_exist:
            word = random.choice(word_list)
        else:
            word = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
        word_type = "n."
        meaning = ''.join(random.choice(string.ascii_lowercase) for i in range(20))

        list_insert_with_sort = timeit('hp.add_meaning_to_list(my_list,word,word_type,meaning,True)',
                                    number=1, globals=globals())
        list_insert_no_sort = timeit('hp.add_meaning_to_list(my_list,word,word_type,meaning,False)',
                                    number=1, globals=globals())
        dict_insert = timeit('hp.add_meaning_to_dict(my_dict,word,word_type,meaning)',
                                    number=1, globals=globals())

        li_sort.append(list_insert_with_sort)
        li_no_sort.append(list_insert_no_sort)
        di.append(dict_insert)

    plt.plot(li_sort, label="Insert on List and Sort")
    plt.plot(li_no_sort, label="Insert on List No Sorting (Using Binary Search)")
    plt.plot(di, label="Insert on Dictionary")
    if word_exist:
        plt.title("Insertion of meaning of existing words")
    else:
        plt.title("Insertion of meaning of new words")
    plt.legend()
    plt.show()

# ------------------------------------------------------------------------------------------------------- #

plot_insert_runtime(lo=200, hi=500, word_exist=False)
