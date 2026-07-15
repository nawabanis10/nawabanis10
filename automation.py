import os
import shutil

source_folder="D:\\my-documents"
destination_folder="D:\\New_documents"

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for filename in os.listdir(source_folder):
    source_file = os.path.join(source_folder, filename)
    destination_file = os.path.join(destination_folder, filename)

    shutil.move(source_file, destination_file)
    print(f"Moved: {source_file} to {destination_file}")