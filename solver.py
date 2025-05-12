from cubeSimulator import *
import random


alpha = 0.2
gamma = 0.95
epsilon = 1.0
epsilonDecayRate = 0.99
minEpsilon = 0.05
episodes = 10000

mycube3 = [[[0]*9, [1]*9, [2]*9, [3]*9, [4]*9, [5]*9, [6]*9], []]
# scrambeledCube = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [4, 5, 2, 2, 1, 3, 6, 4, 4], [6, 4, 2, 2, 2, 3, 1, 1, 2], [3, 5, 6, 6, 3, 6, 6, 4, 4], [1, 1, 3, 1, 4, 5, 5, 6, 2], [4, 1, 5, 4, 5, 6, 5, 3, 3], [1, 5, 5, 2, 6, 2, 1, 3, 3], []]

scramble = ['f', 'ri', 'u', 'u', 'l', 'di', 'b', 'b', 'ui', 'r', 'fi', 'd', 'd', 'u', 'l', 'l', 'b', 'd', 'fi', 'r', 'r', 'di', 'u', 'u']


def maxState(q, state):


    max = q[list(q.keys())[0]]
    maxMove = list(q.keys())[0][1]
    found = 0
    for moves in possibleMoves:
        if (str(state), moves) in q.keys():
            if q[(str(state), moves)] > max:
                max = q[(str(state),  moves)]
                maxMove = moves
                found = 1
    if found == 0:
        return [-1, -1]
    else:
        return [max, maxMove]

# state = mycube3
# action = 'r'
# nextState = moveCube('r', mycube3)
q = {
    (str(mycube3), 'r') : 0,
    (str(mycube3), 'ri') : 0,
    (str(mycube3), 'l') : 0,
    (str(mycube3), 'li') : 0,
    (str(mycube3), 'u') : 0,
    (str(mycube3), 'ui') : 0,
    (str(mycube3), 'd') : 0,
    (str(mycube3), 'di' ): 0,
    (str(mycube3), 'f') : 0,
    (str(mycube3), 'fi') : 0,
    (str(mycube3), 'b') : 0,
    (str(mycube3), 'bi') : 0
}

# q[(state, action)] = q[(state, action)] + alpha * (reward(state, action) + gamma * maxState(q, nextState)[0] - q[(state, action)])

scrambleCube(scramble, mycube3)
printCube(mycube3[0])

for ep in range(episodes):
    score = 0
    # scrambeledCube = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [4, 5, 2, 2, 1, 3, 6, 4, 4], [6, 4, 2, 2, 2, 3, 1, 1, 2], [3, 5, 6, 6, 3, 6, 6, 4, 4], [1, 1, 3, 1, 4, 5, 5, 6, 2], [4, 1, 5, 4, 5, 6, 5, 3, 3], [1, 5, 5, 2, 6, 2, 1, 3, 3], []]
    scrambeledCube = mycube3
    currentState = scrambeledCube.copy()
    for tries in range(300):
        if random.uniform(0, 1) < epsilon:
            #exploration
            action = possibleMoves[random.randint(0, len(possibleMoves)-1)]
            actiontype = "random"
        else:
            #exploitation
            action = maxState(q, currentState[0])[1]
            if action == -1:
                action = possibleMoves[random.randint(0, len(possibleMoves) - 1)]
                actiontype = "random"
            else:
                actiontype = "best"

        nextState = moveCube(action, currentState)

        if (str(currentState[0]), action) in q.keys():
            q[(str(currentState[0]), action)] = q[(str(currentState[0]), action)] + alpha * (reward(currentState, action) + gamma * maxState(q, nextState[0])[0] - q[(str(currentState[0]), action)])
            score += reward(currentState, action)
        else:
            q[(str(currentState[0]), action)] = 0
        print(action, score, actiontype)
        currentState = nextState

        if isSolved(currentState[0]):
            print("I have solved it!!")
            break
        epsilon = max(minEpsilon, epsilon * epsilonDecayRate)
    print("end of episode")