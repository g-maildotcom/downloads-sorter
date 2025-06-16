#************************************************************************

#first project: downloads auto sorter
import os
import shutil

#************************************************************************

#made dictionary; mapping file types (values) to folders (keys)
types = {
    "images": [".jpg", "jpeg", ".png", ".gif", ".heif", ".heic"],
    "pdfs": [".pdf"],
    "docs": [".docx", ".doc", ".gdoc", ".odt", ".txt"],
    "musica": [".wav", ".mp3"],
    "zips": [".zip", ".rar", ".7z", ".tar.gz"],
    "code": [".py", ".js", ".html", ".css", ".c"],
    "sheets": [".xlsx", ".sheets", ".gsheet", ".csv"]
}

#************************************************************************

downloads = os.path.expanduser("~/Downloads")

for filename in os.listdir(downloads): #os.listdir returns a list of all file and folder names in the downloads_folder
    filepath = os.path.join(downloads, filename)
    
    if os.path.isfile(filepath):
        _, ext = os.path.splitext(filename) #sees file type regardless of name

        for folder, extensions in types.items():
            if ext.lower() in extensions:
                folderpath = os.path.join(downloads, folder)
                os.makedirs(folderpath, exist_ok=True) #makes the folder if it doesn’t already exist

                shutil.move(filepath, os.path.join(folderpath, filename)) #actually moves the file from the Downloads folder to the appropriate subfolder
                print(f"following file moved: {filename} → {folder}//")
                break

#**************** MISC FILES*********************************************

miscfold = os.path.join(downloads, "misc")
os.makedirs(miscfold, exist_ok=True)
shutil.move(filepath, os.path.join(miscfold, filename))
print(f"FILETYPE NOT IN CODE: {filename} → misc/")