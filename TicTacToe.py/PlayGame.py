""" Create a class to play the tic tac toe game so as to decouple gameplay from the game itself """
import GameProblem
import copy

class PlayGame:
    def __init__(self):
        # Initialize a board
        initialState = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.board = GameProblem.ticTacToe(initialState)
        self.state = initialState

    def makeAMove(self, state):
        newState = copy.deepcopy(state) # Do I need to create a newState here? 
        yCoord = int( input("Enter a row #(between 0 and 2):") )
        xCoord = int( input("Enter a column #(between 0 and 2):") )
        for row in range( len(newState) ):
            for column in range(3):
                # access the x and y coordinate on the board. 
                if row == yCoord and column == xCoord: # Comparing coords rather than elements
                    newState[row][column] = -1 # "o" vs. -1
        return newState
                    
    def startGame(self):

        # Loop until an end condition has been met
        while True: # Not sure how to only check the "end" variable from the isgoal method here
            # Have the ai go first(i.e. as x)
            newState1 = self.board.miniMax(self.state)[1]
            # Return the board associated with their move, and update self.state
            self.board.prettyPrint(newState1)
            self.state = newState1
            end, score = self.board.isGoal(self.state)
            if end == False:
                pass
            else:
                return "Game Over"
            # Have the player go second through typing in a row and column(i.e. as o)
            newState2 = self.makeAMove(newState1)
            # Return the board associated with their move 
            self.board.prettyPrint(newState2)
            self.state = newState2
            end, score = self.board.isGoal(self.state)
            if end == False:
                pass
            else:
                return "Game Over"


PlayGameObject = PlayGame()
PlayGameObject.startGame()
# PlayGameObject