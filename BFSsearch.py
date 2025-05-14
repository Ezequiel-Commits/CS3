""" A search algorithm to find a path to the goal """

# BFS (FIFO)

import DataStructures
import Problem

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
    

def BFSSearch(specificProblem):
    """ Run BFS on the specific problem """
    frontier = DataStructures.Queue()
    # Add the initial state to the frontier
    initialNode = Node(specificProblem.initState, None)
    frontier.enqueue(initialNode)
    # Initialize an array of explored "nodes"
    ExploredValues = []

    while frontier.myQueue != []:
        # choose a frontier node which serves as a state
        nextNode = frontier.dequeue()

        if specificProblem.isGoal( nextNode.state ):
            print(nextNode.state)
            while nextNode.parent != None:
                nextNode = nextNode.parent
                print(nextNode.state)
            return
            # for parents in nextNode.parent:
                # return the solution by returning a list of all the actions


        # Add the node to the explored set 
        ExploredValues.append(nextNode.state) # Memorization

        successors = specificProblem.getSuccessors( nextNode.state )
        
        for successor in successors: 
            listedState = searchForState(nextNode)
            if (successor not in ExploredValues) and (listedState not in frontier.myQueue): #Compare the state(successor) to nextNode states in the frontier 
                frontier.enqueue( Node(successor, nextNode) ) #Not sure this is what Proshanto wanted me to do
        
    return False