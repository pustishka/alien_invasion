import pygame

class Character:
    '''A class to manage a character'''
    def __init__(self, ai_game):
        '''Initialize the ship and set it's stating position.'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get it's rect.
        self.image = pygame.image.load('images/character.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        '''Draw the ship at it's current location.'''
        # self.screen.blit(self.image, self.rect)