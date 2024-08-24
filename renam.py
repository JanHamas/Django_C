import os

# Define the folder path
folder_path = r"C:\Users\PyCaptter\Desktop\Django_C\ScreenShot"

# Get a list of all files in the directory
files = os.listdir(folder_path)

# Sort files to ensure they are processed in the correct order
files.sort()

# Initialize a counter
counter = 1

# Loop through each file in the directory
for file_name in files:
    # Construct the full file path
    old_file_path = os.path.join(folder_path, file_name)
    
    # Check if it's a file (not a directory)
    if os.path.isfile(old_file_path):
        # Create the new file name
        new_file_name = f"{counter}.png"  # Assuming the files are PNGs; change extension if necessary
        
        # Construct the full new file path
        new_file_path = os.path.join(folder_path, new_file_name)
        
        # Rename the file
        os.rename(old_file_path, new_file_path)
        
        # Increment the counter
        counter += 1

print("Files renamed successfully.")
