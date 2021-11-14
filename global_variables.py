import helpers as hp

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

csvdata_list = hp.load_csv_data("dictionary.csv")
csvdata_dict = hp.list_to_dictionary(csvdata_list)

# Panel background colors
RP_BACKGROUND = "Beige"
BP_BACKGROUND = "CadetBlue"