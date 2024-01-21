import pygame


class Person(pygame.sprite.Sprite):
    def __init__(self, screen_x, person, screen, *group):
        super().__init__(*group)
        self.pos = 800, 840

        self.is_run = True
        self.per_run_speed = 10
        self.run_animation_cnt = 0

        self.flip = False

        self.is_jump = False
        self.jump_animation_cnt = 0
        self.jump_count = 10

        self.is_reverse_jump = False

        self.on_the_wall = False

        self.screen_x = screen_x

        self.b_d = False

        self.on_the_floor = False
        self.floor_rect = pygame.Rect(0, 0, 0, 0)

        self.coins_collected = 0

        self.jump_particle = ''
        self.jump_particle_rect = ''
        self.jump_particle_pos = (0, 0)
        self.jump_particle_cnt = 0
        self.jump_particle_b = False

        self.screen = screen

        self.person = person

        self.default_image()

    def jump_animation(self):
        if self.person == 'samurai':
            if self.jump_animation_cnt == 13:
                self.jump_animation_cnt = 12
        elif self.person == 'hero':
            if self.jump_animation_cnt == 11:
                self.jump_animation_cnt = 10
        self.image = pygame.image.load(f'data/{self.person}/jumping_hero/jump{self.jump_animation_cnt}.png')
        self.image.set_colorkey(self.image.get_at((0, 0)))
        if self.flip:
            self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() * 1.5, self.image.get_height() * 1.5))
        self.rect = self.image.get_rect(center=self.pos)

    def jump(self):
        pygame.time.wait(10)
        if self.flip:
            if self.jump_count > 0:
                self.pos = self.pos[0], self.pos[1] - (self.jump_count ** 2) / 6
            else:
                self.pos = self.pos[0], self.pos[1] + (self.jump_count ** 2) / 6
        else:
            if self.jump_count > 0:
                self.pos = self.pos[0], self.pos[1] - (self.jump_count ** 2) / 6
            else:
                self.pos = self.pos[0], self.pos[1] + (self.jump_count ** 2) / 6
        self.per_run_speed = (self.jump_count ** 2) / 6
        self.run()
        self.per_run_speed = 10
        self.rect = self.image.get_rect(center=self.pos)

    def default_image(self):
        self.image = pygame.image.load(f'data/{self.person}/pic.png')
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
        pygame.time.wait(25)
        self.image = pygame.image.load(f'data/{self.person}/running_hero/run{self.run_animation_cnt}.png')
        self.image.set_colorkey(self.image.get_at((0, 0)))
        if self.flip:
            self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() * 1.5, self.image.get_height() * 1.5))
        self.rect = self.image.get_rect(center=self.pos)

    def wall_collide(self, other, left, right):
        if self.on_the_wall:
            if not self.rect.colliderect(self.floor_rect):
                self.pos = self.pos[0], self.pos[1] + 0.5
                self.rect = self.image.get_rect(center=self.pos)
        else:
            self.image = pygame.image.load(f'data/{self.person}/hero_onthewall.png')
            self.image.set_colorkey(self.image.get_at((0, 0)))
            if right:
                self.image = pygame.transform.flip(self.image, True, False)
            self.is_jump = False
            self.is_reverse_jump = False
            self.jump_animation_cnt = 0
            self.jump_count = 10
            if (right and self.flip) or (left and not self.flip):
                self.flip = not self.flip
            self.image = pygame.transform.scale(self.image,
                                                (self.image.get_width() * 1.5, self.image.get_height() * 1.5))
            if self.person == 'samurai':
                if left:
                    self.pos = other[0] - 20, self.pos[1]
                if right:
                    self.pos = other[0] + 20, self.pos[1]
            elif self.person == 'hero':
                self.pos = other[0], self.pos[1]
            self.rect = self.image.get_rect(center=self.pos)
            self.on_the_wall = True

    def jump_landing(self):
        if self.is_jump:
            self.is_run = True
            self.default_image()
            self.pos = self.pos[0], self.floor_rect[1] - 50
            self.jump_animation_cnt = 0
            self.is_jump = False
            self.jump_count = 10
            self.per_run_speed = 10
            self.jump_particle_cnt = 0
        else:
            self.jump_animation_cnt = 5
            self.jump_count = 0
            if self.flip:
                self.is_reverse_jump = True
            else:
                self.is_jump = True

    def jump_particle_animation(self):
        if self.jump_particle_cnt == 10:
            self.jump_particle_b = False
            return
        self.jump_particle_cnt %= 10
        self.jump_particle_cnt += 1
        self.jump_particle = pygame.image.load(f'data/jump_particles/{self.jump_particle_cnt}.png')
        if not self.flip:
            self.jump_particle = pygame.transform.flip(self.jump_particle, True, False)
        self.jump_particle = pygame.transform.scale(self.jump_particle, (self.jump_particle.get_width() * 0.25,
                                                                         self.jump_particle.get_height() * 0.25))
        self.jump_particle_rect = self.jump_particle.get_rect(center=self.jump_particle_pos)
        self.screen.blit(self.jump_particle, self.jump_particle_rect)

    def jump_upping(self):
        if self.person == 'hero':
            if self.jump_count % 2 == 0 and self.jump_count != -10:
                self.jump_animation_cnt += 1
                self.jump_animation()
        elif self.person == 'samurai':
            if self.jump_count > 0:
                if self.jump_count % 2 == 1 and self.jump_count != -10:
                    self.jump_animation_cnt += 1
                    self.jump_animation()
            else:
                if self.jump_count <= -2:
                    self.jump_animation_cnt += 1
                    self.jump_animation()
        if self.jump_particle_b:
            self.jump_particle_animation()
        self.jump()
        if self.b_d:
            self.jump_count -= 0.25
        else:
            self.jump_count -= 1

    def reverse_jump_landing(self):
        self.is_run = True
        self.default_image()
        self.pos = self.pos[0], 840
        self.jump_animation_cnt = 0
        self.is_reverse_jump = False
        self.jump_count = 10
        self.per_run_speed = 10
        self.jump_particle_cnt = 0

    def if_is_jump(self):
        self.on_the_floor = False
        self.is_run = False
        if self.pos[1] > (self.floor_rect[1] + self.floor_rect[3]):
            self.jump_landing()
        else:
            self.jump_upping()

    def if_is_reverse_jump(self):
        self.on_the_floor = False
        self.is_run = False
        if self.pos[1] > (self.floor_rect[1] + self.floor_rect[3]):
            self.reverse_jump_landing()
        else:
            self.jump_upping()

    def if_is_run(self):
        self.run_animation_cnt %= 8
        self.run_animation_cnt += 1
        self.run()
        self.run_animation()

    def floor_collide(self, other):
        if self.on_the_floor:
            self.is_run = True
        else:
            self.is_jump = False
            self.is_reverse_jump = False
            self.jump_animation_cnt = 0
            self.jump_count = 10
            self.pos = self.pos[0], other[1] - 50
            self.rect = self.image.get_rect(center=self.pos)
            self.floor_rect = other
            self.on_the_floor = True

    def kill_all(self, walls, floors, obstacles, coins):
        for sprite in walls:
            sprite.kill()
        for sprite in floors:
            sprite.kill()
        for sprite in obstacles:
            sprite.kill()
        for sprite in coins:
            sprite.kill()

    def is_collide(self, walls, floors, obstacles, coins, floor):
        if not pygame.sprite.spritecollideany(self, walls):
            self.on_the_wall = False
        if not pygame.sprite.spritecollideany(self, floors):
            self.floor_rect = floor
        if not pygame.sprite.spritecollideany(self, floors) and not self.rect.colliderect(
                floor) and not pygame.sprite.spritecollideany(self,
                                                              walls) and not self.is_jump and not self.is_reverse_jump:
            self.on_the_floor = False
            self.pos = 800, self.pos[1]
            self.jump_landing()
        for el in walls:
            if self.rect.colliderect(el.left_border):
                if not self.on_the_floor:
                    self.per_run_speed = 0
                    self.wall_collide(el.left_border, True, False)
                else:
                    self.flip = not self.flip
            elif self.rect.colliderect(el.right_border):
                if not self.on_the_floor:
                    self.per_run_speed = 0
                    self.wall_collide(el.right_border, False, True)
                else:
                    self.flip = not self.flip
            elif self.rect.colliderect(el.top_border):
                self.floor_collide(el.top_border)
        for el in floors:
            if self.rect.colliderect(el.top_border):
                self.floor_collide(el.top_border)
                if el.finish:
                    self.kill_all(walls, floors, obstacles, coins)
                    return True
                return False
            if self.rect.colliderect(el.bottom_border):
                self.jump_landing()
        for el in obstacles:
            if self.rect.colliderect(el.rect):
                self.kill_all(walls, floors, obstacles, coins)

    def person_swap(self, person):
        self.person = person
