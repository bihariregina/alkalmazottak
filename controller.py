from fileManager import FileManager
class WorkerManager:

    def __init__( self ):
        
        self.workerList = []

    def controller(self):
        self.workerList = FileManager.betolt_alkalmazottakat("alkalmazottak.txt"):
        highestSalaryName, highestSalaryNumber=self.legnagyobb_fizetett()
        print("Legtöbbet kereső ember: {:^10}\n".format(highestSalaryName, highestSalaryNumber))


    def legnagyobb_fizetett(self):
            max=0
            Highest=int(self.workerList[0])
            for worker in self.workerList:
                if Highest<int(worker.fizetes):
                    Highest=int(worker.fizetes)
                    max = worker.nev
            return max, tempHighest