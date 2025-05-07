def R(cube):
    w1, w3 = cube[1][1], cube[1][3]
    r1, r3 = cube[6][1], cube[6][3]
    y2, y0 = cube[3][2], cube[3][0]
    o1, o3 = cube[5][1], cube[5][3]

    cube[5][1], cube[5][3] = w1, w3
    cube[1][1], cube[1][3] = r1, r3
    cube[6][1], cube[6][3] = y2, y0
    cube[3][2], cube[3][0] = o1, o3

    m0, m1, m2, m3 = cube[2]
    cube[2][0], cube[2][1], cube[2][2], cube[2][3] = m2, m0, m3, m1
    return cube

def RI(cube):
    # Backup edges
    w1, w3 = cube[1][1], cube[1][3]
    r1, r3 = cube[6][1], cube[6][3]
    y2, y0 = cube[3][2], cube[3][0]
    o1, o3 = cube[5][1], cube[5][3]

    # Rotate edges
    cube[1][1], cube[1][3] = o1, o3
    cube[6][1], cube[6][3] = w1, w3
    cube[3][2], cube[3][0] = r1, r3
    cube[5][1], cube[5][3] = y2, y0

    # Rotate right face (Blue face, index 2)
    m0, m1, m2, m3 = cube[2]
    cube[2][0] = m1
    cube[2][1] = m3
    cube[2][2] = m0
    cube[2][3] = m2

    return cube

def L(cube):
    w0, w2 = cube[1][0], cube[1][2]
    r0, r2 = cube[6][0], cube[6][2]
    y3, y1 = cube[3][3], cube[3][1]
    o0, o2 = cube[5][0], cube[5][2]

    cube[1][0], cube[1][2] = o0, o2
    cube[6][0], cube[6][2] = w0, w2
    cube[3][3], cube[3][1] = r0, r2
    cube[5][0], cube[5][2] = y3, y1

    m0, m1, m2, m3 = cube[4]
    cube[4][0], cube[4][1], cube[4][2], cube[4][3] = m2, m0, m3, m1
    return cube

def LI(cube):
    w0, w2 = cube[1][0], cube[1][2]
    r0, r2 = cube[6][0], cube[6][2]
    y3, y1 = cube[3][3], cube[3][1]
    o0, o2 = cube[5][0], cube[5][2]

    cube[5][0], cube[5][2] = w0, w2
    cube[1][0], cube[1][2] = r0, r2
    cube[6][0], cube[6][2] = y3, y1
    cube[3][3], cube[3][1] = o0, o2

    m0, m1, m2, m3 = cube[4]
    cube[4][0], cube[4][1], cube[4][2], cube[4][3] = m1, m3, m0, m2
    return cube

def UI(cube):
    g0, g1 = cube[4][0], cube[4][1]
    w0, w1 = cube[1][0], cube[1][1]
    b0, b1 = cube[2][0], cube[2][1]
    y0, y1 = cube[3][0], cube[3][1]

    cube[1][0], cube[1][1] = g0, g1
    cube[2][0], cube[2][1] = w0, w1
    cube[3][0], cube[3][1] = b0, b1
    cube[4][0], cube[4][1] = y0, y1

    m0, m1, m2, m3 = cube[5]
    cube[5][0], cube[5][1], cube[5][2], cube[5][3] = m1, m3, m0, m2
    return cube

def U(cube):
    g0, g1 = cube[4][0], cube[4][1]
    w0, w1 = cube[1][0], cube[1][1]
    b0, b1 = cube[2][0], cube[2][1]
    y0, y1 = cube[3][0], cube[3][1]

    cube[4][0], cube[4][1] = w0, w1
    cube[1][0], cube[1][1] = b0, b1
    cube[2][0], cube[2][1] = y0, y1
    cube[3][0], cube[3][1] = g0, g1

    m0, m1, m2, m3 = cube[5]
    cube[5][0], cube[5][1], cube[5][2], cube[5][3] = m2, m0, m3, m1
    return cube

def D(cube):
    g2, g3 = cube[4][2], cube[4][3]
    w2, w3 = cube[1][2], cube[1][3]
    b2, b3 = cube[2][2], cube[2][3]
    y2, y3 = cube[3][2], cube[3][3]

    cube[1][2], cube[1][3] = g2, g3
    cube[2][2], cube[2][3] = w2, w3
    cube[3][2], cube[3][3] = b2, b3
    cube[4][2], cube[4][3] = y2, y3

    m0, m1, m2, m3 = cube[6]
    cube[6][0], cube[6][1], cube[6][2], cube[6][3] = m2, m0, m3, m1
    return cube

def DI(cube):
    g2, g3 = cube[4][2], cube[4][3]
    w2, w3 = cube[1][2], cube[1][3]
    b2, b3 = cube[2][2], cube[2][3]
    y2, y3 = cube[3][2], cube[3][3]

    cube[4][2], cube[4][3] = w2, w3
    cube[1][2], cube[1][3] = b2, b3
    cube[2][2], cube[2][3] = y2, y3
    cube[3][2], cube[3][3] = g2, g3

    m0, m1, m2, m3 = cube[6]
    cube[6][0], cube[6][1], cube[6][2], cube[6][3] = m1, m3, m0, m2
    return cube

def BI(cube):
    o0, o1 = cube[5][0], cube[5][1]
    r2, r3 = cube[6][2], cube[6][3]
    g0, g2 = cube[4][0], cube[4][2]
    b1, b3 = cube[2][1], cube[2][3]

    cube[5][0], cube[5][1] = g0, g2
    cube[4][0], cube[4][2] = r3, r2
    cube[6][2], cube[6][3] = b3, b1
    cube[2][1], cube[2][3] = o1, o0

    m0, m1, m2, m3 = cube[3]
    cube[3][0], cube[3][1], cube[3][2], cube[3][3] = m1, m3, m0, m2
    return cube

def B(cube):
    o0, o1 = cube[5][0], cube[5][1]
    r2, r3 = cube[6][2], cube[6][3]
    g0, g2 = cube[4][0], cube[4][2]
    b1, b3 = cube[2][1], cube[2][3]

    cube[2][1], cube[2][3] = r3, r2
    cube[6][2], cube[6][3] = g2, g0
    cube[4][0], cube[4][2] = o0, o1
    cube[5][0], cube[5][1] = b3, b1

    m0, m1, m2, m3 = cube[3]
    cube[3][0], cube[3][1], cube[3][2], cube[3][3] = m2, m0, m3, m1
    return cube

def F(cube):
    o2, o3 = cube[5][2], cube[5][3]
    r0, r1 = cube[6][0], cube[6][1]
    g3, g1 = cube[4][3], cube[4][1]
    b0, b2 = cube[2][0], cube[2][2]

    cube[5][2], cube[5][3] = g3, g1
    cube[4][1], cube[4][3] = r0, r1
    cube[6][0], cube[6][1] = b2, b0
    cube[2][0], cube[2][2] = o2, o3

    m0, m1, m2, m3 = cube[1]
    cube[1][0], cube[1][1], cube[1][2], cube[1][3] = m2, m0, m3, m1
    return cube

def FI(cube):
    o2, o3 = cube[5][2], cube[5][3]
    r0, r1 = cube[6][0], cube[6][1]
    g1, g3 = cube[4][1], cube[4][3]
    b0, b2 = cube[2][0], cube[2][2]

    cube[2][0], cube[2][2] = r1, r0
    cube[6][0], cube[6][1] = g1, g3
    cube[4][1], cube[4][3] = o3, o2
    cube[5][2], cube[5][3] = b0, b2

    m0, m1, m2, m3 = cube[1]
    cube[1][0], cube[1][1], cube[1][2], cube[1][3] = m1, m3, m0, m2
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

