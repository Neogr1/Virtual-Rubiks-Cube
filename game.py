import sys
import pygame as pg
from pygame.locals import *
from cube import Cube

'''
FULL_SIGHT:
    True  - see all faces
    False - see only U, F, R faces
'''
FULL_SIGHT = True

# screen
W = 900 if FULL_SIGHT else 600
H = 600 if FULL_SIGHT else 600
fps = 30

# colors
BLACK  = (  0,  0,  0)
GREY   = (100,100,100)
WHITE  = (255,255,255)
GREEN  = (0,255,0)
RED    = (255,0,0)
YELLOW = (255,255,0)
BLUE   = (0,0,255)
ORANGE = (255,127,0)
COLORS = (WHITE, GREEN, RED, YELLOW, BLUE, ORANGE)
DARK_COLORS = tuple(tuple(map(lambda x: x*0.35, color)) for color in COLORS)


# cube size
SIZE = 60 if FULL_SIGHT else 90
GAP = 0
DIA_H = 30 if FULL_SIGHT else 45
DIA_W = 30 if FULL_SIGHT else 45

# base cube position
U_BASE_X = 400 if FULL_SIGHT else 230
U_BASE_Y = 90 if FULL_SIGHT else 100
F_BASE_X = U_BASE_X - 3*DIA_W
F_BASE_Y = U_BASE_Y + 3*DIA_H + 3*GAP
R_BASE_X = F_BASE_X + 3*SIZE  + 3*GAP
R_BASE_Y = F_BASE_Y
# unseen faces position
D_BASE_X = U_BASE_X - 3*DIA_W
D_BASE_Y = U_BASE_Y + 3*SIZE + 3*DIA_H
B_BASE_X = U_BASE_X + 3*SIZE
B_BASE_Y = U_BASE_Y
L_BASE_X = U_BASE_X - 3*SIZE - 3*DIA_W
L_BASE_Y = U_BASE_Y + 3*DIA_H


# positions for every tile
u_face = [[[],[],[]],
          [[],[],[]],
          [[],[],[]]]
f_face = [[[],[],[]],
          [[],[],[]],
          [[],[],[]]]
r_face = [[[],[],[]],
          [[],[],[]],
          [[],[],[]]]
d_face = [[[],[],[]],
          [[],[],[]],
          [[],[],[]]]
b_face = [[[],[],[]],
          [[],[],[]],
          [[],[],[]]]
l_face = [[[],[],[]],
          [[],[],[]],
          [[],[],[]]]
for r in range(3):
    for c in range(3):
        u_face[r][c].append((U_BASE_X +     c*SIZE + c*GAP -     r*DIA_W, U_BASE_Y +     r*DIA_H + r*GAP))
        u_face[r][c].append((U_BASE_X + (c+1)*SIZE + c*GAP -     r*DIA_W, U_BASE_Y +     r*DIA_H + r*GAP))
        u_face[r][c].append((U_BASE_X + (c+1)*SIZE + c*GAP - (r+1)*DIA_W, U_BASE_Y + (r+1)*DIA_H + r*GAP))
        u_face[r][c].append((U_BASE_X +     c*SIZE + c*GAP - (r+1)*DIA_W, U_BASE_Y + (r+1)*DIA_H + r*GAP))

        f_face[r][c].append((F_BASE_X +     c*SIZE + c*GAP, F_BASE_Y +     r*SIZE + r*GAP))
        f_face[r][c].append((F_BASE_X + (c+1)*SIZE + c*GAP, F_BASE_Y +     r*SIZE + r*GAP))
        f_face[r][c].append((F_BASE_X + (c+1)*SIZE + c*GAP, F_BASE_Y + (r+1)*SIZE + r*GAP))
        f_face[r][c].append((F_BASE_X +     c*SIZE + c*GAP, F_BASE_Y + (r+1)*SIZE + r*GAP))

        r_face[r][c].append((R_BASE_X +     c*DIA_W + c*GAP, R_BASE_Y +     r*SIZE + r*GAP - c*DIA_H))
        r_face[r][c].append((R_BASE_X + (c+1)*DIA_W + c*GAP, R_BASE_Y +     r*SIZE + r*GAP - (c+1)*DIA_H))
        r_face[r][c].append((R_BASE_X + (c+1)*DIA_W + c*GAP, R_BASE_Y + (r+1)*SIZE + r*GAP - (c+1)*DIA_H))
        r_face[r][c].append((R_BASE_X +     c*DIA_W + c*GAP, R_BASE_Y + (r+1)*SIZE + r*GAP - c*DIA_H))

        d_face[r][c].append((D_BASE_X +     c*SIZE + c*GAP, D_BASE_Y +     r*SIZE + r*GAP))
        d_face[r][c].append((D_BASE_X + (c+1)*SIZE + c*GAP, D_BASE_Y +     r*SIZE + r*GAP))
        d_face[r][c].append((D_BASE_X + (c+1)*SIZE + c*GAP, D_BASE_Y + (r+1)*SIZE + r*GAP))
        d_face[r][c].append((D_BASE_X +     c*SIZE + c*GAP, D_BASE_Y + (r+1)*SIZE + r*GAP))

        b_face[r][c].append((B_BASE_X +     c*SIZE + c*GAP, B_BASE_Y +     r*SIZE + r*GAP))
        b_face[r][c].append((B_BASE_X + (c+1)*SIZE + c*GAP, B_BASE_Y +     r*SIZE + r*GAP))
        b_face[r][c].append((B_BASE_X + (c+1)*SIZE + c*GAP, B_BASE_Y + (r+1)*SIZE + r*GAP))
        b_face[r][c].append((B_BASE_X +     c*SIZE + c*GAP, B_BASE_Y + (r+1)*SIZE + r*GAP))

        l_face[r][c].append((L_BASE_X +     c*SIZE + c*GAP, L_BASE_Y +     r*SIZE + r*GAP))
        l_face[r][c].append((L_BASE_X + (c+1)*SIZE + c*GAP, L_BASE_Y +     r*SIZE + r*GAP))
        l_face[r][c].append((L_BASE_X + (c+1)*SIZE + c*GAP, L_BASE_Y + (r+1)*SIZE + r*GAP))
        l_face[r][c].append((L_BASE_X +     c*SIZE + c*GAP, L_BASE_Y + (r+1)*SIZE + r*GAP))


# positions for every line between tiles
border_lines = [
    ((U_BASE_X +   SIZE,  U_BASE_Y)          , (U_BASE_X +   SIZE - 3*DIA_W, U_BASE_Y + 3*DIA_H)),
    ((U_BASE_X + 2*SIZE,  U_BASE_Y)          , (U_BASE_X + 2*SIZE - 3*DIA_W, U_BASE_Y + 3*DIA_H)),
    ((U_BASE_X -   DIA_W, U_BASE_Y +   DIA_H), (U_BASE_X + 3*SIZE -   DIA_W, U_BASE_Y +   DIA_H)),
    ((U_BASE_X - 2*DIA_W, U_BASE_Y + 2*DIA_H), (U_BASE_X + 3*SIZE - 2*DIA_W, U_BASE_Y + 2*DIA_H)),
    ((F_BASE_X +   SIZE, F_BASE_Y), (F_BASE_X +   SIZE, F_BASE_Y + 3*SIZE)),
    ((F_BASE_X + 2*SIZE, F_BASE_Y), (F_BASE_X + 2*SIZE, F_BASE_Y + 3*SIZE)),
    ((F_BASE_X, F_BASE_Y +   SIZE), (F_BASE_X + 3*SIZE, F_BASE_Y +   SIZE)),
    ((F_BASE_X, F_BASE_Y + 2*SIZE), (F_BASE_X + 3*SIZE, F_BASE_Y + 2*SIZE)),
    ((R_BASE_X +   DIA_W, R_BASE_Y -   DIA_H), (R_BASE_X +   DIA_W, R_BASE_Y + 3*SIZE -   DIA_H)),
    ((R_BASE_X + 2*DIA_W, R_BASE_Y - 2*DIA_H), (R_BASE_X + 2*DIA_W, R_BASE_Y + 3*SIZE - 2*DIA_H)),
    ((R_BASE_X, R_BASE_Y +   SIZE),(R_BASE_X + 3*DIA_W, R_BASE_Y +   SIZE - 3*DIA_H)),
    ((R_BASE_X, R_BASE_Y + 2*SIZE),(R_BASE_X + 3*DIA_W, R_BASE_Y + 2*SIZE - 3*DIA_H))
]
if FULL_SIGHT:
    border_lines.extend([
        ((D_BASE_X +   SIZE, D_BASE_Y), (D_BASE_X +   SIZE, D_BASE_Y + 3*SIZE)),
        ((D_BASE_X + 2*SIZE, D_BASE_Y), (D_BASE_X + 2*SIZE, D_BASE_Y + 3*SIZE)),
        ((D_BASE_X, D_BASE_Y +   SIZE), (D_BASE_X + 3*SIZE, D_BASE_Y +   SIZE)),
        ((D_BASE_X, D_BASE_Y + 2*SIZE), (D_BASE_X + 3*SIZE, D_BASE_Y + 2*SIZE)),
        ((B_BASE_X +   SIZE, B_BASE_Y), (B_BASE_X +   SIZE, B_BASE_Y + 3*SIZE)),
        ((B_BASE_X + 2*SIZE, B_BASE_Y), (B_BASE_X + 2*SIZE, B_BASE_Y + 3*SIZE)),
        ((B_BASE_X, B_BASE_Y +   SIZE), (B_BASE_X + 3*SIZE, B_BASE_Y +   SIZE)),
        ((B_BASE_X, B_BASE_Y + 2*SIZE), (B_BASE_X + 3*SIZE, B_BASE_Y + 2*SIZE)),
        ((L_BASE_X +   SIZE, L_BASE_Y), (L_BASE_X +   SIZE, L_BASE_Y + 3*SIZE)),
        ((L_BASE_X + 2*SIZE, L_BASE_Y), (L_BASE_X + 2*SIZE, L_BASE_Y + 3*SIZE)),
        ((L_BASE_X, L_BASE_Y +   SIZE), (L_BASE_X + 3*SIZE, L_BASE_Y +   SIZE)),
        ((L_BASE_X, L_BASE_Y + 2*SIZE), (L_BASE_X + 3*SIZE, L_BASE_Y + 2*SIZE))
    ])



cube = Cube(shuffle=True)

pg.init()
pg.display.set_caption("Rubik's Cube Simulator")
screen = pg.display.set_mode((W, H), 0, 32)
clock = pg.time.Clock()

count = 0

font = pg.font.SysFont('ubuntu', 25, True, False)
text = font.render("Rotation counts: {}".format(count), True, (255, 255, 255))

while True:
    # count display
    
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_F4:
                count = 0
                cube.reset()
                cube.shuffle()
            if event.key == K_F5:
                count = 0
                cube.reset()
                

            if event.key == K_j:
                cube.move_U()
                count += 1
            if event.key == K_f:
                cube.move_U_()
                count += 1
            if event.key == K_h:
                cube.move_F()
                count += 1
            if event.key == K_g:
                cube.move_F_()
                count += 1
            if event.key == K_i:
                cube.move_R()
                count += 1
            if event.key == K_k:
                cube.move_R_()
                count += 1
            if event.key == K_s:
                cube.move_D()
                count += 1
            if event.key == K_l:
                cube.move_D_()
                count += 1
            if event.key == K_w:
                cube.move_B()
                count += 1
            if event.key == K_o:
                cube.move_B_()
                count += 1
            if event.key == K_d:
                cube.move_L()
                count += 1
            if event.key == K_e:
                cube.move_L_()
                count += 1

            if event.key == K_COMMA:
                cube.move_u()
                count += 1
            if event.key == K_c:
                cube.move_u_()
                count += 1
            # if event.key == K_:
            #     cube.move_f()
            # if event.key == K_:
            #     cube.move_f_()
            if event.key == K_u:
                cube.move_r()
                count += 1
            if event.key == K_m:
                cube.move_r_()
                count += 1
            if event.key == K_z:
                cube.move_d()
                count += 1
            if event.key == K_SLASH:
                cube.move_d_()
                count += 1
            # if event.key == K_:
            #     cube.move_b()
            # if event.key == K_:
            #     cube.move_b_()
            if event.key == K_v:
                cube.move_l()
                count += 1
            if event.key == K_r:
                cube.move_l_()
                count += 1

            if event.key == K_5 or event.key == K_6:
                cube.move_M()
                count += 1
            if event.key == K_x or event.key == K_PERIOD:
                cube.move_M_()
                count += 1
            # if event.key == K_:
            #     cube.move_E()
            # if event.key == K_:
            #     cube.move_E_()
            # if event.key == K_:
            #     cube.move_S()
            # if event.key == K_:
            #     cube.move_S_()
                
            if event.key == K_t or event.key == K_y:
                cube.rotate_x()
            if event.key == K_b or event.key == K_n:
                cube.rotate_x_()
            if event.key == K_SEMICOLON:
                cube.rotate_y()
            if event.key == K_a:
                cube.rotate_y_()
            if event.key == K_p:
                cube.rotate_z()
            if event.key == K_q:
                cube.rotate_z_()

    screen.fill(GREY)
    

    # fill cube coor
    face_color = cube.get_face_color()
    for r in range(3):
        for c in range(3):
            pg.draw.polygon(screen, COLORS[face_color[0][r][c]], u_face[r][c])
            pg.draw.polygon(screen, COLORS[face_color[1][r][c]], f_face[r][c])
            pg.draw.polygon(screen, COLORS[face_color[2][r][c]], r_face[r][c])

            if FULL_SIGHT:
                pg.draw.polygon(screen, DARK_COLORS[face_color[3][r][c]], d_face[r][c])
                pg.draw.polygon(screen, DARK_COLORS[face_color[4][r][c]], b_face[r][c])
                pg.draw.polygon(screen, DARK_COLORS[face_color[5][r][c]], l_face[r][c])

    # draw lines
    for start, end in border_lines:
        pg.draw.line(screen, BLACK, start, end, width=5)
        
    screen.blit(text, (10, 5))
    
    pg.display.update()
    clock.tick(fps)