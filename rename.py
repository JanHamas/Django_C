import os
import re
from datetime import datetime

# Replace this with the actual path to your screenshots folder
folder_path = r"C:\Users\PyCaptter\Desktop\Django_C\ScreenShot"

# Regular expression to extract date and time from the screenshot filenames
pattern = re.compile(r'ScreenShot Tool -(\d{14})')

# Dictionary to store filenames with their corresponding timestamps
files_with_timestamps = {}

# Iterate through all files in the directory
for filename in os.listdir(folder_path):
    match = pattern.search(filename)
    if match:
        # Extract timestamp and convert it to datetime object for sorting
        timestamp = match.group(1)
        datetime_obj = datetime.strptime(timestamp, '%Y%m%d%H%M%S')
        files_with_timestamps[filename] = datetime_obj

# Sort the files based on their timestamps
sorted_files = sorted(files_with_timestamps.items(), key=lambda x: x[1])

# Rename files in the sorted order
for index, (filename, _) in enumerate(sorted_files, start=1):
    # Construct new filename
    new_filename = f"D_{index}{os.path.splitext(filename)[1]}"
    # Full path for old and new filenames
    old_file = os.path.join(folder_path, filename)
    new_file = os.path.join(folder_path, new_filename)
    # Rename the file
    os.rename(old_file, new_file)
    print(f"Renamed {old_file} to {new_file}")

print("Renaming completed.")
