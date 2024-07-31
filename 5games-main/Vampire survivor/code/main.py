from settings import *

pygame.init()
pygame.display.set_caption('Vampire Shooter')

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0)
game_running = True
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load('../images/player/down/0.png').convert_alpha()
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH / 2, 100 + (WINDOW_HEIGHT / 2)))
        self.direction = pygame.Vector2()
        self.speed = 250

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt


# sprite

# import
allSprite = pygame.sprite.Group()

# player
player = Player(allSprite)

while game_running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.QUIT
            sys.exit()

    allSprite.update(dt)

    allSprite.draw(screen)
    pygame.display.update
