import copy
import NewProblem

# define a class for the tic tac toe problem 
class ticTacToe(NewProblem.ProblemClass): # Inherit the problem super class from Problem.py

    def __init__(self, initState):
        """ Arbitrary state: where 1 is an x, 0 is an empty cell, and -1 is an O
            [0, 0, 0],
            [0, 1, 0],
            [-1, 0, 0]
        """
        super().__init__(initState)

        self.initState = initState 
    
    def whoseTurn(self, state):
        # find out whose turn it is given the current state
        xCount = 0
        oCount = 0
        for row in range( len(state) ):
            for column in range( len(state[0]) ):
                if state[row][column] == 1:
                    xCount += 1
                elif state[row][column] == -1:
                    oCount += 1
        if xCount == oCount:
            # x's turn
            return 1
        elif xCount > oCount:
            # o's turn
            return -1        
    
    def getSuccessors(self, state): # Override the super class' getSuccessors()
        successors = []
        # Go through all cells of the board to determine whose turn it is, and store that in variable "turn"
        Turn = self.whoseTurn(state)
        # based on the "turn" variable, go through each open cell in the board and fill it in to get a successor
        for row in range( len(state) ):
            for column in range( len(state[0]) ):
                if state[row][column] == 0:
                    newState = copy.deepcopy(state)
                    newState[row][column] = Turn
                    successors.append(newState)
                    # successors.append("newState")
        return successors
    
    """ Define some helper functions for the isGoal method """
    def checkRow(self, row):
        # pass in a row somehow
        if row[0] == row[1]and row[1] == row[2]:
            # Check if there's three in a row
            if row[0] == 1:
                return (True, 1)
            elif row[0] == -1:
                return (True, -1)

    def checkColumn(self, column):
        # pass in a column somehow
        if column[0] == column[1]and column[1] == column[2]:
            if column[0] == 1:
                return (True, 1)
            elif column[0] == -1:
                return (True, -1)

    def checkDiagonal(self, diagonal):
        # pass in a diagonal somehow 
        if diagonal[0] == diagonal[1]and diagonal[1] == diagonal[2]:
            if diagonal[0] == 1:
                return (True, 1)
            elif diagonal[0] == -1:
                return (True, -1)

    # define an isgoal function
    def isGoal(self, state): 
        # Check every row
        if self.checkRow(state[0]): # Don't exactly get how this if statement works
            return self.checkRow(state[0])
        elif self.checkRow(state[1]):
            return self.checkRow(state[1])
        elif self.checkRow(state[2]):
            return self.checkRow(state[2])
        
        # Check every column
        column1 = [state[0][0], state[1][0], state[2][0]]
        column2 = [state[0][1], state[1][1], state[2][1]]
        column3 = [state[0][2], state[1][2], state[2][2]]
        if self.checkColumn(column1): 
            return self.checkColumn(column1)
        elif self.checkColumn(column2):
            return self.checkColumn(column2)
        elif self.checkColumn(column3):
            return self.checkColumn(column3)
        
        # Check both diagonals
        diagonal1 = [state[0][0],state[1][1],state[2][2]] 
        diagonal2= [state[2][2],state[1][1],state[0][0]] 
        if self.checkDiagonal(diagonal1):
            return self.checkDiagonal(diagonal1)
        if self.checkDiagonal(diagonal2):
            return self.checkDiagonal(diagonal2)
        
        emptyCount = 0
        for row in range( len(state) ):
            for column in range( len(state[0]) ):
                if state[row][column] == 0:
                    emptyCount += 1
        
        if emptyCount == 0:
            # All cells are filled and no other conditional works, so there's a tie
            return (True, 0) 
        
        # Else, the state is not an end state
        return (False, None)
            
    def argMax(self, childScores):
        # Find the maximum score given a list of childScores
        maxScore = childScores[0][0]
        for element in childScores:
            # Get the score associated with an element
            if element[0] > maxScore:
                maxScore = element[0]
        return maxScore
    
    def argMaxPos(self, childScores):
        # Find the maximum score position given a list of childScores
        maxScore = childScores[0]
        maxScorePos = childScores[0]
        for i in range( len(childScores) ):
            # Get the score associated with an element
            if childScores[i] > maxScore:
                maxScore = childScores[i]
                maxScorePos = i
        return maxScorePos

    def argMin(self, childScores):
        # Find the mimimum score given a list of childScores
        minScore = 2
        # print(maxScore)
        for element in childScores:
            # Get the score associated with an element
            if element[0] < minScore:
                minScore = element[0]
        return minScore

    def prettyPrint(self, state):
        # Turn each "1" or "-1" into an x or o 
        newState = copy.deepcopy(state)
        for row in range( len(newState) ):
            for column in range(3):
                if newState[row][column] == 1:
                    newState[row][column] = "x"
                elif newState[row][column] == -1:
                    newState[row][column] = "o"

        # print each row on a diff line
        for row in newState: 
            print(row)
        return

    def makeAMove(self, state, xCoord, yCoord):
        # Given an x and y coordinate, have the player place a piece on the board. 
        # Find out whose turn it is
        Turn = self.whoseTurn(state)
        newState = copy.deepcopy(state)
        for row in range( len(newState) ):
            for column in range(3):
                # access the x and y coordinate on the board. 
                if newState[row][column] == newState[yCoord][xCoord]:
                    if Turn == 1:
                        newState[row][column] = 1
                    else:
                        newState[row][column] = -1

    def makeAMove2(self, state, xCoord, yCoord):
        # Given an x and y coordinate, have the player place a piece on the board. 
        # Have a prompt for the user to enter coordinates
        # Change the board to reflect the user's move
        # Use this as a helper function in a gameplay loop 
        Turn = self.whoseTurn(state)
        newState = copy.deepcopy(state)
        for row in range( len(newState) ):
            for column in range(3):
                # access the x and y coordinate on the board. 
                if newState[row][column] == newState[yCoord][xCoord]:
                    if Turn == 1:
                        newState[row][column] = 1
                    else:
                        newState[row][column] = -1


    def miniMax(self, state):
        # Building a tree for the miniMax algorithm 
        (end, score) = self.isGoal(state)
        if end == True:
            return score, state
        else:
            childScores = []
            # Go through each childState given by the getSuccessors function
            for childState in self.getSuccessors(state):
                # Recurse to get the score of the child
                childScore = self.miniMax(childState)
                # Add that score, as well as the state associated with that score to a table of childScores
                childScores.append((childScore[0], childState))
        
        Turn = self.whoseTurn(state)

        # Choose the top level action with the highest or lowest val, depending on whose turn it is
        if Turn == 1:
            # Get the position of the max child score
            for i in range( len(childScores) ):
                if childScores[i][0] == self.argMax(childScores):
                    return self.argMax(childScores), childScores[i][1]
        elif Turn == -1:
            # Get the position of the min child score
            for i in range( len(childScores) ):
                if childScores[i][0] == self.argMin(childScores):
                    return self.argMin(childScores), childScores[i][1]

# Notes:
    # Design choices 

# Questions:
    # Were you hoping for a gameplay loop? 
        # Basic user interfacing, using a game instance. 