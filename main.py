import pygame

from persona import Person
from wall import Wall


if __name__ == '__main__':
    pygame.init()

    pygame.display.set_caption('game')
    pygame.display.set_icon(pygame.image.load('data/pic.png'))

    size = width, height = 1600, 900
    screen = pygame.display.set_mode(size)

    bg = pygame.transform.scale(pygame.image.load('data/bg.jpg'), (1600, 900))
    bg_2 = pygame.Surface((1600, 900))
    bg_2.fill(bg.get_at((0, 0)))

    clock = pygame.time.Clock()

    walls = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()

    jump_sound = pygame.mixer.Sound("action_jump.mp3")

    def level_creator(level_name, walls, obstacles):
        level = []
        cnt = 0
        with open(f'{level_name}', encoding='UTF-8') as file:
            for i in file.readlines():
                for x in i:
                    if x == '|':
                        Wall(cnt, i.find(x), walls)
                cnt += 1

        player = Person(0)
        return player

    per = level_creator('level', walls, obstacles)

    b_d = False

    running = True

    while running:
        if -1600 >= per.screen_x or 1600 <= per.screen_x:
            per.screen_x = 0
        screen.blit(bg, (per.screen_x, 0))
        if per.screen_x < 0:
            screen.blit(bg, (per.screen_x + 1600, 0))
        else:
            screen.blit(bg, (per.screen_x - 1600, 0))
        walls.update(per)
        per.is_collide(walls, obstacles)
        walls.draw(screen)
        screen.blit(per.image, per.rect)

        if per.is_jump:
            per.if_is_jump()

        if per.is_reverse_jump:
            per.if_is_reverse_jump()

        if per.is_run or per.is_reverse_run:
            per.if_is_run()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    b_d = True
                    if not per.is_jump and not per.is_reverse_jump:
                        per.is_jump = True
                        jump_sound.play()

                    elif per.is_jump and not per.is_reverse_jump:
                        per.is_jump = False
                        per.jump_count = 10
                        per.jump_animation_cnt = 0
                        per.is_reverse_jump = True
                        per.flip = not per.flip
                        jump_sound.play()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    b_d = False
        pygame.display.flip()
        clock.tick(180)
    pygame.quit()
