import pygame
from player import Player
from monster import Monstre

class Game:

    def __init__(self):
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.pressed = {}
        self.all_monsters = pygame.sprite.Group()
        self.is_playing = False
    
    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()
        self.spawn_monster()
        self.player.rect.y = 250
        self.player.rect.x = 20

    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.health_max
        self.is_playing = False
    
    def update(self, screen):
        screen.blit(self.player.image, self.player.rect)

        self.player.update_health_bar(screen)

    # for monster in self.all_monsters:
    #     screen.blit(monster.image, monster.rect)
    #     monster.forward()

        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        for projectile in self.player.all_projectiles:
            projectile.move()

        self.player.all_projectiles.draw(screen)
        self.all_monsters.draw(screen)


        if self.pressed.get(pygame.K_UP) and self.player.rect.y > 0:
            self.player.move_up()
        elif self.pressed.get(pygame.K_DOWN) and self.player.rect.y < (screen.get_height() - self.player.rect.height):
            self.player.move_down()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        elif self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < (screen.get_width() - self.player.rect.width):
            self.player.move_right()

    def spawn_monster(self):
        monster = Monstre(self)
        self.all_monsters.add(monster)
    
    def check_collision(self, sprite1, sprites):
        return pygame.sprite.spritecollide(sprite1, sprites, False, pygame.sprite.collide_mask)