import pygame

class Player:
    position = pygame.Vector2(0, 0)
    def __init__(self, p_lives, p_init_position, p_color):
        self.lives = p_lives
        self.position = p_init_position
        self.size = pygame.Vector2(50, 35)
        self.color = p_color
        self.speed = 500
        self.shape = pygame.Rect(self.position, self.size)
        
    def draw(self, p_surface):
        pygame.draw.rect(p_surface, self.color, self.shape, 2, 5)
        
    def moveLeft(self, p_dt):
        self.position.x -= self.speed * p_dt
        self.shape = pygame.Rect(self.position, self.size)
        
    def moveRight(self, p_dt):
        self.position.x += self.speed * p_dt
        self.shape = pygame.Rect(self.position, self.size)
