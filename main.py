import pygame

from persona import Person

if __name__ == '__main__':
    pygame.init()

    pygame.display.set_caption('game')
    pygame.display.set_icon(pygame.image.load('pic.png'))

    size = width, height = 1600, 900
    screen = pygame.display.set_mode(size)

    per = Person()
    bg = pygame.transform.scale(pygame.image.load('bg.jpg'), (1600, 900))

    clock = pygame.time.Clock()

    is_run = True
    per_run_speed = 15
    run_animation = 0

    hero_flipped = False

    is_reverse_run = False

    is_jump = False
    jump_animation_cnt = 0
    jump_count = 10

    is_reverse_jump = False

    jump_time_down = 0
    jump_time_up = 0
    jump_time = 0

    running = True

    while running:

        screen.blit(bg, (0, 0, 1600, 900))
        screen.blit(per.image, per.rect)
        pygame.display.flip()

        if is_jump:
            is_run = False
            is_reverse_run = False
            if hero_flipped:
                if jump_count >= -10:
                    if jump_count % 2 == 0 and jump_count != -10:
                        jump_animation_cnt += 1
                        per.jump_animation(jump_animation_cnt, True)
                    per.jump(jump_count, True)
                    jump_count -= 1
                else:
                    is_reverse_run = True
                    per.default_image(True)
                    per.pos = per.pos[0], 819
                    jump_animation_cnt = 0
                    is_jump = False
                    jump_count = 10
            else:
                if jump_count >= -10:
                    if jump_count % 2 == 0 and jump_count != -10:
                        jump_animation_cnt += 1
                        per.jump_animation(jump_animation_cnt)
                    per.jump(jump_count)
                    jump_count -= 1
                else:
                    is_run = True
                    per.default_image()
                    per.pos = per.pos[0], 819
                    jump_animation_cnt = 0
                    is_jump = False
                    jump_count = 10

        if is_reverse_jump:
            is_reverse_run = False
            is_run = False
            if hero_flipped:
                if per.pos[1] >= 819:
                    per.default_image()
                    per.pos = per.pos[0], 819
                    jump_animation_cnt = 0
                    is_reverse_jump = False
                    jump_count = 10
                    is_run = True
                    hero_flipped = False
                else:
                    if jump_count % 2 == 0 and jump_count != -10:
                        jump_animation_cnt += 1
                        per.jump_animation(jump_animation_cnt)
                    per.jump(jump_count)
                    jump_count -= 1
            else:
                if per.pos[1] >= 819:
                    per.default_image()
                    per.pos = per.pos[0], 819
                    jump_animation_cnt = 0
                    is_reverse_jump = False
                    jump_count = 10
                    is_reverse_run = True
                    hero_flipped = True
                else:
                    if jump_count % 2 == 0 and jump_count != -10:
                        jump_animation_cnt += 1
                        per.jump_animation(jump_animation_cnt, True)
                    per.jump(jump_count, True)
                    jump_count -= 1

        if is_run:
            hero_flipped = False
            run_animation += 1
            run_animation %= 8
            if run_animation == 0:
                run_animation += 1
                run_animation %= 8
            per.run(per_run_speed)
            per.run_animation(run_animation)

        if is_reverse_run:
            is_run = False
            hero_flipped = True
            run_animation += 1
            run_animation %= 8
            if run_animation == 0:
                run_animation += 1
                run_animation %= 8
            per.run(per_run_speed, True)
            per.run_animation(run_animation, True)

        if per.pos[0] >= 1600:
            per.get_back()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jump_time_down = pygame.time.get_ticks()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    jump_time_up = pygame.time.get_ticks()
                    jump_time = jump_time_down - jump_time_up
                    if not is_jump and not is_reverse_jump:
                        is_jump = True
                    elif is_jump and not is_reverse_jump:
                        is_jump = False
                        jump_count = 10
                        jump_animation_cnt = 0
                        is_reverse_jump = True
        clock.tick(60)
    pygame.quit()
