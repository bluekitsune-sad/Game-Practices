import pygame, sys
from random import random, choice, randint, uniform
from pygame import *
from os.path import join

pygame.init()
pygame.display.set_caption('Space Shooter')
WINDOWWIDTH, WINDOWHEIGHT = 600, 400
WINDOW_SIZE = (WINDOWWIDTH, WINDOWHEIGHT)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

# display = pygame.Surface((300, 200))

clock = pygame.time.Clock()

stopdiagnalspeed = True


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load('../images/player.png').convert_alpha()
        self.rect = self.image.get_frect(center=(WINDOWWIDTH / 2, 100 + (WINDOWHEIGHT / 2)))
        self.direction = pygame.Vector2()
        self.speed = 250

        # cooldown
        self.can_shoot = True
        self.lazer_shoot_time = 0
        self.cooldown_duration = 400

    def lazer_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()  # get time in ms
            if current_time - self.lazer_shoot_time >= self.cooldown_duration:
                self.can_shoot = True

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            Lazer(lazer_image, self.rect.midtop, all_sprites)
            self.can_shoot = False
            self.lazer_shoot_time = pygame.time.get_ticks()
        self.lazer_timer()


class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center=(randint(0, WINDOWWIDTH), randint(0, WINDOWHEIGHT)))


class Meteor(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load('../images/meteor.png').convert_alpha()
        self.rect = self.image.get_frect(midbottom=(randint(0, WINDOWWIDTH), 0))
        self.start_time = pygame.time.get_ticks()
        self.lifetime = 3000
        self.direction = pygame.Vector2(uniform(-0.5, 0.5), 1)
        self.speed = randint(400, 500)

    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        if self.rect.top > WINDOWHEIGHT:
            self.kill()
        # if pygame.time.get_ticks() - self.start_time >= self.lifetime:
        #     self.kill()


class Lazer(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom=pos)

    def update(self, dt):
        self.rect.centery -= 400 * dt
        if self.rect.bottom < 0:
            self.kill()


all_sprites = pygame.sprite.Group()

star_surf = pygame.image.load('../images/star.png').convert_alpha()
for i in range(20):
    Star(all_sprites, star_surf)

# Meteor(all_sprites)
# Meteor(all_sprites, pygame.image.load('../images/meteor.png').convert_alpha())

player = Player(all_sprites)

# player
# path = join('images','player.png')
# player_image = pygame.image.load('../images/player.png').convert_alpha()
# player_rect = player_image.get_frect(center=(WINDOWWIDTH / 2, 100 + (WINDOWHEIGHT / 2)))
# playerDiraction = pygame.math.Vector2(1, 1)
# pSpeed = 250

# stars
# star_image = pygame.image.load('../images/star.png')
# star_image.convert_alpha()
# # sx, sy = randint(100, 400), randint(50, 200)
# star_postion = [(randint(0, WINDOWWIDTH), randint(0, WINDOWHEIGHT)) for _ in range(20)]

# meteor
# meteor_image = pygame.image.load('../images/meteor.png').convert_alpha()
# # meteor_rect = meteor_image.get_frect(center=(WINDOWWIDTH / 2, WINDOWHEIGHT / 2))
# Meteor(all_sprites, meteor_image)


# lazer
lazer_image = pygame.image.load('../images/laser.png').convert_alpha()
# lazer_rect = lazer_image.get_frect(bottom=(player_rect.top, player_rect.top))


# custom timer
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)

while True:
    dt = clock.tick(60) / 1000  # delta time = makeing fixed fps / 1 sec

    # collion
    # if player_rect.left <= 0:
    #     player_rect.x += 6
    # if player_rect.right >= WINDOWWIDTH:
    #     player_rect.x -= 6
    # if player_rect.bottom >= WINDOWHEIGHT:
    #     player_rect.y -= 6
    # if player_rect.top <= 0:
    #     player_rect.y += 6
    # if player_rect.right <= 0:
    #     player_rect.x = WINDOWWIDTH - 1
    # if player_rect.left >= WINDOWWIDTH:
    #     player_rect.x = 1 - player_rect.width
    # if player_rect.bottom <= 0:
    #     player_rect.y = WINDOWHEIGHT - 50
    # if player_rect.top >= WINDOWHEIGHT - 1:
    #     player_rect.bottom = 0

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == meteor_event:
            Meteor(all_sprites)
        # if event.type == KEYDOWN:
        #     if event.key == K_w:
        #         playerDiraction.y = -1
        #     if event.key == K_a:
        #         playerDiraction.x = -1
        #     if event.key == K_s:
        #         playerDiraction.y = 1
        #     if event.key == K_d:
        #         playerDiraction.x = 1

    # # input
    # key = pygame.key.get_pressed()
    # if key[pygame.K_w]:  # this will hear the input continuously when pressed
    #     print("w")
    # playerDiraction.x = int(key[pygame.K_d]) - int(key[pygame.K_a])
    # playerDiraction.y = int(key[pygame.K_s]) - int(key[pygame.K_w])
    # recentlyPressed = pygame.key.get_just_pressed()
    #
    # if recentlyPressed[pygame.K_SPACE]:  # hear space once
    #     print("lazer is fired")

    # Player Movements
    # if stopdiagnalspeed:
    # playerDiraction = playerDiraction.normalize() if playerDiraction else playerDiraction
    # player_rect.center += playerDiraction * pSpeed * dt
    # player_rect.x += playerDiraction * pSpeed

    all_sprites.update(dt)

    screen.fill("darkgray")

    # surf = pygame.transform.scale(display, WINDOW_SIZE)
    # screen.blit(surf, (0, 0))
    # for pos in star_postion:
    #     screen.blit(star_image, pos)
    # screen.blit(meteor_image, meteor_rect)
    # screen.blit(lazer_image, lazer_rect)
    # screen.blit(player_image, player_rect)
    all_sprites.draw(screen)
    pygame.display.update()
