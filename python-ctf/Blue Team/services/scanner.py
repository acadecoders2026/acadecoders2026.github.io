### Script to look for files in a folder.

import os
import gamestate
import time

## Tried to make a scanning function, seems like it can only handle 20 files though.
## I wish there was a better way to do this!
def scan_for_files(directory):
    gamestate.log("services/scanner.py > SCANNING FILES IN: "+ directory)
    files = []
    for file in os.scandir(directory):
        gamestate.log("found file " + file.name)
        time.sleep(1)
        files.append(file)

    return files
