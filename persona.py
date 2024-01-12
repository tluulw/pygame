import pygame


class Person(pygame.sprite.Sprite):
    def __init__(self, screen_x, *group):
        super().__init__(*group)
        self.pos = 800, 840

        self.is_run = True
        self.per_run_speed = 10
        self.run_animation_cnt = 0

        self.flip = False

        self.is_reverse_run = False

        self.is_jump = False
        self.jump_animation_cnt = 0
        self.jump_count = 10

        self.is_reverse_jump = False

        self.on_the_wall = False

        self.wall = False

        self.screen_x = screen_x

        self.default_image()

    def jump_animation(self):
        pygame.time.wait(40)
        if self.jump_animation_cnt > 10:
            self.jump_animation_cnt = 10
        self.image = pygame.image.load(f'data/jumping_hero/jump{self.jump_animation_cnt}.png')
        self.image.set_colorkey(self.image.get_at((0, 0)))
        if self.flip:
            self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() * 1.5, self.image.get_height() * 1.5))
        self.rect = self.image.get_rect(center=self.pos)

    def jump(self):
        if self.flip:
            if self.jump_count > 0:
                self.pos = self.pos[0], self.pos[1] - (self.jump_count ** 2) / 2
            else:
                self.pos = self.pos[0], self.pos[1] + (self.jump_count ** 2) / 2
        else:
            if self.jump_count > 0:
                self.pos = self.pos[0], self.pos[1] - (self.jump_count ** 2) / 2
            else:
                self.pos = self.pos[0], self.pos[1] + (self.jump_count ** 2) / 2
        self.per_run_speed = (self.jump_count ** 2) / 2
        self.run()
        self.per_run_speed = 12
        self.rect = self.image.get_rect(center=self.pos)

    def default_image(self):
        self.image = pygame.image.load('data/pic.png')
        self.image.set_colorkey(self.image.get_at((0, 0)))
        if self.flip:
            self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() * 1.5, self.image.get_height() * 1.5))
        self.pos = self.pos[0], 840
        self.rect = self.image.get_rect(center=self.pos)

    def run(self):
        if self.flip:
            self.screen_x += self.per_run_speed
        else:
            self.screen_x -= self.per_run_speed

    def run_animation(self):
        pygame.time.wait(40)
        self.image = pygame.image.load(f'data/running_hero/run{self.run_animation_cnt}.png')
        self.image.set_colorkey(self.image.get_at((0, 0)))
        if self.flip:
            self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() * 1.5, self.image.get_height() * 1.5))
        self.rect = self.image.get_rect(center=self.pos)

    def get_back(self):
        self.pos = 30, self.pos[1]
        self.rect = self.image.get_rect(center=self.pos)

    def wall_collide(self, other, left, right):
        if self.on_the_wall:
            if self.pos[1] < 840:
                pygame.time.wait(20)
                self.pos = self.pos[0], self.pos[1] + 0.5
                self.rect = self.image.get_rect(center=self.pos)
        else:
            self.image = pygame.image.load('data/hero_onthewall.png')
            self.image.set_colorkey(self.image.get_at((0, 0)))
            if right:
                self.image = pygame.transform.flip(self.image, True, False)
            self.is_jump = False
            self.is_reverse_jump = False
            self.jump_animation_cnt = 0
            self.jump_count = 10
            self.flip = not self.flip
            self.image = pygame.transform.scale(self.image,
                                                (self.image.get_width() * 1.5, self.image.get_height() * 1.5))
            self.pos = other[0], self.pos[1]
            self.rect = self.image.get_rect(center=self.pos)
            self.on_the_wall = True

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
        self.per_run_speed = 10

    def jump_upping(self):
        if self.jump_count % 2 == 0 and self.jump_count != -10:
            self.jump_animation_cnt += 1
            self.jump_animation()
        self.jump()
        self.jump_count -= 1

    def jump_reverse_upping(self):
        if self.jump_count % 2 == 0 and self.jump_count != -10:
            self.jump_animation_cnt += 1
            self.jump_animation()
        self.jump()
        self.jump_count -= 1

    def reverse_jump_landing(self):
        if self.flip:
            self.is_reverse_run = True
        else:
            self.is_run = True
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
        self.run_animation_cnt += 1
        self.run_animation_cnt %= 8
        if self.run_animation_cnt == 0:
            self.run_animation_cnt += 1
            self.run_animation_cnt %= 8
        self.run()
        self.run_animation()

    def is_collide(self, walls, obstacles):
        if not pygame.sprite.spritecollideany(self, walls):
            self.on_the_wall = False
        for el in walls:
            sp = [self.is_jump, self.is_reverse_jump, self.is_run, self.is_reverse_run]
            if self.rect.colliderect(el.left_border):
                self.per_run_speed = 0
                self.wall_collide(el.left_border, True, False)
            elif self.rect.colliderect(el.right_border):
                self.per_run_speed = 0
                self.wall_collide(el.right_border, False, True)
            elif not self.on_the_wall and not any(sp) and self.pos[1] < 840:
                self.flip = not self.flip
                self.jump_landing()