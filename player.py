import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        #self.image = {}
        self.health = 100
        self.health_max = 100
        self.image = pygame.image.load('assets/spaceship.png')
        #self.image[1] = pygame.image.load('assets/spaceship_2.png')
        self.attack = 10
        self.velocity = 7
        self.rect = self.image.get_rect()        
        self.rect.y = 250
        self.rect.x = 20
        self.all_projectiles = pygame.sprite.Group()
        self.game = game
    
    def move_down(self):
        self.rect.y += self.velocity
    
    def move_up(self):
        self.rect.y -= self.velocity

    def move_left(self):
        self.test()
        self.rect.x -= self.velocity
    
    def move_right(self):
        self.rect.x += self.velocity
            
    def shot(self):
        pygame.mixer.init()
        pygame.mixer.music.load('assets/tire.mp3')
        pygame.mixer.music.play()
        self.all_projectiles.add(Projectile(self, self.game))

