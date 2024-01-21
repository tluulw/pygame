import pygame


class WinFlag(pygame.sprite.Sprite):
    def __init__(self, y, x, *group):
        super().__init__(*group)
        self.pos = x * 40, y * 180
        self.image = pygame.image.load('data/win.png')
        self.image = pygame.transform.scale(self.image, (250, 150))
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 250, 150)
        self.left_border = pygame.Rect(self.rect[0] - 1, self.rect[1], 1, self.rect[3])
        self.right_border = pygame.Rect(self.rect[0] + 40, self.rect[1], 1, self.rect[3])
        self.top_border = pygame.Rect(self.rect[0], self.rect[1] - 1, self.rect[2], 1)
        self.win_sound = pygame.mixer.Sound("data/win_sound.mp3")
        self.win_sound.set_volume(0.2)

    def update(self, per):
        if per.flip:
            self.pos = self.pos[0] + per.per_run_speed, self.pos[1]
        else:
            self.pos = self.pos[0] - per.per_run_speed, self.pos[1]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 40, 180)
        self.left_border = pygame.Rect(self.rect[0] - 1, self.rect[1] + 20, 1, self.rect[3] - 20)
        self.right_border = pygame.Rect(self.rect[0] + 40, self.rect[1] + 20, 1, self.rect[3] - 20)
        self.top_border = pygame.Rect(self.rect[0], self.rect[1] - 1, self.rect[2], 1)

        if per.rect.colliderect(self.rect):
            self.win_sound.play()