import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = {}
        self.health = 100
        self.health_max = 100
        self.image[0] = pygame.image.load('assets/spaceship.png')
        self.image[1] = pygame.image.load('assets/spaceship_2.png')
        self.attack = 10
        self.velocity = 5
        self.rect = self.image[0].get_rect()        
        self.rect.y = 250
        self.rect.x = 20
    
    def move_down(self):
        self.rect.y += self.velocity
    
    def move_up(self):
        self.rect.y -= self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
    
    def move_right(self):
        self.rect.x += self.velocity
    
    def shot(self):
        pygame.mixer.init()
        pygame.mixer.music.load('assets/tire.mp3')
        pygame.mixer.music.play()
