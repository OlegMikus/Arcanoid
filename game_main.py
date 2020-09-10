import pygame


def play():
	done = True
	ball_up = True
	ball_left = True
	pygame.key.set_repeat(1, 1)

	
	while done:

	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            done = False

	        if event.type == pygame.KEYDOWN:
	            if event.key == pygame.K_RIGHT:
	                if platform.x < (window_size - plat_long):
	                    platform.x += 1
	            if event.key == pygame.K_LEFT:
	                if platform.x > 0:
	                    platform.x -= 1
	           
	        

	    if ball.y < 180:
	        for i in range(65):

	            if ball_square_45(ball.x, ball.y, Square_Array[i].x, Square_Array[i].y):
	                Square_Array[i].x = -square_size
	                Square_Array[i].y = -square_size
	                count += 1
	                ball_up = True

	            if ball_square_down(ball.x, ball.y, Square_Array[i].x, Square_Array[i].y):
	                    Square_Array[i].x = -square_size
	                    Square_Array[i].y = -square_size
	                    count += 1
	                    ball_up = True

	            if ball_square_left(ball.x, ball.y, Square_Array[i].x, Square_Array[i].y):
	                Square_Array[i].x = -square_size
	                Square_Array[i].y = -square_size
	                count += 1
	                ball_left = True
	                ball_up = False

	            if ball_square_right(ball.x, ball.y, Square_Array[i].x, Square_Array[i].y):
	                Square_Array[i].x = -square_size
	                Square_Array[i].y = -square_size
	                count += 1
	                ball_left = False
	                ball_up = False

	            if ball_square_up(ball.x, ball.y, Square_Array[i].x, Square_Array[i].y):
	                Square_Array[i].x = -square_size
	                Square_Array[i].y = -square_size
	                count += 1
	                ball_up = False

	    if ball.y < 0:
	        ball_up = True
	    if ball.y > window_size - plat_high - ball_size:

	        if ball_plat(platform.x, platform.y, ball.x, ball.y):
	            ball_up = False
	            ball.y -= 1
	            if ball.y < 0:
	                ball_up = True
	            if ball_left:
	                ball.x += 1
	                if ball.x > (window_size - ball_size):
	                    ball_left = False
	            else:
	                ball.x -= 1
	                if ball.x < 0:
	                    ball_left = True

	        else:
	            done = False
	    if ball_up:
	        ball.y += 1
	        if ball.y > window_size:
	            ball_up = False
	    else:
	        ball.y -= 1
	    if ball_left:
	        ball.x += 1
	        if ball.x > (window_size - ball_size):
	            ball_left = False
	    else:
	        ball.x -= 1
	        if ball.x < 0:
	            ball_left = True

    screen.fill((0, 0, 0))
    square_render()
    ball.render()
    platform.render()
    window.blit(screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(p)
