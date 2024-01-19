from random import randint

import pygame


class Coin(pygame.sprite.Sprite):
    def __init__(self, y, x, *group):
        super().__init__(*group)
        self.pos = x * 40, y * 180
        self.image = pygame.image.load('data/coins/coin1.png')
        self.image.set_colorkey(self.image.get_at((0, 0)))
        self.image = pygame.transform.scale2x(self.image)
        self.rect = pygame.Rect(randint(self.pos[0], self.pos[0] + 200),
                                self.pos[1] - self.image.get_height(), self.image.get_width(),
                                self.image.get_height())

        self.animation_cnt = 1
        self.coin_collected_sound = pygame.mixer.Sound("data/coin_collected.mp3")
        self.coin_collected_sound.set_volume(0.2)

    def update(self, per, obs):
        for o in obs:
            if self.rect.colliderect(o.rect):
                self.kill()
        self.animation_cnt %= 9
        self.animation_cnt += 1
        self.image = pygame.image.load(f'data/coins/coin{self.animation_cnt}.png')
        self.image = pygame.transform.scale2x(self.image)
        self.image.set_colorkey(self.image.get_at((0, 0)))
        if per.flip:
            self.rect = pygame.Rect(self.rect[0] + per.per_run_speed,
                                    self.pos[1] - self.image.get_height(), self.image.get_width(),
                                    self.image.get_height())
        else:
            self.rect = pygame.Rect(self.rect[0] - per.per_run_speed,
                                    self.pos[1] - self.image.get_height(), self.image.get_width(),
                                    self.image.get_height())
        if per.rect.colliderect(self.rect):
            per.coins_collected += 1
            self.coin_collected_sound.play()
            self.kill()