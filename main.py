import pygame
import os
import random

pygame.init()

score_font = pygame.font.SysFont("AriaL", 30)

width, height = 1900, 1000

screen = pygame.display.set_mode((width, height)) # (()) = a single tuple for the size

clock = pygame.time.Clock() # pygame has a Clock OBJECT

ball1 = pygame.Rect(925, 500, 10, 10)
    # the Rect class is still usable for circle. we initialise it later as a circle shape in the update
    # define objects OUTSIDE of the game loop, else the update will send them back to start position

speed = 500

vx = speed if random.choice([True, False]) else -speed # left or right
vy = random.uniform(-speed/2, speed/2) # random, up/down, but not as fast as x, so it stays on mostly x trajectory

player1 = pygame.Rect(100, 250, 5, 100) # x, y, w, h
player2 = pygame.Rect(1800, 150, 5, 100)
    # "R"ect for pygame class

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
player1_color_index = 0
player2_color_index = 0 # outside the game loop, else they just reset every frame
ball1_color_index = 0

player1_score = 0
player2_score = 0    

def collision(ball1, player1, player2, screen, vx, vy, ball1_color_index, colors, player1_color_index, player2_color_index):
    p1_hit_pos = (ball1.centery - player1.centery) / (player1.height / 2)
    p2_hit_pos = (ball1.centery - player2.centery) / (player2.height / 2)
# ball and player are pygame Rect objects by now. .centery is one of the pygame methods
# .centery calculates the y position (eg 500) and adds the height of the (object / 2) Eg 500 + (10/2) = 505
# so the hit_pos calculates the distance between the center of the ball and center of the player, then divides by half player height

    if ball1.top < 0:
        ball1.top = 0 # keeps from clipping through the wall
        vy *= -1 # reverse trajectory
        vx *= 0.975
        ball1_color_index = ball1_color_index = (ball1_color_index + random.choice([1, -1])) % len(colors)

    elif ball1.bottom > screen.get_height():
        ball1.bottom = screen.get_height()
        vy *= -1
        vx *= 0.975
        ball1_color_index = ball1_color_index = (ball1_color_index + random.choice([1, -1])) % len(colors)
    
    if ball1.colliderect(player1) and ball1_color_index == player1_color_index:
        ball1.left = player1.right
        vx *= -1.05 # you can make this number other than 1.0 so to make the ball speed change the more it bounces
        vx = max(-2*speed, min(vx, 2*speed)) # this is useful if we increase the speed after each hit, keeping the speed capped
        reset_speed = vx
        vy += p1_hit_pos * 150
        ball1_color_index = (ball1_color_index + random.choice([1, -1])) % len(colors)

    elif ball1.colliderect(player2) and ball1_color_index == player2_color_index:
        ball1.right = player2.left
        vx *= -1.05
        vx = max(-2*speed, min(vx, 2*speed))
        reset_speed = vx
        vy += p2_hit_pos * 150
        ball1_color_index = (ball1_color_index + 1) % len(colors)

    return vx, vy, ball1_color_index


def reset_ball(ball, width, height, speed, ball1_color_index):
    ball.center = (width // 2, height // 2)

    vx = speed if random.choice([True, False]) else -speed
    vy = random.uniform(-speed/2, speed/2)

    if abs(vy) < speed * 0.1: # `while` is better than `if`, but makes the game slower because it has to keep checking
        vy = random.uniform(-speed/2, speed/2)
    
    return vx, vy, ball1_color_index


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                player1_color_index = (player1_color_index + 1) % len(colors)

            if event.key == pygame.K_LEFT:
                player2_color_index = (player2_color_index + 1) % len(colors)

    dt = clock.tick(60) / 1000
        # pygame has a tick FUNCTION

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1.y -= (speed * 1.25) * dt
    if keys[pygame.K_s]:
        player1.y += (speed * 1.25) * dt
    
    if keys[pygame.K_UP]:
        player2.y -= (speed * 1.25) * dt
    if keys[pygame.K_DOWN]:
        player2.y += (speed * 1.25) * dt

    player1.y = max(0, min(player1.y, screen.get_height() - player1.height))
    player2.y = max(0, min(player2.y, screen.get_height() - player2.height))

    ball1.x += vx * dt
    ball1.y += vy * dt
    vx, vy, ball1_color_index = collision(ball1, player1, player2, screen, vx, vy, ball1_color_index, colors, player1_color_index, player2_color_index)

    #if collision(ball1, player1, player2, screen, vx, vy) * 5:
    #    ball1.split()

        # Check if ball went off left/right
    if ball1.left <= 0:
        player2_score += 1
        vx, vy, ball1_color_index = reset_ball(ball1, width, height, speed, ball1_color_index)
    
    elif ball1.right >= width:
        player1_score += 1
        vx, vy, ball1_color_index = reset_ball(ball1, width, height, speed, ball1_color_index)

    screen.fill((0, 0, 0))

    p1_score_string = f"P1: {player1_score}"
    p2_score_string = f"P2: {player2_score}"
    text1_surface = score_font.render(p1_score_string, True, (255, 0, 0))
    text2_surface = score_font.render(p2_score_string, True, (0, 255, 0))
    screen.blit(text1_surface, (10, 10))
    screen.blit(text2_surface, (100, 10))

    pygame.draw.rect(screen, (colors)[player1_color_index], player1)
    pygame.draw.rect(screen, (colors)[player2_color_index], player2)
    pygame.draw.circle(screen, (colors)[ball1_color_index], ball1.center, 10)
        # "r"ect for pygame function
    
    pygame.display.flip()

    if player1_score == 5:
        print(f"P1 wins! {player1_score} : {player2_score}")
        running = False
    elif player2_score == 5:
        print(f"P2 wins! {player1_score} : {player2_score}")
        running = False

pygame.quit()
