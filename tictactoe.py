# Final Project
import random


# Tic Tac Toe
class TicTacToe:
    def drawBoard(board):
        # This function prints out the board that it was passed.
        # "board" is a list of 10 strings representing the board (ignore index 0)
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('-----------')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('-----------')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

    def inputPlayerLetter():
        # Lets the player type which letter they want to be.
        # Returns a list with the player's letter as the first item, and the other player's letter as the second.
        return ['O', 'X']

    def whoGoesFirst():
        # Randomly chooses which player goes first.
        if random.randint(0, 1) == 0:
            return 'player1'
        else:
            return 'player2'

    def playAgain():
        # This function returns True if the player wants to play again, otherwise it will False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

    def makeMove(board, letter, move):
        board[move] = letter

    def isWinner(bo, le):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
                (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
                (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
                (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
                (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
                (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
                (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
                (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal

    def getBoardCopy(board):
        # Make a duplicate of the board list and return it the duplicate.
        dupeBoard = []

        for i in board:
            dupeBoard.append(i)

        return dupeBoard

    def isSpaceFree(board, move):
        # Return true if the passed move is free on the passed board.
        return board[move] == ' '

    def getPlayerMove(board):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not TicTacToe.isSpaceFree(board, int(move)):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)

    def isBoardFull(board):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if TicTacToe.isSpaceFree(board, i):
                return False
        return True


print('Welcome to Tic Tac Toe!')
# This will serve as an example for the user
print('Example of Board:')
print(' ' + '7' + ' | ' + '8' + ' | ' + '9')
print('-----------')
print(' ' + '4' + ' | ' + '5' + ' | ' + '6')
print('-----------')
print(' ' + '1' + ' | ' + '2' + ' | ' + '3')

while True:
    # Reset the board
    theBoard = [' '] * 10

    playerLetter, player2Letter = TicTacToe.inputPlayerLetter()

    turn = TicTacToe.whoGoesFirst()
    print(turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player1':
            # Player1's turn.
            TicTacToe.drawBoard(theBoard)
            move = TicTacToe.getPlayerMove(theBoard)
            TicTacToe.makeMove(theBoard, playerLetter, move)

            if TicTacToe.isWinner(theBoard, playerLetter):
                TicTacToe.drawBoard(theBoard)
                print('Hooray! Player1 has won the game!')
                gameIsPlaying = False
            else:
                if TicTacToe.isBoardFull(theBoard):
                    TicTacToe.drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player2'

        else:
            # Player2's turn.
            TicTacToe.drawBoard(theBoard)
            move = TicTacToe.getPlayerMove(theBoard)
            TicTacToe.makeMove(theBoard, player2Letter, move)

            if TicTacToe.isWinner(theBoard, player2Letter):
                TicTacToe.drawBoard(theBoard)
                print('Hooray! Player2 has won the game!')
                gameIsPlaying = False
            else:
                if TicTacToe.isBoardFull(theBoard):
                    TicTacToe.drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player1'

    if not TicTacToe.playAgain():
        break
