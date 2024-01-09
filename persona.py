import pygame


class Person(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.pos = 30, 819
        self.default_image()

    def jump_animation(self, count, reverse=False):
        pygame.time.wait(40)
        if count > 10:
            count = 10
        if reverse:
            self.image = pygame.image.load(f'jumping_hero/jump{count}.png')
            self.image.set_colorkey(self.image.get_at((0, 0)))
            self.image = pygame.transform.flip(self.image, True, False)
            self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
            self.rect = self.image.get_rect(center=self.pos)
        else:
            self.image = pygame.image.load(f'jumping_hero/jump{count}.png')
            self.image.set_colorkey(self.image.get_at((0, 0)))
            self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
            self.rect = self.image.get_rect(center=self.pos)

    def jump(self, cnt, reverse=False):
        if reverse:
            if cnt > 0:
                self.pos = self.pos[0] - (cnt ** 2) / 2, self.pos[1] - (cnt ** 2) / 2
                self.rect = self.image.get_rect(center=self.pos)
            else:
                self.pos = self.pos[0] - (cnt ** 2) / 2, self.pos[1] + (cnt ** 2) / 2
                self.rect = self.image.get_rect(center=self.pos)
        else:
            if cnt > 0:
                self.pos = self.pos[0] + (cnt ** 2) / 2, self.pos[1] - (cnt ** 2) / 2
                self.rect = self.image.get_rect(center=self.pos)
            else:
                self.pos = self.pos[0] + (cnt ** 2) / 2, self.pos[1] + (cnt ** 2) / 2
                self.rect = self.image.get_rect(center=self.pos)

    def default_image(self, reverse=False):
        if reverse:
            self.image = pygame.image.load('pic.png')
            self.image.set_colorkey(self.image.get_at((0, 0)))
            self.image = pygame.transform.flip(self.image, True, False)
            self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
            self.rect = self.image.get_rect(center=self.pos)
        else:
            self.image = pygame.image.load('pic.png')
            self.image.set_colorkey(self.image.get_at((0, 0)))
            self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
            self.rect = self.image.get_rect(center=self.pos)

    def run(self, sp, reverse=False):
        if reverse:
            self.pos = self.pos[0] - sp, self.pos[1]
            self.rect = self.image.get_rect(center=self.pos)
        else:
            self.pos = self.pos[0] + sp, self.pos[1]
            self.rect = self.image.get_rect(center=self.pos)

    def run_animation(self, cnt, reverse=False):
        pygame.time.wait(40)
        if reverse:
            self.image = pygame.image.load(f'running_hero/run{cnt}.png')
            self.image.set_colorkey(self.image.get_at((0, 0)))
            self.image = pygame.transform.flip(self.image, True, False)
            self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
            self.rect = self.image.get_rect(center=self.pos)
        else:
            self.image = pygame.image.load(f'running_hero/run{cnt}.png')
            self.image.set_colorkey(self.image.get_at((0, 0)))
            self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
            self.rect = self.image.get_rect(center=self.pos)

    def get_back(self):
        self.pos = 30, self.pos[1]
        self.rect = self.image.get_rect(center=self.pos)