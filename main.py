import pygame
import random
from ball_physics import *

pygame.init()

width, height = 1900, 1000

screen = pygame.display.set_mode((width, height)) # (()) = a single tuple for the size

clock = pygame.time.Clock() # pygame has a Clock OBJECT

vx = speed if random.choice([True, False]) else -speed # left or right
vy = random.uniform(-speed/2, speed/2) # random, up/down, but not as fast as x, so it stays on mostly x trajectory

player1 = pygame.Rect(100, 250, 5, 100) # x, y, w, h
player2 = pygame.Rect(1800, 150, 5, 100)
    # "R"ect for pygame class
ball1 = pygame.Rect(925, 500, 10, 10)
    # the Rect class is still usable for circle. we initialise it later as a circle shape in the update
    # define objects OUTSIDE of the game loop, else the update will send them back to start position

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60) / 1000
        # pygame has a tick FUNCTION

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1.y -= (speed * 1.2) * dt
    if keys[pygame.K_s]:
        player1.y += (speed * 1.2) * dt
    if keys[pygame.K_UP]:
        player2.y -= (speed * 1.2) * dt
    if keys[pygame.K_DOWN]:
        player2.y += (speed * 1.2) * dt

    player1.y = max(0, min(player1.y, screen.get_height() - player1.height))
    player2.y = max(0, min(player2.y, screen.get_height() - player2.height))

    ball1.x += vx * dt
    ball1.y += vy * dt
    vx, vy = collision(ball1, player1, player2, screen, vx, vy)

    #if collision(ball1, player1, player2, screen, vx, vy) * 5:
    #    ball1.split()

        # Check if ball went off left/right
    if ball1.left <= 0:
        vx, vy = reset_ball(ball1, width, height, speed)

    elif ball1.right >= width:
        vx, vy = reset_ball(ball1, width, height, speed)

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 0, 255), player1)
    pygame.draw.rect(screen, (0, 255, 0), player2)
    pygame.draw.circle(screen, (255, 0, 0), ball1.center, 10)
        # "r"ect for pygame function

    pygame.display.flip()

pygame.quit()

