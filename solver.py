from cubeSimulator import *
alpha = 0.2
gamma = 0.95

state = myCube
action = 'r'
nextState = moveCube(myCube, 'r')
q = {
    (myCube, 'r') : 0,
    (myCube, 'ri') : 0,
    (myCube, 'l') : 0,
    (myCube, 'li') : 0,
    (myCube, 'u') : 0,
    (myCube, 'ui') : 0,
    (myCube, 'd') : 0,
    (myCube, 'di' ): 0,
    (myCube, 'f') : 0,
    (myCube, 'fi') : 0,
    (myCube, 'b') : 0,
    (myCube, 'bi') : 0
}

q[(state, action)] = q[(state, action)] + alpha * (reward(state, action) + gamma * max(q[nextState]) - q[(state, action)])

test