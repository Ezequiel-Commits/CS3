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
    
class WolvesProblem(Problem): 
    """ Arbitrary State:
            [<Wolves right>, <Goats right>, <Raft Side>, <Wolves left>, <Goats right>]
            E.g. [3, 3, 0, 0, 0]
            0 = left side, 1 = right side
        Constraints:
            Wolves must never outnumber goats on either side of the river
            Do I allow moving animals from the right to the left side? 
    """
    def __init__(self, initState):
        super().__init__(initState)
        self.actions = [self.moveRaft, self.moveGoat, self.moveWolf]
    
    def moveAnimals(self, state, animalsToMove):
        # Get the side the raft is on
        raftSide = state[2]
        newState = copy.copy(state)
        if animalsToMove <= 1:
            if animalsToMove == 1 and newState[0] == newState[1]:
                # Move a wolf first
                return None
            # check raft side
            if raftSide == 0:
                if newState[animalsToMove] == 0:
                    return None
                # move 1 animals at a time 
                newState[animalsToMove] -= 1
                newState[animalsToMove + 3] += 1 #Access the right side animals
                newState[2] = 1
                return newState
        # Move the raft first
        return None

    def moveGoat(self, state):
        newState = self.moveAnimals(state, 1)
        return newState
    
    def moveWolf(self, state):
        newState = self.moveAnimals(state, 0)
        return newState

    def moveRaft(self, state):
        # Change the side the raft is on 
        raftSide = state[2]
        newState = copy.copy(state)
        otherSide = 1 - raftSide
        newState[2] = otherSide
        return newState

    def isGoal(self, state):
        if state[3] == 3 and state[4] == 3: #Syntax
            return True
        else:
            return False  

# Notes:
    # I need to create wrapper functions for my actions 