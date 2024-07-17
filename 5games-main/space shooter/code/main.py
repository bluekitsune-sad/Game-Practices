import pygame, sys
from random import random, choice, randint
from pygame import *
from os.path import join

pygame.init()
pygame.display.set_caption('Space Shooter')
WINDOWWIDTH, WINDOWHEIGHT = 600, 400
WINDOW_SIZE = (WINDOWWIDTH, WINDOWHEIGHT)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

display = pygame.Surface((300, 200))

clock = pygame.time.Clock()

# player
# path = join('images','player.png')
player_image = pygame.image.load('../images/player.png').convert_alpha()
player_rect = player_image.get_frect(center=(WINDOWWIDTH / 2, 100 + (WINDOWHEIGHT / 2)))
playerDiraction = pygame.math.Vector2(1, 1)
pSpeed = 250

# stars
star_image = pygame.image.load('../images/star.png')
star_image.convert_alpha()
# sx, sy = randint(100, 400), randint(50, 200)
star_postion = [(randint(0, WINDOWWIDTH), randint(0, WINDOWHEIGHT)) for _ in range(20)]

# meteor
meteor_image = pygame.image.load('../images/meteor.png').convert_alpha()
meteor_rect = meteor_image.get_frect(center=(WINDOWWIDTH / 2, WINDOWHEIGHT / 2))

# lazer
lazer_image = pygame.image.load('../images/laser.png').convert_alpha()
# lazer_rect = lazer_image.get_frect(bottom=(player_rect.top, player_rect.top))

while True:
    dt = clock.tick(60) / 1000  # delta time = makeing fixed fps / 1 sec
    display.fill("darkgray")

    # collion
    # if player_rect.left <= 0:
    #     player_rect.x += 6
    # if player_rect.right >= WINDOWWIDTH:
    #     player_rect.x -= 6
    # if player_rect.bottom >= WINDOWHEIGHT:
    #     player_rect.y -= 6
    # if player_rect.top <= 0:
    #     player_rect.y += 6
    if player_rect.right <= 0:
        player_rect.x = WINDOWWIDTH - 1
    if player_rect.left >= WINDOWWIDTH:
        player_rect.x = 1 - player_rect.width
    if player_rect.bottom <= 0:
        player_rect.y = WINDOWHEIGHT - 1
    if player_rect.top >= WINDOWHEIGHT - 1:
        player_rect.bottom = 0

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_w:
                playerDiraction.y = -1
            if event.key == K_a:
                playerDiraction.x = -1
            if event.key == K_s:
                playerDiraction.y = 1
            if event.key == K_d:
                playerDiraction.x = 1

    # Player Movements
    player_rect.center += playerDiraction * pSpeed * dt
    # player_rect.x += playerDiraction * pSpeed

    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0, 0))
    for pos in star_postion:
        screen.blit(star_image, pos)
    screen.blit(meteor_image, meteor_rect)
    # screen.blit(lazer_image, lazer_rect)
    screen.blit(player_image, player_rect)
    pygame.display.update()
1:32