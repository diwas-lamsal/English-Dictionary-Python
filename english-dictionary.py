from tkinter import *
from create_widgets import *
import globals
from helpers import load_csv_data

def setup_display(root, width = globals.SCREEN_WIDTH, height = globals.SCREEN_HEIGHT, resizex = 0, resizey = 0):
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
show_all_dictionary_data(left_frame)
merge_csv_files()

right_frame = create_right_frame(root, left_frame)
bottom_frame = create_bottom_frame(root)

root.grid_rowconfigure(0, weight=3)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=2)
root.grid_columnconfigure(1, weight=1)

root.mainloop()



