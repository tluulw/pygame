import pygame
import button


class Menu:
    def __init__(self, size, screen):
        self.screen = screen

        self.menu_state = "main"

        self.font = pygame.font.SysFont("TimesNewRoman", 40)

        self.TEXT_COL = (255, 255, 255)

        self.play_image = pygame.image.load("data/buttons/play.png").convert_alpha()
        self.options_image = pygame.image.load("data/buttons/opt.png").convert_alpha()
        self.quit_image = pygame.image.load("data/buttons/quit.png").convert_alpha()

        self.levels_image = pygame.image.load('data/buttons/levels.png').convert_alpha()
        self.audio_image = pygame.image.load('data/buttons/play.png').convert_alpha()
        self.back_image = pygame.image.load('data/buttons/back.png').convert_alpha()

        self.play_button = button.Button(size[0] / 2 - 222, 50, self.play_image, 2)
        self.levels_button = button.Button(size[0] / 2 - 222, 300, self.levels_image, 2)
        self.options_button = button.Button(size[0] - 222, size[1] - 108, self.options_image, 1)
        self.quit_button = button.Button(0, size[1] - 108, self.quit_image, 1)

        self.audio_button = button.Button(size[0] / 2 - 222, 300, self.audio_image, 2)
        self.back_button = button.Button(size[0] / 2 - 135, 550, self.back_image, 2)

        self.lvl1_img = pygame.image.load("data/buttons/1a.png").convert_alpha()
        self.lvl1_btn = button.Button(25, 25, self.lvl1_img, 1)
        self.lvl2_img = pygame.image.load("data/buttons/2a.png").convert_alpha()
        self.lvl2_btn = button.Button(150, 25, self.lvl2_img, 1)
        self.lvl3_img = pygame.image.load("data/buttons/3a.png").convert_alpha()
        self.lvl3_btn = button.Button(275, 25, self.lvl3_img, 1)
        self.lvl4_img = pygame.image.load("data/buttons/4a.png").convert_alpha()
        self.lvl4_btn = button.Button(400, 25, self.lvl4_img, 1)
        self.lvl5_img = pygame.image.load("data/buttons/5a.png").convert_alpha()
        self.lvl5_btn = button.Button(525, 25, self.lvl5_img, 1)

    def menu_rendering1(self):
        if self.play_button.draw(self.screen):
            return 1
        if self.levels_button.draw(self.screen):
            return 103
        if self.options_button.draw(self.screen):
            return 102
        if self.quit_button.draw(self.screen):
            return 100

    def menu_rendering2(self):
        if self.audio_button.draw(self.screen):
            return 4
        if self.back_button.draw(self.screen):
            return 101

    def menu_rendering3(self):
        if self.lvl1_btn.draw(self.screen):
            return 'lvl1_btn'
        if self.lvl2_btn.draw(self.screen):
            return 'lvl2_btn'
        if self.lvl3_btn.draw(self.screen):
            return 'lvl3_btn'
        if self.lvl4_btn.draw(self.screen):
            return 'lvl4_btn'
        if self.lvl5_btn.draw(self.screen):
            return 'lvl5_btn'
        if self.back_button.draw(self.screen):
            return 101
