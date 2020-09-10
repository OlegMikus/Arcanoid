import pygame, sys
import random
count = 0
window_size = 468
plat_high = 20
plat_long = 70
ball_size = 14
square_size = 36
info_string = pygame.Surface((400, 30))
fisrt_ball_poss = 40
'''(int(random.random()*100)*5 - 36)'''
window = pygame.display.set_mode((window_size, window_size))
screen = pygame.Surface((window_size, window_size))


class Sprite:

    def __init__(self, xpos, ypos, filename,boog):
        self.boog = boog
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)

    def render(self):
        if self.boog:
            screen.blit(self.bitmap, (self.x, self.y))
        else:
            self.x = 0
            self.y = 0


Square_Array = [Sprite(0, 0, 'square.png',True) for i in range(65)]

platform = Sprite(window_size/2 - plat_long/2, window_size - plat_high, 'platform.png',True)
ball = Sprite(fisrt_ball_poss, 180, 'ball.png',True)


for i in range(65):
    Square_Array[12].y = square_size
    Square_Array[12].x = 0
    Square_Array[25].y = 2*square_size
    Square_Array[25].x = 0
    Square_Array[38].y = 3*square_size
    Square_Array[38].x = 0
    Square_Array[51].y = 4*square_size
    Square_Array[51].x = 0
    if i in range(0, 12):
        Square_Array[i].y = 0
        Square_Array[i].x = Square_Array[i - 1].x + square_size
        if i == 0:
            print(Square_Array[i-15].x)
    elif i in range(13, 25):
        Square_Array[i].y = square_size
        Square_Array[i].x = Square_Array[i - 1].x + square_size
    elif i in range(26, 38):
        Square_Array[i].y = 2*square_size
        Square_Array[i].x = Square_Array[i - 1].x + square_size
    elif i in range(39, 51):
        Square_Array[i].y = 3*square_size
        Square_Array[i].x = Square_Array[i - 1].x + square_size
    elif i in range(52, 64):
        Square_Array[i].y = 4*square_size
        Square_Array[i].x = Square_Array[i - 1].x + square_size


print(Square_Array[0].y, Square_Array[0].x, Square_Array[1].y, Square_Array[1].x )


def ball_plat(plat_x, plat_y, ball_x, ball_y):
    if (ball_x < plat_x+(plat_long-(ball_size/2 - 2))) and (ball_x > plat_x-(ball_size-2))\
            and (plat_y < ball_y + ball_size):
        return True


def ball_square_down(ball_x, ball_y, square_x, square_y):
    if ((square_x > ball_x - ball_size / 2  \
            and  square_x - square_size  <= ball_x - ball_size / 2 ) or square_size  == ball_x - ball_size / 2) \
            and (square_y + square_size - 1 == ball_y):
        return True
    

def ball_square_left(ball_x, ball_y, square_x, square_y):
    if (square_x + square_size + 1 == ball_x) \
            and (ball_y + ball_size / 2 > square_y) \
            and (square_y + square_size - ball_size / 2 > ball_y):
        return True


def ball_square_right(ball_x, ball_y, square_x, square_y):
    if (ball_x == square_x - ball_size + 1) \
            and (ball_y > square_y - ball_size / 2) \
            and (ball_y < square_y + square_size - ball_size / 2):
        return True


def ball_square_up(ball_x, ball_y, square_x, square_y):
    if (ball_x < square_x + square_size - (ball_size / 2)) \
            and (ball_x > square_x - ball_size/2) \
            and (square_y - ball_size + 1 == ball_y):
        return True


def square_render():
    for i in range(65):
        Square_Array[i].render()
