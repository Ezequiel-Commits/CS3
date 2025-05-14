"""Code containing problem formulation"""
import abc # abstract base class
import copy  


# abstract class 
class ProblemClass(abc.ABC):
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
    
# How to go to a line: control + g

"""Vacuum World"""
class VacuumProblem( ProblemClass ):
    """Arbitray state:
    t = dirty
    f = clean
    [t,t,a]
    """
    def __init__(self, initState):
        # Run the super class constructor
        super().__init__(initState)
        # set actions list
        self.actions = [ self.actClean, self.actMove]

    def actClean(self, state):
        # Group comment
        """Implements the clean action:
        preconditions:
        successors:        
        """
        # Find the room with the vacuum
        vacRoom = state[2]

        # Preconditions:
        if state[vacRoom] == False:
            return None
        else:
            newState = copy.copy(state)
            newState[vacRoom] = False
            return newState
        
    def actMove(self, state):
        # Find the room with the vacuum
        vacRoom = state[2]
        # No preconditions
        otherRoom = 1 - vacRoom
        newState = copy.copy(state) # Why don't we change state? 
        newState[2] = otherRoom # newState[vacRoom] vs newState[2]
        return newState

    def isGoal(self, state):
        if state[0] == False and state[1] == False: #Syntax
            return True
        else:
            return False    