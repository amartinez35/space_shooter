import pygame
from game import Game

pygame.init()

pygame.display.set_caption('Play the Game')
pygame.display.set_icon(pygame.image.load('./assets/icon.png'))
screen = pygame.display.set_mode((1080, 660))

background = pygame.image.load('./assets/bg.jpg')

running = True

game = Game()
test = 0

while(running):

    if test == 0:
        test = 1
    else:
        test = 0
    
    screen.blit(background, (-100, 0))
    screen.blit(game.player.image[test], game.player.rect)
    pygame.display.flip()

    if game.pressed.get(pygame.K_UP) and game.player.rect.y > 0:
        game.player.move_up()
    elif game.pressed.get(pygame.K_DOWN) and game.player.rect.y < (screen.get_height() - game.player.rect.height):
        game.player.move_down()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()
    elif game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < (screen.get_width() - game.player.rect.width):
        game.player.move_right()
    
    if game.pressed.get(pygame.K_SPACE):
        game.player.shot()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            # if event.key == pygame.K_UP:
            #     print('vers le haut')
            #     game.player.move_up()
            # elif event.key == pygame.K_DOWN:
            #     print('vers le bas')
            #     game.player.move_down()

              