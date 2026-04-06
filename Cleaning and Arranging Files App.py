import os
from pathlib import Path
from tkinter import filedialog
from tkinter import *

color_bg ="#192C2C"
color_fg = "#f7f7f7"

def filepath():
    pathFileAndFolder = filedialog.askdirectory(title="Select your Folder to Clean and Arrange")
    
    if not pathFileAndFolder:
        print("Please select the Path or File or Folder")
        return
    
    listItems = Path(pathFileAndFolder)
    files = []
    folders = []

    for item in listItems.iterdir():
        if item.is_dir():
            folders.append(item.name)

        elif item.is_file():
            files.append(item.name)
    
    lfiles = len(files)
    lfolders = len(folders)

    file_list = "\n".join(files)

    folders_list = "\n".join(folders)
    display_text = f"📄 FILES: {lfiles}\n[ {file_list} ]\n\n📁 FOLDERS: {lfolders}\n[ {folders_list} ]"
    nameOfFilesAndFolders.config(text=display_text)
    textBoxForUrl.insert(0, item)
def pathFile():
    pass

root = Tk()
root.title("Cleaning and Arranging Files App")
root.geometry("600x400")
root.configure(bg=color_bg)

textBoxForUrl = Entry(root)
textBoxForUrl.place(x=20,y=50, width=200, height=30)

text_for_your_dirBox = Label(root, bg=color_bg, fg=color_fg ,text="Write your path", font=("Corbel", 12, "bold")).place(x=10, y=25)
button_dir = Button(root, 
                    text="Select your Folder to Clean/Arrange",  
                    width=35, 
                    height=2, 
                    font=("Corbel", 10, "bold"), 
                    command= lambda : filepath())
button_dir.place(x=240, y=45)

nameOfFilesAndFolders = Label(
                            root, 
                            font=("Corbel", 10, "bold"),
                            text=("📄 FILES :\n\n📁 FOLDERS:"), 
                             justify='left', bg=color_bg, fg=color_fg)
nameOfFilesAndFolders.place(x=20, y=100)

# scroll = SCROLL()
# text = Text(root, yscrollcommand=scroll.set)

# scroll_bar = Scrollbar(root, command=text.yview)


root.mainloop()
