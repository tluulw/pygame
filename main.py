import pygame

from persona import Person

from wall import Wall

if __name__ == '__main__':
    pygame.init()

    pygame.display.set_caption('game')
    pygame.display.set_icon(pygame.image.load('pic.png'))

    size = width, height = 1600, 900
    screen = pygame.display.set_mode(size)

    per = Person()
    bg = pygame.transform.scale(pygame.image.load('bg.jpg'), (1600, 900))

    clock = pygame.time.Clock()

    jump_time_down = 0
    jump_time_up = 0
    jump_time = 0
    # jump_key_down = False

    all_sprites = pygame.sprite.Group()
    Wall(all_sprites)

    jump_sound = pygame.mixer.Sound("action_jump.mp3")

    running = True

    while running:
        screen.blit(bg, (0, 0, 1600, 900))
        all_sprites.draw(screen)
        screen.blit(per.image, per.rect)
        pygame.display.flip()

        all_sprites.update(per)

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
                    # jump_key_down = True
                    jump_time_down = pygame.time.get_ticks()
                    if not per.is_jump and not per.is_reverse_jump:
                        per.is_jump = True
                        jump_sound.play()

                    elif per.is_jump and not per.is_reverse_jump:
                        per.is_jump = False
                        per.jump_count = 10
                        per.jump_animation_cnt = 0
                        per.is_reverse_jump = True
                        jump_sound.play()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    jump_time_up = pygame.time.get_ticks()
                    jump_time = jump_time_down - jump_time_up
                    # jump_key_down = False
                    # print(jump_time)
        clock.tick(60)
    pygame.quit()