import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
import button


class Menu:
    def __init__(self, size, screen):
        self.screen = screen

        self.menu_state = "main"

        self.font = pygame.font.Font("data/ARCADEPI.TTF", 100)
        self.small_font = pygame.font.Font("data/ARCADEPI.TTF", 50)

        self.TEXT_COL = (255, 215, 0)

        self.game_over = self.font.render('GAME OVER!', False, self.TEXT_COL)
        self.game_over_rect = (
            size[0] / 2 - self.game_over.get_width() / 2, 100, self.game_over.get_width(), self.game_over.get_height())

        self.your_score = self.font.render('YOUR SCORE:', False, self.TEXT_COL)
        self.your_score_rect = (
            size[0] / 2 - self.your_score.get_width() / 2, 250, self.your_score.get_width(),
            self.your_score.get_height())

        self.score = self.font.render('', False, self.TEXT_COL)
        self.score_rect = (
            size[0] / 2 + self.your_score.get_width() / 2, 250, self.score.get_width(),
            self.score.get_height())

        self.your_coins = self.font.render('YOUR COINS:', False, self.TEXT_COL)
        self.your_coins_rect = (
            size[0] / 2 - self.your_coins.get_width() / 2, 350, self.your_coins.get_width(),
            self.your_coins.get_height())

        self.coins = self.font.render('', False, self.TEXT_COL)
        self.coins_rect = (
            size[0] / 2 + self.your_coins.get_width() / 2, 350, self.coins.get_width(),
            self.coins.get_height())

        self.play_image = pygame.image.load("data/buttons/play.png")
        self.play_image.set_colorkey(self.play_image.get_at((0, 0)))

        self.options_image = pygame.image.load("data/buttons/menu.png")
        self.options_image.set_colorkey(self.options_image.get_at((0, 0)))

        self.quit_image = pygame.image.load("data/buttons/stop.png")
        self.quit_image.set_colorkey(self.quit_image.get_at((0, 0)))

        self.heroes_image = pygame.image.load("data/buttons/heroes.png")
        self.heroes_image.set_colorkey(self.heroes_image.get_at((0, 0)))

        self.music_slider = Slider(screen, size[0] / 2 - 400, 50, 800, 40, min=0, max=100, step=1)
        self.music_text_edit = TextBox(screen, size[0] / 2 - 50, 150, 100, 50, fontSize=30)
        self.music_text_edit.disable()

        self.sound_slider = Slider(screen, size[0] / 2 - 400, 300, 800, 40, min=0, max=100, step=1)
        self.sound_text_edit = TextBox(screen, size[0] / 2 - 50, 400, 100, 50, fontSize=30)
        self.sound_text_edit.disable()

        self.back_image = pygame.image.load('data/buttons/back.png')
        self.back_image.set_colorkey(self.back_image.get_at((0, 0)))

        self.pause_image = pygame.image.load('data/buttons/pause.png')
        self.pause_image.set_colorkey(self.pause_image.get_at((0, 0)))

        self.pause_button = button.Button(0, 0, self.pause_image, 0.5)

        self.coins_now = self.small_font.render('COINS:', False, self.TEXT_COL)
        self.coins_now_rect = (
            1450 - self.coins_now.get_width(), 100, self.coins_now.get_width(),
            self.coins_now.get_height())

        self.score_now = self.small_font.render('SCORE:', False, self.TEXT_COL)
        self.score_now_rect = (
            1450 - self.score_now.get_width(), 0, self.score_now.get_width(),
            self.score_now.get_height())

        self.coins_now_cnt = self.small_font.render('', False, self.TEXT_COL)
        self.coins_now_cnt_rect = (
            1600 - self.coins_now_cnt.get_width(), 100, self.coins_now_cnt.get_width(),
            self.coins_now_cnt.get_height())

        self.score_now_cnt = self.small_font.render('', False, self.TEXT_COL)
        self.score_now_cnt_rect = (
            1600 - self.score_now_cnt.get_width(), 0, self.score_now_cnt.get_width(),
            self.score_now_cnt.get_height())

        self.play_button = button.Button(size[0] / 2 - 250, 300, self.play_image, 1)

        self.play_button_game = button.Button(size[0] / 2 - 125, 300, self.play_image, 0.5)

        self.menu_button = button.Button(size[0] / 2 - 125, 400, self.options_image, 0.5)

        self.to_main_button = button.Button(size[0] / 2 - 125, 675, self.back_image, 0.38)

        self.main_button = button.Button(size[0] / 2 - 125, 675, self.back_image, 0.38)

        self.options_button = button.Button(size[0] - 250, size[1] - 79, self.options_image, 0.5)

        self.quit_button = button.Button(0, size[1] - 102, self.quit_image, 0.5)

        self.heroes_button = button.Button(size[0] / 2 - 187.5, 500, self.heroes_image, 0.75)

        self.back_button = button.Button(size[0] / 2 - 163, 675, self.back_image, 0.5)

        self.lvl1_img = pygame.image.load("data/buttons/1a.png")
        self.lvl1_img.set_colorkey(self.lvl1_img.get_at((0, 0)))
        self.lvl1_btn = button.Button(535, 25, self.lvl1_img, 0.75)

        self.lvl2_img = pygame.image.load("data/buttons/2a.png")
        self.lvl2_img.set_colorkey(self.lvl2_img.get_at((0, 0)))
        self.lvl2_btn = button.Button(671, 25, self.lvl2_img, 0.75)

        self.lvl3_img = pygame.image.load("data/buttons/3a.png")
        self.lvl3_img.set_colorkey(self.lvl3_img.get_at((0, 0)))
        self.lvl3_btn = button.Button(882, 25, self.lvl3_img, 0.75)

        self.hero_default_img = pygame.image.load("data/hero/pic.png")
        self.hero_default_img.set_colorkey(self.hero_default_img.get_at((0, 0)))
        self.hero_default_btn = button.Button(400, 50, self.hero_default_img, 2)

        self.hero_samurai_img = pygame.image.load("data/samurai/pic.png")
        self.hero_samurai_img.set_colorkey(self.hero_default_img.get_at((0, 0)))
        self.hero_samurai_btn = button.Button(510, 50, self.hero_samurai_img, 2)

    def main_menu_rendering1(self):
        if self.play_button.draw(self.screen):
            return 'levels'
        if self.options_button.draw(self.screen):
            return 'options'
        if self.heroes_button.draw(self.screen):
            return 'heroes'
        if self.quit_button.draw(self.screen):
            return 'quit'

    def options_menu_rendering2(self, events):
        if self.back_button.draw(self.screen):
            return 'back'
        self.music_text_edit.setText(self.music_slider.getValue())
        self.sound_text_edit.setText(self.sound_slider.getValue())
        pygame_widgets.update(events)
        return self.music_slider.getValue(), self.sound_slider.getValue()

    def play_menu_rendering3(self):
        if self.lvl1_btn.draw(self.screen):
            return 'lvl1_btn'
        if self.lvl2_btn.draw(self.screen):
            return 'lvl2_btn'
        if self.lvl3_btn.draw(self.screen):
            return 'lvl3_btn'
        if self.back_button.draw(self.screen):
            return 'back'

    def heroes_menu_rendering4(self):
        if self.hero_default_btn.draw(self.screen):
            return 'per_default'
        if self.hero_samurai_btn.draw(self.screen):
            return 'per_samurai'
        if self.back_button.draw(self.screen):
            return 'back'

    def game_rendering(self, coins, score):
        if self.pause_button.draw(self.screen):
            return 'paused'
        self.screen.blit(self.coins_now, self.coins_now_rect)
        self.screen.blit(self.score_now, self.score_now_rect)

        self.coins_now_cnt = self.small_font.render(f'{coins}', False, self.TEXT_COL)
        self.coins_now_cnt_rect = (
            1600 - self.coins_now_cnt.get_width(), 100, self.coins_now_cnt.get_width(),
            self.coins_now_cnt.get_height())

        self.score_now_cnt = self.small_font.render(f'{score}', False, self.TEXT_COL)
        self.score_now_cnt_rect = (
            1600 - self.score_now_cnt.get_width(), 0, self.score_now_cnt.get_width(),
            self.score_now_cnt.get_height())

        self.screen.blit(self.coins_now_cnt, self.coins_now_cnt_rect)
        self.screen.blit(self.score_now_cnt, self.score_now_cnt_rect)

    def pause_rendering(self):
        if self.play_button_game.draw(self.screen):
            return 'resume'
        if self.menu_button.draw(self.screen):
            return 'options'
        if self.to_main_button.draw(self.screen):
            return 'menu'

    def game_over_rendering(self, score, coins):
        self.screen.blit(self.game_over, self.game_over_rect)

        self.screen.blit(self.your_score, self.your_score_rect)

        self.screen.blit(self.your_coins, self.your_coins_rect)

        self.score = self.font.render(f'{score}', False, self.TEXT_COL)

        self.score_rect = (
            800 + self.your_score.get_width() / 2, 250, self.score.get_width(),
            self.score.get_height())

        self.screen.blit(self.score, self.score_rect)

        self.coins = self.font.render(f'{coins}', False, self.TEXT_COL)

        self.coins_rect = (
            800 + self.your_coins.get_width() / 2, 350, self.coins.get_width(),
            self.coins.get_height())

        self.screen.blit(self.coins, self.coins_rect)

        if self.quit_button.draw(self.screen):
            return 'quit'

        if self.main_button.draw(self.screen):
            return 'main'
