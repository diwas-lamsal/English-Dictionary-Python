import csv
import glob
import pickle
import os


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
    meaning_list = [x for x in meaning_list if len(x) == 3]

    # Sort meaning list in ascending order
    meaning_list = sorted(meaning_list, key=lambda s: s[0].lower())

    # The meaning list is now ready to be saved as a CSV file
    with open('dictionary.csv', 'w', newline='') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f)
        write.writerows(meaning_list)

    return meaning_list


# --------------------------------------------------------------------------------------------------

def csv_to_list(csv_filename, list_save_name):
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

def load_list_from_file(filename):
    a_file = open(filename, "rb")
    output = pickle.load(a_file)
    return output


# --------------------------------------------------------------------------------------------------

def list_to_dictionary(meaning_list, dict_save_name):
    d = {}

    # https://stackoverflow.com/questions/48705143/efficiency-2d-list-to-dictionary-in-python
    # Runs in O(n)
    for elem in meaning_list:
        try:
            d[elem[0]].append([elem[1], elem[2]])
        except KeyError:
            d[elem[0]] = [elem[1], elem[2]]

    # https://www.kite.com/python/answers/how-to-save-a-dictionary-to-a-file-in-python
    a_file = open(dict_save_name, "wb")
    pickle.dump(d, a_file)
    a_file.close()
    return d


# --------------------------------------------------------------------------------------------------

def load_dictionary_from_file(filename="meaning_data_as_dictionary.pkl"):
    a_file = open(filename, "rb")
    output = pickle.load(a_file)
    return output


# --------------------------------------------------------------------------------------------------

def get_meaning_from_search_list(word_list, search):
    for word in word_list:
        if word[0] == search:
            return word


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
        meaning_list.append([word, "(" + type + ")", meaning])
        # sorted() in python is Timsort algorithm
        # Timsort combines merge sort and insertion sort
        meaning_list = sorted(meaning_list, key=lambda s: s[0].lower())
        return meaning_list
    else:
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
    # https://stackoverflow.com/questions/2793324/is-there-a-simple-way-to-delete-a-list-element-by-value
    if word in [x[0] for x in meaning_list]:
        meaning_list = [x for x in meaning_list if x[0] != word]
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

def sort_dict(d):
    d = dict(sorted(d.items()))
    return d


# --------------------------------------------------------------------------------------------------

def search_list(meaning_list, word):
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

def search_dict(meaning_dict, word):
    found = False
    filtered_dict = {}
    if word in meaning_dict:
        found = True
        filtered_dict={word:meaning_dict[word]}
    return filtered_dict, found