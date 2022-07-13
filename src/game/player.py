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
