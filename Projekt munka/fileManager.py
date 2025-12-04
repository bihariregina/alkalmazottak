class Worker:
    def __init__(self, id, nev, fizetes, munkakor):
        self.id = id
        self.nev = nev
        self.fizetes = int(fizetes)
        self.munkakor = munkakor

    def __repr__(self):
        return f"{self.id} - {self.nev} - {self.fizetes} - {self.munkakor}"

class FileManager:

    def betolt_alkalmazottakat(fajlnev):
        workerList = []
        with open(fajlnev, "r", encoding="utf8") as file:
            for line in file:
                adat = line.strip().split(";")
                if len(adat) == 4:
                    worker = Worker(adat[0], adat[1], adat[2], adat[3])
                    workerList.append(worker)
        return workerList


