from cubeSimulator import *
alpha = 0.2
gamma = 0.95

def maxState(q, state):
    max = q[(state, 'r')]
    for moves in possibleMoves:
        if q[(state, moves)] > max:
            max = q[(state,  moves)]

    return max

state = mycube3
action = 'r'
nextState = moveCube(mycube3, 'r')
q = {
    (mycube3, 'r') : 0,
    (mycube3, 'ri') : 0,
    (mycube3, 'l') : 0,
    (mycube3, 'li') : 0,
    (mycube3, 'u') : 0,
    (mycube3, 'ui') : 0,
    (mycube3, 'd') : 0,
    (mycube3, 'di' ): 0,
    (mycube3, 'f') : 0,
    (mycube3, 'fi') : 0,
    (mycube3, 'b') : 0,
    (mycube3, 'bi') : 0
}

q[(state, action)] = q[(state, action)] + alpha * (reward(state, action) + gamma * maxState(q, nextState) - q[(state, action)])