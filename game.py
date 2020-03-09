import pygame
from player import Player
from monster import Monstre

class Game:

    def __init__(self):
        self.player = Player(self)
        self.pressed = {}
        self.all_monsters = pygame.sprite.Group()
        self.all_monsters.add(Monstre(self))
        self.is_playing = 0
    
    def check_collision(self, sprite1, sprites):
        return pygame.sprite.spritecollide(sprite1, sprites, False, pygame.sprite.collide_mask)