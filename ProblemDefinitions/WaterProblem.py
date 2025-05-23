import abc
import copy # abstract base class

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

class WaterPouringProblem(Problem):
    """ Arbitray state:
        [<jug 1 pints>, <jug 2 pints>]
        [2, 3]  
        Goal state:
        exactly 2 pints in jug 2
        Constraints:
        Not sure what they are, though they would affect the code in the pouring action. 
    """
    def __init__(self, initState):
        super().__init__(initState)
        self.actions = [self.emptyJug0, self.emptyJug1, self.fillJug0, self.fillJug1, self.pouringJug0, self.pouringJug1]
    
    def emptyJug0(self, state):
        newState = self.emptyJug(state, 0)
        return newState
    
    def emptyJug1(self, state):
        newState = self.emptyJug(state, 1)
        return newState

    def emptyJug(self, state, jugToEmpty):
        # Get the jugToEmpty
        newState = copy.copy(state)
        if newState[jugToEmpty] == 0:
            return None
        else:
            newState[jugToEmpty] = 0
            return newState

    def fillJug0(self, state):
        newState = self.fillJug(state, 0)
        return newState
    
    def fillJug1(self, state):
        newState = self.fillJug(state, 1)
        return newState

    def fillJug(self, state, jugToFill):
        # Get the jugToFill
        """ Jug 1 has a capacity of 7 pints
            Jug 2 has a capacity of 3 pints
        """
        newState = copy.copy(state)
        if jugToFill == 0:
            if state[jugToFill] == 7:
                return None
            newState[jugToFill] = 7
            return newState
        else:
            if state[jugToFill] == 3:
                return None
            newState[jugToFill] = 3
            return newState

    def pouringJug0(self, state):
        newState = self.pouring(state, 0)
        return newState
    
    def pouringJug1(self, state):
        newState = self.pouring(state, 1)
        return newState

    def pouring(self, state, jugToFill):
        # Get both jugs and name them appropriately 
        jugToEmpty = 1 - jugToFill
        newState = copy.copy(state)
        currentFill = newState[jugToFill]
        # Define the capacity based on the jug
        if jugToFill == 0:
            if state[jugToFill] == 7:
                return None
            currentMax = 7
        else:
            if state[jugToFill] == 3:
                return None
            currentMax = 3
        # Add to one jug and subtract from the other
        amountToSet = min(currentMax, (newState[jugToFill] + newState[jugToEmpty]) )
        newState[jugToFill] = amountToSet
        newState[jugToEmpty] -= (amountToSet - currentFill)
        return newState
    
    def isGoal(self, state):
        if state[1] == 2:
            return True
        else:
            return False
