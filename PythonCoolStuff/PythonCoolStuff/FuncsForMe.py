class File:
    def __init__(self, File_ID, Information):
        self.File_ID = File_ID
        self.Information = Information
    def __str__(self):
        return f'ID: {self.File_ID}\n{self.Information}\n'

def startUp():
    Files = []
    Config = open('Config\Config.txt', 'r')
    FilesAmount = int(Config.readline()[15:])
    Path = Config.readline()[7:]
    Config.close()
    StartUpFiles = open('Config\FilesIShouldLoad.txt', 'r')
    tmp = StartUpFiles.readlines()
    StartUpFiles.close()
    for i in range(len(tmp)):
        File_IDS = [tmp[i].split()]
        tmp_File_IDS = []
        for z in range(len(File_IDS[i])):
            tmp_File_IDS.append(File_IDS[i][z])
        for j in tmp_File_IDS:
            File_ID = int(j)
            print(File_ID)
            Files.append(LoadFile(Path, File_ID))
    return FilesAmount, Path, Files
      
def aWriter(Number):
    if Number != int():
        rNumber = int(Number)
    else:
        rNumber = Number

def LoadAllFiles(Path, FilesAmount):
    Files = []
    for i in range(FilesAmount):
        Loaded_File = open(f'{Path}\{i}.penis', 'r')
        tmp_File = ''
        tmp_Information = ''
        Information = Loaded_File.readlines()
        for j in range(len(Information)):
            tmp_Information+=Information[j]
        tmp_File = File(i,tmp_Information)
        Files.append(tmp_File)
        Loaded_File.close()
    return Files

def LoadFile(Path, File_ID):
    Loaded_File = open(f'{Path}\{File_ID}.penis', 'r')
    Information = Loaded_File.readlines()
    tmp_Information = ''
    for i in range(len(Information)):
        tmp_Information += Information[i]
    tmp_File = File(File_ID, tmp_Information)
    return tmp_File

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




    