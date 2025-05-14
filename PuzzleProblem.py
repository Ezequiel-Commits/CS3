import abc # abstract base class
import copy 

# abstract class 
class Problem(abc.ABC):
    def __init__(self, initState):
        super().__init__()
        self.initState = initState
        self.actions = None

    def getSuccessors(self, state):
        """ returns a list of sucessor states(children states) """
        retVal = []
        # for each action in self.actions:
        for action in self.actions:
            # run the action and get the resulting state
            newState = action(state)
            if  newState != None:
                # if the result is not none, append the value
                retVal.append(newState)
        return retVal

class puzzle(Problem):
    """ Arbitrary state:
        [ [<top row>],
        [<middle row>],
        [<bottom row>] ]
        0 stands for the blank space

        [ [1, 3, 2],
        [4, 6, 5],
        [7, 0, 8] ]   

        Constraints:
            Some movement will return None, as they're "illegal"
    """
    def __init__(self, initState):
        super().__init__(initState)
        self.actions = [ self.actMoveUp, self.actMoveDown, self.actMoveRight, self.actMoveLeft]

    def getBlank(self, state):
        for i in range(len(state)):
            for j in range(len(state)):
                if state[i][j] == 0:
                    return (i, j)
        
        assert(False) # Throw an error otherwise
                        

    def actMoveUp(self, state):
        """ Preconditions: 
            If moving the blank space(0) up, it can't be against the north wall
         Successors:
        """
        # Find the blank space
        (row, column) = self.getBlank(state)
        if row == 0:
            # illegal move
            return state
        newState = copy.deepcopy(state) #Copy all sublists
        newState[row-1][column] = state[row][column]
        newState[row][column] = state[row-1][column]
        return newState

    def actMoveDown(self, state):
        """ Preconditions: 
            If moving the blank space(0) Down, it can't be against the south wall
         Successors:
        """
        # Find the blank space
        (row, column) = self.getBlank(state)
        if row == 2:
            # illegal move
            return state
        newState = copy.deepcopy(state) #Copy all sublists
        newState[row+1][column] = state[row][column]
        newState[row][column] = state[row+1][column]
        return newState

    def actMoveRight(self, state):
        # Move right
        """ Preconditions:
            If moving the blank space right, it can't be against the east wall
         Successors:
        """
        # Find the blank space
        (row, column) = self.getBlank(state)
        if column == 2:
            # illegal move
            return state
        newState = copy.deepcopy(state) #Copy all sublists
        newState[row][column+1] = state[row][column]
        newState[row][column] = state[row][column+1]
        return newState
    
    def actMoveLeft(self, state):
        # Move right
        """ Preconditions:
            If moving the blank space right, it can't be against the west wall
         Successors:
        """
        # Find the blank space
        (row, column) = self.getBlank(state)
        if column == 0:
            # illegal move
            return state
        newState = copy.deepcopy(state) #Copy all sublists
        newState[row][column-1] = state[row][column]
        newState[row][column] = state[row][column-1]
        return newState
    
    def isGoal(self, state):
        if state == [[1,2,3],[4,5,6],[7,8,0]]: #Syntax
            return True
        else:
            return False  
    
# Questions: How can I avoid loads of if statements starting on line 59? 
    # define a getBlank() function
    # (r,c) = getBlank()
    # newState(r,c) = newState(r,c+1); newState(r,c+1) = blankSpace(example of right movement) 
# Do I have to repeat these nested loops again for each movement? 