import pygame

class Bullet:
    def __init__(self, p_shoot_position, p_color, p_speed):
        self.position = p_shoot_position
        self.color = p_color
        self.speed = p_speed
        self.size = pygame.Vector2(5, 5)
        self.shape = pygame.Rect(self.position, self.size)
        
    def draw(self, p_surface):
        pygame.draw.rect(p_surface, self.color, self.shape, 5, 5)
        
    def move(self):
        self.position.y -= self.speed
        self.shape = pygame.Rect(self.position, self.size)