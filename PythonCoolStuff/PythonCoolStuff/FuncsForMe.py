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


    