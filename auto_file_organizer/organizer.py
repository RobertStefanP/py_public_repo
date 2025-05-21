import os
from file_manager import FileManager
from categories import CATEGORIES


class Organizer:
    def run(self):
        desktop_path = r"C:\Users\Robert\OneDrive\Desktop"
        manager = FileManager(desktop_path)        
        files = manager.scan_files()
        
        for file_path in files:
            print(file_path)
            name, extension = os.path.splitext(file_path)
            category = manager.get_categories(extension)
            destination_folder = os.path.join(desktop_path, category)
            
            manager.move_file(file_path, destination_folder)
            print(f"Moved: {file_path} - {destination_folder}")

if __name__ == "__main__":
    organizer = Organizer()
    organizer.run()
    