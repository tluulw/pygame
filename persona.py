import pygame


class Person(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.pos = 45, 840

        self.default_image()

        self.is_run = True
        self.per_run_speed = 15
        self.run_animation_cnt = 0

        self.flip = False

        self.is_reverse_run = False

        self.is_jump = False
        self.jump_animation_cnt = 0
        self.jump_count = 10

        self.is_reverse_jump = False


    def jump_animation(self):
        pygame.time.wait(40)
        if self.jump_animation_cnt > 10:
            self.jump_animation_cnt = 10
        self.image = pygame.image.load(f'jumping_hero/jump{self.jump_animation_cnt}.png')
        self.image.set_colorkey(self.image.get_at((0, 0)))
        if self.flip:
            self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() * 1.5, self.image.get_height() * 1.5))
        self.rect = self.image.get_rect(center=self.pos)

    def jump(self):
        if self.flip:
            if self.jump_count > 0:
                self.pos = self.pos[0] - (self.jump_count ** 2) / 2, self.pos[1] - (self.jump_count ** 2) / 2
            else:
                self.pos = self.pos[0] - (self.jump_count ** 2) / 2, self.pos[1] + (self.jump_count ** 2) / 2
        else:
            if self.jump_count > 0:
                self.pos = self.pos[0] + (self.jump_count ** 2) / 2, self.pos[1] - (self.jump_count ** 2) / 2
            else:
                self.pos = self.pos[0] + (self.jump_count ** 2) / 2, self.pos[1] + (self.jump_count ** 2) / 2
        self.rect = self.image.get_rect(center=self.pos)

    def default_image(self):
        self.image = pygame.image.load('pic.png')
        self.image.set_colorkey(self.image.get_at((0, 0)))
        #if self.flip:
            #self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() * 1.5, self.image.get_height() * 1.5))
        self.rect = self.image.get_rect(center=self.pos)

    def run(self):
        if self.flip:
            self.pos = self.pos[0] - self.per_run_speed, self.pos[1]
        else:
            self.pos = self.pos[0] + self.per_run_speed, self.pos[1]
        self.rect = self.image.get_rect(center=self.pos)

    def run_animation(self):
        pygame.time.wait(40)
        self.image = pygame.image.load(f'running_hero/run{self.run_animation_cnt}.png')
        self.image.set_colorkey(self.image.get_at((0, 0)))
        if self.flip:
            self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() * 1.5, self.image.get_height() * 1.5))
        self.rect = self.image.get_rect(center=self.pos)

    def get_back(self):
        self.pos = 30, self.pos[1]
        self.rect = self.image.get_rect(center=self.pos)

    def wall_collide(self, other):
        self.image = pygame.image.load(f'hero_onthewall.png')
        self.image.set_colorkey(self.image.get_at((0, 0)))
        if self.flip:
            self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() * 1.5, self.image.get_height() * 1.5))
        self.pos = other.pos[0] + 48, self.pos[1]
        self.rect = self.image.get_rect(center=self.pos)

    def jump_landing(self):
        if self.flip:
            self.is_reverse_run = True
        else:
            self.is_run = True
        self.default_image()
        self.pos = self.pos[0], 840
        self.jump_animation_cnt = 0
        self.is_jump = False
        self.jump_count = 10

    def jump_upping(self):
        if self.jump_count % 2 == 0 and self.jump_count != -10:
            self.jump_animation_cnt += 1
            self.jump_animation()
        self.jump()
        self.jump_count -= 1

    def jump_reverse_upping(self):
        self.flip = not self.flip
        if self.jump_count % 2 == 0 and self.jump_count != -10:
            self.jump_animation_cnt += 1
            self.jump_animation()
        self.jump()
        self.jump_count -= 1
        self.flip = not self.flip

    def reverse_jump_landing(self):
        if self.flip:
            self.is_run = True
            self.flip = False
        else:
            self.is_reverse_run = True
            self.flip = True
        self.default_image()
        self.pos = self.pos[0], 840
        self.jump_animation_cnt = 0
        self.is_reverse_jump = False
        self.jump_count = 10

    def if_is_jump(self):
        self.is_run = False
        self.is_reverse_run = False
        if self.pos[1] > 840:
            self.jump_landing()
        else:
            self.jump_upping()

    def if_is_reverse_jump(self):
        self.is_run = False
        self.is_reverse_run = False
        if self.pos[1] > 840:
            self.reverse_jump_landing()
        else:
            self.jump_reverse_upping()

    def if_is_run(self):
        if self.flip:
            self.flip = True
        else:
            self.flip = False
        self.run_animation_cnt += 1
        self.run_animation_cnt %= 8
        if self.run_animation_cnt == 0:
            self.run_animation_cnt += 1
            self.run_animation_cnt %= 8
        self.run()
        self.run_animation()