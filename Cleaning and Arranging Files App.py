import os
from pathlib import Path
from tkinter import filedialog
from tkinter import *
from tkinter import ttk

color_bg = "#192C2C"
color_fg = "#f7f7f7"

def filepath():
    pathFileAndFolder = filedialog.askdirectory(title="Select your Folder to Clean and Arrange")
    
    if not pathFileAndFolder:
        print("Please select a folder")
        return
    
    textBoxForUrl.delete(0, END)
    textBoxForUrl.insert(0, pathFileAndFolder)
    
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

    file_list = "\n".join(files[:20])
    if lfiles > 20:
        file_list += f"\n... and {lfiles - 20} more"
    
    folders_list = "\n".join(folders[:20])
    if lfolders > 20:
        folders_list += f"\n... and {lfolders - 20} more"
    
    display_text = f"📄 FILES: {lfiles}\n{file_list}\n\n📁 FOLDERS: {lfolders}\n{folders_list}"
    nameOfFilesAndFolders.config(text=display_text)

root = Tk()
root.title("Cleaning and Arranging Files App")
root.geometry("600x500")
root.configure(bg=color_bg)

# Main frame
mainFrame = Frame(root, bg=color_bg)
mainFrame.pack(fill=BOTH, expand=True)

# Canvas and scrollbar
canvas = Canvas(mainFrame, bg=color_bg, highlightthickness=0)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

scrollBar = ttk.Scrollbar(mainFrame, orient=VERTICAL, command=canvas.yview)
scrollBar.pack(side=RIGHT, fill=Y)

canvas.configure(yscrollcommand=scrollBar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Second frame (holds all widgets)
secondFrame = Frame(canvas, bg=color_bg)
canvas.create_window((0, 0), window=secondFrame, anchor="nw")

# ========== WIDGETS USING .pack() ==========

# Top section - Entry and Label
top_frame = Frame(secondFrame, bg=color_bg)
top_frame.pack(fill=X, padx=20, pady=(20, 10))

Label(top_frame, bg=color_bg, fg=color_fg, text="Write your path", font=("Corbel", 12, "bold")).pack(anchor="w")

entry_frame = Frame(top_frame, bg=color_bg)
entry_frame.pack(fill=X, pady=5)

textBoxForUrl = Entry(entry_frame, width=40, font=("Corbel", 10))
textBoxForUrl.pack(side=LEFT, fill=X, expand=True)

button_dir = Button(
    entry_frame,
    text="Select Folder",
    width=20,
    height=1,
    font=("Corbel", 10, "bold"),
    command=filepath
)
button_dir.pack(side=RIGHT, padx=(10, 0))

# Display area
nameOfFilesAndFolders = Label(
    secondFrame,
    font=("Corbel", 10),
    text="📄 FILES :\n\n📁 FOLDERS:",
    justify='left',
    bg=color_bg,
    fg=color_fg,
    anchor="nw"
)
nameOfFilesAndFolders.pack(fill=BOTH, expand=True, padx=20, pady=10)

# Spacer to make scrolling work
Label(secondFrame, bg=color_bg, text="", height=5).pack()

# Update scroll region
def update_scroll_region(event=None):
    canvas.configure(scrollregion=canvas.bbox("all"))

secondFrame.bind("<Configure>", update_scroll_region)

root.mainloop()