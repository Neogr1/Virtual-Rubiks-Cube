# rotation notation: https://jperm.net/3x3/moves

class Cube:
    DEGREE = ['', "'", '2']
    SIDE = ['U', 'F', 'R', 'D', 'B', 'L']
    # EDGE = ['UF', 'UR', 'UD', 'UL', 'FL', 'FR', 'DR', 'DL', 'DF', 'DR', 'DB', 'DL']
    # CORNER = ['UFL', 'UFR', 'UDF', 'UDL', 'DFL', 'DFR', 'DBR', 'DBL']
    COLOR = ['w', 'g', 'r', 'y', 'b', 'o'] # U, F, R, D, B, L


    center = [0, 1, 2, 3, 4, 5] # U, F, R, D, B, L
    edge   = [[0, True], [1, True], [2, True], [3, True], [4, True], [5, True], [6, True], [7, True], [8, True], [9, True], [10, True], [11, True]] # uf, ur, ud, ul, fl, fr, ..., dl
    corner = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0]] # ufl, ufr, udr, udl, dfl, dfr, dbr, dbl


    def __init__(self, scramble=[], shuffle=False):
        if shuffle:
            scramble = self.make_scramble()
        self.shuffle(scramble=scramble)
        # print(self)
    
    def reset(self):
        self.center = [0, 1, 2, 3, 4, 5]
        self.edge   = [[0, True], [1, True], [2, True], [3, True], [4, True], [5, True], [6, True], [7, True], [8, True], [9, True], [10, True], [11, True]]
        self.corner = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0]]

    def is_solved(self):
        # center가 회전된 경우 고려 필요
        # 대문자 move만 하면 괜찮음
        return self.edge == [[e, True] for e in range(12)] and self.corner == [[c, 0] for c in range(8)]
    




    def make_scramble(self):
        import random

        scramble_length = random.randint(19, 21)

        scramble = []
        
        # generate first two moves
        sides = random.sample([0, 1, 2, 3, 4, 5], 2)
        scramble.append((sides[0], random.randint(0, 2)))
        scramble.append((sides[1], random.randint(0, 2)))

        # generate other moves
        for i in range(scramble_length - 2):
            side = random.randint(0, 5)
            degree = random.randint(0, 2)

            while side == scramble[-1][0] or side % 3 == scramble[-1][0] % 3 == scramble[-2][0] % 3:
                side = random.randint(0, 5)

            scramble.append((side, degree))

        return scramble


    # default: shuffle 19~21 moves
    # not to shuffle: scramble=[]
    def shuffle(self, scramble=None):
        if scramble == None:
            scramble = self.make_scramble()
        
        MOVE_FUNC = [self.move_U, self.move_U_, self.move_U2, 
                     self.move_F, self.move_F_, self.move_F2, 
                     self.move_R, self.move_R_, self.move_R2, 
                     self.move_D, self.move_D_, self.move_D2, 
                     self.move_B, self.move_B_, self.move_B2, 
                     self.move_L, self.move_L_, self.move_L2, 
        ]

        scramble_in_text = ""
        for side, degree in scramble:
            MOVE_FUNC[side*3 + degree]()
            scramble_in_text += self.SIDE[side] + self.DEGREE[degree] + ' '

        print("Scramble:", scramble_in_text)
        print()



    # 0 3 2 1
    # 1 0 3 2
    def move_U(self):
        self.edge[0], self.edge[3], self.edge[2], self.edge[1] = self.edge[1], self.edge[0], self.edge[3], self.edge[2]
        self.corner[1], self.corner[0], self.corner[3], self.corner[2] = self.corner[2], self.corner[1], self.corner[0], self.corner[3]

        self.corner[1][1], self.corner[0][1], self.corner[3][1], self.corner[2][1] = [0,2,1][self.corner[1][1]], [0,2,1][self.corner[0][1]], [0,2,1][self.corner[3][1]], [0,2,1][self.corner[2][1]]
    def move_U_(self):
        self.edge[0], self.edge[3], self.edge[2], self.edge[1] = self.edge[3], self.edge[2], self.edge[1], self.edge[0]
        self.corner[1], self.corner[0], self.corner[3], self.corner[2] = self.corner[0], self.corner[3], self.corner[2], self.corner[1]

        self.corner[1][1], self.corner[0][1], self.corner[3][1], self.corner[2][1] = [0,2,1][self.corner[1][1]], [0,2,1][self.corner[0][1]], [0,2,1][self.corner[3][1]], [0,2,1][self.corner[2][1]]
    def move_U2(self):
        self.edge[0], self.edge[3], self.edge[2], self.edge[1] = self.edge[2], self.edge[1], self.edge[0], self.edge[3]
        self.corner[1], self.corner[0], self.corner[3], self.corner[2] = self.corner[3], self.corner[2], self.corner[1], self.corner[0]
    def move_u(self):
        self.move_D()
        self.rotate_y()
    def move_u_(self):
        self.move_D_()
        self.rotate_y_()
    def move_u2(self):
        self.move_D2()
        self.rotate_y2()
    
    # 0 5 8 4
    # 0 1 5 4
    def move_F(self):
        self.edge[0], self.edge[5], self.edge[8], self.edge[4] = self.edge[4], self.edge[0], self.edge[5], self.edge[8]
        self.corner[0], self.corner[1], self.corner[5], self.corner[4] = self.corner[4], self.corner[0], self.corner[1], self.corner[5]
        
        self.edge[0][1], self.edge[5][1], self.edge[8][1], self.edge[4][1] = not self.edge[0][1], not self.edge[5][1], not self.edge[8][1], not self.edge[4][1]
        self.corner[0][1], self.corner[1][1], self.corner[5][1], self.corner[4][1] = [2,1,0][self.corner[0][1]], [2,1,0][self.corner[1][1]], [2,1,0][self.corner[5][1]], [2,1,0][self.corner[4][1]]
    def move_F_(self):
        self.edge[0], self.edge[5], self.edge[8], self.edge[4] = self.edge[5], self.edge[8], self.edge[4], self.edge[0]
        self.corner[0], self.corner[1], self.corner[5], self.corner[4] = self.corner[1], self.corner[5], self.corner[4], self.corner[0]

        self.edge[0][1], self.edge[5][1], self.edge[8][1], self.edge[4][1] = not self.edge[0][1], not self.edge[5][1], not self.edge[8][1], not self.edge[4][1]
        self.corner[0][1], self.corner[1][1], self.corner[5][1], self.corner[4][1] = [2,1,0][self.corner[0][1]], [2,1,0][self.corner[1][1]], [2,1,0][self.corner[5][1]], [2,1,0][self.corner[4][1]]
    def move_F2(self):
        self.edge[0], self.edge[5], self.edge[8], self.edge[4] = self.edge[8], self.edge[4], self.edge[0], self.edge[5]
        self.corner[0], self.corner[1], self.corner[5], self.corner[4] = self.corner[5], self.corner[4], self.corner[0], self.corner[1]
    def move_f(self):
        self.move_B()
        self.rotate_z()
    def move_f_(self):
        self.move_B_()
        self.rotate_z_()
    def move_f2(self):
        self.move_B2()
        self.rotate_z2()


    # 1 6 9 5
    # 1 2 6 5
    def move_R(self):
        self.edge[1], self.edge[6], self.edge[9], self.edge[5] = self.edge[5], self.edge[1], self.edge[6], self.edge[9]
        self.corner[1], self.corner[2], self.corner[6], self.corner[5] = self.corner[5], self.corner[1], self.corner[2], self.corner[6]

        self.corner[1][1], self.corner[2][1], self.corner[6][1], self.corner[5][1] = [1,0,2][self.corner[1][1]], [1,0,2][self.corner[2][1]], [1,0,2][self.corner[6][1]], [1,0,2][self.corner[5][1]]
    def move_R_(self):
        self.edge[1], self.edge[6], self.edge[9], self.edge[5] = self.edge[6], self.edge[9], self.edge[5], self.edge[1]
        self.corner[1], self.corner[2], self.corner[6], self.corner[5] = self.corner[2], self.corner[6], self.corner[5], self.corner[1]

        self.corner[1][1], self.corner[2][1], self.corner[6][1], self.corner[5][1] = [1,0,2][self.corner[1][1]], [1,0,2][self.corner[2][1]], [1,0,2][self.corner[6][1]], [1,0,2][self.corner[5][1]]
    def move_R2(self):
        self.edge[1], self.edge[6], self.edge[9], self.edge[5] = self.edge[9], self.edge[5], self.edge[1], self.edge[6]
        self.corner[1], self.corner[2], self.corner[6], self.corner[5] = self.corner[6], self.corner[5], self.corner[1], self.corner[2]
    def move_r(self):
        self.move_L()
        self.rotate_x()
    def move_r_(self):
        self.move_L_()
        self.rotate_x_()
    def move_r2(self):
        self.move_L2()
        self.rotate_x2()

    # 8 9 10 11
    # 4 5 6 7
    def move_D(self):
        self.edge[8], self.edge[9], self.edge[10], self.edge[11] = self.edge[11], self.edge[8], self.edge[9], self.edge[10]
        self.corner[4], self.corner[5], self.corner[6], self.corner[7] = self.corner[7], self.corner[4], self.corner[5], self.corner[6]

        self.corner[4][1], self.corner[5][1], self.corner[6][1], self.corner[7][1] = [0,2,1][self.corner[4][1]], [0,2,1][self.corner[5][1]], [0,2,1][self.corner[6][1]], [0,2,1][self.corner[7][1]]
    def move_D_(self):
        self.edge[8], self.edge[9], self.edge[10], self.edge[11] = self.edge[9], self.edge[10], self.edge[11], self.edge[8]
        self.corner[4], self.corner[5], self.corner[6], self.corner[7] = self.corner[5], self.corner[6], self.corner[7], self.corner[4]

        self.corner[4][1], self.corner[5][1], self.corner[6][1], self.corner[7][1] = [0,2,1][self.corner[4][1]], [0,2,1][self.corner[5][1]], [0,2,1][self.corner[6][1]], [0,2,1][self.corner[7][1]]
    def move_D2(self):
        self.edge[8], self.edge[9], self.edge[10], self.edge[11] = self.edge[10], self.edge[11], self.edge[8], self.edge[9]
        self.corner[4], self.corner[5], self.corner[6], self.corner[7] = self.corner[6], self.corner[7], self.corner[4], self.corner[5]
    def move_d(self):
        self.move_U()
        self.rotate_y_()
    def move_d_(self):
        self.move_U_()
        self.rotate_y()
    def move_d2(self):
        self.move_U2()
        self.rotate_y2()

    # 2 7 10 6
    # 2 3 7 6
    def move_B(self):
        self.edge[2], self.edge[7], self.edge[10], self.edge[6] = self.edge[6], self.edge[2], self.edge[7], self.edge[10]
        self.corner[2], self.corner[3], self.corner[7], self.corner[6] = self.corner[6], self.corner[2], self.corner[3], self.corner[7]

        self.edge[2][1], self.edge[7][1], self.edge[10][1], self.edge[6][1] = not self.edge[2][1], not self.edge[7][1], not self.edge[10][1], not self.edge[6][1]
        self.corner[2][1], self.corner[3][1], self.corner[7][1], self.corner[6][1] = [2,1,0][self.corner[2][1]], [2,1,0][self.corner[3][1]], [2,1,0][self.corner[7][1]], [2,1,0][self.corner[6][1]]
    def move_B_(self):
        self.edge[2], self.edge[7], self.edge[10], self.edge[6] = self.edge[7], self.edge[10], self.edge[6], self.edge[2]
        self.corner[2], self.corner[3], self.corner[7], self.corner[6] = self.corner[3], self.corner[7], self.corner[6], self.corner[2]

        self.edge[2][1], self.edge[7][1], self.edge[10][1], self.edge[6][1] = not self.edge[2][1], not self.edge[7][1], not self.edge[10][1], not self.edge[6][1]
        self.corner[2][1], self.corner[3][1], self.corner[7][1], self.corner[6][1] = [2,1,0][self.corner[2][1]], [2,1,0][self.corner[3][1]], [2,1,0][self.corner[7][1]], [2,1,0][self.corner[6][1]]
    def move_B2(self):
        self.edge[2], self.edge[7], self.edge[10], self.edge[6] = self.edge[10], self.edge[6], self.edge[2], self.edge[7]
        self.corner[2], self.corner[3], self.corner[7], self.corner[6] = self.corner[7], self.corner[6], self.corner[2], self.corner[3]
    def move_b(self):
        self.move_F()
        self.rotate_z_()
    def move_b_(self):
        self.move_F_()
        self.rotate_z()
    def move_b2(self):
        self.move_F2()
        self.rotate_z2()

    # 3 4 11 7
    # 3 0 4 7
    def move_L(self):
        self.edge[3], self.edge[4], self.edge[11], self.edge[7] = self.edge[7], self.edge[3], self.edge[4], self.edge[11]
        self.corner[3], self.corner[0], self.corner[4], self.corner[7] = self.corner[7], self.corner[3], self.corner[0], self.corner[4]

        self.corner[3][1], self.corner[0][1], self.corner[4][1], self.corner[7][1] = [1,0,2][self.corner[3][1]], [1,0,2][self.corner[0][1]], [1,0,2][self.corner[4][1]], [1,0,2][self.corner[7][1]]
    def move_L_(self):
        self.edge[3], self.edge[4], self.edge[11], self.edge[7] = self.edge[4], self.edge[11], self.edge[7], self.edge[3]
        self.corner[3], self.corner[0], self.corner[4], self.corner[7] = self.corner[0], self.corner[4], self.corner[7], self.corner[3]

        self.corner[3][1], self.corner[0][1], self.corner[4][1], self.corner[7][1] = [1,0,2][self.corner[3][1]], [1,0,2][self.corner[0][1]], [1,0,2][self.corner[4][1]], [1,0,2][self.corner[7][1]]
    def move_L2(self):
        self.edge[3], self.edge[4], self.edge[11], self.edge[7] = self.edge[11], self.edge[7], self.edge[3], self.edge[4]
        self.corner[3], self.corner[0], self.corner[4], self.corner[7] = self.corner[4], self.corner[7], self.corner[3], self.corner[0]
    def move_l(self):
        self.move_R()
        self.rotate_x_()
    def move_l_(self):
        self.move_R_()
        self.rotate_x()
    def move_l2(self):
        self.move_R2()
        self.rotate_x2()


    # L
    def move_M(self):
        self.center[0], self.center[4], self.center[3], self.center[1] = self.center[4], self.center[3], self.center[1], self.center[0]
        self.edge[0], self.edge[2], self.edge[10], self.edge[8] = self.edge[2], self.edge[10], self.edge[8], self.edge[0]
        self.edge[0][1], self.edge[2][1], self.edge[10][1], self.edge[8][1] = not self.edge[0][1], not self.edge[2][1], not self.edge[10][1], not self.edge[8][1]
    def move_M_(self):
        self.center[0], self.center[4], self.center[3], self.center[1] = self.center[1], self.center[0], self.center[4], self.center[3]
        self.edge[0], self.edge[2], self.edge[10], self.edge[8] = self.edge[8], self.edge[0], self.edge[2], self.edge[10]
        self.edge[0][1], self.edge[2][1], self.edge[10][1], self.edge[8][1] = not self.edge[0][1], not self.edge[2][1], not self.edge[10][1], not self.edge[8][1]

    # F
    def move_E(self):
        self.center[0], self.center[2], self.center[3], self.center[5] = self.center[5], self.center[0], self.center[2], self.center[3]
        self.edge[3], self.edge[1], self.edge[9], self.edge[11] =  self.edge[11], self.edge[3], self.edge[1], self.edge[9]
        
        self.edge[3][1], self.edge[1][1], self.edge[9][1], self.edge[11][1] = not self.edge[3][1], not self.edge[1][1], not self.edge[9][1], not self.edge[11][1]
    def move_E_(self):
        self.center[0], self.center[2], self.center[3], self.center[5] = self.center[2], self.center[3], self.center[5], self.center[0]
        self.edge[3], self.edge[1], self.edge[9], self.edge[11] =  self.edge[1], self.edge[9], self.edge[11], self.edge[3]
        
        self.edge[3][1], self.edge[1][1], self.edge[9][1], self.edge[11][1] = not self.edge[3][1], not self.edge[1][1], not self.edge[9][1], not self.edge[11][1]

    # D
    def move_S(self):
        self.center[1], self.center[2], self.center[4], self.center[5] = self.center[5], self.center[1], self.center[2], self.center[4]
        self.edge[4], self.edge[7], self.edge[6], self.edge[5] = self.edge[7], self.edge[6], self.edge[5], self.edge[4]

        self.edge[4][1], self.edge[7][1], self.edge[6][1], self.edge[5][1] = not self.edge[4][1], not self.edge[7][1], not self.edge[6][1], not self.edge[5][1]
    def move_S_(self):
        self.center[1], self.center[2], self.center[4], self.center[5] = self.center[2], self.center[4], self.center[5], self.center[1]
        self.edge[4], self.edge[7], self.edge[6], self.edge[5] = self.edge[5], self.edge[4], self.edge[7], self.edge[6]

        self.edge[4][1], self.edge[7][1], self.edge[6][1], self.edge[5][1] = not self.edge[4][1], not self.edge[7][1], not self.edge[6][1], not self.edge[5][1]

    
    # R
    def rotate_x(self):
        self.center[0], self.center[4], self.center[3], self.center[1] = self.center[1], self.center[0], self.center[4], self.center[3]
        self.edge[1], self.edge[6], self.edge[9], self.edge[5] = self.edge[5], self.edge[1], self.edge[6], self.edge[9]
        self.edge[0], self.edge[2], self.edge[10], self.edge[8] = self.edge[8], self.edge[0], self.edge[2], self.edge[10]
        self.edge[3], self.edge[4], self.edge[11], self.edge[7] = self.edge[4], self.edge[11], self.edge[7], self.edge[3]
        self.corner[1], self.corner[2], self.corner[6], self.corner[5] = self.corner[5], self.corner[1], self.corner[2], self.corner[6]
        self.corner[3], self.corner[0], self.corner[4], self.corner[7] = self.corner[0], self.corner[4], self.corner[7], self.corner[3]

        self.edge[0][1], self.edge[2][1], self.edge[10][1], self.edge[8][1] = not self.edge[0][1], not self.edge[2][1], not self.edge[10][1], not self.edge[8][1]
        self.corner[1][1], self.corner[2][1], self.corner[6][1], self.corner[5][1] = [1,0,2][self.corner[1][1]], [1,0,2][self.corner[2][1]], [1,0,2][self.corner[6][1]], [1,0,2][self.corner[5][1]]
        self.corner[3][1], self.corner[0][1], self.corner[4][1], self.corner[7][1] = [1,0,2][self.corner[3][1]], [1,0,2][self.corner[0][1]], [1,0,2][self.corner[4][1]], [1,0,2][self.corner[7][1]]
    def rotate_x_(self):
        self.center[0], self.center[4], self.center[3], self.center[1] = self.center[4], self.center[3], self.center[1], self.center[0]
        self.edge[1], self.edge[6], self.edge[9], self.edge[5] = self.edge[6], self.edge[9], self.edge[5], self.edge[1]
        self.edge[0], self.edge[2], self.edge[10], self.edge[8] = self.edge[2], self.edge[10], self.edge[8], self.edge[0]
        self.edge[3], self.edge[4], self.edge[11], self.edge[7] = self.edge[7], self.edge[3], self.edge[4], self.edge[11]
        self.corner[1], self.corner[2], self.corner[6], self.corner[5] = self.corner[2], self.corner[6], self.corner[5], self.corner[1]
        self.corner[3], self.corner[0], self.corner[4], self.corner[7] = self.corner[7], self.corner[3], self.corner[0], self.corner[4]

        self.edge[0][1], self.edge[2][1], self.edge[10][1], self.edge[8][1] = not self.edge[0][1], not self.edge[2][1], not self.edge[10][1], not self.edge[8][1]
        self.corner[1][1], self.corner[2][1], self.corner[6][1], self.corner[5][1] = [1,0,2][self.corner[1][1]], [1,0,2][self.corner[2][1]], [1,0,2][self.corner[6][1]], [1,0,2][self.corner[5][1]]
        self.corner[3][1], self.corner[0][1], self.corner[4][1], self.corner[7][1] = [1,0,2][self.corner[3][1]], [1,0,2][self.corner[0][1]], [1,0,2][self.corner[4][1]], [1,0,2][self.corner[7][1]]
    def rotate_x2(self):
        pass

    # U
    def rotate_y(self):
        self.center[1], self.center[2], self.center[4], self.center[5] = self.center[2], self.center[4], self.center[5], self.center[1]
        self.edge[0], self.edge[3], self.edge[2], self.edge[1] = self.edge[1], self.edge[0], self.edge[3], self.edge[2]
        self.edge[4], self.edge[7], self.edge[6], self.edge[5] = self.edge[5], self.edge[4], self.edge[7], self.edge[6]
        self.edge[8], self.edge[9], self.edge[10], self.edge[11] = self.edge[9], self.edge[10], self.edge[11], self.edge[8]
        self.corner[1], self.corner[0], self.corner[3], self.corner[2] = self.corner[2], self.corner[1], self.corner[0], self.corner[3]
        self.corner[4], self.corner[5], self.corner[6], self.corner[7] = self.corner[5], self.corner[6], self.corner[7], self.corner[4]

        self.edge[4][1], self.edge[7][1], self.edge[6][1], self.edge[5][1] = not self.edge[4][1], not self.edge[7][1], not self.edge[6][1], not self.edge[5][1]
        self.corner[1][1], self.corner[0][1], self.corner[3][1], self.corner[2][1] = [0,2,1][self.corner[1][1]], [0,2,1][self.corner[0][1]], [0,2,1][self.corner[3][1]], [0,2,1][self.corner[2][1]]
        self.corner[4][1], self.corner[5][1], self.corner[6][1], self.corner[7][1] = [0,2,1][self.corner[4][1]], [0,2,1][self.corner[5][1]], [0,2,1][self.corner[6][1]], [0,2,1][self.corner[7][1]]
        
    def rotate_y_(self):
        self.center[1], self.center[2], self.center[4], self.center[5] = self.center[5], self.center[1], self.center[2], self.center[4]
        self.edge[0], self.edge[3], self.edge[2], self.edge[1] = self.edge[3], self.edge[2], self.edge[1], self.edge[0]
        self.edge[4], self.edge[7], self.edge[6], self.edge[5] = self.edge[7], self.edge[6], self.edge[5], self.edge[4]
        self.edge[8], self.edge[9], self.edge[10], self.edge[11] = self.edge[11], self.edge[8], self.edge[9], self.edge[10]
        self.corner[1], self.corner[0], self.corner[3], self.corner[2] = self.corner[0], self.corner[3], self.corner[2], self.corner[1]
        self.corner[4], self.corner[5], self.corner[6], self.corner[7] = self.corner[7], self.corner[4], self.corner[5], self.corner[6]

        self.edge[4][1], self.edge[7][1], self.edge[6][1], self.edge[5][1] = not self.edge[4][1], not self.edge[7][1], not self.edge[6][1], not self.edge[5][1]
        self.corner[1][1], self.corner[0][1], self.corner[3][1], self.corner[2][1] = [0,2,1][self.corner[1][1]], [0,2,1][self.corner[0][1]], [0,2,1][self.corner[3][1]], [0,2,1][self.corner[2][1]]
        self.corner[4][1], self.corner[5][1], self.corner[6][1], self.corner[7][1] = [0,2,1][self.corner[4][1]], [0,2,1][self.corner[5][1]], [0,2,1][self.corner[6][1]], [0,2,1][self.corner[7][1]]
    def rotate_y2(self):
        pass
    
    # F
    def rotate_z(self):
        self.center[0], self.center[2], self.center[3], self.center[5] = self.center[5], self.center[0], self.center[2], self.center[3]
        self.edge[0], self.edge[5], self.edge[8], self.edge[4] = self.edge[4], self.edge[0], self.edge[5], self.edge[8]
        self.edge[3], self.edge[1], self.edge[9], self.edge[11] =  self.edge[11], self.edge[3], self.edge[1], self.edge[9]
        self.edge[2], self.edge[7], self.edge[10], self.edge[6] = self.edge[7], self.edge[10], self.edge[6], self.edge[2]
        self.corner[2], self.corner[3], self.corner[7], self.corner[6] = self.corner[3], self.corner[7], self.corner[6], self.corner[2]
        self.corner[0], self.corner[1], self.corner[5], self.corner[4] = self.corner[4], self.corner[0], self.corner[1], self.corner[5]
        
        self.edge[0][1], self.edge[5][1], self.edge[8][1], self.edge[4][1] = not self.edge[0][1], not self.edge[5][1], not self.edge[8][1], not self.edge[4][1]
        self.edge[3][1], self.edge[1][1], self.edge[9][1], self.edge[11][1] = not self.edge[3][1], not self.edge[1][1], not self.edge[9][1], not self.edge[11][1]
        self.edge[2][1], self.edge[7][1], self.edge[10][1], self.edge[6][1] = not self.edge[2][1], not self.edge[7][1], not self.edge[10][1], not self.edge[6][1]
        self.corner[0][1], self.corner[1][1], self.corner[5][1], self.corner[4][1] = [2,1,0][self.corner[0][1]], [2,1,0][self.corner[1][1]], [2,1,0][self.corner[5][1]], [2,1,0][self.corner[4][1]]
        self.corner[2][1], self.corner[3][1], self.corner[7][1], self.corner[6][1] = [2,1,0][self.corner[2][1]], [2,1,0][self.corner[3][1]], [2,1,0][self.corner[7][1]], [2,1,0][self.corner[6][1]]
    def rotate_z_(self):
        self.center[0], self.center[2], self.center[3], self.center[5] = self.center[2], self.center[3], self.center[5], self.center[0]
        self.edge[0], self.edge[5], self.edge[8], self.edge[4] = self.edge[5], self.edge[8], self.edge[4], self.edge[0]
        self.edge[3], self.edge[1], self.edge[9], self.edge[11] =  self.edge[1], self.edge[9], self.edge[11], self.edge[3]
        self.edge[2], self.edge[7], self.edge[10], self.edge[6] = self.edge[6], self.edge[2], self.edge[7], self.edge[10]
        self.corner[2], self.corner[3], self.corner[7], self.corner[6] = self.corner[6], self.corner[2], self.corner[3], self.corner[7]
        self.corner[0], self.corner[1], self.corner[5], self.corner[4] = self.corner[1], self.corner[5], self.corner[4], self.corner[0]
        
        self.edge[0][1], self.edge[5][1], self.edge[8][1], self.edge[4][1] = not self.edge[0][1], not self.edge[5][1], not self.edge[8][1], not self.edge[4][1]
        self.edge[3][1], self.edge[1][1], self.edge[9][1], self.edge[11][1] = not self.edge[3][1], not self.edge[1][1], not self.edge[9][1], not self.edge[11][1]
        self.edge[2][1], self.edge[7][1], self.edge[10][1], self.edge[6][1] = not self.edge[2][1], not self.edge[7][1], not self.edge[10][1], not self.edge[6][1]
        self.corner[0][1], self.corner[1][1], self.corner[5][1], self.corner[4][1] = [2,1,0][self.corner[0][1]], [2,1,0][self.corner[1][1]], [2,1,0][self.corner[5][1]], [2,1,0][self.corner[4][1]]
        self.corner[2][1], self.corner[3][1], self.corner[7][1], self.corner[6][1] = [2,1,0][self.corner[2][1]], [2,1,0][self.corner[3][1]], [2,1,0][self.corner[7][1]], [2,1,0][self.corner[6][1]]
    def rotate_z2(self):
        pass



    def get_face_color(self):
        u_face = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
        f_face = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
        r_face = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
        d_face = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
        b_face = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
        l_face = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]

        self._fill_center(u_face, f_face, r_face, d_face, b_face, l_face)
        self._fill_edge(u_face, f_face, r_face, d_face, b_face, l_face)
        self._fill_corner(u_face, f_face, r_face, d_face, b_face, l_face)

        return u_face, f_face, r_face, d_face, b_face, l_face

    def _fill_center(self, u_face, f_face, r_face, d_face, b_face, l_face):
        u_face[1][1],f_face[1][1],r_face[1][1] = self.center[0],self.center[1],self.center[2]
        d_face[1][1],b_face[1][1],l_face[1][1] = self.center[3],self.center[4],self.center[5]

    def _fill_edge(self, u_face, f_face, r_face, d_face, b_face, l_face):
        E = EDGE_COLOR = [(0,1),(0,2),(0,4),(0,5),
                          (1,5),(1,2),(4,2),(4,5),
                          (3,1),(3,2),(3,4),(3,5)]

        u_face[2][1],f_face[0][1] = E[self.edge[0][0]][::1 if self.edge[0][1] else -1]
        u_face[1][2],r_face[0][1] = E[self.edge[1][0]][::1 if self.edge[1][1] else -1]
        u_face[0][1],b_face[0][1] = E[self.edge[2][0]][::1 if self.edge[2][1] else -1]
        u_face[1][0],l_face[0][1] = E[self.edge[3][0]][::1 if self.edge[3][1] else -1]
        f_face[1][0],l_face[1][2] = E[self.edge[4][0]][::1 if self.edge[4][1] else -1]
        f_face[1][2],r_face[1][0] = E[self.edge[5][0]][::1 if self.edge[5][1] else -1]
        b_face[1][0],r_face[1][2] = E[self.edge[6][0]][::1 if self.edge[6][1] else -1]
        b_face[1][2],l_face[1][0] = E[self.edge[7][0]][::1 if self.edge[7][1] else -1]
        d_face[0][1],f_face[2][1] = E[self.edge[8][0]][::1 if self.edge[8][1] else -1]
        d_face[1][2],r_face[2][1] = E[self.edge[9][0]][::1 if self.edge[9][1] else -1]
        d_face[2][1],b_face[2][1] = E[self.edge[10][0]][::1 if self.edge[10][1] else -1]
        d_face[1][0],l_face[2][1] = E[self.edge[11][0]][::1 if self.edge[11][1] else -1]

    def _fill_corner(self, u_face, f_face, r_face, d_face, b_face, l_face):
        C = CORNER_COLOR = [(0,1,5,0,1),(0,1,2,0,1),(0,4,2,0,4),(0,4,5,0,4),
                            (3,1,5,3,1),(3,1,2,3,1),(3,4,2,3,4),(3,4,5,3,4)]

        start, reverse = [[0,2,1],[1,2,0]][self.corner[0][0] in [1,3,4,6]][self.corner[0][1]], self.corner[0][0] in [1,3,4,6]
        u_face[2][0],f_face[0][0],l_face[0][2] = C[self.corner[0][0]][start:start+3][::[1,-1][reverse]]
        start, reverse = [[0,2,1],[1,2,0]][self.corner[1][0] in [0,2,5,7]][self.corner[1][1]], self.corner[1][0] in [0,2,5,7]
        u_face[2][2],f_face[0][2],r_face[0][0] = C[self.corner[1][0]][start:start+3][::[1,-1][reverse]]
        start, reverse = [[0,2,1],[1,2,0]][self.corner[2][0] in [1,3,4,6]][self.corner[2][1]], self.corner[2][0] in [1,3,4,6]
        u_face[0][2],b_face[0][0],r_face[0][2] = C[self.corner[2][0]][start:start+3][::[1,-1][reverse]]
        start, reverse = [[0,2,1],[1,2,0]][self.corner[3][0] in [0,2,5,7]][self.corner[3][1]], self.corner[3][0] in [0,2,5,7]
        u_face[0][0],b_face[0][2],l_face[0][0] = C[self.corner[3][0]][start:start+3][::[1,-1][reverse]]
        start, reverse = [[0,2,1],[1,2,0]][self.corner[4][0] in [0,2,5,7]][self.corner[4][1]], self.corner[4][0] in [0,2,5,7]
        d_face[0][0],f_face[2][0],l_face[2][2] = C[self.corner[4][0]][start:start+3][::[1,-1][reverse]]
        start, reverse = [[0,2,1],[1,2,0]][self.corner[5][0] in [1,3,4,6]][self.corner[5][1]], self.corner[5][0] in [1,3,4,6]
        d_face[0][2],f_face[2][2],r_face[2][0] = C[self.corner[5][0]][start:start+3][::[1,-1][reverse]]
        start, reverse = [[0,2,1],[1,2,0]][self.corner[6][0] in [0,2,5,7]][self.corner[6][1]], self.corner[6][0] in [0,2,5,7]
        d_face[2][2],b_face[2][0],r_face[2][2] = C[self.corner[6][0]][start:start+3][::[1,-1][reverse]]
        start, reverse = [[0,2,1],[1,2,0]][self.corner[7][0] in [1,3,4,6]][self.corner[7][1]], self.corner[7][0] in [1,3,4,6]
        d_face[2][0],b_face[2][2],l_face[2][0] = C[self.corner[7][0]][start:start+3][::[1,-1][reverse]]



    def __str__(self):
        u_face, f_face, r_face, d_face, b_face, l_face = self.get_face_color()

        for row in range(3):
            u_face[row] = list(map(lambda x: self.COLOR[x], u_face[row]))
            f_face[row] = list(map(lambda x: self.COLOR[x], f_face[row]))
            r_face[row] = list(map(lambda x: self.COLOR[x], r_face[row]))
            d_face[row] = list(map(lambda x: self.COLOR[x], d_face[row]))
            b_face[row] = list(map(lambda x: self.COLOR[x], b_face[row]))
            l_face[row] = list(map(lambda x: self.COLOR[x], l_face[row]))

        sep = ' | ' # length should be odd
        cube_in_string = ""
        cube_in_string += "   " + sep + ''.join(u_face[0]) + sep + '\n'
        cube_in_string += "   " + sep + ''.join(u_face[1]) + sep + '\n'
        cube_in_string += "   " + sep + ''.join(u_face[2]) + sep + '\n'
        cube_in_string += "---" + "- -" + "---" + "- -" + "---" + "- -" + "---" + '\n'
        cube_in_string += ''.join(l_face[0]) + sep + ''.join(f_face[0]) + sep + ''.join(r_face[0]) + sep + ''.join(b_face[0]) + '\n'
        cube_in_string += ''.join(l_face[1]) + sep + ''.join(f_face[1]) + sep + ''.join(r_face[1]) + sep + ''.join(b_face[1]) + '\n'
        cube_in_string += ''.join(l_face[2]) + sep + ''.join(f_face[2]) + sep + ''.join(r_face[2]) + sep + ''.join(b_face[2]) + '\n'
        cube_in_string += "---" + "- -" + "---" + "- -" + "---" + "- -" + "---" + '\n'
        cube_in_string += "   " + sep + ''.join(d_face[0]) + sep + '\n'
        cube_in_string += "   " + sep + ''.join(d_face[1]) + sep + '\n'
        cube_in_string += "   " + sep + ''.join(d_face[2]) + sep + '\n'
        cube_in_string += '\n'

        return cube_in_string