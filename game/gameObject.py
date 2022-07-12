import pygame
from pygame.locals import *


class GameObject:
    def __init__(self, image, height, speed, screen_size):
        self.screen_size = screen_size
        self.image = image
        self.speed = speed
        self.pos = image.get_rect().move(0, height)

    def move(self):
        self.pos = self.pos.move(self.speed)
        if self.pos.left < 0 or self.pos.right > self.screen_size[0]:
            self.speed[0] = -self.speed[0]
        if self.pos.top < 0 or self.pos.bottom > self.screen_size[1]:
            self.speed[1] = -self.speed[1]

    # self.ball_position = self.ball_position.move(self.speed)
    # # if self.ball_position.left < 0 or self.ball_position.right > self.width:
    # #     self.speed[0] = -self.speed[0]
    # # if self.ball_position.top < 0 or self.ball_position.bottom > self.height:
    # #     self.speed[1] = -self.speed[1]
