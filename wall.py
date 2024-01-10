import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.pos = 200, 600
        self.image = pygame.image.load('walls/default_wall.png')
        self.rect = self.image.get_rect(center=self.pos)

    def update(self, per):
        if self.rect.collidepoint(per.pos):
            if per.is_jump:
                per.is_jump = False
                per.jump_animation_cnt = 0
                per.jump_count = 10
            else:
                per.is_reverse_jump = False
                per.jump_animation_cnt = 0
                per.jump_count = 10
            per.flip = False
            per.wall_collide(self)