import csv
import glob

def merge_csv_files(foldername="dictionary"):
    csv.field_size_limit(256 << 20)
    meaning_list = []
    csv_files = glob.glob(foldername +"/*.csv")
    for filename in csv_files:
        with open(filename, newline='') as csvfile:
            meaning_list = meaning_list + list(csv.reader(csvfile))
            for i in range(len(meaning_list)):
                if i > 5: break
                print(i)
                print(meaning_list[i])
                try:
                    print("meaning list first:",meaning_list[i][0])
                    split_opening = meaning_list[i][0].split(' (', 1)
                except Exception as e:
                    print(e)
                    meaning_list.pop(i)
                    continue

                print("Split opening:",split_opening)
                meaning_list[i][0] = split_opening[0]

                split_closing = split_opening[1].split(')',1)
                print("Split closing:", split_closing)

                split_middle = f"({split_closing[0]})"
                print("Split middle:", split_middle)

                meaning_list[i].append(split_middle)
                meaning_list[i].append(split_closing[1])
                print("Meaning list after:",meaning_list[i])


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
