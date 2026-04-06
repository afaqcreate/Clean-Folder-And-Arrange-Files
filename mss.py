import os

folder_path = r"D:\Clean Folder And Arrange Files"

# Get all items
all_items = os.listdir(folder_path)

# Create two empty lists
files = []
folders = []

# Check each item
for item in all_items:
    full_path = os.path.join(folder_path, item)
    
    if os.path.isfile(full_path):
        files.append(item)      # It's a file
    elif os.path.isdir(full_path):
        folders.append(item)    # It's a folder

# See the results
print(f"FILES: {files}")
print(f"FOLDERS: {folders}")