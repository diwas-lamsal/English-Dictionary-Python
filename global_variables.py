import helpers as hp
from os.path import exists

DATA_STRUCTURE = "list"

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

csv_filename = "dictionary.csv"
csvlist_filename = "meaning_data_as_list.pkl"
csvdict_filename = "meaning_data_as_dictionary.pkl"

csvdata_list = hp.load_list_from_file(csvlist_filename) if exists(csvlist_filename) \
    else hp.csv_to_list(csv_filename, csvlist_filename)
csvdata_dict = hp.load_dictionary_from_file(csvdict_filename) if exists(csvdict_filename) \
    else hp.list_to_dictionary(csvdata_list, csvdict_filename)

data_to_display = csvdata_list if DATA_STRUCTURE == "list" else csvdata_dict

# Panel background colors
RP_BACKGROUND = "Beige"
BP_BACKGROUND = "CadetBlue"