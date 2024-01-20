import pygame

class Enemy:
    def __init__(self, p_lives, p_init_position, p_color):
        self.lives = p_lives
        self.position = p_init_position
        self.size = pygame.Vector2(35, 35)
        self.color = p_color
        self.speed = 5
        self.shape = pygame.Rect(self.position, self.size)
        self.multiplier = 1
        
    def draw(self, p_surface):
        pygame.draw.rect(p_surface, self.color, self.shape, 2, 5)
        
    def move(self):
        self.position.x += self.speed * self.multiplier
        self.shape = pygame.Rect(self.position, self.size)