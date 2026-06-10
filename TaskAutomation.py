# To move all .jpg files from a folder to a new folder.
import os
import shutil

source_folder = "source"
destination_folder = "destination"

for file in os.listdir(source_folder):
    if file.endswith(".jpg"):
        shutil.move(
            os.path.join(source_folder, file),
            os.path.join(destination_folder, file)
        )

print("All JPG files moved.")