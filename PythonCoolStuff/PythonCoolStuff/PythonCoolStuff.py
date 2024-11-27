from FuncsForMe import *
FilesAmount, Path, Files = startUp()
#FilesAmount and path are loaded from conf file
while True:
    print('Menu of my engine:')
    print('0. Exit')
    print('1. Load All Files to RAM')
    choice = int(input())
    match choice:
        case 0:
            break
        case 1:
            LoadAllFiles(Path,FilesAmount)

