import pygame
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

running = True

game = Game()
test = 0

while(running):
    
    screen.blit(background, (-100, 0))
    screen.blit(game.player.image, game.player.rect)

    for monster in game.all_monsters:
        screen.blit(monster.image, monster.rect)
        monster.forward()


    for projectile in game.player.all_projectiles:
        projectile.move()

    game.player.all_projectiles.draw(screen)



    if game.pressed.get(pygame.K_UP) and game.player.rect.y > 0:
        game.player.move_up()
    elif game.pressed.get(pygame.K_DOWN) and game.player.rect.y < (screen.get_height() - game.player.rect.height):
        game.player.move_down()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()
    elif game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < (screen.get_width() - game.player.rect.width):
        game.player.move_right()
    
    # if game.pressed.get(pygame.K_SPACE):
    #     game.player.shot()
        
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

              