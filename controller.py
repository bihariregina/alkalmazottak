from fileManager import FileManager

class WorkerManager(FileManager):

    def __init__(self):
        self.workerList = []

    def controller(self):
        self.workerList = self.betolt_alkalmazottakat("alkalmazottak.txt")

        self.addWorker()

        data = self.legnagyobb_fizetett()
        name = self.workerList[self.workerList.index(data)][1]
        salary = self.workerList[self.workerList.index(data)][2]
print(f"Legjobban fizetett ember: {name} fizetése: {salary}")

        self.ment_alkalmazottakat(self.workerList, "teszt.txt")

    def addWorker(self):
        worker = ['1016','János Jani','450000','Fejlesztő']
        self.workerList.append(worker)
        print(self.workerList)

    def legnagyobb_fizetett(self):
        highest_worker = self.workerList[0]
        for worker in self.workerList:
            if int(worker[2]) > int(highest_worker[2]):
                highest_worker = worker
        return highest_worker


wm = WorkerManager()
wm.controller()