from fileManager import FileManager

class WorkerManager:

    def __init__(self):
        self.workerList = []

    def controller(self):
        self.workerList = FileManager.betolt_alkalmazottakat("alkalmazottak.txt")
        
        name, salary = self.legnagyobb_fizetett()
        print(f"Legjobban fizetett ember: {name} fizetése: {salary}")

    def legnagyobb_fizetett(self):
        highest_worker = self.workerList[0]
        for worker in self.workerList:
            if int(worker.fizetes) > int(highest_worker.fizetes):
                highest_worker = worker
        return highest_worker.nev, highest_worker.fizetes