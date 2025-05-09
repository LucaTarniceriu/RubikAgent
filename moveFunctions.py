def R(cube):
    o2, o5, o8 = cube[1][2], cube[1][5], cube[1][8]
    y2, y5, y8 = cube[5][2], cube[5][5], cube[5][8]
    r0, r3, r6 = cube[3][0], cube[3][3], cube[3][6]
    w2, w5, w8 = cube[6][2], cube[6][5], cube[6][8]
    b0, b1, b2, b3, b4, b5, b6, b7, b8 = cube[2]

    cube[1][2], cube[1][5], cube[1][8] = w2, w5, w8
    cube[5][2], cube[5][5], cube[5][8] = o2, o5, o8
    cube[3][0], cube[3][3], cube[3][6] = y8, y5, y2
    cube[6][2], cube[6][5], cube[6][8] = r6, r3, r0

    cube[2][0], cube[2][1], cube[2][2], cube[2][3], cube[2][4], cube[2][5], cube[2][6], cube[2][7], cube[2][8] = b6, b3, b0, b7, b4, b1, b8, b5, b2
    return cube

def RI(cube):
    o2, o5, o8 = cube[1][2], cube[1][5], cube[1][8]
    y2, y5, y8 = cube[5][2], cube[5][5], cube[5][8]
    r0, r3, r6 = cube[3][0], cube[3][3], cube[3][6]
    w2, w5, w8 = cube[6][2], cube[6][5], cube[6][8]
    b0, b1, b2, b3, b4, b5, b6, b7, b8 = cube[2]

    cube[1][2], cube[1][5], cube[1][8] = y2, y5, y8
    cube[5][2], cube[5][5], cube[5][8] = r6, r3, r0
    cube[3][0], cube[3][3], cube[3][6] = w8, w5, w2
    cube[6][2], cube[6][5], cube[6][8] = o2, o5, o8

    cube[2][0], cube[2][1], cube[2][2], cube[2][3], cube[2][4], cube[2][5], cube[2][6], cube[2][7], cube[2][8] = b2, b5, b8, b1, b4, b7, b0, b3, b6
    return cube

def L(cube):

    y0, y3, y6 = cube[5][0], cube[5][3], cube[5][6]
    o0, o3, o6  = cube[1][0], cube[1][3], cube[1][6]
    w0, w3, w6 = cube[6][0], cube[6][3], cube[6][6]
    r2, r5, r8 = cube[3][2], cube[3][5], cube[3][8]

    g0, g1, g2, g3, g4, g5, g6, g7, g8 = cube[4]

    cube[5][0], cube[5][3], cube[5][6] = r8, r5, r2
    cube[1][0], cube[1][3], cube[1][6] = y0, y3, y6
    cube[6][0], cube[6][3], cube[6][6] = o0, o3, o6
    cube[3][2], cube[3][5], cube[3][8] = w6, w3, w0

    cube[4][0], cube[4][1], cube[4][2], cube[4][3], cube[4][4], cube[4][5], cube[4][6], cube[4][7], cube[4][8] = g6, g3, g0, g7, g4, g1, g8, g5, g2

    return cube

def LI(cube):
    y0, y3, y6 = cube[5][0], cube[5][3], cube[5][6]
    o0, o3, o6 = cube[1][0], cube[1][3], cube[1][6]
    w0, w3, w6 = cube[6][0], cube[6][3], cube[6][6]
    r2, r5, r8 = cube[3][2], cube[3][5], cube[3][8]

    g0, g1, g2, g3, g4, g5, g6, g7, g8 = cube[4]

    cube[5][0], cube[5][3], cube[5][6] = o0, o3, o6
    cube[1][0], cube[1][3], cube[1][6] = w0, w3, w6
    cube[6][0], cube[6][3], cube[6][6] = r8, r5, r2
    cube[3][2], cube[3][5], cube[3][8] = y6, y3, y0

    cube[4][0], cube[4][1], cube[4][2], cube[4][3], cube[4][4], cube[4][5], cube[4][6], cube[4][7], cube[4][8] = g2, g5, g8, g1, g4, g7, g0, g3, g6

    return cube

def U(cube):

    o0, o1, o2 = cube[1][0], cube[1][1], cube[1][2]
    g0, g1, g2 = cube[4][0], cube[4][1], cube[4][2]
    r0, r1, r2 = cube[3][0], cube[3][1], cube[3][2]
    b0, b1, b2 = cube[2][0], cube[2][1], cube[2][2]

    y0, y1, y2, y3, y4, y5, y6, y7, y8 = cube[5]

    cube[1][0], cube[1][1], cube[1][2] = b0, b1, b2
    cube[4][0], cube[4][1], cube[4][2] = o0, o1, o2
    cube[3][0], cube[3][1], cube[3][2] = g0, g1, g2
    cube[2][0], cube[2][1], cube[2][2] = r0, r1, r2

    cube[5][0], cube[5][1], cube[5][2], cube[5][3], cube[5][4], cube[5][5], cube[5][6], cube[5][7], cube[5][8] = y6, y3, y0, y7, y4, y1, y8, y5, y2
    return cube

def UI(cube):
    o0, o1, o2 = cube[1][0], cube[1][1], cube[1][2]
    g0, g1, g2 = cube[4][0], cube[4][1], cube[4][2]
    r0, r1, r2 = cube[3][0], cube[3][1], cube[3][2]
    b0, b1, b2 = cube[2][0], cube[2][1], cube[2][2]

    cube[1][0], cube[1][1], cube[1][2] = g0, g1, g2
    cube[4][0], cube[4][1], cube[4][2] = r0, r1, r2
    cube[3][0], cube[3][1], cube[3][2] = b0, b1, b2
    cube[2][0], cube[2][1], cube[2][2] = o0, o1, o2

    y0, y1, y2, y3, y4, y5, y6, y7, y8 = cube[5]

    cube[5][0], cube[5][1], cube[5][2], cube[5][3], cube[5][4], cube[5][5], cube[5][6], cube[5][7], cube[5][8] = y2, y5, y8, y1, y4, y7, y0, y3, y6

    return cube

def D(cube):
    o6, o7, o8 = cube[1][6], cube[1][7], cube[1][8]
    g6, g7, g8 = cube[4][6], cube[4][7], cube[4][8]
    r6, r7, r8 = cube[3][6], cube[3][7], cube[3][8]
    b6, b7, b8 = cube[2][6], cube[2][7], cube[2][8]

    w0, w1, w2, w3, w4, w5, w6, w7, w8 = cube[6]


    cube[1][6], cube[1][7], cube[1][8] = g6, g7, g8
    cube[4][6], cube[4][7], cube[4][8] = r6, r7, r8
    cube[3][6], cube[3][7], cube[3][8] = b6, b7, b8
    cube[2][6], cube[2][7], cube[2][8] = o6, o7, o8

    cube[6][0], cube[6][1], cube[6][2], cube[6][3], cube[6][4], cube[6][5], cube[6][6], cube[6][7], cube[6][8] = w6, w3, w0, w7, w4, w1, w8, w5, w2


    return cube

def DI(cube):
    o6, o7, o8 = cube[1][6], cube[1][7], cube[1][8]
    g6, g7, g8 = cube[4][6], cube[4][7], cube[4][8]
    r6, r7, r8 = cube[3][6], cube[3][7], cube[3][8]
    b6, b7, b8 = cube[2][6], cube[2][7], cube[2][8]

    w0, w1, w2, w3, w4, w5, w6, w7, w8 = cube[6]

    cube[1][6], cube[1][7], cube[1][8] = b6, b7, b8
    cube[4][6], cube[4][7], cube[4][8] = o6, o7, o8
    cube[3][6], cube[3][7], cube[3][8] = g6, g7, g8
    cube[2][6], cube[2][7], cube[2][8] = r6, r7, r8


    cube[6][0], cube[6][1], cube[6][2], cube[6][3], cube[6][4], cube[6][5], cube[6][6], cube[6][7], cube[6][8] = w2, w5, w8, w1, w4, w7, w0, w3, w6
    return cube

def B(cube):
    y0, y1, y2 = cube[5][0], cube[5][1], cube[5][2]
    b2, b5, b8 = cube[2][2], cube[2][5], cube[2][8]
    g0, g3, g6 = cube[4][0], cube[4][3], cube[4][6]
    w6, w7, w8 = cube[6][6], cube[6][7], cube[6][8]

    r0, r1, r2, r3, r4, r5, r6, r7, r8 = cube[3]

    cube[5][0], cube[5][1], cube[5][2] = b2, b5, b8
    cube[2][2], cube[2][5], cube[2][8] = w8, w7, w6
    cube[4][0], cube[4][3], cube[4][6] = y2, y1, y0
    cube[6][6], cube[6][7], cube[6][8] = g0, g3, g6

    cube[3][0], cube[3][1], cube[3][2], cube[3][3], cube[3][4], cube[3][5], cube[3][6], cube[3][7], cube[3][8] = r6, r3, r0, r7, r4, r1, r8, r5, r2

    return cube

def BI(cube):
    y0, y1, y2 = cube[5][0], cube[5][1], cube[5][2]
    b2, b5, b8 = cube[2][2], cube[2][5], cube[2][8]
    g0, g3, g6 = cube[4][0], cube[4][3], cube[4][6]
    w6, w7, w8 = cube[6][6], cube[6][7], cube[6][8]

    r0, r1, r2, r3, r4, r5, r6, r7, r8 = cube[3]

    cube[5][0], cube[5][1], cube[5][2] = g6, g3, g0
    cube[2][2], cube[2][5], cube[2][8] = y0, y1, y2
    cube[4][0], cube[4][3], cube[4][6] = w6, w7, w8
    cube[6][6], cube[6][7], cube[6][8] = b8, b5, b2

    cube[3][0], cube[3][1], cube[3][2], cube[3][3], cube[3][4], cube[3][5], cube[3][6], cube[3][7], cube[3][8] = r2, r5, r8, r1, r4, r7, r0, r3, r6

    return cube

def F(cube):
    y6, y7, y8 = cube[5][6], cube[5][7], cube[5][8]
    b0, b3, b6 = cube[2][0], cube[2][3], cube[2][6]
    g2, g5, g8 = cube[4][2], cube[4][5], cube[4][8]
    w0, w1, w2 = cube[6][0], cube[6][1], cube[6][2]

    o0, o1, o2, o3, o4, o5, o6, o7, o8 = cube[1]

    cube[5][6], cube[5][7], cube[5][8] = g2, g5, g8
    cube[2][0], cube[2][3], cube[2][6] = y6, y7, y8
    cube[4][2], cube[4][5], cube[4][8] = w0, w1, w2
    cube[6][0], cube[6][1], cube[6][2] = b0, b3, b6

    cube[1][0], cube[1][1], cube[1][2], cube[1][3], cube[1][4], cube[1][5], cube[1][6], cube[1][7], cube[1][8] = o6, o3, o0, o7, o4, o1, o8, o5, o2
    return cube

def FI(cube):
    y6, y7, y8 = cube[5][6], cube[5][7], cube[5][8]
    b0, b3, b6 = cube[2][0], cube[2][3], cube[2][6]
    g2, g5, g8 = cube[4][2], cube[4][5], cube[4][8]
    w0, w1, w2 = cube[6][0], cube[6][1], cube[6][2]

    o0, o1, o2, o3, o4, o5, o6, o7, o8 = cube[1]

    cube[5][6], cube[5][7], cube[5][8] = b6, b3, b0
    cube[2][0], cube[2][3], cube[2][6] = w2, w1, w0
    cube[4][2], cube[4][5], cube[4][8] = y8, y7, y6
    cube[6][0], cube[6][1], cube[6][2] = g2, g5, g8

    cube[1][0], cube[1][1], cube[1][2], cube[1][3], cube[1][4], cube[1][5], cube[1][6], cube[1][7], cube[1][8] = o2, o5, o8, o1, o4, o7, o0, o3, o6
    return cube

def moveCube(move, cube):
    if move == 'R' or move == 'r':
        R(cube)
    elif move == 'RI' or move == 'ri':
        RI(cube)
    elif move == 'L' or move == 'l':
        L(cube)
    elif move == 'LI' or move == 'li':
        LI(cube)
    elif move == 'U' or move == 'u':
        U(cube)
    elif move == 'UI' or move == 'ui':
        UI(cube)
    elif move == 'D' or move == 'd':
        D(cube)
    elif move == 'DI' or move == 'di':
        DI(cube)
    elif move == 'F' or move == 'f':
        F(cube)
    elif move == 'FI' or move == 'fi':
        FI(cube)
    elif move == 'B' or move == 'b':
        B(cube)
    elif move == 'BI' or move == 'bi':
        BI(cube)
    else:
        print("Not a valid move")

