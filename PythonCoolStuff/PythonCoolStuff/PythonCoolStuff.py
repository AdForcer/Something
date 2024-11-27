from FuncsForMe import *
FilesAmount, Path = startUp()
#FilesAmount and path are loaded from conf file
CopyFile(Path,0,1)
while True:
    print('Menu of my engine:')
    print('0. Exit')
    print('1. Load Files to memory')
    choice = int(input())
    match choice:
        case 0:
            break
        case 1:
            Files = LoadFiles(Path, FilesAmount)
print(*Files[0])

