import os
import time
from moveFunctions import *

possibleMoves = ['r', 'ri', 'l', 'li', 'u', 'ui', 'd', 'di', 'f', 'fi', 'b', 'bi']

# ANSI escape code for 24-bit RGB foreground color
def rgb_bg(r, g, b):
    return f" \033[48;2;{r};{g};{b}m  \033[0m"
# Color definitions for each face
color_map_rgb = {
    1: (255, 165, 0),     # Orange
    2: (0, 100, 255),     # Blue
    3: (255, 0, 0),       # Red
    4: (0, 255, 0),       # Green
    5: (255, 255, 0),     # Yellow
    6: (255, 255, 255),   # White
}
reverseOf = {
    'r' : 'ri',
    'ri' : 'r',
    'l' : 'li',
    'li' : 'l',
    'u' : 'ui',
    'ui' : 'u',
    'b' : 'bi',
    'bi' : 'b',
    'f' : 'if',
    'fi' : 'f',
    'd' : 'di',
    'di' : 'd'
}
oppositeOf = {
    'r': 'l',
    'ri': 'li',
    'l': 'r',
    'li': 'ri',
    'u': 'd',
    'ui': 'di',
    'b': 'f',
    'bi': 'fi',
    'f': 'b',
    'fi': 'bi',
    'd': 'u',
    'di': 'ui'
}
def render_face(face_idx, cube):
    face = cube[face_idx]
    # Build each row by looking up color from the value in the square
    row1 = rgb_bg(*color_map_rgb[face[0]]) + rgb_bg(*color_map_rgb[face[1]]) + rgb_bg(*color_map_rgb[face[2]])
    row2 = rgb_bg(*color_map_rgb[face[3]]) + rgb_bg(*color_map_rgb[face[4]]) + rgb_bg(*color_map_rgb[face[5]])
    row3 = rgb_bg(*color_map_rgb[face[6]]) + rgb_bg(*color_map_rgb[face[7]]) + rgb_bg(*color_map_rgb[face[8]])
    return [row1, row2, row3]

def printCube(cube):
    # Fetch formatted faces
    face1 = render_face(1, cube)
    face2 = render_face(2, cube)
    face3 = render_face(3, cube)
    face4 = render_face(4, cube)
    face5 = render_face(5, cube)
    face6 = render_face(6, cube)

    # Print in net layout:
    print("          " + face5[0])
    print("          " + face5[1])
    print("          " + face5[2])
    print()
    print(face4[0] + " " + face1[0] + " " + face2[0] + " " + face3[0])
    print(face4[1] + " " + face1[1] + " " + face2[1] + " " + face3[1])
    print(face4[2] + " " + face1[2] + " " + face2[2] + " " + face3[2])
    print()
    print("          " + face6[0])
    print("          " + face6[1])
    print("          " + face6[2])

def isSolved(cube):
    for faces in range(1, 7):
        for tile in range(9):
            if cube[faces][tile] != cube[faces][0]:
                return False

    return True


def reward(cube, move):
    points = 0
    for faces in range(1, 7):
        beforeMove = 0
        for i in range(9):
            if cube[0][faces][i] == cube[0][faces][4] and i != 4:
                beforeMove += 1

    testcube = moveCube(move, cube)

    for faces in range(1, 7):
        afterMove = 0
        for i in range(9):
            if testcube[0][faces][i] == testcube[0][faces][4] and i != 4:
                afterMove += 1

    points += (afterMove - beforeMove)

    if cube[1][-1] == oppositeOf[cube[1][-2]]:
        points -= 1000
    try:
        if cube[1][-1] == cube[1][-2] == cube[1][-3] == cube[1][-4]:
            points -= 1000
    except:
        pass

    if isSolved(cube[0]):
        points += 1000

    points -= 1
    return points

os.system("clear")
print()

# while True:
#     printCube(mycube3)
#     move = input("move: ").lower()
#     os.system('clear')
#     moveCube(move, mycube3)
#     print()


def scrambleCube(scramble, cube):
    for moves in scramble:
        cube = moveCube(moves, cube)
    cube[1].clear()
    print(cube)