import GameProblem


initialState1 = [
    [0, 0, 0],
    [0, -1, 1],
    [1, -1, 1] #Using tracer bullets
]

initialState2 = [
    [0, 0, 0],
    [0, -1, 1],
    [0, -1, 1] #Using tracer bullets
]

initialState3 = [
    [0, 1, -1],
    [0, -1, 1],
    [0, -1, 1] #Using tracer bullets
]

initialState4 = [
    [1, 0, 1],
    [0, -1, 0],
    [1, 0, -1] #Using tracer bullets
]


gameObject = GameProblem.ticTacToe(initialState1)

# print(gameObject.getSuccessors(initialState))
# print(gameObject.miniMax(initialState1))
# print(gameObject.miniMax(initialState2))
# print(gameObject.miniMax(initialState3))
print(gameObject.miniMax(initialState4))

