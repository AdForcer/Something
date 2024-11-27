def startUp():
    Config = open('Config.txt')
    FilesAmount = int(Config.readline()[15:])
    Path = Config.readline()[7:]
    Config.close()
    return FilesAmount, Path
def aWriter(Number):
    if Number != int():
        rNumber = int(Number)
    else:
        rNumber = Number
def LoadFiles(Path, FilesAmount):
    Files = []
    for i in range(FilesAmount):
        File = open(f'{Path}\{i}.penis', 'r')
        Files.append(File.readlines())
        File.close()
    return Files
def WriteAFile(Path, File_ID, Information):
    File = open(f'{Path}\{File_ID}.penis','w')
    File.write(Information)
    File.close()
def CopyFile(Path, File_ID, New_File_ID):
    Original_File = open(f'{Path}\{File_ID}.penis', 'r')
    Original_Information = Original_File.readlines()
    Original_File.close()
    tmp = ''
    for i in range(len(Original_Information)):
        tmp+=Original_Information[i]
    WriteAFile(Path,New_File_ID,tmp)



    