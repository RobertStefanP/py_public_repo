import os
import shutil

from categories import CATEGORIES


class FileManager:
    def __init__(self, target_folder):
        self.target_folder = target_folder

    def scan_files(self):
        """Return all file paths in the target folder."""
        files = []
        for item in os.listdir(self.target_folder):
            full_path = os.path.join(self.target_folder, item)
            if os.path.isfile(full_path):
                files.append(full_path)
        return files

    def get_categories(self, extension):
        """Return the category name for a given file estension."""       
        for category, extensions in CATEGORIES.items():
            if extension.lower() in extensions:
                return category
        return 'Others'
        
    def move_file(self, file_path, destination_folder):
        """Move a file to the specified folder, creating the folder if needed."""
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        file_name = os.path.basename(file_path)
        destination_path = os.path.join(destination_folder, file_name)

        shutil.move(file_path, destination_path)
        