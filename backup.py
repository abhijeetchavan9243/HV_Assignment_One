import os
import sys
import shutil
from datetime import datetime

def backup_files(source_dir, dest_dir):
    # Check if source directory exists
    if not os.path.isdir(source_dir):
        print(f"Source directory does not exist: {source_dir}")
        return

    # Check if destination directory exists
    if not os.path.isdir(dest_dir):
        print(f"Destination directory does not exist: {dest_dir}")
        return

    # List files in source directory
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)

        # Only process files, skip subdirectories
        if os.path.isfile(source_file):
            dest_file = os.path.join(dest_dir, filename)

            # If file already exists, append timestamp
            if os.path.exists(dest_file):
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                name, ext = os.path.splitext(filename)
                new_filename = f"{name}_{timestamp}{ext}"
                dest_file = os.path.join(dest_dir, new_filename)
                print(f"File exists. Saving as: {new_filename}")

            # Copy file
            try:
                shutil.copy2(source_file, dest_file)
                print(f"Backed up: {filename} → {dest_file}")
            except Exception as e:
                print(f"Failed to copy {filename}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py /path/to/source /path/to/destination")
    else:
        src = sys.argv[1]
        dst = sys.argv[2]
        backup_files(src, dst)