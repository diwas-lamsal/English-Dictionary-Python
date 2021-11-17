from tkinter import *
from create_widgets import *
import global_variables as gb
from helpers import merge_csv_files

def setup_display(root, width = gb.SCREEN_WIDTH, height = gb.SCREEN_HEIGHT, resizex = 0, resizey = 0):
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

# Uncomment the line below to reset the dictionary
# merge_csv_files() # Commenting because done merging

left_frame = create_left_frame(root)

show_all_dictionary_data(left_frame, gb.data_list if gb.DATA_STRUCTURE == "list" else gb.data_dict)

right_frame = create_right_frame(root, left_frame)
bottom_frame = create_bottom_frame(root, left_frame)

root.grid_rowconfigure(0, weight=3)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=2)
root.grid_columnconfigure(1, weight=1)

root.mainloop()



