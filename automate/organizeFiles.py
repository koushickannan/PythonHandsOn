import os
import shutil

download_folder = "/home/bglbgsz0j3/Downloads"
destination = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".csv", ".xlsx"],
    "Archives": [".zip", ".rar", ".tar"],
}

for file in os.listdir(download_folder):
    file_path = os.path.join(download_folder, file)
    if os.path.isfile(file_path):
        for folder, extensions in destination.items():
            if file.endswith(tuple(extensions)):
                folder_path = os.path.join(download_folder, folder)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(file_path, folder_path)

print("Download folder sorted!")
