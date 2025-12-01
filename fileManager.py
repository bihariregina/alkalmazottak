class FileManager:
    def __init__(self):
        pass

    def betolt_alkalmazottakat(self, fajlnev):

        workerList = []
        file = open(fajlnev, "r", encoding="utf8")
        row = True
        while row:
            row = file.readline()
            rowSp = row.split(";")
            if len(rowSp) > 1:
                workerList.append(rowSp)
        return workerList

    def ment_alkalmazottakat(self, workerList ,fajlnev):

        file = open(fajlnev, "w", encoding="utf8")
        for worker in workerList:
            for data in worker:
                file.write(data)
                file.write(" ")
        file.close()
        print("A lista átírva a",fajlnev,"fájlba")

