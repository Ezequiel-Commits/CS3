""" A depth first search algorithm to find a path to the goal """

# DFS (LIFO)

import DataStructures
import ProblemDefinitions.Problem as Problem

class Node:
    def __init__(self, state = None, parent = None):
        self.state = state
        self.parent = parent
    
    def __repr__(self):
        return str(self.state)

def searchForState(node):
    # Search for the state of a given node 
    if node.state != None:
        return node.state
    else:
        return None
    

def DFSSearch(specificProblem):
    frontier = DataStructures.Stack()
    # Add the initial state to the frontier
    initialNode = Node(specificProblem.initState, None)
    frontier.push(initialNode)
    # Initialize an array of explored "nodes"
    ExploredValues = []
    while frontier.myStack != []:
        # choose a frontier node which serves as a state
        nextNode = frontier.pop()

        if specificProblem.isGoal( nextNode.state ):
            print(nextNode.state)
            while nextNode.parent != None:
                nextNode = nextNode.parent
                print(nextNode.state)
            return

        # Add the node to the explored set 
        ExploredValues.append(nextNode.state) # Memorization

        successors = specificProblem.getSuccessors( nextNode.state )
        
        for successor in successors: 
            listedState = searchForState(nextNode)
            if (successor not in ExploredValues) and (listedState not in frontier.myStack): #Compare the state(successor) to nextNode states in the frontier 
                frontier.push( Node(successor, nextNode) ) #Not sure this is what Proshanto wanted me to do

    print("returning this false")    
    return False

# Notes:
    # I assume my problem is between lines 47 and 50; likely in the searchForState function 
