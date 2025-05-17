import GameProblem


initialState1 = [
    # loss, o's turn
    [0, 0, 0],
    [0, -1, 1],
    [1, -1, 1] 
]

initialState2 = [
    # win, x's turn
    [0, 0, 0],
    [0, -1, 1],
    [0, -1, 1] 
]

initialState3 = [
    # Draw, x's turn
    [0, 1, -1],
    [0, -1, 1],
    [0, -1, 1] 
]

initialState4 = [
    # win in 2, x's turn
    [1, 0, 1],
    [0, -1, 0],
    [1, 0, -1] 
]


gameObject = GameProblem.ticTacToe(initialState1)

# print(gameObject.getSuccessors(initialState))
# print(gameObject.miniMax(initialState1))
# print(gameObject.miniMax(initialState2))
# print(gameObject.miniMax(initialState3))
gameObject.prettyPrint(initialState1)

