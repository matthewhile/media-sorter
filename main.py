from pathlib import Path
from datetime import datetime
import shutil

sourceDir = '/Users/mattw/OneDrive/Desktop/PhotoStorage'
targetDir = '/Users/mattw/OneDrive/Desktop/Photos'

sPath = Path(sourceDir)
tPath = Path(targetDir)

if not tPath.exists():
    print("Target directory not found.") 

files = sPath.iterdir()
count = 0

for f in files:
    count += 1
    img = Path(f)
    created_timestamp = img.stat().st_ctime
    created_datetime = datetime.fromtimestamp(created_timestamp)

    year = created_datetime.year

    yPath = tPath / str(year)
    yPath.mkdir(parents = True, exist_ok = True)

    shutil.copy2(f, yPath)

    print(count)
    print(created_datetime)

#print(created_datetime.year)



