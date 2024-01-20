import pygame
import player, bullet, enemy

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
pygame.display.set_caption("Space Invaders")

# Color Values
BLUE = pygame.Color(0, 0, 255, 255)
RED = pygame.Color(255, 0, 0, 255)
WHITE = pygame.Color(255, 255, 255, 255)

# Initial values
player_col = WHITE
enemy_col = BLUE
bullet_col = RED
bullets = []
enemies = []
score = 0
level = 0

# Spawn player
hero = player.Player(3, pygame.Vector2(screen.get_width()/2, screen.get_height() - 50), player_col)

# Spawn enemy
enemies.append(enemy.Enemy(1, pygame.Vector2(50, 50), enemy_col))

def SpawnEnemy():
    enemies.append(enemy.Enemy(1, pygame.Vector2(50, 50), enemy_col))

def RedrawGameWindow():
    
    # Wipe screen everytime
    screen.fill("black")
    
    # Draw player
    hero.draw(screen)
    
    # Draw enemy
    for eachEnemy in enemies:
        eachEnemy.draw(screen)
    
    # Draw bullets
    for eachBullet in bullets:
        eachBullet.draw(screen)
    
    # Update screen
    pygame.display.update()


while running:
    
    for event in pygame.event.get():
        
        # Quit the game from X on Window pane
        if event.type == pygame.QUIT:
            running = False
        
        # Player actions
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                bullets.append(bullet.Bullet(pygame.Vector2(hero.position.x + hero.size.x/2, hero.position.y), bullet_col, 5))
    
    keys = pygame.key.get_pressed()
    
    # Quit the game with q key
    if keys[pygame.K_q]:
        running = False
    
    # Player movement
    if keys[pygame.K_a]:
        hero.moveLeft(dt)
    if keys[pygame.K_d]:
        hero.moveRight(dt)
    
    # Move bullets
    for eachBullet in bullets[:]:
        eachBullet.move()
        
        if eachBullet.position.y < 20:
            bullets.remove(eachBullet)
        
        for eachEnemy in enemies:
            if eachBullet.shape.colliderect(eachEnemy.shape):
                bullets.remove(eachBullet)
                enemies.remove(eachEnemy)
                SpawnEnemy()
                score += 1
                                
    for eachEnemy in enemies[:]:
        eachEnemy.move()
        
        if eachEnemy.position.x > screen.get_width() - 50:
            eachEnemy.position.x = screen.get_width() - 50
            eachEnemy.multiplier = -1
            eachEnemy.position.y += eachEnemy.size.y
            
        if eachEnemy.position.x < 50:
            eachEnemy.position.x = 50
            eachEnemy.multiplier = 1
            eachEnemy.position.y += eachEnemy.size.y
    
    # Wrap the screen width
    if hero.position.x > screen.get_width():
        hero.position.x = 0
    if hero.position.x < 0:
        hero.position.x = screen.get_width()
    
    # limit FPS to 60
    dt = clock.tick(60) / 1000
    
    RedrawGameWindow()

print(f"Your score is: {score}")
pygame.quit()