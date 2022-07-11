import pygame
from pygame.locals import *
import pygame.locals
from pathlib import Path

from map.level import Level
from map.sprite import Sprite
from map.tileCache import TileCache

ASSETS_FOLDER = Path(__file__).parent / "Assets"

class App:
    def __init__(self):
        self.level = None
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 640, 400
        # self._filename = filename
        self.SPRITE_CACHE = TileCache(32, 32)
        self.speed = [2,2]
        self.black = 0,0,0

    def on_init(self):
        # print("Initializing Pygame")
        pygame.init()
        # self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surf = pygame.display.set_mode(self.size)
        # self._display_surf.fill((255, 255, 255))

        self.level = Level()
        self.level.load_file('level.map')

        self.ball = pygame.image.load(ASSETS_FOLDER / "intro_ball.gif")
        self.ball_rect = self.ball.get_rect()


        clock = pygame.time.Clock()

        # self.background, overlay_dict = self.level.render()
        # self.overlays = pygame.sprite.RenderUpdates()
        # for (x, y), image in overlay_dict.items():
        #     overlay = pygame.sprite.Sprite(self.overlays)
        #     overlay.image = image
        #     overlay.rect = image.get_rect().move(x * 24, y * 16 - 16)
        # self._display_surf.blit(self.background, (0, 0))

        # clock.tick(15)

        self._running = True

    def on_event(self, event):
        # print("Checking Event")
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            pressed_key = event.key

    def on_loop(self):
        # self.sprites = pygame.sprite.RenderUpdates()
        # for pos, tile in self.level.items.items():
        #     sprite = Sprite(pos, self.SPRITE_CACHE[tile["sprite"]])
        #     self.sprites.add(sprite)

        self.ball_rect = self.ball_rect.move(self.speed)
        if self.ball_rect.left < 0 or self.ball_rect.right > self.width:
            self.speed[0] = -self.speed[0]
        if self.ball_rect.top < 0 or self.ball_rect.bottom > self.height:
            self.speed[1] = -self.speed[1]

        pass

    def on_render(self):
        # self.sprites.clear(self._display_surf, self.background)
        # dirty = self.sprites.draw(self._display_surf)
        # self.overlays.draw(self._display_surf)
        # pygame.display.update(dirty)
        # pygame.display.flip()
        self._display_surf.fill(self.black)
        self._display_surf.blit(self.ball, self.ball_rect)
        pygame.display.flip()
        pass

    def on_cleanup(self):
        # print("cleaning up")
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == '__main__':
    game = App()
    game.on_execute()
