from tkinter import *
import global_variables as gb
from tkinter import ttk, messagebox
from tkinter.font import BOLD, Font
import tkinter

import helpers
import helpers as hp
import time

# --------------------------------------------------------------------------------------------------

# Create Menu Bar
def create_menubar(root):
    menubar = Menu(root)
    file = Menu(menubar, tearoff=0)
    file.add_command(label="New")
    file.add_command(label="Open")
    file.add_command(label="Save")
    file.add_command(label="Save as...")
    file.add_command(label="Close")

    file.add_separator()

    file.add_command(label="Exit", command=root.quit)

    menubar.add_cascade(label="File", menu=file)
    edit = Menu(menubar, tearoff=0)
    edit.add_command(label="Undo")

    edit.add_separator()

    edit.add_command(label="Cut")
    edit.add_command(label="Copy")
    edit.add_command(label="Paste")
    edit.add_command(label="Delete")
    edit.add_command(label="Select All")

    menubar.add_cascade(label="Edit", menu=edit)
    help = Menu(menubar, tearoff=0)
    help.add_command(label="About")
    menubar.add_cascade(label="Help", menu=help)
    # display the menu
    root.config(menu=menubar)

# --------------------------------------------------------------------------------------------------

def show_app_info():
    tkinter.messagebox.showinfo(title="Diwas English Dictionary", message="English Dictionary App version 1.0")
    # print("Hello")


# --------------------------------------------------------------------------------------------------

def create_left_frame(root):
    """
    :param root: The main window
    :return: The left frame
    """
    lp = Frame(root,
               highlightthickness=3,
               background="white"
               )
    lp.grid(row=0, column=0, rowspan=2, columnspan=1, sticky="NSEW")
    lp.grid_propagate(0)
    return lp


# --------------------------------------------------------------------------------------------------

# Reference for creating a scrollable textblock
# https://www.geeksforgeeks.org/scrollable-frames-in-tkinter/#:~:text=A%20scrollbar%20is%20a%20widget,are%20two%20types%20of%20scrollbars.

def show_all_dictionary_data(lp, meaning_object):
    """
    Loads all the dictionary data into the left frame
    :param lp: The left frame object created using the function create_left_frame()
    :param meaning_object: the list/dictionary of meaning
    :return: None
    """
    # Destroy everything that exists
    for widget in lp.winfo_children():
        widget.destroy()

    v = Scrollbar(lp, orient='vertical')
    v.pack(side=RIGHT, fill=Y)

    t = Text(lp, width=10, height=55,
             yscrollcommand=v.set)

    if gb.DATA_STRUCTURE == "list":
        for row in meaning_object:
            try:
                t.insert(END, f"{row[0]}: {row[1]}\n     {row[2]}")
            except Exception as e:
                t.insert(END, f"{row}")
            t.insert(END, "\n-----------------------------------------------------------------------\n \n")
    else:
        for row, cols in meaning_object.items():
            for col in cols:
                try:
                    t.insert(END, f"{col[0]}: {col[1]}\n     {col[2]}")
                except Exception as e:
                    pass
                t.insert(END, "\n \n")
            t.insert(END, "-----------------------------------------------------------------------\n \n")

    t.config(state=DISABLED)
    # attach Text widget to root window at top
    t.pack(side=TOP, fill=X)
    v.config(command=t.yview)


# --------------------------------------------------------------------------------------------------

def create_right_frame(root, left_frame):
    """
    :param mf: The main window
    :return: The right panel
    """
    rp = Frame(root,
               highlightthickness=3,
               background=gb.RP_BACKGROUND
               )
    rp.grid(row=0,column=1,rowspan=2,columnspan=1, sticky="NSEW")

    x_pos = 0.1

    # Add Search box
    search_y_start = 0.05
    search_label = Label(rp, text="Search:", font=Font(size=10, weight="bold"), bg=gb.RP_BACKGROUND)
    search_label.place(relx=x_pos, rely= search_y_start)

    search_entry = Entry(rp)
    search_entry.place(relx=x_pos, rely=search_y_start+0.05, width = "200", height="25")
    search_entry.bind("<KeyRelease>", lambda event : show_search_dictionary_data(left_frame, search_entry.get()))

    search_button = Button(rp, text="Search", command= lambda : show_search_dictionary_data(left_frame, search_entry.get()))
    search_button.place(relx=x_pos,rely=search_y_start+0.12,width="95")

    reset_button = Button(rp, text="Reset", command=lambda: reset_button_command(left_frame))
    reset_button.place(relx=0.50,rely=search_y_start+0.12, width = "95")

    # Add new word meaning
    add_meaning_y_start = 0.35
    add_new_label = Label(rp, text="Add new Meaning:", font=Font(size=10,weight="bold"), bg=gb.RP_BACKGROUND)
    add_new_label.place(relx=x_pos, rely=add_meaning_y_start-0.05, anchor=NW)

    word_label = Label(rp, text="Word:", bg=gb.RP_BACKGROUND)
    word_label.place(relx=x_pos, rely=add_meaning_y_start, anchor=NW)

    word_entry = Entry(rp)
    word_entry.place(relx=x_pos, rely=add_meaning_y_start + 0.05, width = "200", height="25")

    type_label = Label(rp, text="Word type (Ex: n. for noun):", bg=gb.RP_BACKGROUND)
    type_label.place(relx=x_pos, rely=add_meaning_y_start + 0.10, anchor=NW)

    type_entry = Entry(rp)
    type_entry.place(relx=x_pos,rely=add_meaning_y_start + 0.15, width = "200", height="25")

    meaning_label = Label(rp, text="Meaning of the word:", bg=gb.RP_BACKGROUND)
    meaning_label.place(relx=x_pos, rely=add_meaning_y_start + 0.20)

    meaning_text = Text(rp, height=4)
    meaning_text.place(relx=x_pos,rely=add_meaning_y_start + 0.25, width = "200")

    sort_var = IntVar()
    sort_or_not = Checkbutton(rp, text="Sort list while adding", bg=gb.RP_BACKGROUND, variable=sort_var)
    sort_or_not.place(relx=x_pos,rely=add_meaning_y_start + 0.42, width = "200")

    add_button = Button(rp, text="Add",
                        command=lambda: add_meaning_button_command(word_entry.get(),
                                                               type_entry.get(),
                                                               meaning_text.get("1.0",END),
                                                               left_frame, sort_var.get()))
    add_button.place(relx=x_pos,rely=add_meaning_y_start + 0.50, width = "200")
    return rp

# --------------------------------------------------------------------------------------------------

def add_meaning_button_command(word, type, meaning, left_frame, sort_list = True):
    if word == "" or word.isspace() or ' ' in word or meaning == "" or meaning.isspace():
        tkinter.messagebox.showerror(title="Error!", message="Word and meaning cannot be empty")
        return

    start = time.time()
    if gb.DATA_STRUCTURE == "list":
        gb.data_to_display = hp.add_meaning_to_list(gb.data_to_display,
                               word,
                               type,
                               meaning,
                               sort_list = sort_list)
    else:
        gb.data_to_display = hp.add_meaning_to_dict(gb.data_to_display,
                                                    word,type,meaning)
    end = time.time()
    time_taken = end - start
    show_all_dictionary_data(left_frame, gb.data_to_display)
    tkinter.messagebox.showinfo(title="Word Added", message="Time taken to add the word: " + str(time_taken))
    gb.made_changes = True

# --------------------------------------------------------------------------------------------------

def reset_button_command(left_frame):
    show_all_dictionary_data(left_frame, gb.data_to_display)

# --------------------------------------------------------------------------------------------------

def show_search_dictionary_data(lp, searchterm):
    if searchterm=="":
        show_all_dictionary_data(lp, gb.data_to_display)
        return

    for widget in lp.winfo_children():
        widget.destroy()

    v = Scrollbar(lp, orient='vertical')
    v.pack(side=RIGHT, fill=Y)

    t = Text(lp, width=10, height=55,
             yscrollcommand=v.set)

    if gb.DATA_STRUCTURE == "list":
        filtered_list, found = hp.search_list_binary(gb.data_to_display, searchterm)
    else:
        filtered_list, found = hp.search_dict(gb.data_to_display, searchterm)
    if not found:
        t.insert(END, f"Word Not Found")
    else:
        for row in filtered_list:
            try:
                t.insert(END, f"{row[0]}: {row[1]}\n     {row[2]}")
            except Exception as e:
                t.insert(END, f"{row}")
            t.insert(END, "\n-----------------------------------------------------------------------\n \n")
    t.config(state=DISABLED)
    # attach Text widget to root window at top
    t.pack(side=TOP, fill=X)
    v.config(command=t.yview)

# --------------------------------------------------------------------------------------------------

def create_bottom_frame(root, left_frame):
    """
    :param mf: The main window
    :return: The bottom panel
    """
    bp = Frame(root,
               highlightthickness=3,
               background=gb.BP_BACKGROUND, height=250)
    bp.grid(row=2,column=0,rowspan=1,columnspan=2, sticky="NSEW")

    x_pos = 1-0.15
    y_pos = 0.35

    save_button = Button(bp, text="Save", command=lambda: save_button_command())
    save_button.place(relx=x_pos, rely=y_pos,width="100")

    x_pos = 0.40
    text = "Using List Data Structure" if gb.DATA_STRUCTURE == "list" else "Using Dictionary(HashTable) Data Structure"
    ds_label = Label(bp, text=text, font=Font(size=10, weight="bold"),
                         bg=gb.BP_BACKGROUND, fg="White")
    ds_label.place(relx=x_pos, rely=y_pos)

    x_pos = 0.05
    delete_label = Label(bp, text="Delete Word:", font=Font(size=10, weight="bold"),
                         bg=gb.BP_BACKGROUND, fg="White")
    delete_label.place(relx=x_pos, rely=y_pos-0.2)

    delete_entry = Entry(bp)
    delete_entry.place(relx=x_pos, rely=y_pos, width="150", height="25")

    delete_button = Button(bp, text="Delete", command=lambda: delete_word(left_frame, delete_entry.get()))
    delete_button.place(relx=x_pos+0.18, rely=y_pos, width="45")

    return bp

# --------------------------------------------------------------------------------------------------

def delete_word(left_frame, word):
    if gb.DATA_STRUCTURE == "list":
        gb.data_to_display, found_word = hp.delete_word_from_list(gb.data_to_display,word)
    else:
        gb.data_to_display, found_word = hp.delete_word_from_dict(gb.data_to_display,word)

    show_all_dictionary_data(left_frame, gb.data_to_display)
    if found_word:
        tkinter.messagebox.showinfo(title="Word Found", message="Deleted the word " + word)
        gb.made_changes = True
    else:
        tkinter.messagebox.showerror(title="Word Not Found", message="No such word was found")

# --------------------------------------------------------------------------------------------------

def save_button_command(filename="dictionary.csv"):
    if(hp.save_list_to_file(gb.data_to_display, gb.made_changes, gb.DATA_STRUCTURE)):
        tkinter.messagebox.showinfo(title="File Saved Successfully", message="Saved the dictionary to " + filename)

