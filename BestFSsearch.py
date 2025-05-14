""" A Best first search algorithm to find a path to the goal """

# BFS (BIFO)

import DataStructures
import Problem

class Node:
    def __init__(self, state = None, parent = None): # Add a cost data member? 
        self.state = state
        self.parent = parent
    
    def __repr__(self):
        return str(self.state)

def searchForState(node):
    # Search for the state of a given node 
    if isinstance(node, list):
        if node[0] != None:
            return node[0] #Messy?
        else:
            return None
    elif node.state != None:
        return node.state
    else:
        return None

def BestFSsearch(specificProblem):
    frontier = DataStructures.PriorityQueue()
    # Add the initial state to the frontier
    initialNode = Node(specificProblem.initState, None)
    frontier.enqueue(initialNode)
    # Initialize an array of explored "nodes"
    ExploredValues = []
    while frontier.myPriorityQueue != []:
        # choose a frontier node which serves as a state
        nextNode = frontier.dequeue()

        if specificProblem.isGoal( nextNode.state ):
            # Print that path in its entirety
            print(nextNode.state)
            while nextNode.parent != None:
                nextNode = nextNode.parent
                print(nextNode.state)
            return
        
        ExploredValues.append(nextNode.state)

        # Get successors now gives action cost as well 
        successors = specificProblem.getSuccessors( nextNode.state )

        for successor in successors: 
            listedState = searchForState(nextNode)
            if (successor not in ExploredValues) and (listedState not in frontier.myPriorityQueue): 
                # Get the action cost of the successor
                frontier.enqueue( Node(successor, nextNode) ) 

# Questions:
    # my successor loop keeps on adding "Z" and "O"
# Notes:
    # Still have to replace a duplicate path with different costs somehow 
    # Don't exactly get the second conditional in line 49, nor that loop in general 
