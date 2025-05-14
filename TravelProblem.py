import Problem

class travelProblem( Problem.ProblemClass ):
    """ Arbitray state:
        "O",
        "Z",
        "S"
    """
    def __init__(self, initState):
        super().__init__(initState)
        
        # Define a dictionary
        self.cities = {
            "O": (["Z", 71], ["S", 151]),
            "Z": (["O", 71], ["A", 75]),
            "S": (["O", 151], ["A", 140])
        } 

    def getSuccessors(self, state):
        # Get the values associated with a key(state) from self.cities
        if isinstance(state, list):
            # Get the letter in the value list
            city = state[0]
            successors = self.cities.get(city)
        else:
            successors = self.cities.get(state)
        return successors
    
    def isGoal(self, state):
            if state[0] == "A":
                return True
            else:
                return False

# Questions:
    # How do I write dry comments? 
    # Do I need to change the way my dictionary values are structured?(lists to tuples?)
# Notes:
