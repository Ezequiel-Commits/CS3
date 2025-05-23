import DFSsearch
import ProblemDefinitions.PuzzleProblem as PuzzleProblem
import ProblemDefinitions.Problem as Problem
import BFSsearch 
import ProblemDefinitions.TravelProblem as TravelProblem
import WolvesAndGoats
import WaterProblem
import BestFSsearch
import English

""" Combine problem formulation with search """
# vacuumProblem = Problem.VacuumProblem([True, True, 0])
# initialState = vacuumProblem.initState

# puzzleProblem = PuzzleProblem.puzzle( [[1,2,3],[4,0,6],[7,5,8]] )
# initialState = puzzleProblem.initState

# waterProblem1 = WaterProblem.WaterPouringProblem([0,0])
# initialState = waterProblem1.initState

# newState = waterProblem1.fillJug(initialState, 1)
# print(waterProblem1.pouring(newState, 0))

# print(DFSsearch.DFSSearch(puzzleProblem))
# print(BFSsearch.BFSSearch(puzzleProblem))


""" Best first search """
# travelProblemObject = TravelProblem.travelProblem("O")
# initialState = travelProblemObject.initState

# print(BestFSsearch.BestFSsearch(travelProblemObject))
# print(travelProblemObject.getSuccessors(initialState))

