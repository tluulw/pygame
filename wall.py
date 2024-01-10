import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.pos = 200, 600
        self.image = pygame.image.load('walls/default_wall.png')
        self.rect = pygame.Rect(200, 600, 48, 266)