from cubeSimulator import *

def Q(state, action):
    return Q(state, action) + alpha * ( reward(state, action) + gamma * Q(nextState, nextAction) - Q(state, action))