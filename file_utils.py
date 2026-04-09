from pathlib import Path
from typing import List, Tuple

def scan_folder(folder_path: str) -> List[Path]:
    """Returns all items in folder. Returns empty list if folder doesn't exist."""
    path = Path(folder_path)
    if not path.exists():
        return []
    return list(path.iterdir())

def separate_files_and_folders(items: List[Path]) -> Tuple[List[Path], List[Path]]:
    """Returns (files, folders) from list of items."""
    files = [item for item in items if item.is_file()]
    folders = [item for item in items if item.is_dir()]
    return files, folders

def filter_by_extension(items: List[Path], extensions: set) -> List[Path]:
    """Returns items with given extensions."""
    return [item for item in items if item.suffix.lower() in extensions]

def get_file_info(file_path: Path) -> dict:
    """Returns file information: name, size, extension, modified date."""
    return {
        'name': file_path.name,
        'size': file_path.stat().st_size,
        'extension': file_path.suffix,
        'modified': file_path.stat().st_mtime
    }
