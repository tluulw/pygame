import pygame


class Spike(pygame.sprite.Sprite):
    def __init__(self, y, x, wall, floor, *group):
        super().__init__(*group)
        self.image = pygame.image.load('data/spikes.png')
        self.image.set_colorkey(self.image.get_at((0, 0)))
        if wall:
            self.pos = x * 40 + 10, y * 180
            self.image = pygame.transform.rotate(self.image, 90)
            self.image = pygame.transform.scale(self.image, (30, 180))
            self.rect = pygame.Rect(self.pos[0], self.pos[1], 30, 180)
        elif floor:
            self.pos = x * 40, y * 180 + 150
            self.image = pygame.transform.scale(self.image, (200, 30))
            self.rect = pygame.Rect(self.pos[0], self.pos[1], 200, 30)

    def update(self, per):
        if per.flip:
            self.pos = self.pos[0] + per.per_run_speed, self.pos[1]
        else:
            self.pos = self.pos[0] - per.per_run_speed, self.pos[1]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.rect[2], self.rect[3])