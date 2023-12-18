#!/usr/bin/env python
# Found and export all sqlite 3 into output folder.

# don't end with '/'

INPUT_DIR = "/home/mane/Downloads/OpTinselTrace/elfidence_collection/TriageData/C/users/Elfin/Appdata/Roaming/eM Client"
OUTPUT_DIR = "email"

import os
from pathlib import Path
path = Path(OUTPUT_DIR)
path.mkdir(parents=True, exist_ok=True)


# 0x1 find all sqlite 3 files
found_sqlite3_files = []

def checkSqlite3File(filename):
    with open(filename, 'rb') as fd:
        header = fd.read(100)
        if header[:16] == b'SQLite format 3\x00' :
            fd.close()
            return True
    return False

def checkDir(dir):
    for dirpath, dirnames, filenames in os.walk(dir):
        for f in filenames:
            filename = (dirpath + '/' + f)
            if checkSqlite3File(filename):
                found_sqlite3_files.append(filename)

checkDir(INPUT_DIR)
print("[*] Found %s sqlite files." % (len(found_sqlite3_files)))


## 0x2 export all sqlite 3 files
index = 0
for filename in found_sqlite3_files:
    file_full_path = filename
    file_basename = os.path.basename(filename)

    # make output folder
    save_folder = OUTPUT_DIR + "/" + str(index) + "_" +  file_basename.replace(" ",'_')
    from pathlib import Path
    path = Path(save_folder)
    path.mkdir(parents=True, exist_ok=True)

    # Run command
    os.system('python3 sqlite_dump.py --db "%s"  --output "%s"' % (file_full_path, save_folder))

    index += 1

print("OK!")
