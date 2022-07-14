import pygame

from settings import TILE_SIZE

filename = 'Assets/Dungeon Crawl Stone Soup Full/dungeon/boulder.png'


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups: list[pygame.sprite.Group], sprite_type,
                 surface=pygame.Surface((TILE_SIZE, TILE_SIZE))):
        # noinspection PyTypeChecker
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))

        if sprite_type == 'object':
            self.rect = self.image.get_rect(topleft=(pos[0], pos[1] - TILE_SIZE))
        else:
            self.rect = self.image.get_rect(topleft=pos)

        self.hitbox = self.rect.inflate(0, -10)
