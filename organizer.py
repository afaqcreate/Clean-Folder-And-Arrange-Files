import shutil
from pathlib import Path
from file_utils import scan_folder, separate_files_and_folders

class FileOrganizer:
    def __init__(self, config):
        self.config = config
        self.moved_files = []
        self.errors = []
    
    def organize_by_extension(self, source_folder: str, dest_base: str) -> dict:
        """Organizes files into folders by extension."""
        items = scan_folder(source_folder)
        files, _ = separate_files_and_folders(items)
        
        for file in files:
            try:
                ext = file.suffix.lower()[1:]  # Remove dot
                if not ext:
                    ext = "no_extension"
                
                dest_folder = Path(dest_base) / ext
                dest_folder.mkdir(parents=True, exist_ok=True)
                
                dest_path = dest_folder / file.name
                shutil.move(str(file), str(dest_path))
                self.moved_files.append(str(dest_path))
            except Exception as e:
                self.errors.append(f"Failed to move {file.name}: {e}")
        
        return {
            'moved': len(self.moved_files),
            'errors': len(self.errors),
            'error_details': self.errors
        }
    
    def organize_by_type(self, source_folder: str, dest_base: str) -> dict:
        """Organizes files by type (images, documents, etc.)."""
        items = scan_folder(source_folder)
        files, _ = separate_files_and_folders(items)
        
        type_folders = {
            'images': self.config.IMAGE_EXTENSIONS,
            'documents': self.config.DOCUMENT_EXTENSIONS,
            'other': set()
        }
        
        for file in files:
            ext = file.suffix.lower()
            
            # Find which category
            category = 'other'
            for cat, exts in type_folders.items():
                if ext in exts:
                    category = cat
                    break
            
            dest_folder = Path(dest_base) / category
            dest_folder.mkdir(parents=True, exist_ok=True)
            shutil.move(str(file), str(dest_folder / file.name))
        
        return {'status': 'complete'}
