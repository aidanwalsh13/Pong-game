import pygame
import os
import random

speed = 500

def collision(ball1, player1, player2, screen, vx, vy):
    p1_hit_pos = (ball1.centery - player1.centery) / (player1.height / 2)
    p2_hit_pos = (ball1.centery - player2.centery) / (player2.height / 2)
# ball and player are pygame Rect objects by now. .centery is one of the pygame methods
# .centery calcualtes the y position (eg 500) and adds the height of the (object / 2) Eg 500 + (10/2) = 505
# so the hit_pos calculates the distance between the center of the ball and center of the player, then divides by half player height

    if ball1.top < 0:
        ball1.top = 0 # keeps from clipping through the wall
        vy *= -1 # reverse trajectory

    elif ball1.bottom > screen.get_height():
        ball1.bottom = screen.get_height()
        vy *= -1
    
    if ball1.colliderect(player1):
        ball1.left = player1.right
        vx *= -1
        vx = max(-3*speed, min(vx, 3*speed)) # this is useful if we increase the speed after each hit, keeping the speed capped
        vy += p1_hit_pos * 150

    elif ball1.colliderect(player2):
        ball1.right = player2.left
        vx *= -1
        vx = max(-3*speed, min(vx, 3*speed))
        vy += p2_hit_pos * 150

    return vx, vy

def reset_ball(ball, width, height, speed):
    ball.center = (width // 2, height // 2)

    vx = speed if random.choice([True, False]) else -speed
    vy = random.uniform(-speed/2, speed/2)

    if abs(vy) < speed * 0.1: # while is better, but makes the game slower because it has to keep checking
        vy = random.uniform(-speed/2, speed/2)
    
    return vx, vy
"""
def split(self):
    self.kill()
    b1 = ball1(self.position.x, self.position.y, 5, 100)
    b2 = ball1(self.position.x, self.position.y, 5, 100)
    b1.velocity = vx
    b2.velocity = vx
    return b1, b2
    """