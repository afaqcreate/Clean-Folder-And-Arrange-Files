import os
from tkinter import *
from tkinter import filedialog

def open_dir():
    pass

# color
color_bg ="#192C2C"
color_fg = "#f7f7f7"

# Window
root = Tk()
root.title("Cleaning and Arranging Files App")
root.geometry("500x500")
root.configure(background=color_bg)

text_for_your_dirBox = Label(root, bg=color_bg, fg=color_fg ,text="Text Path Your Diractary", font=("Corbel", 12, "bold")).place(x=10, y=25)

button_for_chose_path = Button(root, text="Select your Folder to Clean/Arrange",  width=35, height=2, font=("Corbel", 10, "bold")).place(x=230, y=45)
# logic for path how it's work
def select_file ():
    select_files = ''
    select_files = filedialog.askdirectory(title="Select your Folder to Clean and Arrange")

textBox_for_path_url = Entry(root).place(x=20, y=50, height= 30, width=200)

root.mainloop()
