# A cell on the board
class Cell:
    def __init__(self):
        self._cell = "dead"

    def setDead(self):
        self._cell = "dead"

    def setAlive(self):
        self._cell = "alive"

    def isAlive(self):
        return self._cell == "alive"

    def getStatus(self):
        if self._cell == "alive":
            return "O"
        if self._cell == "dead":
            return "."
