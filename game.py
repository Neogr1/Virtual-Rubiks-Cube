import sys
import pygame as pg
from pygame.locals import *
from cube import Cube


W = 600
H = 600
BLACK  = (  0,  0,  0)
GREY   = (100,100,100)
WHITE  = (255,255,255)
GREEN  = (0,255,0)
RED    = (255,0,0)
YELLOW = (255,255,0)
BLUE   = (0,0,255)
ORANGE = (255,127,0)
COLORS = (WHITE, GREEN, RED, YELLOW, BLUE, ORANGE)

fps = 30

pg.init()
pg.display.set_caption("Rubik's Cube Simulator")
screen = pg.display.set_mode((W, H), 0, 32)
clock = pg.time.Clock()


# gulimfont = pg.font.SysFont('굴림', 70) # 서체 설정
# helloworld = gulimfont.render('Hello, world!', 1, black)
# # .render[] 함수에 내용과 안티앨리어싱, 색을 전달하여 글자 이미지 생성
# hellorect = helloworld.get_rect() # 생성한 이미지의 rect 객체를 가져온다
# hellorect.center = (W / 2, H / 2) # 해당 rect의 중앙을 화면 중앙에 맞춘다

SIZE = 90
GAP = 0
DIA_H = 50
DIA_W = 30

U_BASE_X = 200
U_BASE_Y = 100
F_BASE_X = U_BASE_X - 3*DIA_W
F_BASE_Y = U_BASE_Y + 3*DIA_H + 3*GAP
R_BASE_X = F_BASE_X + 3*SIZE  + 3*GAP
R_BASE_Y = F_BASE_Y


u_face = [[[],[],[]],
          [[],[],[]],
          [[],[],[]]
]
for r in range(3):
    for c in range(3):
        u_face[r][c].append((U_BASE_X +     c*SIZE + c*GAP -     r*DIA_W, U_BASE_Y +     r*DIA_H + r*GAP))
        u_face[r][c].append((U_BASE_X + (c+1)*SIZE + c*GAP -     r*DIA_W, U_BASE_Y +     r*DIA_H + r*GAP))
        u_face[r][c].append((U_BASE_X + (c+1)*SIZE + c*GAP - (r+1)*DIA_W, U_BASE_Y + (r+1)*DIA_H + r*GAP))
        u_face[r][c].append((U_BASE_X +     c*SIZE + c*GAP - (r+1)*DIA_W, U_BASE_Y + (r+1)*DIA_H + r*GAP))

f_face = [[[],[],[]],
          [[],[],[]],
          [[],[],[]]
]
for r in range(3):
    for c in range(3):
        f_face[r][c].append((F_BASE_X +     c*SIZE + c*GAP, F_BASE_Y +     r*SIZE + r*GAP))
        f_face[r][c].append((F_BASE_X + (c+1)*SIZE + c*GAP, F_BASE_Y +     r*SIZE + r*GAP))
        f_face[r][c].append((F_BASE_X + (c+1)*SIZE + c*GAP, F_BASE_Y + (r+1)*SIZE + r*GAP))
        f_face[r][c].append((F_BASE_X +     c*SIZE + c*GAP, F_BASE_Y + (r+1)*SIZE + r*GAP))

r_face = [[[],[],[]],
          [[],[],[]],
          [[],[],[]]
]
for r in range(3):
    for c in range(3):
        r_face[r][c].append((R_BASE_X +     c*DIA_W + c*GAP, R_BASE_Y +     r*SIZE + r*GAP - c*DIA_H))
        r_face[r][c].append((R_BASE_X + (c+1)*DIA_W + c*GAP, R_BASE_Y +     r*SIZE + r*GAP - (c+1)*DIA_H))
        r_face[r][c].append((R_BASE_X + (c+1)*DIA_W + c*GAP, R_BASE_Y + (r+1)*SIZE + r*GAP - (c+1)*DIA_H))
        r_face[r][c].append((R_BASE_X +     c*DIA_W + c*GAP, R_BASE_Y + (r+1)*SIZE + r*GAP - c*DIA_H))

lines = [((U_BASE_X +   SIZE,  U_BASE_Y)          , (U_BASE_X +   SIZE - 3*DIA_W, U_BASE_Y + 3*DIA_H)),
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
         ((R_BASE_X, R_BASE_Y + 2*SIZE),(R_BASE_X + 3*DIA_W, R_BASE_Y + 2*SIZE - 3*DIA_H)),
]






# cube = Cube(scramble=[(1,0),(0,0)])
cube = Cube(shuffle=True)

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_j:
                cube.move_U()
            if event.key == K_f:
                cube.move_U_()
            if event.key == K_h:
                cube.move_F()
            if event.key == K_g:
                cube.move_F_()
            if event.key == K_i:
                cube.move_R()
            if event.key == K_k:
                cube.move_R_()
            if event.key == K_s:
                cube.move_D()
            if event.key == K_l:
                cube.move_D_()
            if event.key == K_w:
                cube.move_B()
            if event.key == K_o:
                cube.move_B_()
            if event.key == K_d:
                cube.move_L()
            if event.key == K_e:
                cube.move_L_()

    screen.fill(GREY)

    # fill cube color
    face_color = cube.get_face_color()
    for r in range(3):
        for c in range(3):
            pg.draw.polygon(screen, COLORS[face_color[0][r][c]], u_face[r][c])
            pg.draw.polygon(screen, COLORS[face_color[1][r][c]], f_face[r][c])
            pg.draw.polygon(screen, COLORS[face_color[2][r][c]], r_face[r][c])

    # draw lines
    for start, end in lines:
        pg.draw.line(screen, BLACK, start, end, width=5)
    
    pg.display.update()
    clock.tick(fps)