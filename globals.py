from helpers import *

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

# CSVDATA_LIST = load_csv_data("dictionary.csv", "list")
CSVDATA_LIST = merge_csv_files()
CSVDATA_DICT = load_csv_data("dictionary.csv", "dict")