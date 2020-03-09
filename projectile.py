import pygame
#from player import Player

class Projectile(pygame.sprite.Sprite):

    def __init__(self, player, game):
        super().__init__()
        self.velocity = 15
        self.player = player
        self.image = pygame.image.load('assets/tire.png')
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 90
        self.rect.y = player.rect.y + 37
        self.game = game
    
    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        if not self.game.check_collision(self, self.game.all_monsters):
          self.rect.x += self.velocity
          if self.rect.x > 1080:
              self.remove()
        else:
          self.remove()
