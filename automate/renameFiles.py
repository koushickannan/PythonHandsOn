import os

folder_path = "/Users/Aashish/Downloads"

for index, filename in enumerate(os.listdir(folder_path), start=1):
    new_name = f"report_{index}.pdf"
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, new_name)
    os.rename(old_path, new_path)

print("Renaming complete!")
