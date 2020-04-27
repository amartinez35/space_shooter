import pygame
import random

class Monstre(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        #self.image = {}
        self.health = 100
        self.health_max = 100
        self.attack = 10
        self.velocity = 1
        self.image = pygame.image.load('assets/ufo.png')
        #self.image[1] = pygame.image.load('assets/ufo_2.png')
        self.rect = self.image.get_rect()        
        self.rect.y = 250 + random.randint(0, 300)
        self.rect.x = 1000
        self.game = game
    
    def damage(self, amount):
        self.health -= amount
        
        if self.health <=0:
            self.image = pygame.image.load('assets/explosion.png')
            self.game.all_monsters.remove(self)

    def update_health_bar(self, surface):
        #def couleur
        bar_color = (111, 210, 4)
        bar_color_background = (151, 151, 151)
        #position de la bar
        bar_position = [self.rect.x - 6, self.rect.y - 20, self.health, 5]
        bar_position_background = [self.rect.x - 6, self.rect.y - 20, self.health_max, 5]
        #dessin de la bar
        pygame.draw.rect(surface, bar_color_background, bar_position_background)
        pygame.draw.rect(surface, bar_color, bar_position)
    
    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)

