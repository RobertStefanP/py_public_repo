# Auto File Organizer

This is a simple Python project that organizes files on your desktop. It scans 
the folder, detects file types by extension (like .jpg, .pdf, .mp4), and moves 
them into folders like "Images", "Documents", or "Videos".


## Features

- Scans a target folder 
- Detects file types based on their extension
- Moves files into category folders (Images, Documents, Videos, etc.)
- Creates folders if they don’t exist
- Keeps your desktop clean and organized


## How It Works

1. You set the folder you want to organize 
2. The program finds all the files in that folder
3. It checks the extension of each file
4. It moves the file to a matching category folder
5. Files with unknown types go into the "Others" folder


## Project Structure

- `organizer.py` — Runs the program and main controller logic
- `file_manager.py` — Handles scanning and moving files
- `categories.py` — Contains file type categories


## How to execute

1. Clone the repository
2. Navigate to the project folder
3. Run the script: python organizer.py
