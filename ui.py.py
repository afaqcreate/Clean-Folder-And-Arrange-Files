from tkinter import *
from tkinter import filedialog, messagebox
from pathlib import Path
from file_utils import scan_folder, separate_files_and_folders, get_file_info
from organizer import FileOrganizer
from config import Config

class FolderCleanerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Folder Cleaner")
        self.root.geometry("700x600")
        
        self.config = Config()
        self.organizer = FileOrganizer(self.config)
        self.current_folder = None
        
        self.setup_ui()
    
    def setup_ui(self):
        # Menu bar
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        
        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open Folder", command=self.select_folder)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        # Main frame
        main_frame = Frame(self.root)
        main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        # Top section
        top_frame = Frame(main_frame)
        top_frame.pack(fill=X)
        
        Label(top_frame, text="Folder:", font=("Arial", 10, "bold")).pack(side=LEFT)
        self.folder_label = Label(top_frame, text="No folder selected", anchor="w")
        self.folder_label.pack(side=LEFT, fill=X, expand=True, padx=5)
        
        Button(top_frame, text="Browse", command=self.select_folder).pack(side=RIGHT)
        
        # Middle section - results
        self.result_text = Text(main_frame, wrap=WORD, height=20)
        self.result_text.pack(fill=BOTH, expand=True, pady=10)
        
        scrollbar = Scrollbar(self.result_text)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.result_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.result_text.yview)
        
        # Bottom section - buttons
        bottom_frame = Frame(main_frame)
        bottom_frame.pack(fill=X)
        
        Button(bottom_frame, text="Scan Folder", command=self.scan_folder).pack(side=LEFT, padx=5)
        Button(bottom_frame, text="Organize by Extension", command=self.organize_by_extension).pack(side=LEFT, padx=5)
        Button(bottom_frame, text="Organize by Type", command=self.organize_by_type).pack(side=LEFT, padx=5)
    
    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.current_folder = folder
            self.folder_label.config(text=folder)
            self.scan_folder()
    
    def scan_folder(self):
        if not self.current_folder:
            messagebox.showwarning("No Folder", "Please select a folder first")
            return
        
        self.result_text.delete(1.0, END)
        self.result_text.insert(END, f"Scanning: {self.current_folder}\n")
        self.result_text.insert(END, "="*50 + "\n\n")
        
        items = scan_folder(self.current_folder)
        files, folders = separate_files_and_folders(items)
        
        self.result_text.insert(END, f"📊 SUMMARY:\n")
        self.result_text.insert(END, f"   Total items: {len(items)}\n")
        self.result_text.insert(END, f"   Files: {len(files)}\n")
        self.result_text.insert(END, f"   Folders: {len(folders)}\n\n")
        
        self.result_text.insert(END, f"📄 FILES:\n")
        for file in files[:20]:
            info = get_file_info(file)
            self.result_text.insert(END, f"   • {info['name']} ({info['size']} bytes)\n")
        if len(files) > 20:
            self.result_text.insert(END, f"   ... and {len(files)-20} more\n")
        
        self.result_text.insert(END, f"\n📁 FOLDERS:\n")
        for folder in folders[:20]:
            self.result_text.insert(END, f"   • {folder.name}\n")
    
    def organize_by_extension(self):
        if not self.current_folder:
            messagebox.showwarning("No Folder", "Please select a folder first")
            return
        
        result = self.organizer.organize_by_extension(self.current_folder, self.current_folder)
        messagebox.showinfo("Complete", f"Moved {result['moved']} files.\nErrors: {result['errors']}")
        self.scan_folder()  # Refresh display
    
    def organize_by_type(self):
        if not self.current_folder:
            messagebox.showwarning("No Folder", "Please select a folder first")
            return
        
        result = self.organizer.organize_by_type(self.current_folder, self.current_folder)
        messagebox.showinfo("Complete", "Organization complete!")
        self.scan_folder()

def main():
    root = Tk()
    app = FolderCleanerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    def __init__(self, root):
        self.root = root
        self.root.title("Folder Cleaner")
        self.root.geometry("700x600")
        
        self.config = Config()
        self.organizer = FileOrganizer(self.config)
        self.current_folder = None
        
        self.setup_ui()
    
    def setup_ui(self):
        # Menu bar
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        
        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open Folder", command=self.select_folder)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        # Main frame
        main_frame = Frame(self.root)
        main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        # Top section
        top_frame = Frame(main_frame)
        top_frame.pack(fill=X)
        
        Label(top_frame, text="Folder:", font=("Arial", 10, "bold")).pack(side=LEFT)
        self.folder_label = Label(top_frame, text="No folder selected", anchor="w")
        self.folder_label.pack(side=LEFT, fill=X, expand=True, padx=5)
        
        Button(top_frame, text="Browse", command=self.select_folder).pack(side=RIGHT)
        
        # Middle section - results
        self.result_text = Text(main_frame, wrap=WORD, height=20)
        self.result_text.pack(fill=BOTH, expand=True, pady=10)
        
        scrollbar = Scrollbar(self.result_text)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.result_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.result_text.yview)
        
        # Bottom section - buttons
        bottom_frame = Frame(main_frame)
        bottom_frame.pack(fill=X)
        
        Button(bottom_frame, text="Scan Folder", command=self.scan_folder).pack(side=LEFT, padx=5)
        Button(bottom_frame, text="Organize by Extension", command=self.organize_by_extension).pack(side=LEFT, padx=5)
        Button(bottom_frame, text="Organize by Type", command=self.organize_by_type).pack(side=LEFT, padx=5)
    
    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.current_folder = folder
            self.folder_label.config(text=folder)
            self.scan_folder()
    
    def scan_folder(self):
        if not self.current_folder:
            messagebox.showwarning("No Folder", "Please select a folder first")
            return
        
        self.result_text.delete(1.0, END)
        self.result_text.insert(END, f"Scanning: {self.current_folder}\n")
        self.result_text.insert(END, "="*50 + "\n\n")
        
        items = scan_folder(self.current_folder)
        files, folders = separate_files_and_folders(items)
        
        self.result_text.insert(END, f"📊 SUMMARY:\n")
        self.result_text.insert(END, f"   Total items: {len(items)}\n")
        self.result_text.insert(END, f"   Files: {len(files)}\n")
        self.result_text.insert(END, f"   Folders: {len(folders)}\n\n")
        
        self.result_text.insert(END, f"📄 FILES:\n")
        for file in files[:20]:
            info = get_file_info(file)
            self.result_text.insert(END, f"   • {info['name']} ({info['size']} bytes)\n")
        if len(files) > 20:
            self.result_text.insert(END, f"   ... and {len(files)-20} more\n")
        
        self.result_text.insert(END, f"\n📁 FOLDERS:\n")
        for folder in folders[:20]:
            self.result_text.insert(END, f"   • {folder.name}\n")
    
    def organize_by_extension(self):
        if not self.current_folder:
            messagebox.showwarning("No Folder", "Please select a folder first")
            return
        
        result = self.organizer.organize_by_extension(self.current_folder, self.current_folder)
        messagebox.showinfo("Complete", f"Moved {result['moved']} files.\nErrors: {result['errors']}")
        self.scan_folder()  # Refresh display
    
    def organize_by_type(self):
        if not self.current_folder:
            messagebox.showwarning("No Folder", "Please select a folder first")
            return
        
        result = self.organizer.organize_by_type(self.current_folder, self.current_folder)
        messagebox.showinfo("Complete", "Organization complete!")
        self.scan_folder()

def main():
    root = Tk()
    app = FolderCleanerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()