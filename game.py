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
        self.spawn_monster()
        self.spawn_monster()
        self.spawn_monster()
        self.is_playing = 0

    def spawn_monster(self):
        monster = Monstre(self)
        self.all_monsters.add(monster)
    
    def check_collision(self, sprite1, sprites):
        return pygame.sprite.spritecollide(sprite1, sprites, False, pygame.sprite.collide_mask)