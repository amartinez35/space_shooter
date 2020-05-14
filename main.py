import pygame
import math
from game import Game
import os

x = 150
y = 30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

pygame.init()

pygame.display.set_caption('Play the Game')
pygame.display.set_icon(pygame.image.load('./assets/icon.png'))
screen = pygame.display.set_mode((1080, 660))

background = pygame.image.load('./assets/bg.jpg')

banner = pygame.image.load('./assets/banner.png')
#banner = pygame.transform.scale(banner, (300, 300))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 3.5)
banner_rect.y = math.ceil(screen.get_height() / 6)

play_button = pygame.image.load('./assets/play.png')
play_button = pygame.transform.scale(play_button, (200, 100))
play_button_rect = play_button.get_rect()
play_button_rect.x = screen.get_width() / 2.6
play_button_rect.y = screen.get_height() / 1.3

running = True

game = Game()
test = 0

while(running):
    
    screen.blit(background, (-100, 0))

    if game.is_playing:
        game.update(screen)
    else: 
      screen.blit(banner, banner_rect)
      screen.blit(play_button, play_button_rect)
        
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.shot()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()

              