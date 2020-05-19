from random import randint
from cell import Cell

# Visual representation in the terminal
class Board:
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        self._board = []
        self._generation = 0

        for i in range(self._rows):
            self._board.append([])
            for j in range(self._columns):
                self._board[i].append(Cell())

        self.generate()

    # Method to draw the "board"
    def drawBoard(self):
        for i in range(50):
            print("")

        for row in self._board:
            for cell in row:
                if row.index(cell) == len(row) - 1:
                    print(cell.getStatus())
                else:
                    print(cell.getStatus(), end="")

    # Method to update the "board"
    def update(self):
        aliveList = []
        deadList = []

        for row in range(self._rows):
            for column in range(self._columns):

                neighbours = self.findNeighbour(row, column)
                aliveNeighbours = 0
                for i in neighbours:
                    if i.isAlive():
                        aliveNeighbours += 1

                if self._board[row][column].isAlive():
                    if aliveNeighbours < 2 or aliveNeighbours > 3:
                        deadList.append(self._board[row][column])

                else:
                    if aliveNeighbours == 3:
                        aliveList.append(self._board[row][column])

        for i in aliveList:
            i.setAlive()
        for j in deadList:
            j.setDead()

        self._generation += 1

    # Method to gather amount of live cells
    def getAliveCells(self):
        cellAmount = 0
        for row in range(self._rows):
            for column in range(self._columns):
                if self._board[row][column].isAlive():
                    cellAmount += 1

        return cellAmount

    # Method to generate random amount of dead & alive cells when the program is started
    def generate(self):
        for row in self._board:
            for i in row:
                status = randint(0, 3)
                if status == 0:
                    i.setAlive()

    # Method to locate neighbours
    def findNeighbour(self, row, column):
        cellNeighbours = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                rowNeighbours = row + i
                columnNeighbours = column + j
                trueNeighbour = True

                if rowNeighbours == row and columnNeighbours == column:
                    trueNeighbour = False
                if rowNeighbours >= self._rows or rowNeighbours < 0:
                    trueNeighbour = False
                if columnNeighbours >= self._columns or columnNeighbours < 0:
                    trueNeighbour = False
                if trueNeighbour:
                    cellNeighbours.append(self._board[rowNeighbours][columnNeighbours])

        return cellNeighbours
