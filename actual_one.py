import pygame
import random
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('background.png')
pygame.display.set_caption('Trash Escape')

playerImg = pygame.image.load('fish.png')
playerX = 370
playerY = 480

def player(x, y):
    screen.blit(playerImg, (x, y))

running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5

    player(playerX, playerY)