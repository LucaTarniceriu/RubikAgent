def R(cube):
    cubeCopy = cube[0].copy()
    o2, o5, o8 = cubeCopy[1][2], cubeCopy[1][5], cubeCopy[1][8]
    y2, y5, y8 = cubeCopy[5][2], cubeCopy[5][5], cubeCopy[5][8]
    r0, r3, r6 = cubeCopy[3][0], cubeCopy[3][3], cubeCopy[3][6]
    w2, w5, w8 = cubeCopy[6][2], cubeCopy[6][5], cubeCopy[6][8]
    b0, b1, b2, b3, b4, b5, b6, b7, b8 = cubeCopy[2]

    cubeCopy[1][2], cubeCopy[1][5], cubeCopy[1][8] = w2, w5, w8
    cubeCopy[5][2], cubeCopy[5][5], cubeCopy[5][8] = o2, o5, o8
    cubeCopy[3][0], cubeCopy[3][3], cubeCopy[3][6] = y8, y5, y2
    cubeCopy[6][2], cubeCopy[6][5], cubeCopy[6][8] = r6, r3, r0

    cubeCopy[2][0], cubeCopy[2][1], cubeCopy[2][2], cubeCopy[2][3], cubeCopy[2][4], cubeCopy[2][5], cubeCopy[2][6], cubeCopy[2][7], cubeCopy[2][8] = b6, b3, b0, b7, b4, b1, b8, b5, b2
    return [cubeCopy, cube[1]]

def RI(cube):
    cubeCopy = cube[0].copy()
    o2, o5, o8 = cubeCopy[1][2], cubeCopy[1][5], cubeCopy[1][8]
    y2, y5, y8 = cubeCopy[5][2], cubeCopy[5][5], cubeCopy[5][8]
    r0, r3, r6 = cubeCopy[3][0], cubeCopy[3][3], cubeCopy[3][6]
    w2, w5, w8 = cubeCopy[6][2], cubeCopy[6][5], cubeCopy[6][8]
    b0, b1, b2, b3, b4, b5, b6, b7, b8 = cubeCopy[2]

    cubeCopy[1][2], cubeCopy[1][5], cubeCopy[1][8] = y2, y5, y8
    cubeCopy[5][2], cubeCopy[5][5], cubeCopy[5][8] = r6, r3, r0
    cubeCopy[3][0], cubeCopy[3][3], cubeCopy[3][6] = w8, w5, w2
    cubeCopy[6][2], cubeCopy[6][5], cubeCopy[6][8] = o2, o5, o8

    cubeCopy[2][0], cubeCopy[2][1], cubeCopy[2][2], cubeCopy[2][3], cubeCopy[2][4], cubeCopy[2][5], cubeCopy[2][6], cubeCopy[2][7], cubeCopy[2][8] = b2, b5, b8, b1, b4, b7, b0, b3, b6
    return [cubeCopy, cube[1]]

def L(cube):
    cubeCopy = cube[0].copy()
    y0, y3, y6 = cubeCopy[5][0], cubeCopy[5][3], cubeCopy[5][6]
    o0, o3, o6  = cubeCopy[1][0], cubeCopy[1][3], cubeCopy[1][6]
    w0, w3, w6 = cubeCopy[6][0], cubeCopy[6][3], cubeCopy[6][6]
    r2, r5, r8 = cubeCopy[3][2], cubeCopy[3][5], cubeCopy[3][8]

    g0, g1, g2, g3, g4, g5, g6, g7, g8 = cubeCopy[4]

    cubeCopy[5][0], cubeCopy[5][3], cubeCopy[5][6] = r8, r5, r2
    cubeCopy[1][0], cubeCopy[1][3], cubeCopy[1][6] = y0, y3, y6
    cubeCopy[6][0], cubeCopy[6][3], cubeCopy[6][6] = o0, o3, o6
    cubeCopy[3][2], cubeCopy[3][5], cubeCopy[3][8] = w6, w3, w0

    cubeCopy[4][0], cubeCopy[4][1], cubeCopy[4][2], cubeCopy[4][3], cubeCopy[4][4], cubeCopy[4][5], cubeCopy[4][6], cubeCopy[4][7], cubeCopy[4][8] = g6, g3, g0, g7, g4, g1, g8, g5, g2

    return [cubeCopy, cube[1]]

def LI(cube):
    cubeCopy = cube[0].copy()
    y0, y3, y6 = cubeCopy[5][0], cubeCopy[5][3], cubeCopy[5][6]
    o0, o3, o6 = cubeCopy[1][0], cubeCopy[1][3], cubeCopy[1][6]
    w0, w3, w6 = cubeCopy[6][0], cubeCopy[6][3], cubeCopy[6][6]
    r2, r5, r8 = cubeCopy[3][2], cubeCopy[3][5], cubeCopy[3][8]

    g0, g1, g2, g3, g4, g5, g6, g7, g8 = cubeCopy[4]

    cubeCopy[5][0], cubeCopy[5][3], cubeCopy[5][6] = o0, o3, o6
    cubeCopy[1][0], cubeCopy[1][3], cubeCopy[1][6] = w0, w3, w6
    cubeCopy[6][0], cubeCopy[6][3], cubeCopy[6][6] = r8, r5, r2
    cubeCopy[3][2], cubeCopy[3][5], cubeCopy[3][8] = y6, y3, y0

    cubeCopy[4][0], cubeCopy[4][1], cubeCopy[4][2], cubeCopy[4][3], cubeCopy[4][4], cubeCopy[4][5], cubeCopy[4][6], cubeCopy[4][7], cubeCopy[4][8] = g2, g5, g8, g1, g4, g7, g0, g3, g6

    return [cubeCopy, cube[1]]

def U(cube):
    cubeCopy = cube[0].copy()
    o0, o1, o2 = cubeCopy[1][0], cubeCopy[1][1], cubeCopy[1][2]
    g0, g1, g2 = cubeCopy[4][0], cubeCopy[4][1], cubeCopy[4][2]
    r0, r1, r2 = cubeCopy[3][0], cubeCopy[3][1], cubeCopy[3][2]
    b0, b1, b2 = cubeCopy[2][0], cubeCopy[2][1], cubeCopy[2][2]

    y0, y1, y2, y3, y4, y5, y6, y7, y8 = cubeCopy[5]

    cubeCopy[1][0], cubeCopy[1][1], cubeCopy[1][2] = b0, b1, b2
    cubeCopy[4][0], cubeCopy[4][1], cubeCopy[4][2] = o0, o1, o2
    cubeCopy[3][0], cubeCopy[3][1], cubeCopy[3][2] = g0, g1, g2
    cubeCopy[2][0], cubeCopy[2][1], cubeCopy[2][2] = r0, r1, r2

    cubeCopy[5][0], cubeCopy[5][1], cubeCopy[5][2], cubeCopy[5][3], cubeCopy[5][4], cubeCopy[5][5], cubeCopy[5][6], cubeCopy[5][7], cubeCopy[5][8] = y6, y3, y0, y7, y4, y1, y8, y5, y2
    return [cubeCopy, cube[1]]

def UI(cube):
    cubeCopy = cube[0].copy()
    o0, o1, o2 = cubeCopy[1][0], cubeCopy[1][1], cubeCopy[1][2]
    g0, g1, g2 = cubeCopy[4][0], cubeCopy[4][1], cubeCopy[4][2]
    r0, r1, r2 = cubeCopy[3][0], cubeCopy[3][1], cubeCopy[3][2]
    b0, b1, b2 = cubeCopy[2][0], cubeCopy[2][1], cubeCopy[2][2]

    cubeCopy[1][0], cubeCopy[1][1], cubeCopy[1][2] = g0, g1, g2
    cubeCopy[4][0], cubeCopy[4][1], cubeCopy[4][2] = r0, r1, r2
    cubeCopy[3][0], cubeCopy[3][1], cubeCopy[3][2] = b0, b1, b2
    cubeCopy[2][0], cubeCopy[2][1], cubeCopy[2][2] = o0, o1, o2

    y0, y1, y2, y3, y4, y5, y6, y7, y8 = cubeCopy[5]

    cubeCopy[5][0], cubeCopy[5][1], cubeCopy[5][2], cubeCopy[5][3], cubeCopy[5][4], cubeCopy[5][5], cubeCopy[5][6], cubeCopy[5][7], cubeCopy[5][8] = y2, y5, y8, y1, y4, y7, y0, y3, y6

    return [cubeCopy, cube[1]]

def D(cube):
    cubeCopy = cube[0].copy()
    o6, o7, o8 = cubeCopy[1][6], cubeCopy[1][7], cubeCopy[1][8]
    g6, g7, g8 = cubeCopy[4][6], cubeCopy[4][7], cubeCopy[4][8]
    r6, r7, r8 = cubeCopy[3][6], cubeCopy[3][7], cubeCopy[3][8]
    b6, b7, b8 = cubeCopy[2][6], cubeCopy[2][7], cubeCopy[2][8]

    w0, w1, w2, w3, w4, w5, w6, w7, w8 = cubeCopy[6]


    cubeCopy[1][6], cubeCopy[1][7], cubeCopy[1][8] = g6, g7, g8
    cubeCopy[4][6], cubeCopy[4][7], cubeCopy[4][8] = r6, r7, r8
    cubeCopy[3][6], cubeCopy[3][7], cubeCopy[3][8] = b6, b7, b8
    cubeCopy[2][6], cubeCopy[2][7], cubeCopy[2][8] = o6, o7, o8

    cubeCopy[6][0], cubeCopy[6][1], cubeCopy[6][2], cubeCopy[6][3], cubeCopy[6][4], cubeCopy[6][5], cubeCopy[6][6], cubeCopy[6][7], cubeCopy[6][8] = w6, w3, w0, w7, w4, w1, w8, w5, w2


    return [cubeCopy, cube[1]]

def DI(cube):
    cubeCopy = cube[0].copy()
    o6, o7, o8 = cubeCopy[1][6], cubeCopy[1][7], cubeCopy[1][8]
    g6, g7, g8 = cubeCopy[4][6], cubeCopy[4][7], cubeCopy[4][8]
    r6, r7, r8 = cubeCopy[3][6], cubeCopy[3][7], cubeCopy[3][8]
    b6, b7, b8 = cubeCopy[2][6], cubeCopy[2][7], cubeCopy[2][8]

    w0, w1, w2, w3, w4, w5, w6, w7, w8 = cubeCopy[6]

    cubeCopy[1][6], cubeCopy[1][7], cubeCopy[1][8] = b6, b7, b8
    cubeCopy[4][6], cubeCopy[4][7], cubeCopy[4][8] = o6, o7, o8
    cubeCopy[3][6], cubeCopy[3][7], cubeCopy[3][8] = g6, g7, g8
    cubeCopy[2][6], cubeCopy[2][7], cubeCopy[2][8] = r6, r7, r8


    cubeCopy[6][0], cubeCopy[6][1], cubeCopy[6][2], cubeCopy[6][3], cubeCopy[6][4], cubeCopy[6][5], cubeCopy[6][6], cubeCopy[6][7], cubeCopy[6][8] = w2, w5, w8, w1, w4, w7, w0, w3, w6
    return [cubeCopy, cube[1]]

def B(cube):
    cubeCopy = cube[0].copy()
    y0, y1, y2 = cubeCopy[5][0], cubeCopy[5][1], cubeCopy[5][2]
    b2, b5, b8 = cubeCopy[2][2], cubeCopy[2][5], cubeCopy[2][8]
    g0, g3, g6 = cubeCopy[4][0], cubeCopy[4][3], cubeCopy[4][6]
    w6, w7, w8 = cubeCopy[6][6], cubeCopy[6][7], cubeCopy[6][8]

    r0, r1, r2, r3, r4, r5, r6, r7, r8 = cubeCopy[3]

    cubeCopy[5][0], cubeCopy[5][1], cubeCopy[5][2] = b2, b5, b8
    cubeCopy[2][2], cubeCopy[2][5], cubeCopy[2][8] = w8, w7, w6
    cubeCopy[4][0], cubeCopy[4][3], cubeCopy[4][6] = y2, y1, y0
    cubeCopy[6][6], cubeCopy[6][7], cubeCopy[6][8] = g0, g3, g6

    cubeCopy[3][0], cubeCopy[3][1], cubeCopy[3][2], cubeCopy[3][3], cubeCopy[3][4], cubeCopy[3][5], cubeCopy[3][6], cubeCopy[3][7], cubeCopy[3][8] = r6, r3, r0, r7, r4, r1, r8, r5, r2

    return [cubeCopy, cube[1]]

def BI(cube):
    cubeCopy = cube[0].copy()
    y0, y1, y2 = cubeCopy[5][0], cubeCopy[5][1], cubeCopy[5][2]
    b2, b5, b8 = cubeCopy[2][2], cubeCopy[2][5], cubeCopy[2][8]
    g0, g3, g6 = cubeCopy[4][0], cubeCopy[4][3], cubeCopy[4][6]
    w6, w7, w8 = cubeCopy[6][6], cubeCopy[6][7], cubeCopy[6][8]

    r0, r1, r2, r3, r4, r5, r6, r7, r8 = cubeCopy[3]

    cubeCopy[5][0], cubeCopy[5][1], cubeCopy[5][2] = g6, g3, g0
    cubeCopy[2][2], cubeCopy[2][5], cubeCopy[2][8] = y0, y1, y2
    cubeCopy[4][0], cubeCopy[4][3], cubeCopy[4][6] = w6, w7, w8
    cubeCopy[6][6], cubeCopy[6][7], cubeCopy[6][8] = b8, b5, b2

    cubeCopy[3][0], cubeCopy[3][1], cubeCopy[3][2], cubeCopy[3][3], cubeCopy[3][4], cubeCopy[3][5], cubeCopy[3][6], cubeCopy[3][7], cubeCopy[3][8] = r2, r5, r8, r1, r4, r7, r0, r3, r6

    return [cubeCopy, cube[1]]

def F(cube):
    cubeCopy = cube[0].copy()
    y6, y7, y8 = cubeCopy[5][6], cubeCopy[5][7], cubeCopy[5][8]
    b0, b3, b6 = cubeCopy[2][0], cubeCopy[2][3], cubeCopy[2][6]
    g2, g5, g8 = cubeCopy[4][2], cubeCopy[4][5], cubeCopy[4][8]
    w0, w1, w2 = cubeCopy[6][0], cubeCopy[6][1], cubeCopy[6][2]

    o0, o1, o2, o3, o4, o5, o6, o7, o8 = cubeCopy[1]

    cubeCopy[5][6], cubeCopy[5][7], cubeCopy[5][8] = g2, g5, g8
    cubeCopy[2][0], cubeCopy[2][3], cubeCopy[2][6] = y6, y7, y8
    cubeCopy[4][2], cubeCopy[4][5], cubeCopy[4][8] = w0, w1, w2
    cubeCopy[6][0], cubeCopy[6][1], cubeCopy[6][2] = b0, b3, b6

    cubeCopy[1][0], cubeCopy[1][1], cubeCopy[1][2], cubeCopy[1][3], cubeCopy[1][4], cubeCopy[1][5], cubeCopy[1][6], cubeCopy[1][7], cubeCopy[1][8] = o6, o3, o0, o7, o4, o1, o8, o5, o2
    return [cubeCopy, cube[1]]

def FI(cube):
    cubeCopy = cube[0].copy()
    y6, y7, y8 = cubeCopy[5][6], cubeCopy[5][7], cubeCopy[5][8]
    b0, b3, b6 = cubeCopy[2][0], cubeCopy[2][3], cubeCopy[2][6]
    g2, g5, g8 = cubeCopy[4][2], cubeCopy[4][5], cubeCopy[4][8]
    w0, w1, w2 = cubeCopy[6][0], cubeCopy[6][1], cubeCopy[6][2]

    o0, o1, o2, o3, o4, o5, o6, o7, o8 = cubeCopy[1]

    cubeCopy[5][6], cubeCopy[5][7], cubeCopy[5][8] = b6, b3, b0
    cubeCopy[2][0], cubeCopy[2][3], cubeCopy[2][6] = w2, w1, w0
    cubeCopy[4][2], cubeCopy[4][5], cubeCopy[4][8] = y8, y7, y6
    cubeCopy[6][0], cubeCopy[6][1], cubeCopy[6][2] = g2, g5, g8

    cubeCopy[1][0], cubeCopy[1][1], cubeCopy[1][2], cubeCopy[1][3], cubeCopy[1][4], cubeCopy[1][5], cubeCopy[1][6], cubeCopy[1][7], cubeCopy[1][8] = o2, o5, o8, o1, o4, o7, o0, o3, o6
    return [cubeCopy, cube[1]]

def moveCube(move, cube):
    if move == 'R' or move == 'r':
        cubeCopy = R(cube)
        cubeCopy[1].append("r")
        return cubeCopy
    elif move == 'RI' or move == 'ri':
        cubeCopy = RI(cube)
        cubeCopy[1].append("ri")
        return cubeCopy
    elif move == 'L' or move == 'l':
        cubeCopy = L(cube)
        cubeCopy[1].append("l")
        return cubeCopy
    elif move == 'LI' or move == 'li':
        cubeCopy = LI(cube)
        cubeCopy[1].append("li")
        return cubeCopy
    elif move == 'U' or move == 'u':
        cubeCopy = U(cube)
        cubeCopy[1].append("u")
        return cubeCopy
    elif move == 'UI' or move == 'ui':
        cubeCopy = UI(cube)
        cubeCopy[1].append("ui")
        return cubeCopy
    elif move == 'D' or move == 'd':
        cubeCopy = D(cube)
        cubeCopy[1].append("d")
        return cubeCopy
    elif move == 'DI' or move == 'di':
        cubeCopy = DI(cube)
        cubeCopy[1].append("di")
        return cubeCopy
    elif move == 'F' or move == 'f':
        cubeCopy = F(cube)
        cubeCopy[1].append("f")
        return cubeCopy
    elif move == 'FI' or move == 'fi':
        cubeCopy = FI(cube)
        cubeCopy[1].append("fi")
        return cubeCopy
    elif move == 'B' or move == 'b':
        cubeCopy = B(cube)
        cubeCopy[1].append("b")
        return cubeCopy
    elif move == 'BI' or move == 'bi':
        cubeCopy = BI(cube)
        cubeCopy[1].append("bi")
        return cubeCopy
    else:
        print("Not a valid move (" + str(move) + ")")