from tkinter import *
from create_widgets import *
import global_variables
from helpers import load_csv_data, merge_csv_files

def setup_display(root, width = global_variables.SCREEN_WIDTH, height = global_variables.SCREEN_HEIGHT, resizex = 0, resizey = 0):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/1.7)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(resizex, resizey)
    root.title("Diwas English Dictionary")
    root.iconbitmap("icon.ico")

root = Tk()

setup_display(root)
create_menubar(root)
left_frame = create_left_frame(root)
show_all_dictionary_data(left_frame, global_variables.csvdata_list)

sorted_list = []
sorted_list[:] = global_variables.csvdata_list
sorted_list = sorted(sorted_list, key=lambda s: s[0].lower(), reverse=True)

# Uncomment the line below to reset the dictionary
# merge_csv_files() # Commenting because done merging

right_frame = create_right_frame(root, left_frame)
bottom_frame = create_bottom_frame(root, left_frame)

root.grid_rowconfigure(0, weight=3)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=2)
root.grid_columnconfigure(1, weight=1)

root.mainloop()



