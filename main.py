import DFSsearch
import PuzzleProblem
import Problem
import BFSsearch 
import TravelProblem
import WolvesAndGoats
import WaterProblem
import BestFSsearch

# vacuumProblem = Problem.VacuumProblem([True, True, 0])
# initialState = vacuumProblem.initState

# puzzleProblem = PuzzleProblem.puzzle( [[1,2,3],[4,0,6],[7,5,8]] )
# initialState = puzzleProblem.initState


# print(DFSsearch.DFSSearch(puzzleProblem))
# print(BFSsearch.BFSSearch(puzzleProblem))


""" Diff assign. """
travelProblemObject = TravelProblem.travelProblem("O")
initialState = travelProblemObject.initState

print(BestFSsearch.BestFSsearch(travelProblemObject))
# print(travelProblemObject.getSuccessors(initialState))
