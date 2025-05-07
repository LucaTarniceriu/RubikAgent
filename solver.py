from cubeSimulator import *
alpha = 0.2
gamma = 0.95

state = myCube
action = 'r'
nextState = moveCube(myCube, 'r')
q = [{}]
q[state][action] = q[state][action] + alpha * (reward(state, action) + gamma * max(q[nextState]) - q[state][action])