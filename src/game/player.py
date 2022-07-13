import pygame

from settings import TILE_SIZE, SOURCE_ROOT

filename = 'Assets/Dungeon Crawl Stone Soup Full/player/transform/dragon_form.png'


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups: list[pygame.sprite.Group]):
        # noinspection PyTypeChecker
        super().__init__(groups)
        self.image = pygame.image.load(SOURCE_ROOT / filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2()
        self.speed = 5

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self, speed):
        self.rect.center += self.direction * speed

    def update(self):
        self.input()
        self.move(self.speed)
