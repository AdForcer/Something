from FuncsForMe import *
FilesAmount, Path = startUp()
#FilesAmount and path are loaded from conf file
Files = LoadFiles(Path, FilesAmount)
print(Files[0])
#while True:
#    print('Menu of my engine:')
#    print('1. Load Files to memory')

