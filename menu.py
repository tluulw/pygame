import pygame

import button


class Menu:
    def __init__(self, size, screen):
        self.screen = screen

        self.menu_state = "main"

        self.font = pygame.font.SysFont("TimesNewRoman", 40)

        self.TEXT_COL = (255, 255, 255)

        self.play_image = pygame.image.load("data/buttons/play.png")
        self.play_image.set_colorkey(self.play_image.get_at((0, 0)))

        self.options_image = pygame.image.load("data/buttons/menu.png")
        self.options_image.set_colorkey(self.options_image.get_at((0, 0)))

        self.quit_image = pygame.image.load("data/buttons/stop.png")
        self.quit_image.set_colorkey(self.quit_image.get_at((0, 0)))

        self.audio_image = pygame.image.load('data/buttons/play.png').convert_alpha()

        self.back_image = pygame.image.load('data/buttons/back.png')
        self.back_image.set_colorkey(self.back_image.get_at((0, 0)))

        self.play_button = button.Button(size[0] / 2 - 250, 300, self.play_image, 1)
        self.options_button = button.Button(size[0] - 250, size[1] - 79, self.options_image, 0.5)
        self.quit_button = button.Button(0, size[1] - 102, self.quit_image, 0.5)

        self.audio_button = button.Button(size[0] / 2 - 222, 300, self.audio_image, 2)
        self.back_button = button.Button(size[0] / 2 - 163, 550, self.back_image, 0.5)

        self.lvl1_img = pygame.image.load("data/buttons/1a.png")
        self.lvl1_img.set_colorkey(self.lvl1_img.get_at((0, 0)))
        self.lvl1_btn = button.Button(535, 25, self.lvl1_img, 0.75)

        self.lvl2_img = pygame.image.load("data/buttons/2a.png")
        self.lvl2_img.set_colorkey(self.lvl2_img.get_at((0, 0)))
        self.lvl2_btn = button.Button(671, 25, self.lvl2_img, 0.75)

        self.lvl3_img = pygame.image.load("data/buttons/3a.png")
        self.lvl3_img.set_colorkey(self.lvl3_img.get_at((0, 0)))
        self.lvl3_btn = button.Button(882, 25, self.lvl3_img, 0.75)

    def menu_rendering1(self):
        if self.play_button.draw(self.screen):
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
        if self.back_button.draw(self.screen):
            return 101

    def menu_rendering4(self):
        pass