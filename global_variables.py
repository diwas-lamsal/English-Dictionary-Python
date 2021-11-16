import helpers as hp
from os.path import exists

# the data structure to use: list or dict
DATA_STRUCTURE = "list"

# set the window size, recommended is 900x600
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

# File name of the csv file, and binary list and dictionary files
csv_filename = "dictionary.csv"
list_filename = "meaning_data_as_list.pkl"
dict_filename = "meaning_data_as_dictionary.pkl"

# if the list binary file exists, load it, otherwise load it from the csv file
data_list = hp.load_list_from_file(list_filename) if exists(list_filename) \
    else hp.csv_to_list(csv_filename, list_filename)

# if the dict binary file exists, load it otherwise load it from the list loaded above
data_dict = hp.load_dictionary_from_file(dict_filename) if exists(dict_filename) \
    else hp.list_to_dictionary(data_list, dict_filename)
# data_dict=None

# Point the data_to_display variable to one of the above loaded variables according to configuration
data_to_display = data_list if DATA_STRUCTURE == "list" else data_dict

made_changes = False

# Panel background colors
# RP = Right Panel, BP = Bottom Panel
RP_BACKGROUND = "Beige"
BP_BACKGROUND = "CadetBlue"