import csv
import glob
import pickle
import os


# --------------------------------------------------------------------------------------------------

def merge_csv_files(foldername="dictionary"):
    """
    This function merges the contents of every word csv file (ex: A.csv, B.csv, etc.) to a single csv file
    In the unprepared CSV files, the words and their meanings are not separated and are a single sentence
    This function also separates them for searching
    :param foldername: The folder where the list of csv files are stored
    :return: The merged contents as a list
    """
    csv.field_size_limit(256 << 20)
    meaning_list_all = []
    csv_files = glob.glob(foldername + "/*.csv")

    # Get all the lines from each csv files for each alphabet into a single meaning list
    for filename in csv_files:
        with open(filename, newline='') as csvfile:
            meaning_list_all = meaning_list_all + list(csv.reader(csvfile))

    # Remove all the blank lines
    meaning_list = [e for e in meaning_list_all if e]

    # Loop through all the lines to prepare the list
    for i in range(len(meaning_list)):
        try:
            split_opening = meaning_list[i][0].split(' (', 1)
            meaning_list[i][0] = split_opening[0]
            split_closing = split_opening[1].split(')', 1)
            split_middle = f"({split_closing[0]})"
            meaning_list[i].append(split_middle)
            meaning_list[i].append(split_closing[1])
        except Exception as e:
            continue

    # Remove the invalid rows
    meaning_list = [x for x in meaning_list if len(x) == 3]

    # Sort meaning list in ascending order according to the word (first index of each row is the word)
    meaning_list = sorted(meaning_list, key=lambda s: s[0].lower())

    # The meaning list is now ready to be saved as a CSV file
    with open('dictionary.csv', 'w', newline='') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f)
        write.writerows(meaning_list)

    return meaning_list


# --------------------------------------------------------------------------------------------------
# --------------------------OPERATIONS ON LIST DATA STRUCTURE---------------------------------------
# --------------------------------------------------------------------------------------------------

def csv_to_list(csv_filename, list_save_name):
    """
    Creates a list from the given csv file and saves it to a binary file
    :param csv_filename: File name of the csv to convert into a list
    :param list_save_name: The filename for saving the list as a binary file
    :return: The converted list
    """
    csv.field_size_limit(256 << 20)
    meaning_list = []
    with open(csv_filename, newline='') as csvfile:
        meaning_list = meaning_list + list(csv.reader(csvfile))
        # https://www.kite.com/python/answers/how-to-save-a-dictionary-to-a-file-in-python
        a_file = open(list_save_name, "wb")
        pickle.dump(meaning_list, a_file)
        a_file.close()
        return meaning_list


# --------------------------------------------------------------------------------------------------

def load_list_from_file(filename="meaning_data_as_list.pkl"):
    """
    Load list data from binary file
    :param filename: Name of the binary file to load the list from
    :return: The list extracted from the file
    """
    a_file = open(filename, "rb")
    output = pickle.load(a_file)
    return output


# --------------------------------------------------------------------------------------------------

def add_meaning_to_list(meaning_list, word, type, meaning, sort_list=False):
    """
    This function can be used to add a meaning to the english dictionary
    :param meaning_list: The list of meaning
    :param word: The word to be added
    :param type: The type of word
    :param meaning: The meaning of the word
    :param sort_list: Either to add the item at the end, and then sort the list or add it to proper position
    :return: the list after adding the element
    """

    if sort_list:
        # If the sort_list variable is True, append the element to the end of the list
        meaning_list.append([word, "(" + type + ")", meaning])

        # Then sort the list again

        # sorted() in python uses Timsort algorithm
        # Timsort combines merge sort and insertion sort
        # The running time is O(nlogn)
        # https://drops.dagstuhl.de/opus/volltexte/2018/9467/pdf/LIPIcs-ESA-2018-4.pdf
        meaning_list = sorted(meaning_list, key=lambda s: s[0].lower())
        return meaning_list
    else:
        # Recursively perform binary search to find the right index to place the new word and insert it there
        # Code taken and modified from stackoverflow:
        # https://stackoverflow.com/questions/41902958/insert-item-into-case-insensitive-sorted-list-in-python
        key = word.lower()
        lo, hi = 0, len(meaning_list)
        while lo < hi:
            mid = (lo + hi) // 2
            if key < meaning_list[mid][0].lower():
                hi = mid
            else:
                lo = mid + 1
        meaning_list.insert(lo, [word, "(" + type + ")", meaning])
        return meaning_list


# --------------------------------------------------------------------------------------------------


def delete_word_from_list(meaning_list, word):
    """
    Finds the given word in the list and deletes it if exists
    :param meaning_list: The list to delete the word from
    :param word: The word to delete
    :return: The new list after deleting the word, True of False based on whether the word was found
    """
    # https://stackoverflow.com/questions/2793324/is-there-a-simple-way-to-delete-a-list-element-by-value
    if word.casefold() in [x[0].casefold() for x in meaning_list]:
        meaning_list = [x for x in meaning_list if x[0].casefold() != word.casefold()]
        return [meaning_list, True]
    else:
        return [meaning_list, False]


# --------------------------------------------------------------------------------------------------

def save_list_to_file(meaning_list, csv_filename="dictionary.csv",
                      list_filename="meaning_data_as_list.pkl",
                      dict_filename="meaning_data_as_dictionary.pkl"):
    try:
        with open(csv_filename, 'w', newline='') as f:
            write = csv.writer(f)
            write.writerows(meaning_list)

        # Whenever the csv is saved, delete the list and dictionary binary files to reload them later
        if os.path.exists(list_filename):
            os.remove(list_filename)
        if os.path.exists(dict_filename):
            os.remove(dict_filename)
        return True
    except Exception as e:
        return False


# --------------------------------------------------------------------------------------------------

def search_list(meaning_list, word):
    """
    Linear search the meaning list for the given word and return found meanings
    :param meaning_list: The list to search
    :param word: The word for which to find the meaning
    :return: The set of meanings for the given word
    """
    filter_list = []
    found = False
    for row in meaning_list:
        if row[0].casefold() == word.casefold():
            found = True
        else:
            if found:
                break
            else:
                continue
        filter_list.append(row)
    return filter_list, found


# --------------------------------------------------------------------------------------------------

# Modified binary search for specific use to this english dictionary
# Running time rougly O(logn+m) where n is the number elements in the list and m is the number of matching words
def search_list_binary(meaning_list, word):
    """
    Binary search the meaning list for the given word and return found meanings
    :param meaning_list: The list to search
    :param word: The word for which to find the meaning
    :return: The set of meanings for the given word
    """
    filter_list = []
    found = False

    first = 0
    last = len(meaning_list) - 1
    while first <= last and not found:
        middle = (first + last) // 2
        if meaning_list[middle][0].casefold() == word.casefold():
            found = True
            filter_list.append(meaning_list[middle])

            ##################################################################
            # the modified part to perform search before and after the word
            # to get all the words

            # Check the previous elements
            previous = True
            previous_counter = 1
            while previous:
                if meaning_list[middle - previous_counter][0].casefold() == word.casefold():
                    filter_list.insert(0, meaning_list[middle - previous_counter])
                    previous_counter += 1
                else:
                    previous = False
            next = True
            next_counter = 1
            while next:
                if meaning_list[middle + next_counter][0].casefold() == word.casefold():
                    filter_list.append(meaning_list[middle - next_counter])
                    next_counter += 1
                else:
                    next = False
            ##################################################################
        else:
            if word.casefold() < meaning_list[middle][0].casefold():
                last = middle - 1
            else:
                first = middle + 1
    return filter_list, found


# --------------------------------------------------------------------------------------------------
# -----------------------OPERATIONS ON DICTIONARY DATA STRUCTURE------------------------------------
# --------------------------------------------------------------------------------------------------

def list_to_dictionary(meaning_list, dict_save_name):
    """
    Takes a list and converts it to a dictionary in context of this english dictionary application
    :param meaning_list: The list to convert to a dictionary data type
    :param dict_save_name: Name of the binary file to save the dictionary
    :return: The dictionary object created from the list
    """
    d = {}

    # https://stackoverflow.com/questions/48705143/efficiency-2d-list-to-dictionary-in-python
    # Runs in O(n)
    for elem in meaning_list:
        try:
            # using casefold() here to be able to perform case insensitive search later
            d[elem[0].casefold()].append([elem[0], elem[1], elem[2]])
        except KeyError:
            d[elem[0].casefold()] = [[elem[0], elem[1], elem[2]]]

    # https://www.kite.com/python/answers/how-to-save-a-dictionary-to-a-file-in-python
    a_file = open(dict_save_name, "wb")
    pickle.dump(d, a_file)
    a_file.close()
    return d


# --------------------------------------------------------------------------------------------------

def load_dictionary_from_file(filename="meaning_data_as_dictionary.pkl"):
    """
    Load dictionary data from binary file
    :param filename: Name of the binary file to load the dictionary from
    :return: The dictionary extracted from the file
    """
    a_file = open(filename, "rb")
    output = pickle.load(a_file)
    return output


# --------------------------------------------------------------------------------------------------

def search_dict(meaning_dict, word):
    """
    Search the dictionary for given word
    :param meaning_dict: The dictionary
    :param word: The word to search for meaning
    :return: The list containing meanings for the given word, True of False based on whether the word
             was found
    """
    found = False
    filtered_dict_list = []
    if word.casefold() in meaning_dict:
        found = True
        filtered_dict_list = meaning_dict[word.casefold()]
    return filtered_dict_list, found


# --------------------------------------------------------------------------------------------------

# Keeping for possible use later
# def sort_dict(d):
#     """
#     Sorts the items in the dictionary by key
#     :param d: The dictionary to sort
#     :return: The sorted dictionary
#     """
#     d = dict(sorted(d.items()))
#     return d


# --------------------------------------------------------------------------------------------------

def add_meaning_to_dict(meaning_dict, word, type, meaning):
    """
    Adds a meaning to the english dictionary dict
    :param meaning_dict: The dict of meaning
    :param word: The word to be added
    :param type: The type of word
    :param meaning: The meaning of the word
    :return: the list after adding the element
    """
    # If the word already exists, then no need to sort the dictionary
    try:
        meaning_dict[word.casefold()].append([word, type, meaning])
        print(meaning_dict[word.casefold()])
    # If it does not, then insert and sort
    except KeyError:
        meaning_dict[word.casefold()] = [word, type, meaning]
        # Then sort the dict again
        # the original dictionary itself is already sorted, hence,
        meaning_dict = dict(sorted(meaning_dict.items()))
    return meaning_dict


# --------------------------------------------------------------------------------------------------
