import sqlite3

import pygame.mixer

from coins import Coin
from floor import Floor
from menu import Menu
from persona import Person
from spike import Spike
from wall import Wall
from win_flag import WinFlag

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1600, 900
    screen = pygame.display.set_mode(size)

    bg = pygame.transform.scale(pygame.image.load('data/bg.jpg'), (1600, 900))
    bg_day = pygame.transform.scale(pygame.image.load('data/bg_day.jpg'), (1600, 900))

    clock = pygame.time.Clock()

    walls = pygame.sprite.Group()
    floors = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    win_flag = pygame.sprite.Group()

    jump_sound = pygame.mixer.Sound("data/action_jump.mp3")
    pygame.mixer.music.load("data/bg_music.mp3")
    game_over_sound = pygame.mixer.Sound("data/game_over_sound.mp3")
    game_over_sound.set_volume(0.2)

    vol = 0.5
    pygame.mixer.music.set_volume(vol)
    pygame.mixer.music.play(-1)


    def kill_all():
        for sprite in walls:
            sprite.kill()
        for sprite in floors:
            sprite.kill()
        for sprite in obstacles:
            sprite.kill()
        for sprite in coins:
            sprite.kill()
        for sprite in win_flag:
            sprite.kill()


    per = Person(0, 'hero', screen)


    def level_creator(level_name):
        cnt = 0
        with open(f'{level_name}', encoding='UTF-8') as file:
            for i in file.readlines():
                for x in i:
                    if x == '|':
                        Wall(cnt, i.find(x), walls)
                        if i[i.find(x) + 1] == '*':
                            continue
                        i = i.replace(x, '.', 1)
                    if x == '_':
                        Coin(cnt, i.find(x), coins)
                        Floor(cnt, i.find(x), False, floors)
                        i = i.replace(x, '.', 1)
                    if x == '*':
                        if i[i.find(x) + 1] == '|':
                            Spike(cnt, i.find(x), True, 90, False, obstacles)
                        elif i[i.find(x) - 1] == '|':
                            Spike(cnt, i.find(x), True, 270, False, obstacles)
                            i = i.replace('|', '.', 1)
                        else:
                            Spike(cnt, i.find(x), False, 0, True, obstacles)
                        i = i.replace(x, '.', 1)
                    if x == '!':
                        WinFlag(cnt, i.find(x), win_flag)
                        i = i.replace(x, '.', 1)
                cnt += 1
        return level_name


    game_menu = True
    block_hotkey = 0
    change_tab = 'main'
    btn_tab = ''
    level = level_creator('data/levels/level.txt')
    menu = Menu(size, screen)

    completed = False

    heroes = ['hero', 'samurai']
    hero_cnt = 0

    sounds = [jump_sound]

    floor = pygame.Rect(0, 895, 1600, 5)

    running = True

    while running:
        events = pygame.event.get()
        if change_tab == 'pause':
            per.per_run_speed = 0
            per.is_run = False
            if per.is_jump:
                per.is_jump = False
            if per.is_reverse_jump:
                per.is_reverse_jump = False

        if not (any((walls, obstacles, floors, coins))):
            if (level[17:][:1] == '1' or level[17:][:1] == '2' or level[17:][:1] == '3') and not completed:
                with sqlite3.connect('game_data.db') as con:
                    cur = con.cursor()
                    cur.execute(
                        f"""INSERT INTO results (level, coins, goal) VALUES ('{level[17:][:1]}', 
                        '{per.coins_collected}', 'failed')""")
                    con.commit()
                change_tab = 'game_over'
                level = level_creator('data/levels/level.txt')
                game_over_sound.play()
            elif (level[17:][:1] == '1' or level[17:][:1] == '2' or level[17:][:1] == '3') and completed:
                with sqlite3.connect('game_data.db') as con:
                    cur = con.cursor()
                    cur.execute(
                        f"""INSERT INTO results (level, coins, goal) VALUES ('{level[17:][:1]}', 
                        '{per.coins_collected}', 'completed')""")
                    con.commit()
                change_tab = 'win'
                completed = False
                level = level_creator('data/levels/level.txt')

        if per.rect.colliderect(floor) and not game_menu and per.screen_x != 0:
            kill_all()

        if per.on_the_floor:
            if per.pos[0] <= 800 - 12:
                per.pos = per.pos[0] + 12, per.pos[1]

            elif per.pos[0] >= 800 + 12:
                per.pos = per.pos[0] - 12, per.pos[1]

        if -1600 >= per.screen_x or 1600 <= per.screen_x:
            per.screen_x = 0

        screen.blit(bg, (per.screen_x, 0))

        if per.screen_x < 0:
            screen.blit(bg, (per.screen_x + 1600, 0))
        else:
            screen.blit(bg, (per.screen_x - 1600, 0))

        if change_tab != 'pause' and change_tab != 'options':
            walls.update(per)
            floors.update(per)
            obstacles.update(per)
            win_flag.update(per)
            coins.update(per, obstacles)
            if per.is_collide(walls, floors, obstacles, coins, floor, win_flag):
                completed = True

        walls.draw(screen)
        floors.draw(screen)
        obstacles.draw(screen)
        coins.draw(screen)
        win_flag.draw(screen)
        screen.blit(per.image, per.rect)

        if change_tab == 'pause':

            btn_tab = menu.pause_rendering()

            if btn_tab == 'resume':
                per.per_run_speed = 10
                per.is_run = True
                change_tab = 'game'

            if btn_tab == 'menu':
                kill_all()
                level = level_creator('data/levels/level.txt')
                per.per_run_speed = 10
                per.is_run = True
                change_tab = 'main'
                game_menu = True

            if btn_tab == 'options':
                change_tab = 'options'

        if change_tab == 'options':

            btn_tab = menu.options_menu_rendering2(events)

            if btn_tab != 'back':
                vol = btn_tab[0] / 100
                pygame.mixer.music.set_volume(vol)
                for sound in sounds:
                    sound.set_volume(btn_tab[1] / 100)
            else:
                change_tab = 'pause'

        if per.is_jump:
            per.if_is_jump()

        if per.is_reverse_jump:
            per.if_is_reverse_jump()

        if per.is_run:
            per.if_is_run()

        if change_tab == 'game':
            btn_tab = menu.game_rendering(per.coins_collected)

        if btn_tab == 'paused':
            change_tab = 'pause'

        if change_tab == 'game_over':
            with sqlite3.connect('game_data.db') as con:
                cur = con.cursor()
                y_c = cur.execute(
                    f"""SELECT coins FROM results""").fetchall()
                y_c = [int(el) for el in y_c[-1]]
            btn_tab = menu.game_over_rendering(y_c)

        if change_tab == 'win':
            with sqlite3.connect('game_data.db') as con:
                cur = con.cursor()
                y_c = cur.execute(
                    f"""SELECT coins FROM results""").fetchall()
                y_c = [int(el) for el in y_c[-1]]
            btn_tab = menu.win(y_c)

        if btn_tab == 'main':
            game_menu = True
            change_tab = 'main'
            block_hotkey = 0
            per.coins_collected = 0

        if btn_tab == 'quit':
            game_menu = True
            block_hotkey = 0
            per.coins_collected = 0

        if game_menu:
            if change_tab == 'main':
                per.person_swap(heroes[hero_cnt])
                level = level_creator('data/levels/level.txt')
                per.coins_collected = 0
                per.flip = False
                btn_tab = menu.main_menu_rendering1()
            if change_tab == 'options':
                btn_tab = menu.options_menu_rendering2(events)
                if btn_tab != 'back':
                    vol = btn_tab[0] / 100
                    pygame.mixer.music.set_volume(vol)
                    for sound in sounds:
                        sound.set_volume(btn_tab[1] / 100)
            if change_tab == 'levels':
                btn_tab = menu.play_menu_rendering3()
            if change_tab == 'heroes':
                btn_tab = menu.select_rendering(heroes[hero_cnt])

            if btn_tab == 'quit':
                running = False

            if btn_tab == 'options':
                change_tab = 'options'

            if btn_tab == 'back':
                change_tab = 'main'

            if btn_tab == 'levels':
                change_tab = 'levels'

            if btn_tab == 'select':
                change_tab = 'heroes'

            if btn_tab == 'left':
                hero_cnt -= 1
                if hero_cnt == -1:
                    hero_cnt = 1

            if btn_tab == 'right':
                hero_cnt += 1
                if hero_cnt == 2:
                    hero_cnt = 0

            if btn_tab == 'lvl1_btn':
                per.screen_x = 0
                per.pos = per.pos[0], 600
                level = level_creator('data/levels/level1.txt')
                sounds = [jump_sound, game_over_sound]
                for el in coins:
                    sounds.append(el.coin_collected_sound)
                for el in win_flag:
                    sounds.append(el.win_sound)
                for el in sounds:
                    el.set_volume(menu.sound_slider.getValue())
                pygame.mixer.music.set_volume(menu.music_slider.getValue())
                game_menu = False
                change_tab = 'game'
                block_hotkey = 1
            if btn_tab == 'lvl2_btn':
                per.screen_x = 0
                per.pos = per.pos[0], 600
                level = level_creator('data/levels/level2.txt')
                sounds = [jump_sound, game_over_sound]
                for el in coins:
                    sounds.append(el.coin_collected_sound)
                for el in win_flag:
                    sounds.append(el.win_sound)
                for el in sounds:
                    el.set_volume(menu.sound_slider.getValue())
                pygame.mixer.music.set_volume(menu.music_slider.getValue())
                game_menu = False
                change_tab = 'game'
                block_hotkey = 1
            if btn_tab == 'lvl3_btn':
                per.screen_x = 0
                per.pos = per.pos[0], 600
                level = level_creator('data/levels/level3.txt')
                sounds = [jump_sound, game_over_sound]
                for el in coins:
                    sounds.append(el.coin_collected_sound)
                for el in win_flag:
                    sounds.append(el.win_sound)
                for el in sounds:
                    el.set_volume(menu.sound_slider.getValue())
                pygame.mixer.music.set_volume(menu.music_slider.getValue())
                game_menu = False
                change_tab = 'game'
                block_hotkey = 1

        for event in events:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and block_hotkey == 1:
                if event.key == pygame.K_ESCAPE:
                    if change_tab == 'game':
                        change_tab = 'pause'
                    elif change_tab == 'pause':
                        btn_tab = 'resume'
                elif event.key == pygame.K_SPACE:
                    j_s = per.screen_x
                    per.b_d = True
                    if not per.is_jump and not per.is_reverse_jump:
                        per.jump_particle_cnt = 0
                        per.jump_particle_b = True
                        per.jump_particle_pos = per.pos
                        per.is_jump = True
                        jump_sound.play()

                    elif per.is_jump and not per.is_reverse_jump:
                        per.jump_particle_cnt = 0
                        per.jump_particle_b = True
                        per.jump_particle_pos = per.pos
                        per.is_jump = False
                        per.jump_count = 10
                        per.jump_animation_cnt = 0
                        per.is_reverse_jump = True
                        per.flip = not per.flip
                        jump_sound.play()
            if event.type == pygame.KEYUP and block_hotkey == 1:
                if event.key == pygame.K_SPACE:
                    j_e = per.screen_x
                    per.b_d = False
        pygame.display.flip()
        clock.tick(60)
pygame.quit()
