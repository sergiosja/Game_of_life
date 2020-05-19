from board import Board


def main():
    rowAmount = int(input("How many rows would you like? "))
    columnAmount = int(input("How many columns would you like? "))
    game = Board(rowAmount, columnAmount)
    game.drawBoard()
    aliveCells = game.getAliveCells()

    print("Generation: ", game._generation, "| Alive cells: ", aliveCells)
    decision = input("Press 'enter' to update board, or 'q' to end program ")

    while decision != "q":
        game.update()
        game.drawBoard()
        aliveCells = game.getAliveCells()

        print("Generation: ", game._generation, "| Alive cells: ", aliveCells)
        decision = input("Press 'enter' to update board or 'q' to end program ")


main()
