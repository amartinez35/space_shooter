import pygame

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
        self.rect.y = 250
        self.rect.x = 1000
        self.game = game
    
    def forward(self):
        if not self.game.check_collision(self, self.game.player.all_projectiles):
            self.rect.x -= self.velocity
    
    def update_health_bar(self):
        print('test')
