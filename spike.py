import pygame


class Spike(pygame.sprite.Sprite):
    def __init__(self, y, x, wall, angle, floor, *group):
        super().__init__(*group)
        self.image = pygame.image.load('data/spikes/spikes1.png')
        self.image.set_colorkey(self.image.get_at((0, 0)))
        self.floor = floor
        self.wall = wall
        self.angle = angle
        if wall:
            if self.angle == 90:
                self.pos = x * 40 + 10, y * 180
            else:
                self.pos = x * 40, y * 180
            self.image = pygame.transform.rotate(self.image, angle)
            self.image = pygame.transform.scale(self.image, (30, 180))
            self.rect = pygame.Rect(self.pos[0], self.pos[1], 30, 180)
        elif floor:
            self.pos = x * 40, y * 180 + 150
            self.image = pygame.transform.scale(self.image, (200, 30))
            self.rect = pygame.Rect(self.pos[0], self.pos[1], 200, 30)
        self.anim_cnt = 0

    def animate(self):
        self.anim_cnt %= 7
        self.anim_cnt += 1
        self.image = pygame.image.load(f'data/spikes/spikes{self.anim_cnt}.png')
        self.image.set_colorkey(self.image.get_at((0, 0)))
        if self.wall:
            self.image = pygame.transform.rotate(self.image, self.angle)
            self.image = pygame.transform.scale(self.image, (30, 180))
        elif self.floor:
            self.image = pygame.transform.scale(self.image, (200, 30))

    def update(self, per):
        if per.flip:
            self.pos = self.pos[0] + per.per_run_speed, self.pos[1]
        else:
            self.pos = self.pos[0] - per.per_run_speed, self.pos[1]
        self.animate()
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.rect[2], self.rect[3])
