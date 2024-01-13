import pygame
import random

pygame.init()
window = pygame.display.set_mode((1300,970))
blue = (0,0,255)
back_a = 0
class back:
    back_play = pygame.image.load('images/BG_03.png')
    back_play2 = pygame.image.load('images/BG_032.png')
    back_menu = pygame.image.load('images/BG_04.png')
    x = 0
    y = 0

button_play_one = pygame.image.load('images/button_play.jpg')
butoon_one_rect = button_play_one.get_rect(topleft=(312,370))
pause_button = pygame.image.load('images/pause.png')
pause_rect = pause_button.get_rect(topleft=(1150,0))

back = back()
menu = True
pause = False
run_player1 = False
run_player2 = False
while menu:
    window.blit(back.back_menu,(0,0))
    window.blit(button_play_one,(312,370))



    mouse = pygame.mouse.get_pos()
    if butoon_one_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
        pause = True
        run_player1 = True

    while pause:

        

        while run_player1:
            window.blit(back.back_play,(back.x,0))
            window.blit(pause_button, (1150, 0))
            window.blit(back.back_play2,(back.x + 1170,0))
            back.x -= 5
            if back.x == -1300:
                back.x = 0

            mouse = pygame.mouse.get_pos()
            if pause_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                run_player1 = False



            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     run_player1 = False

        while run_player2:



            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu = False

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False

pygame.quit()