from pathlib import Path
from datetime import datetime
import shutil
import sys

sourceDir = '/Desktop/PhotoStorage'
targetDir = 'Desktop/Photos'

sPath = Path(sourceDir)
tPath = Path(targetDir)

if not sPath.exists():
    print("Source directory not found!") 
    sys.exit(0)

if not tPath.exists():
    print("Target directory not found!") 
    sys.exit(0)

def getAction():
    while(True):
        action = input("Enter C to copy or M to move: ")
        if action in ("C", "c", "M", "m"):
            return action
        print("Invalid input!")

files = sPath.iterdir()
count = 0

action = getAction()

print("File transfer started...")

for f in files:
    try:
        count += 1
        img = Path(f)
        created_timestamp = img.stat().st_ctime
        created_datetime = datetime.fromtimestamp(created_timestamp)

        year = created_datetime.year

        yPath = tPath / str(year)
        
        yPath.mkdir(parents = True, exist_ok = True)

        if action == "C" or action == "c":
            shutil.copy2(f, yPath)
        else:
            shutil.move(f, yPath)

    except OSError as err:
        print("Filesystem error occured processing file: " + f.name + "\nError message: ", err)
        sys.exit(0)

print("Transfer completed!")
print(str(count) + " total files processed.")




