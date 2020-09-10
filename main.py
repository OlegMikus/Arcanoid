import module as mod


mod.pygame.display.set_caption('My_Game_01')


done = True
ball_up = True
ball_left = True
mod.pygame.key.set_repeat(1, 1)

p = 1
while done:

    for event in mod.pygame.event.get():
        if event.type == mod.pygame.QUIT:
            done = False

        if event.type == mod.pygame.KEYDOWN:
            if event.key == mod.pygame.K_RIGHT:
                if mod.platform.x < (mod.window_size - mod.plat_long):
                    mod.platform.x += 1
            if event.key == mod.pygame.K_LEFT:
                if mod.platform.x > 0:
                    mod.platform.x -= 1
       
            
    if mod.ball.y < 180:
        for i in range(65):

          
            if mod.ball_square_down(mod.ball.x, mod.ball.y, mod.Square_Array[i].x, mod.Square_Array[i].y):
                    mod.Square_Array[i].boog = False
                    ball_up = True

            elif mod.ball_square_left(mod.ball.x, mod.ball.y, mod.Square_Array[i].x, mod.Square_Array[i].y):
                mod.Square_Array[i].boog = False
                ball_left = True
                ball_up = False

            elif mod.ball_square_right(mod.ball.x, mod.ball.y, mod.Square_Array[i].x, mod.Square_Array[i].y):
                mod.Square_Array[i].boog = False
                ball_left = False
                ball_up = False

            if mod.ball_square_up(mod.ball.x, mod.ball.y, mod.Square_Array[i].x, mod.Square_Array[i].y):
                mod.Square_Array[i].boog = False
                ball_up = False

    if mod.ball.y < 0:
        ball_up = True
    if mod.ball.y > mod.window_size - mod.plat_high - mod.ball_size:

        if mod.ball_plat(mod.platform.x, mod.platform.y, mod.ball.x, mod.ball.y):
            ball_up = False
            mod.ball.y -= 1
            if mod.ball.y < 0:
                ball_up = True
            if ball_left:
                mod.ball.x += 1
                if mod.ball.x > (mod.window_size - mod.ball_size):
                    ball_left = False
            else:
                mod.ball.x -= 1
                if mod.ball.x < 0:
                    ball_left = True

        #else:
         #   done = False
    if ball_up:
        mod.ball.y += 1
        if mod.ball.y > mod.window_size:
            ball_up = False
    else:
        mod.ball.y -= 1
    if ball_left:
        mod.ball.x += 1
        if mod.ball.x > (mod.window_size - mod.ball_size):
            ball_left = False
    else:
        mod.ball.x -= 1
        if mod.ball.x < 0:
            ball_left = True

    mod.screen.fill((0, 0, 0))
    mod.square_render()
    mod.ball.render()
    mod.platform.render()
    mod.window.blit(mod.screen, (0, 0))
    mod.pygame.display.flip()
    mod.pygame.time.delay(p)
