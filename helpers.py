import csv
import glob

def merge_csv_files(foldername="dictionary"):
    csv.field_size_limit(256 << 20)
    meaning_list_all = []
    csv_files = glob.glob(foldername +"/*.csv")

    # Get all the lines from each csv files for each alphabet into a single meaning list
    for filename in csv_files:
        with open(filename, newline='') as csvfile:
            meaning_list_all = meaning_list_all + list(csv.reader(csvfile))

    # Remove all the blank lines
    meaning_list = [e for e in meaning_list_all if e]

    for i in range(len(meaning_list)):
        try:
            split_opening = meaning_list[i][0].split(' (', 1)
            meaning_list[i][0] = split_opening[0]
            split_closing = split_opening[1].split(')',1)
            split_middle = f"({split_closing[0]})"
            meaning_list[i].append(split_middle)
            meaning_list[i].append(split_closing[1])
        except Exception as e:
            continue

    return meaning_list


def load_csv_data(foldername, returntype):
    csv.field_size_limit(256 << 20)

    meaning_list = []
    meaning_dict = {}

    csv_files = glob.glob("dictionary/*.csv")

    for filename in csv_files:
        with open(filename, newline='') as csvfile:
            if returntype == "list":
                meaning_list = meaning_list + list(csv.reader(csvfile))
            else:
                meaning_dict = csv.DictReader(csvfile)
        return meaning_list

def get_meaning_from_search_list(word_list, search):
    for word in word_list:
        if word[0]==search:
            return word
