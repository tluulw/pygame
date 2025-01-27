import pygame


class Floor(pygame.sprite.Sprite):
    def __init__(self, y, x, finish, *group):
        super().__init__(*group)
        self.pos = x * 40, y * 180

        self.image = pygame.image.load('data/walls/default_wall.png')
        self.image = pygame.transform.scale(self.image, (30, 200))
        self.image = pygame.transform.rotate(self.image, 90)

        self.rect = pygame.Rect(self.pos[0], self.pos[1], 200, 30)

        self.top_border = pygame.Rect(self.rect[0], self.rect[1] - 1, self.rect[2], 1)
        self.bottom_border = pygame.Rect(self.rect[0], self.rect[1] + 30, self.rect[2], 1)

        self.finish = finish

    def update(self, per):
        if per.flip:
            self.pos = self.pos[0] + per.per_run_speed, self.pos[1]
        else:
            self.pos = self.pos[0] - per.per_run_speed, self.pos[1]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 200, 30)
        self.top_border = pygame.Rect(self.rect[0], self.rect[1] - 1, self.rect[2], 1)
        self.bottom_border = pygame.Rect(self.rect[0], self.rect[1] + 30, self.rect[2], 1)