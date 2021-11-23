# This file performs tests on the data structures and algorithms

import global_variables as gb
import helpers as hp
import matplotlib.pyplot as plt
import timeit
import math
import random
import custom_linked_list as cl

from timeit import timeit
import string


# ------------------------------------------------------------------------------------------------------- #
# ------------------------------------- TESTING SEARCH -------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------- #

def plot_search_runtime(lo=100, hi=200, search_exist=True, num=0):
    sl_arr = []
    sl_bin_arr = []
    sd_arr = []
    sdll_arr = []

    global my_list, search_term, my_dict, my_dllist

    for n in range(lo, hi):
        my_list = []
        my_list[:] = gb.data_list[:n][:]
        my_dllist = cl.DoublyLinkedList()

        word_list = []
        for row in my_list:
            my_dllist.Insert(row[0],row[1],row[2])
            word_list.append(row[0])

        my_dict = dict((k, gb.data_dict[k]) for k in word_list if k in gb.data_dict)

        if search_exist:
            search_term = random.choice(word_list)
        else:
            search_term = ''.join(random.choice(string.ascii_lowercase) for i in range(5))

        list_search_linear = timeit('hp.search_list(my_list,search_term)', number=1, globals=globals())
        list_search_binary = timeit('hp.search_list_binary(my_list,search_term)', number=1, globals=globals())
        dict_search = timeit('hp.search_dict(my_dict, search_term)', number=1, globals=globals())
        dllist_search = timeit('my_dllist.Search(search_term)', number=1, globals=globals())

        sl_arr.append(list_search_linear)
        sl_bin_arr.append(list_search_binary)
        sd_arr.append(dict_search)
        sdll_arr.append(dllist_search)

    plt.figure(num)
    plt.plot(sl_arr, label="Linear search on List")
    plt.plot(sl_bin_arr, label="Binary search on List")
    plt.plot(sd_arr, label="Search on Dictionary")
    plt.plot(sdll_arr, label="Search on DoublyLinkedList", c ="lightgreen",linestyle='dashed')
    plt.legend()
    if search_exist:
        plt.title("Search of existing words")
    else:
        plt.title("Search of nonexistent words")
    return plt


# ------------------------------------------------------------------------------------------------------- #
# ------------------------------------- TESTING INSERT -------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------- #

def plot_insert_runtime(lo=100, hi=len(gb.data_list) - 1, word_exist=True, num=0):
    li_sort = []
    li_no_sort = []
    di = []
    dll = []

    global my_list, word, my_dict, meaning, word_type, my_dllist

    for n in range(lo, hi):
        my_list = []
        my_list[:] = gb.data_list[:n][:]
        my_dllist = cl.DoublyLinkedList()

        word_list = []
        for row in my_list:
            my_dllist.Insert(row[0],row[1],row[2])
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
        dllist_insert = timeit('my_dllist.Insert(word,word_type,meaning)', number=1, globals=globals())

        li_sort.append(list_insert_with_sort)
        li_no_sort.append(list_insert_no_sort)
        di.append(dict_insert)
        dll.append(dllist_insert)

    plt.figure(num)
    plt.plot(li_sort, label="Insert on List and Sort")
    plt.plot(li_no_sort, label="Insert on List No Sorting (Using Binary Search)")
    plt.plot(di, label="Insert on Dictionary")
    plt.plot(dll, label="Insert on DoublyLinkedList",c ="lightgreen",linestyle='dashed')

    if word_exist:
        plt.title("Insertion of meaning of existing words")
    else:
        plt.title("Insertion of meaning of new words")
    plt.legend()
    return plt


# ------------------------------------------------------------------------------------------------------- #
# ------------------------------------- TESTING DELETE -------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------- #

def plot_delete_runtime(lo=100, hi=len(gb.data_list) - 1, word_exist=True, num=0):
    ldarr = []
    ddarr = []
    ldbinarr = []
    sdll_arr = []

    global my_list, word, my_dict, meaning, word_type, my_dllist

    for n in range(lo, hi):
        my_list = []
        my_list[:] = gb.data_list[:n][:]
        my_dllist = cl.DoublyLinkedList()

        word_list = []
        for row in my_list:
            my_dllist.Insert(row[0],row[1],row[2])
            word_list.append(row[0])

        my_dict = dict((k, gb.data_dict[k]) for k in word_list if k in gb.data_dict)

        # Generate random
        if word_exist:
            word = random.choice(word_list)
        else:
            word = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
        word_type = "n."
        meaning = ''.join(random.choice(string.ascii_lowercase) for i in range(20))

        list_delete = timeit('hp.delete_word_from_list(my_list,word)',
                                    number=1, globals=globals())
        list_delete_binary = timeit('hp.delete_word_from_list_binary(my_list,word)',
                             number=1, globals=globals())
        dict_delete = timeit('hp.delete_word_from_dict(my_dict,word)',
                                    number=1, globals=globals())
        dllist_delete = timeit('my_dllist.Delete(word)', number=1, globals=globals())

        ldarr.append(list_delete)
        ldbinarr.append(list_delete_binary)
        ddarr.append(dict_delete)
        sdll_arr.append(dllist_delete)

    plt.figure(num)
    plt.plot(ldarr, label="Delete on List")
    plt.plot(ldbinarr, label="Delete on List Using Binary Search")
    plt.plot(ddarr, label="Delete on Dictionary", c="g")
    plt.plot(sdll_arr, label="Delete on DoublyLinkedList", c ="lightgreen",linestyle='dashed')

    if word_exist:
        plt.title("Deletion of meaning of existing words")
    else:
        plt.title("Deletion of meaning of nonexistent words")
    plt.legend()
    return plt

# ------------------------------------------------------------------------------------------------------- #

lo = 50
hi = 300

num_start = -1
def add_one():
    global num_start
    num_start += 1
    return num_start

# ------------------------------------------------------------------------------------------------------- #

# plot_search_runtime(lo=lo, hi=hi, search_exist=True, num=add_one())
# plot_search_runtime(lo=lo, hi=hi, search_exist=False, num=add_one())
# plt.show()

# ------------------------------------------------------------------------------------------------------- #

plot_insert_runtime(lo=lo, hi=hi, word_exist=True, num=add_one())
plot_insert_runtime(lo=lo, hi=hi, word_exist=False, num=add_one())
plt.show()

# ------------------------------------------------------------------------------------------------------- #

# plot_delete_runtime(lo=lo, hi=hi, word_exist=True, num=add_one())
# plot_delete_runtime(lo=lo, hi=hi, word_exist=False, num=add_one())
# plt.show()

# ------------------------------------------------------------------------------------------------------- #
