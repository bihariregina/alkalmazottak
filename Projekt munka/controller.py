from fileManager import FileManager

class WorkerManager:

    def __init__(self):
        self.workerList = []

    def controller(self):
        self.workerList = FileManager.betolt_alkalmazottakat("alkalmazottak.txt")
        name, salary = self.legnagyobb_fizetett()
        print(f"Legjobban fizetett ember: {name} fizetése: {salary} Ft")
    
    def legnagyobb_fizetett(self):
        highest_worker = self.workerList[0]
        for worker in self.workerList:
            if worker.fizetes > highest_worker.fizetes:
                highest_worker = worker
        return highest_worker.nev, highest_worker.fizetes

if __name__ == "__main__":
    wm = WorkerManager()
    wm.controller()